/* Auto Solution — site script (every page). Features run only if their markup exists. */
(function () {
  'use strict';
  var WA = '917303897496';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function wa(t) { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(t); }
  function fmt(n) { return Math.round(n).toLocaleString('en-IN'); }

  $$('.yr').forEach(function (e) { e.textContent = new Date().getFullYear(); });
  requestAnimationFrame(function () { document.body.classList.add('loaded'); });

  /* Header, mega menus, drawer */
  var hdr = $('#hdr'), mbar = $('#mbar');
  var mmBtns = $$('.mm-btn');
  function closeMM() {
    mmBtns.forEach(function (b) { b.setAttribute('aria-expanded', 'false'); var p = document.getElementById(b.getAttribute('aria-controls')); if (p) p.classList.remove('open'); });
    hdr.classList.remove('open-mm');
  }
  mmBtns.forEach(function (b) {
    var panel = document.getElementById(b.getAttribute('aria-controls'));
    b.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = b.getAttribute('aria-expanded') !== 'true';
      closeMM();
      if (open) { b.setAttribute('aria-expanded', 'true'); panel.classList.add('open'); hdr.classList.add('open-mm'); }
    });
    panel.addEventListener('click', function (e) { e.stopPropagation(); });
  });
  document.addEventListener('click', closeMM);

  var menuBtn = $('#menuBtn'), drawer = $('#drawer');
  function setDrawer(open) {
    drawer.classList.toggle('open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    $('use', menuBtn).setAttribute('href', open ? '#i-x' : '#i-menu');
    document.body.style.overflow = open ? 'hidden' : '';
    hdr.classList.toggle('solid', open || scrollY > 30);
  }
  if (menuBtn) {
    menuBtn.addEventListener('click', function () { setDrawer(!drawer.classList.contains('open')); });
    $$('a', drawer).forEach(function (a) { a.addEventListener('click', function () { setDrawer(false); }); });
  }
  addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeMM(); if (drawer && drawer.classList.contains('open')) setDrawer(false); } });

  /* Scroll-driven bits */
  var storyEl = $('.story');
  function onScroll() {
    hdr.classList.toggle('solid', scrollY > 30 || (drawer && drawer.classList.contains('open')));
    if (mbar) {
      var cta = $('.no-mbar');
      var hide = cta && cta.getBoundingClientRect().top < innerHeight * .85;
      mbar.classList.toggle('show', scrollY > innerHeight * .5 && !hide);
    }
    if (storyEl) story();
  }
  var tick = false;
  addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(function () { onScroll(); tick = false; }); } }, { passive: true });

  /* Reveal + count-up */
  function countUp(el) {
    var to = parseFloat(el.dataset.to);
    if (reduce) { el.textContent = fmt(to); return; }
    var t0 = performance.now();
    (function f(now) { var k = Math.min((now - t0) / 1300, 1); el.textContent = fmt(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(f); })(t0);
  }
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('seen');
        $$('.count', e.target).forEach(countUp);
        if (e.target.classList.contains('count')) countUp(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: .2, rootMargin: '0px 0px -40px 0px' });
    $$('.rv').forEach(function (el) { io.observe(el); });
    $$('.count').forEach(function (c) { if (!c.closest('.rv')) io.observe(c); c.textContent = '0'; });
  } else { $$('.rv').forEach(function (el) { el.classList.add('seen'); }); }

  /* Cursor glow */
  if (matchMedia('(pointer:fine)').matches) $$('.glow').forEach(function (el) {
    el.addEventListener('pointermove', function (e) { var r = el.getBoundingClientRect(); el.style.setProperty('--gx', (e.clientX - r.left) + 'px'); el.style.setProperty('--gy', (e.clientY - r.top) + 'px'); });
  });

  /* Pinned GST story (home) */
  var steps = $$('.st'), nodes = $$('.pnode'), dds = $$('.readout dd');
  var path = $('#pipePath'), lit = $('#pipeLit'), packet = $('#packet'), timer = $('#timer'), foot = $('#cfoot');
  var len = path ? path.getTotalLength() : 0;
  if (lit) lit.style.strokeDasharray = len;
  var AT = [0, .3, .58, .86];
  function render(r) {
    var pt = path.getPointAtLength(len * r);
    packet.setAttribute('cx', pt.x); packet.setAttribute('cy', pt.y);
    lit.style.strokeDashoffset = len * (1 - r);
    var idx = 0; AT.forEach(function (a, i) { if (r >= a) idx = i; });
    steps.forEach(function (s, i) { s.classList.toggle('on', i === idx); s.classList.toggle('done', i < idx); });
    nodes.forEach(function (n) { n.classList.toggle('lit', r > .001 && r >= parseFloat(n.dataset.at)); });
    dds.forEach(function (d) {
      var at = parseFloat(d.dataset.at);
      if (d.dataset.text) { d.textContent = r >= at ? d.dataset.text : '–'; return; }
      d.textContent = fmt(parseFloat(d.dataset.to) * clamp((r - at) / .22, 0, 1));
    });
    timer.textContent = (r * 4.2).toFixed(1) + 's';
    foot.classList.toggle('done', r >= .999);
    foot.textContent = r <= .001 ? 'Waiting to start. Keep scrolling.' : r < .999 ? 'Running…' : 'Done in 4.2 seconds. That used to be three hours of someone\u2019s month.';
  }
  function story() {
    if (reduce) return;
    var rc = storyEl.getBoundingClientRect();
    render(clamp((clamp(-rc.top / (rc.height - innerHeight), 0, 1) - .06) / .8, 0, 1));
  }
  if (storyEl) render(reduce ? 1 : 0);

  /* Agent chat demo */
  (function () {
    var body = $('#chatBody'); if (!body) return;
    var did = $$('#agentDid li'), sub = $('#chatSub'), replay = $('#agentReplay');
    var script = [
      { w: 'them', t: 'Hi, is the 2BHK in Sector 62 still available?', at: '11:04 pm' },
      { w: 'sys', t: 'Checked live inventory', s: 1 },
      { w: 'bot', t: 'Yes, one is free: 1,150 sq ft on the 9th floor, \u20b968 lakh. Are you buying to live in, or as an investment?', at: '11:04 pm' },
      { w: 'them', t: 'To live in. We want to move by March.', at: '11:05 pm' },
      { w: 'sys', t: 'Lead qualified', s: 2 },
      { w: 'bot', t: 'March works for this unit. Want to see it? I have Saturday 11:00 am or Sunday 4:00 pm.', at: '11:05 pm' },
      { w: 'them', t: 'Saturday 11 is good', at: '11:06 pm' },
      { w: 'sys', t: 'Visit booked in sales calendar', s: 3 },
      { w: 'bot', t: 'Done. Saturday 11:00 am with Rahul from our sales team. I\u2019ve sent you the location pin.', at: '11:06 pm' },
      { w: 'sys', t: 'Lead and summary saved to CRM', s: 4 }
    ];
    var timers = [], played = false;
    function reset() { timers.forEach(clearTimeout); timers = []; body.innerHTML = ''; did.forEach(function (d) { d.classList.remove('done'); }); sub.textContent = 'AI assistant, online'; }
    function add(m) {
      var li = document.createElement('li'); li.className = 'msg ' + m.w; li.textContent = m.t;
      if (m.at) { var tm = document.createElement('time'); tm.textContent = m.at; li.appendChild(tm); }
      body.appendChild(li);
      while (body.children.length > 9) body.removeChild(body.firstChild);
      if (m.s) did.forEach(function (d) { if (+d.dataset.s === m.s) d.classList.add('done'); });
    }
    function play() {
      reset();
      if (reduce) { script.forEach(add); return; }
      var t = 400;
      script.forEach(function (m) {
        if (m.w === 'bot') {
          var tp;
          timers.push(setTimeout(function () { tp = document.createElement('li'); tp.className = 'msg bot typing'; tp.innerHTML = '<i></i><i></i><i></i>'; body.appendChild(tp); sub.textContent = 'typing\u2026'; }, t));
          t += 1300;
          timers.push(setTimeout(function () { if (tp) tp.remove(); sub.textContent = 'AI assistant, online'; add(m); }, t));
          t += 900;
        } else { timers.push(setTimeout(function () { add(m); }, t)); t += m.w === 'sys' ? 700 : 1100; }
      });
    }
    if (replay) replay.addEventListener('click', play);
    new IntersectionObserver(function (e, o) { if (e[0].isIntersecting && !played) { played = true; play(); o.disconnect(); } }, { threshold: .4 }).observe(body);
  })();

  /* Savings calculator */
  (function () {
    var form = $('#calc'); if (!form) return;
    var CUR = { INR: ['en-IN', 100, 3000, 50, 400], USD: ['en-US', 5, 200, 5, 30], AED: ['en-AE', 20, 700, 10, 100], GBP: ['en-GB', 5, 150, 5, 25] };
    var p = $('#c-people'), h = $('#c-hours'), r = $('#c-rate'), c = $('#c-cur');
    function money(n) { try { return new Intl.NumberFormat(CUR[c.value][0], { style: 'currency', currency: c.value, maximumFractionDigits: 0 }).format(n); } catch (e) { return c.value + ' ' + fmt(n); } }
    function fill(x) { x.style.setProperty('--p', ((x.value - x.min) / (x.max - x.min) * 100) + '%'); }
    function calc() {
      var hrs = p.value * h.value * 52 * .6;
      $('#o-people').textContent = p.value; $('#o-hours').textContent = h.value; $('#o-rate').textContent = money(+r.value);
      $('#r-hours').textContent = fmt(hrs); $('#r-money').textContent = money(hrs * r.value);
      [p, h, r].forEach(fill); return { hrs: hrs, m: money(hrs * r.value) };
    }
    [p, h, r].forEach(function (x) { x.addEventListener('input', calc); });
    c.addEventListener('change', function () { var k = CUR[c.value]; r.min = k[1]; r.max = k[2]; r.step = k[3]; r.value = k[4]; calc(); });
    calc();
    form.addEventListener('submit', function (e) {
      e.preventDefault(); var o = calc();
      window.open(wa('Hi Auto Solution! I used the savings calculator on your website.\n\nPeople doing repetitive work: ' + p.value + '\nHours each per week: ' + h.value + '\nEstimate: ' + fmt(o.hrs) + ' hours/year, about ' + o.m + '\n\nI\u2019d like a free audit to get the real number.'), '_blank', 'noopener');
    });
  })();

  /* Forms → email (FormSubmit). Falls back to WhatsApp if the email service is unreachable. */
  function post(endpoint, data) {
    return fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw new Error('send failed'); return r.json(); });
  }
  function validator(form) {
    var req = $$('[required]', form);
    function check(el) {
      var ok = el.checkValidity(); el.setAttribute('aria-invalid', String(!ok));
      var er = $('#' + el.id + '-e'); if (er) er.textContent = ok ? '' : (el.validity.typeMismatch ? 'Enter a valid email, like you@company.com.' : 'Please fill this in.');
      return ok;
    }
    req.forEach(function (el) { el.addEventListener('blur', function () { if (el.value) check(el); }); el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') check(el); }); });
    return function () { var bad = null; req.forEach(function (el) { if (!check(el) && !bad) bad = el; }); if (bad) bad.focus(); return !bad; };
  }
  (function () {
    var form = $('#leadForm'); if (!form) return;
    var valid = validator(form), btn = $('button[type=submit]', form), status = $('#formStatus');
    form.addEventListener('submit', function (e) {
      e.preventDefault(); if (!valid()) return;
      var fd = new FormData(form); if (fd.get('_honey')) return;
      function v(k) { return (fd.get(k) || '').toString().trim() || '-'; }
      var data = { _subject: 'New website enquiry: ' + v('name'), _template: 'table', name: v('name'), company: v('company'), email: v('email'), phone: v('phone'), interested_in: v('service'), message: v('message'), page: location.pathname };
      btn.disabled = true; btn.textContent = 'Sending…'; status.textContent = '';
      post(form.dataset.endpoint, data).then(function () {
        status.textContent = 'Thanks, ' + data.name.split(' ')[0] + '. Your message is with us and we\u2019ll reply within 24 hours.';
        form.reset();
      }).catch(function () {
        status.textContent = 'Our form is having trouble, so we\u2019ve opened WhatsApp with your message instead.';
        window.open(wa('*New enquiry from the website*\n\nName: ' + data.name + '\nCompany: ' + data.company + '\nEmail: ' + data.email + '\nPhone: ' + data.phone + '\nInterested in: ' + data.interested_in + '\n\n' + data.message), '_blank', 'noopener');
      }).then(function () { btn.disabled = false; btn.textContent = 'Send message'; });
    });
  })();
  (function () {
    var form = $('#dlForm'); if (!form) return;
    var valid = validator(form), btn = $('button[type=submit]', form), status = $('#dlStatus');
    function give() {
      status.innerHTML = 'Your checklist is ready. <a href="' + form.dataset.file + '" download>Download it again</a> if it didn\u2019t open.';
      var a = document.createElement('a'); a.href = form.dataset.file; a.download = ''; document.body.appendChild(a); a.click(); a.remove();
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault(); if (!valid()) return;
      var fd = new FormData(form); if (fd.get('_honey')) return;
      btn.disabled = true; btn.textContent = 'Preparing…';
      post(form.dataset.endpoint, { _subject: 'Checklist download: ' + fd.get('email'), _template: 'table', name: (fd.get('name') || '-'), email: fd.get('email'), source: 'AI Automation Checklist' })
        .catch(function () {}).then(function () { give(); btn.disabled = false; btn.textContent = 'Download the checklist'; });
    });
  })();

  /* Time zones */
  (function () {
    var items = $$('.zones li[data-tz]'); if (!items.length) return;
    function t() {
      var now = new Date();
      items.forEach(function (li) { try { var s = new Intl.DateTimeFormat('en-GB', { timeZone: li.dataset.tz, hour: '2-digit', minute: '2-digit', hour12: false }).format(now); $('b', li).textContent = s; var hh = parseInt(s, 10); li.classList.toggle('awake', hh >= 9 && hh < 19); } catch (e) {} });
    }
    t(); setInterval(t, 30000);
  })();

  onScroll();
})();
