/* =========================================================
   Hero particle field — "chaos to order"
   Scattered particles (manual work) organise into flowing
   data streams (automation). Plain WebGL, no libraries.
   ========================================================= */
(function () {
  'use strict';
  var canvas = document.getElementById('field');
  if (!canvas) return;

  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gl = canvas.getContext('webgl', { antialias: false, alpha: true, premultipliedAlpha: true, powerPreference: 'high-performance' });
  if (!gl) { canvas.remove(); return; }

  var small = Math.min(innerWidth, innerHeight) < 700;
  var N = small ? 2600 : 6500;

  var VS = [
    'precision highp float;',
    'attribute vec4 aSeed;',
    'uniform float uTime, uProgress, uAspect, uHalfW, uDpr, uPointerOn, uSpeed;',
    'uniform vec2 uMouse, uPointer;',
    'varying vec3 vColor; varying float vAlpha;',
    'const float PI = 3.14159265;',
    'mat3 rotY(float a){float c=cos(a),s=sin(a);return mat3(c,0.,-s, 0.,1.,0., s,0.,c);}',
    'mat3 rotX(float a){float c=cos(a),s=sin(a);return mat3(1.,0.,0., 0.,c,s, 0.,-s,c);}',
    'void main(){',
    '  // ---- chaos: a slowly churning cloud on the right',
    '  float th = aSeed.x * 2. * PI, ph = acos(2. * aSeed.y - 1.);',
    '  float r = 1.15 * pow(aSeed.z, .45);',
    '  vec3 dir = vec3(sin(ph)*cos(th), cos(ph), sin(ph)*sin(th));',
    '  vec3 chaos = dir * r;',
    '  chaos = rotY(uTime * (.06 + aSeed.w * .12)) * chaos;',
    '  chaos += .05 * vec3(sin(uTime*.7 + aSeed.x*40.), cos(uTime*.6 + aSeed.y*40.), sin(uTime*.5 + aSeed.z*40.));',
    '  chaos.x += uHalfW * .42;',
    '  // ---- order: lanes that funnel from wide (left) to tight (right)',
    '  float lane = floor(aSeed.x * 9.);',
    '  float u = fract(aSeed.y + uTime * uSpeed * (.035 + aSeed.w * .03));',
    '  float x = mix(-uHalfW * 1.15, uHalfW * 1.15, u);',
    '  float funnel = mix(1.9, .55, u);',
    '  float y = (lane - 4.) * .17 * funnel + sin(x * 1.6 + lane + uTime * .8) * .035 - .15;',
    '  vec3 order = vec3(x, y, (aSeed.w - .5) * .5);',
    '  // ---- blend with a per-particle stagger and a 3D swoop mid-flight',
    '  float s0 = aSeed.z * .55;',
    '  float t = smoothstep(s0, s0 + .45, uProgress);',
    '  vec3 p = mix(chaos, order, t);',
    '  p.z += sin(t * PI) * (aSeed.x - .5) * 1.6;',
    '  p.y += sin(t * PI) * (aSeed.y - .5) * .6;',
    '  // ---- camera: gentle parallax from pointer',
    '  p = rotX(uMouse.y * .12) * rotY(uMouse.x * .22) * p;',
    '  float camZ = 3.2, focal = 1.7;',
    '  float z = camZ - p.z;',
    '  vec2 ndc = p.xy * focal / z;',
    '  ndc.x /= uAspect;',
    '  // ---- pointer pushes particles aside',
    '  vec2 d = ndc - uPointer; d.x *= uAspect;',
    '  float dist = length(d);',
    '  ndc += (dist > .0001 ? d / dist : vec2(0.)) * vec2(1./uAspect, 1.) * .09 * exp(-dist*dist*22.) * uPointerOn;',
    '  gl_Position = vec4(ndc, 0., 1.);',
    '  bool packet = fract(aSeed.x * 37.13 + aSeed.z * 11.7) > .965;',
    '  float size = (1.8 + aSeed.z * 2.6) * (packet ? mix(1.4, 2.6, t) : 1.);',
    '  gl_PointSize = size * uDpr * (3.2 / z);',
    '  vec3 dim = vec3(.62,.68,.95), cyan = vec3(.31,.89,1.), flux = vec3(1.,.48,.10);',
    '  vColor = packet ? mix(dim, flux, t) : mix(dim, cyan, t * (.55 + aSeed.y * .45));',
    '  vAlpha = clamp(1.45 - z * .2, .25, 1.) * (packet ? 1. : mix(.75, 1., t));',
    '}'
  ].join('\n');

  var FS = [
    'precision mediump float;',
    'varying vec3 vColor; varying float vAlpha;',
    'void main(){',
    '  float d = length(gl_PointCoord - .5);',
    '  float a = smoothstep(.5, .0, d) * vAlpha;',
    '  gl_FragColor = vec4(vColor * a, a);',
    '}'
  ].join('\n');

  function sh(type, src) {
    var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) { console.warn(gl.getShaderInfoLog(s)); return null; }
    return s;
  }
  var vs = sh(gl.VERTEX_SHADER, VS), fs = sh(gl.FRAGMENT_SHADER, FS);
  if (!vs || !fs) { canvas.remove(); return; }
  var prog = gl.createProgram();
  gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) { canvas.remove(); return; }
  gl.useProgram(prog);

  var seeds = new Float32Array(N * 4);
  for (var i = 0; i < seeds.length; i++) seeds[i] = Math.random();
  var buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, seeds, gl.STATIC_DRAW);
  var aSeed = gl.getAttribLocation(prog, 'aSeed');
  gl.enableVertexAttribArray(aSeed);
  gl.vertexAttribPointer(aSeed, 4, gl.FLOAT, false, 0, 0);

  var U = {};
  ['uTime', 'uProgress', 'uAspect', 'uHalfW', 'uDpr', 'uPointerOn', 'uSpeed', 'uMouse', 'uPointer'].forEach(function (n) { U[n] = gl.getUniformLocation(prog, n); });

  gl.enable(gl.BLEND);
  gl.blendFunc(gl.ONE, gl.ONE);
  gl.clearColor(0, 0, 0, 0);

  var dpr = Math.min(window.devicePixelRatio || 1, small ? 1.5 : 2);
  var aspect = 1;
  function resize() {
    var w = canvas.clientWidth, h = canvas.clientHeight;
    canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
    gl.viewport(0, 0, canvas.width, canvas.height);
    aspect = w / Math.max(h, 1);
    gl.uniform1f(U.uAspect, aspect);
    // visible half-width at z=0 (camZ / focal * aspect)
    gl.uniform1f(U.uHalfW, (3.2 / 1.7) * aspect);
    gl.uniform1f(U.uDpr, dpr);
  }
  resize();
  addEventListener('resize', resize);

  // Pointer (mouse + touch)
  var mouse = { x: 0, y: 0, tx: 0, ty: 0 }, pointerOn = 0, pointerTarget = 0;
  function onMove(e) {
    var r = canvas.getBoundingClientRect();
    var cx = (e.touches ? e.touches[0].clientX : e.clientX), cy = (e.touches ? e.touches[0].clientY : e.clientY);
    mouse.tx = ((cx - r.left) / r.width) * 2 - 1;
    mouse.ty = -(((cy - r.top) / r.height) * 2 - 1);
    pointerTarget = 1;
  }
  var hero = canvas.parentElement;
  hero.addEventListener('pointermove', onMove, { passive: true });
  hero.addEventListener('touchmove', onMove, { passive: true });
  hero.addEventListener('pointerleave', function () { pointerTarget = 0; });

  // Timeline: settle from chaos into order once, after load
  var start = performance.now();
  var DELAY = 900, DUR = 3400;
  function ease(t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }

  var speed = 1, running = false, raf = 0, lastScroll = scrollY;
  function frame(now) {
    var el = (now - start);
    var prog = reduce ? 1 : ease(Math.min(Math.max((el - DELAY) / DUR, 0), 1));
    // scrolling briefly speeds the streams up
    var sv = Math.abs(scrollY - lastScroll); lastScroll = scrollY;
    speed += ((1 + Math.min(sv * .08, 4)) - speed) * .08;
    mouse.x += (mouse.tx - mouse.x) * .05; mouse.y += (mouse.ty - mouse.y) * .05;
    pointerOn += (pointerTarget - pointerOn) * .08;

    gl.uniform1f(U.uTime, reduce ? 12 : el / 1000);
    gl.uniform1f(U.uProgress, prog);
    gl.uniform1f(U.uSpeed, speed);
    gl.uniform2f(U.uMouse, mouse.x, mouse.y);
    gl.uniform2f(U.uPointer, mouse.x, mouse.y);
    gl.uniform1f(U.uPointerOn, pointerOn);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.POINTS, 0, N);
    if (running && !reduce) raf = requestAnimationFrame(frame);
  }
  function play() { if (running) return; running = true; raf = requestAnimationFrame(frame); }
  function pause() { running = false; cancelAnimationFrame(raf); }

  if (reduce) { frame(performance.now()); return; }

  var visible = true;
  new IntersectionObserver(function (e) { visible = e[0].isIntersecting; visible && !document.hidden ? play() : pause(); }, { threshold: 0 }).observe(hero);
  document.addEventListener('visibilitychange', function () { visible && !document.hidden ? play() : pause(); });
  play();
})();
