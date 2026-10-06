/* Auto Solution v2 — interactions */
(function () {
  'use strict';
  var WA = '917303897496';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function wa(text) { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text); }
  function fmtIN(n) { return Math.round(n).toLocaleString('en-IN'); }

  $('#yr').textContent = new Date().getFullYear();

  // Page-load sequence (one orchestrated moment)
  requestAnimationFrame(function () { document.documentElement.classList.add('loaded'); document.body.classList.add('loaded'); });

  /* ---------- Header + mobile bar ---------- */
  var hdr = $('#hdr'), mbar = $('#mbar'), hero = $('.hero');
  function onScroll() {
    hdr.classList.toggle('solid', scrollY > 40);
    var pastHero = scrollY > hero.offsetHeight * .6;
    var nearContact = $('#contact').getBoundingClientRect().top < innerHeight * .8;
    mbar.classList.toggle('show', pastHero && !nearContact);
    story();
  }

  /* ---------- Mobile menu ---------- */
  var menuBtn = $('#menuBtn'), nav = $('#nav');
  function setMenu(open) {
    nav.classList.toggle('open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    $('use', menuBtn).setAttribute('href', open ? '#i-x' : '#i-menu');
  }
  menuBtn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
  $$('a', nav).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  /* ---------- Pinned story: scroll drives a sample run ---------- */
  var storyEl = $('.story'), steps = $$('.step'), nodes = $$('.pnode'), dds = $$('.readout dd');
  var path = $('#pipePath'), lit = $('#pipeLit'), packet = $('#packet'), timer = $('#timer'), foot = $('#consoleFoot');
  var len = path.getTotalLength();
  lit.style.strokeDasharray = len;
  var STEP_AT = [0, .3, .58, .86];
  function render(r) {
    var pt = path.getPointAtLength(len * r);
    packet.setAttribute('cx', pt.x); packet.setAttribute('cy', pt.y);
    lit.style.strokeDashoffset = len * (1 - r);
    var idx = 0;
    STEP_AT.forEach(function (a, i) { if (r >= a) idx = i; });
    steps.forEach(function (s, i) { s.classList.toggle('on', i === idx); s.classList.toggle('done', i < idx); });
    nodes.forEach(function (n) { n.classList.toggle('lit', r >= parseFloat(n.dataset.at) && r > 0.001); });
    dds.forEach(function (d) {
      var at = parseFloat(d.dataset.at);
      if (d.dataset.text) { d.textContent = r >= at ? d.dataset.text : '–'; return; }
      var k = clamp((r - at) / .22, 0, 1);
      d.textContent = fmtIN(parseFloat(d.dataset.to) * k);
    });
    timer.textContent = (r * 4.2).toFixed(1) + 's';
    if (r <= 0.001) { foot.textContent = 'Waiting to start. Keep scrolling.'; foot.classList.remove('done'); }
    else if (r < .999) { foot.textContent = 'Running…'; foot.classList.remove('done'); }
    else { foot.textContent = 'Done in 4.2 seconds. That used to be three hours of someone\u2019s month.'; foot.classList.add('done'); }
  }
  function story() {
    if (reduce) return;
    var rect = storyEl.getBoundingClientRect();
    var total = rect.height - innerHeight;
    var p = clamp(-rect.top / total, 0, 1);
    render(clamp((p - .06) / .8, 0, 1));
  }
  if (reduce) render(1); else render(0);

  var ticking = false;
  addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(function () { onScroll(); ticking = false; }); }
  }, { passive: true });
  addEventListener('resize', story);
  onScroll();

  /* ---------- Results: line sweep + count-up when seen ---------- */
  function countUp(el) {
    var to = parseFloat(el.dataset.to);
    if (reduce) { el.textContent = fmtIN(to); return; }
    var t0 = performance.now();
    (function f(now) {
      var k = Math.min((now - t0) / 1200, 1);
      el.textContent = fmtIN(to * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(f);
    })(t0);
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('seen');
        $$('.count', e.target).forEach(countUp);
        io.unobserve(e.target);
      });
    }, { threshold: .35 });
    $$('.result').forEach(function (r) { $$('.count', r).forEach(function (c) { c.textContent = '0'; }); io.observe(r); });
  }

  /* ---------- Magnetic primary CTA (fine pointers only) ---------- */
  if (!reduce && matchMedia('(pointer:fine)').matches) {
    $$('.magnetic').forEach(function (b) {
      b.addEventListener('pointermove', function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = 'translate(' + (e.clientX - r.left - r.width / 2) * .18 + 'px,' + (e.clientY - r.top - r.height / 2) * .3 + 'px)';
      });
      b.addEventListener('pointerleave', function () { b.style.transform = ''; });
    });
  }

  /* ---------- Savings estimate ---------- */
  var CUR = {
    INR: { loc: 'en-IN', min: 100, max: 3000, step: 50, def: 400 },
    USD: { loc: 'en-US', min: 5, max: 200, step: 5, def: 30 },
    AED: { loc: 'en-AE', min: 20, max: 700, step: 10, def: 100 },
    GBP: { loc: 'en-GB', min: 5, max: 150, step: 5, def: 25 }
  };
  var cPeople = $('#c-people'), cHours = $('#c-hours'), cRate = $('#c-rate'), cCur = $('#c-cur');
  var SHARE = .6;
  function money(n, cur) {
    try { return new Intl.NumberFormat(CUR[cur].loc, { style: 'currency', currency: cur, maximumFractionDigits: 0 }).format(n); }
    catch (e) { return cur + ' ' + fmtIN(n); }
  }
  function fill(r) { r.style.setProperty('--p', ((r.value - r.min) / (r.max - r.min) * 100) + '%'); }
  function calc() {
    var cur = cCur.value;
    var hours = cPeople.value * cHours.value * 52 * SHARE;
    $('#o-people').textContent = cPeople.value;
    $('#o-hours').textContent = cHours.value;
    $('#o-rate').textContent = money(+cRate.value, cur);
    $('#r-hours').textContent = fmtIN(hours);
    $('#r-money').textContent = money(hours * cRate.value, cur);
    [cPeople, cHours, cRate].forEach(fill);
    return { hours: hours, money: money(hours * cRate.value, cur) };
  }
  [cPeople, cHours, cRate].forEach(function (r) { r.addEventListener('input', calc); });
  cCur.addEventListener('change', function () {
    var c = CUR[cCur.value];
    cRate.min = c.min; cRate.max = c.max; cRate.step = c.step; cRate.value = c.def;
    calc();
  });
  calc();
  $('#calc').addEventListener('submit', function (e) {
    e.preventDefault();
    var r = calc();
    window.open(wa(
      'Hi Auto Solution! I used the savings estimate on your site.\n\n' +
      'People doing repetitive work: ' + cPeople.value + '\n' +
      'Hours each per week: ' + cHours.value + '\n' +
      'Estimated: ' + fmtIN(r.hours) + ' hours/year, about ' + r.money + '\n\n' +
      'I\u2019d like a free audit to get the real number.'
    ), '_blank', 'noopener');
  });

  /* ---------- Contact form → WhatsApp ---------- */
  var form = $('#leadForm'), req = $$('[required]', form);
  function check(el) {
    var ok = el.checkValidity();
    el.setAttribute('aria-invalid', String(!ok));
    var err = $('#' + el.id + '-e');
    if (err) err.textContent = ok ? '' : (el.validity.typeMismatch ? 'Enter a valid email, like you@company.com.' : 'Fill this in so we know who to reply to.');
    return ok;
  }
  req.forEach(function (el) {
    el.addEventListener('blur', function () { if (el.value) check(el); });
    el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') check(el); });
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var bad = null;
    req.forEach(function (el) { if (!check(el) && !bad) bad = el; });
    if (bad) { bad.focus(); return; }
    var fd = new FormData(form);
    function v(k) { return (fd.get(k) || '').toString().trim() || '-'; }
    window.open(wa(
      '*New enquiry from the website*\n\n' +
      'Name: ' + v('name') + '\nCompany: ' + v('company') + '\nEmail: ' + v('email') + '\nPhone: ' + v('phone') +
      '\n\nWhat to automate:\n' + v('message')
    ), '_blank', 'noopener');
    $('#formStatus').textContent = 'WhatsApp is open with your details. Press send there and we\u2019ll reply within 24 hours.';
    form.reset();
  });

  /* ---------- Highlight current section in nav ---------- */
  if ('IntersectionObserver' in window) {
    var links = $$('a', nav);
    var secIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.setAttribute('aria-current', String(a.getAttribute('href') === '#' + e.target.id)); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    ['how', 'results', 'agents', 'services', 'estimate', 'faq'].forEach(function (id) { var el = document.getElementById(id); if (el) secIO.observe(el); });
  }

  /* ---------- Cursor glow on key panels ---------- */
  if (matchMedia('(pointer:fine)').matches) {
    $$('.glow').forEach(function (el) {
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        el.style.setProperty('--gx', (e.clientX - r.left) + 'px');
        el.style.setProperty('--gy', (e.clientY - r.top) + 'px');
      });
    });
  }

  /* ---------- AI agent demo (scripted example conversation) ---------- */
  (function () {
    var body = $('#chatBody'), did = $$('#agentDid li'), sub = $('#chatSub'), replay = $('#agentReplay');
    if (!body) return;
    var script = [
      { who: 'them', t: 'Hi, is the 2BHK in Sector 62 still available?', at: '11:04 pm' },
      { who: 'sys', t: 'Checked live inventory', step: 1 },
      { who: 'bot', t: 'Yes, one is free: 1,150 sq ft on the 9th floor, \u20b968 lakh. Are you buying to live in, or as an investment?', at: '11:04 pm' },
      { who: 'them', t: 'To live in. We want to move by March.', at: '11:05 pm' },
      { who: 'sys', t: 'Lead qualified', step: 3 },
      { who: 'bot', t: 'March works for this unit. Want to see it? I have Saturday 11:00 am or Sunday 4:00 pm.', at: '11:05 pm' },
      { who: 'them', t: 'Saturday 11 is good', at: '11:06 pm' },
      { who: 'sys', t: 'Visit booked in sales calendar', step: 5 },
      { who: 'bot', t: 'Done. Saturday 11:00 am with Rahul from our sales team. I\u2019ve sent you the location pin.', at: '11:06 pm' },
      { who: 'sys', t: 'Lead and summary saved to HubSpot', step: 6 }
    ];
    var timers = [], played = false;
    function clear() { timers.forEach(clearTimeout); timers = []; body.innerHTML = ''; did.forEach(function (d) { d.classList.remove('done'); }); sub.textContent = 'AI assistant, online'; }
    function msg(m) {
      var li = document.createElement('li');
      li.className = 'msg ' + m.who;
      li.textContent = m.t;
      if (m.at) { var tm = document.createElement('time'); tm.textContent = m.at; li.appendChild(tm); }
      body.appendChild(li);
      while (body.children.length > 9) body.removeChild(body.firstChild);
      if (m.step) did.forEach(function (d) { if (+d.dataset.step === m.step) d.classList.add('done'); });
    }
    function typing() { var li = document.createElement('li'); li.className = 'msg bot typing'; li.innerHTML = '<i></i><i></i><i></i>'; body.appendChild(li); sub.textContent = 'typing\u2026'; return li; }
    function play() {
      clear();
      if (reduce) { script.forEach(msg); return; }
      var t = 400;
      script.forEach(function (m) {
        if (m.who === 'bot') {
          var tp;
          timers.push(setTimeout(function () { tp = typing(); }, t));
          t += 1300;
          timers.push(setTimeout(function () { if (tp) tp.remove(); sub.textContent = 'AI assistant, online'; msg(m); }, t));
          t += 900;
        } else if (m.who === 'sys') {
          timers.push(setTimeout(function () { msg(m); }, t)); t += 700;
        } else {
          timers.push(setTimeout(function () { msg(m); }, t)); t += 1100;
        }
      });
    }
    replay.addEventListener('click', play);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e, o) {
        if (e[0].isIntersecting && !played) { played = true; play(); o.disconnect(); }
      }, { threshold: .4 }).observe(body);
    } else play();
  })();

  /* ---------- Live time zones ---------- */
  (function () {
    var items = $$('#zones li');
    if (!items.length) return;
    function tick() {
      var now = new Date();
      items.forEach(function (li) {
        try {
          var parts = new Intl.DateTimeFormat('en-GB', { timeZone: li.dataset.tz, hour: '2-digit', minute: '2-digit', hour12: false }).format(now);
          $('b', li).textContent = parts;
          var h = parseInt(parts, 10);
          li.classList.toggle('awake', h >= 9 && h < 19);
        } catch (e) {}
      });
    }
    tick(); setInterval(tick, 30000);
  })();
})();
