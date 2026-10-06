/* =========================================================
   AI Live Dashboard (demo data)
   Timers only run while the dashboard tab is open and the
   browser tab is visible — saves CPU/battery.
   ========================================================= */
(function () {
  'use strict';

  var timers = [];
  var running = false;
  var activeTab = null;
  function $(id) { return document.getElementById(id); }
  function rand(min, max) { return Math.random() * (max - min) + min; }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function pad(n) { return String(n).padStart(2, '0'); }
  function hhmmss() { var d = new Date(); return pad(d.getHours()) + ':' + pad(d.getMinutes()) + ':' + pad(d.getSeconds()); }
  function every(ms, fn) { fn(); timers.push(setInterval(fn, ms)); }

  /* Clock */
  function clock() { var el = $('liveClock'); if (el) el.textContent = hhmmss(); }

  /* Throughput chart */
  var N = 12, xStep = 540 / (N - 1), vals = [], last = 85;
  for (var i = 0; i < N; i++) { last = clamp(last + rand(-12, 12), 25, 150); vals.push(last); }
  function renderChart() {
    var line = $('liveLine'), area = $('liveArea'), dot = $('liveDot');
    if (!line) return;
    var pts = vals.map(function (v, i) { return (10 + i * xStep).toFixed(1) + ',' + (150 - v).toFixed(1); });
    line.setAttribute('points', pts.join(' '));
    area.setAttribute('points', pts.join(' ') + ' 550,150 10,150');
    var lp = pts[pts.length - 1].split(',');
    dot.setAttribute('cx', lp[0]); dot.setAttribute('cy', lp[1]);
  }
  function stepChart() {
    last = clamp(last + rand(-14, 16), 20, 155);
    vals.shift(); vals.push(last);
    renderChart();
    var tag = $('chartTag'); if (tag) tag.textContent = 'Updated ' + hhmmss();
  }

  /* KPIs */
  var reqs = 1284, lat = 312, conf = 96.4;
  function kpis() {
    var rc = Math.round(rand(-25, 35));
    reqs = Math.max(900, reqs + rc);
    $('kpiReqs').textContent = reqs.toLocaleString('en-IN');
    var rd = $('kpiReqsDelta');
    rd.textContent = (rc >= 0 ? '↑ ' : '↓ ') + Math.abs(rc) + '/min';
    rd.className = 'an-kpi-delta' + (rc < 0 ? ' down' : '');

    var lc = Math.round(rand(-22, 18));
    lat = clamp(lat + lc, 180, 480);
    $('kpiLatency').textContent = lat + 'ms';
    var ld = $('kpiLatencyDelta');
    ld.textContent = (lc <= 0 ? '↓ ' : '↑ ') + Math.abs(lc) + 'ms';
    // lower latency is good → teal; higher is bad → red
    ld.className = 'an-kpi-delta' + (lc <= 0 ? ' good-down' : ' down');

    conf = clamp(conf + rand(-0.3, 0.3), 92, 99);
    $('kpiConf').textContent = conf.toFixed(1) + '%';
  }

  /* Donuts */
  var CIRC = 2 * Math.PI * 34;
  var donuts = [
    { ring: 'donutConf', val: 'donutConfVal', pct: 96, drift: 2 },
    { ring: 'donutGpu', val: 'donutGpuVal', pct: 72, drift: 8 },
    { ring: 'donutQueue', val: 'donutQueueVal', pct: 15, drift: 10 }
  ];
  function donutStep(move) {
    donuts.forEach(function (d) {
      if (move) d.pct = clamp(d.pct + rand(-d.drift / 2, d.drift / 2), 8, 99);
      var r = $(d.ring); if (!r) return;
      r.setAttribute('stroke-dasharray', CIRC.toFixed(1));
      r.setAttribute('stroke-dashoffset', (CIRC * (1 - d.pct / 100)).toFixed(1));
      $(d.val).textContent = Math.round(d.pct) + '%';
    });
  }

  /* Compute nodes */
  var nodeIds = ['g1u', 'g1v', 'g1t', 'g2u', 'g2v', 'g2t', 'g3u', 'g3v', 'g3t', 'g4u', 'g4v', 'g4t'];
  var nodeState = {};
  nodeIds.forEach(function (id) { var f = $(id); if (f) nodeState[id] = parseFloat(f.style.width) || 50; });
  function nodes() {
    nodeIds.forEach(function (id) {
      var f = $(id), lbl = $(id + '-t');
      if (!f) return;
      nodeState[id] = clamp(nodeState[id] + rand(-7, 7), 8, 97);
      f.style.width = nodeState[id].toFixed(0) + '%';
      if (lbl && /%$/.test(lbl.textContent)) lbl.textContent = nodeState[id].toFixed(0) + '%';
    });
  }

  /* Activity feed (built with textContent, no innerHTML) */
  var agents = ['Doc Extraction Agent', 'Forecast Agent', 'Chat Support Agent', 'Reconciliation Agent', 'OCR Batch Agent', 'Anomaly Detector', 'Routing Agent', 'Compliance Agent'];
  var templates = [
    ['ok', function (a) { return a + ' completed batch: ' + Math.floor(rand(50, 450)) + ' records processed'; }],
    ['info', function (a) { return a + ' started a new inference run'; }],
    ['ok', function (a) { return a + ' responded in ' + Math.floor(rand(120, 420)) + 'ms'; }],
    ['info', function (a) { return a + ' synced with upstream data source'; }],
    ['warn', function (a) { return a + ' retrying a request (timeout after ' + Math.floor(rand(1, 4)) + 's)'; }],
    ['ok', function (a) { return a + ' confidence steady at ' + rand(94, 98).toFixed(1) + '%'; }],
    ['info', function (a) { return a + ' scaled to ' + Math.floor(rand(2, 5)) + ' workers'; }]
  ];
  function span(cls, text) { var s = document.createElement('span'); s.className = cls; s.textContent = text; return s; }
  function feedLine() {
    var feed = $('aiFeed'); if (!feed) return;
    var a = agents[Math.floor(Math.random() * agents.length)];
    var t = templates[Math.floor(Math.random() * templates.length)];
    var row = document.createElement('div');
    row.className = 'ai-feed-line';
    row.appendChild(span('ai-feed-time', hhmmss()));
    row.appendChild(span('ai-feed-tag ' + t[0], t[0]));
    row.appendChild(span('ai-feed-msg', t[1](a)));
    feed.insertBefore(row, feed.firstChild);
    while (feed.children.length > 8) feed.removeChild(feed.lastChild);
  }

  /* Lifecycle */
  var seeded = false;
  function start() {
    if (running) return;
    running = true;
    if (!seeded) { seeded = true; renderChart(); donutStep(false); for (var k = 0; k < 5; k++) feedLine(); }
    every(1000, clock);
    timers.push(setInterval(stepChart, 2200));
    timers.push(setInterval(kpis, 2400));
    timers.push(setInterval(function () { donutStep(true); }, 2600));
    timers.push(setInterval(nodes, 2000));
    timers.push(setInterval(feedLine, 2200));
  }
  function stop() {
    running = false;
    timers.forEach(clearInterval);
    timers = [];
  }
  function sync() {
    if (activeTab === 'dashboard' && !document.hidden) start(); else stop();
  }
  document.addEventListener('as:tabchange', function (e) { activeTab = e.detail.tab; sync(); });
  document.addEventListener('visibilitychange', sync);
  // main.js may have routed before this file loaded
  var current = document.querySelector('.tab-panel.active');
  if (current) { activeTab = current.id.replace('tab-', ''); sync(); }
})();
