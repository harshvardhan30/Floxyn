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

  (function () {
    var form = $('#demoForm'); if (!form) return;
    var q = new URLSearchParams(location.search).get('product'), sel = $('#r-product');
    if (q && sel.querySelector('option[value="' + q + '"]')) sel.value = q;
    var ty = new URLSearchParams(location.search).get('type'), tsel = $('#r-type-req');
    if (tsel && ty === 'pilot') tsel.value = 'pilot';
    var valid = validator(form), btn = $('button[type=submit]', form), status = $('#demoStatus');
    form.addEventListener('submit', function (e) {
      e.preventDefault(); if (!valid()) return;
      var fd = new FormData(form); if (fd.get('_honey')) return;
      var kind = (tsel && tsel.value === 'pilot') ? 'Pilot request' : 'Demo request';
      var data = { _subject: kind + ': ' + sel.options[sel.selectedIndex].text.split(':')[0] + ' from ' + fd.get('organisation'), _template: 'table' };
      fd.forEach(function (v, k) { if (k !== '_honey') data[k] = v || '-'; });
      btn.disabled = true; btn.textContent = 'Sending…';
      post(form.dataset.endpoint, data).then(function () {
        status.textContent = 'Thanks. Your ' + kind.toLowerCase() + ' is with us and we\u2019ll reply within one business day.'; form.reset();
      }).catch(function () {
        status.textContent = 'Our form is having trouble, so we\u2019ve opened WhatsApp with your request instead.';
        window.open(wa('*' + kind + '*\n\nProduct: ' + data.product + '\nName: ' + data.name + '\nRole: ' + data.role + '\nOrganisation: ' + data.organisation + ' (' + data.org_type + ')\nEmail: ' + data.email + '\nPhone: ' + data.phone + '\n\n' + data.message), '_blank', 'noopener');
      }).then(function () { btn.disabled = false; btn.textContent = 'Request demo'; });
    });
  })();

  /* Tabs */
  $$('.tabs').forEach(function (t) {
    var tabs = $$('[role=tab]', t);
    function sel(tab) {
      tabs.forEach(function (x) { var on = x === tab; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute('aria-controls')).hidden = !on; });
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { sel(tab); });
      tab.addEventListener('keydown', function (e) {
        var k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!k) return;
        var n = tabs[(i + k + tabs.length) % tabs.length]; sel(n); n.focus(); e.preventDefault();
      });
    });
  });

  /* Live hero table (demo stream) */
  (function () {
    var tb = $('#liveTbl'); if (!tb || reduce) return;
    var rails = ['UPI', 'Card', 'Netbank', 'Wallet'], n = 0x8F21F;
    function row() {
      var amt = Math.random() < .2 ? 20000 + Math.random() * 90000 : 200 + Math.random() * 9000;
      var sc = Math.min(.99, Math.max(.01, (amt > 40000 ? .45 : .05) + Math.random() * (amt > 40000 ? .5 : .3)));
      var d = sc > .7 ? ['bad', 'Decline'] : sc > .4 ? ['mid', 'Review'] : ['ok', 'Approve'];
      var tr = document.createElement('tr'); tr.className = 'new';
      tr.innerHTML = '<td>TXN ' + (n++).toString(16).toUpperCase() + '</td><td>\u20b9' + fmt(amt) + '</td><td>' + rails[Math.floor(Math.random() * 4)] + '</td><td class="mono">' + sc.toFixed(2) + '</td><td><span class="dec ' + d[0] + '">' + d[1] + '</span></td>';
      tb.insertBefore(tr, tb.firstChild); if (tb.children.length > 5) tb.removeChild(tb.lastChild);
    }
    var iv = null;
    new IntersectionObserver(function (e) { if (e[0].isIntersecting) { if (!iv) iv = setInterval(row, 1800); } else { clearInterval(iv); iv = null; } }).observe(tb);
  })();

  /* Hero collage tilt */
  (function () {
    var c = $('.collage'); if (!c || reduce || !matchMedia('(pointer:fine)').matches) return;
    var hero = $('.hero-l');
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      $('.c-main', c).style.transform = 'rotateX(' + (-y * 5) + 'deg) rotateY(' + (x * 6) + 'deg)';
      var l = $('.c-left', c), rt = $('.c-right', c);
      if (l) l.style.transform = 'translateY(54px) rotateY(' + (8 + x * 6) + 'deg) rotateX(' + (-y * 4) + 'deg)';
      if (rt) rt.style.transform = 'translateY(54px) rotateY(' + (-8 + x * 6) + 'deg) rotateX(' + (-y * 4) + 'deg)';
    });
    hero.addEventListener('pointerleave', function () { $$('.collage>div').forEach(function (d) { d.style.transform = ''; }); });
  })();

  /* Fraud score simulator (simplified illustrative model) */
  (function () {
    var f = $('#sim'); if (!f) return;
    var amt = $('#s-amt'), hr = $('#s-hr'), vel = $('#s-vel'), cat = $('#s-cat'), nw = $('#s-new'), geo = $('#s-geo');
    var CAT = { groceries: [-0.6, 'Low-risk merchant category'], travel: [0.2, 'Travel merchant'], electronics: [0.5, 'Electronics: resale target'], gaming: [0.7, 'Gaming merchant'], giftcards: [1.4, 'Gift cards: high-risk category'], crypto: [1.6, 'Crypto exchange: high-risk category'] };
    function fill(x) { x.style.setProperty('--p', ((x.value - x.min) / (x.max - x.min) * 100) + '%'); }
    function run() {
      var a = +amt.value, h = +hr.value, v = +vel.value, parts = [];
      var amtC = Math.max(-0.4, Math.log10(a / 5000) * 1.3); parts.push([amtC, a > 5000 ? 'Amount higher than usual' : 'Small, typical amount']);
      var night = (h >= 0 && h < 5) ? 1.1 : (h >= 23 ? .6 : -0.2); parts.push([night, night > 0 ? 'Late-night transaction' : 'Normal hours']);
      var velC = (v - 2) * 0.32; parts.push([velC, v > 3 ? v + ' payments from one device in an hour' : 'Normal device activity']);
      parts.push(CAT[cat.value]);
      if (nw.checked) parts.push([1.0, 'First time we\u2019ve seen this device']);
      if (geo.checked) parts.push([1.2, 'Card country doesn\u2019t match location']);
      var z = -2.4 + parts.reduce(function (s, p) { return s + p[0]; }, 0);
      var sc = 1 / (1 + Math.exp(-z));
      $('#so-amt').textContent = '\u20b9' + fmt(a); $('#so-hr').textContent = (h < 10 ? '0' : '') + h + ':00'; $('#so-vel').textContent = v;
      $('#sScore').textContent = sc.toFixed(2);
      $('#gArc').style.strokeDashoffset = 100 - sc * 100;
      var d = sc > .7 ? ['bad', 'Decline'] : sc > .35 ? ['mid', 'Send to review'] : ['ok', 'Approve'];
      var de = $('#sDec'); de.className = 'dec ' + d[0]; de.textContent = d[1];
      var why = $('#sWhy'); why.innerHTML = '';
      parts.sort(function (x, y) { return Math.abs(y[0]) - Math.abs(x[0]); }).slice(0, 3).forEach(function (p) {
        var li = document.createElement('li'); var t = document.createElement('span'); t.textContent = p[1];
        var b = document.createElement('b'); b.textContent = (p[0] >= 0 ? '+' : '\u2212') + Math.abs(p[0]).toFixed(1); if (p[0] < 0) b.className = 'neg';
        li.appendChild(t); li.appendChild(b); why.appendChild(li);
      });
      [amt, hr, vel].forEach(fill);
    }
    [amt, hr, vel, cat, nw, geo].forEach(function (x) { x.addEventListener('input', run); x.addEventListener('change', run); });
    run();
  })();

  /* GridSentinel energy balance demo */
  (function () {
    var f = $('#gsim'); if (!f) return;
    var I = $('#g-in'), B = $('#g-bill'), T = $('#g-tech'), R = $('#g-tar'), leads = $$('#gLeads li');
    function fill(x) { x.style.setProperty('--p', ((x.value - x.min) / (x.max - x.min) * 100) + '%'); }
    function run() {
      var i = +I.value, b = +B.value, t = +T.value, r = +R.value;
      var un = Math.max(0, i - b - i * t / 100), pct = un / i * 100;
      $('#go-in').textContent = fmt(i); $('#go-bill').textContent = fmt(b); $('#go-tech').textContent = t + '%'; $('#go-tar').textContent = '\u20b9' + r.toFixed(1);
      $('#gLoss').textContent = fmt(un) + ' kWh (' + pct.toFixed(1) + '%)';
      $('#gVal').textContent = '\u20b9' + fmt(un * r);
      var d = pct < 2 ? ['ok', 'Within expected loss: no action'] : pct < 8 ? ['mid', 'Watch list: review next cycle'] : ['bad', 'Priority for field inspection'];
      var de = $('#gDec'); de.className = 'dec ' + d[0]; de.textContent = d[1];
      leads.forEach(function (li) {
        var sh = parseFloat(li.dataset.share), rec = $('.rec', li);
        li.classList.toggle('fault', sh === 0); li.classList.toggle('dim', pct < 2);
        rec.textContent = sh === 0 ? 'Not theft' : (fmt(un * sh) + ' kWh');
      });
      [I, B, T, R].forEach(fill);
    }
    [I, B, T, R].forEach(function (x) { x.addEventListener('input', run); });
    run();
  })();

  /* FuelLedger four-way reconciliation demo */
  (function () {
    var f = $('#fsim'); if (!f) return;
    var inv = $('#f-inv'), rec = $('#f-rec'), sold = $('#f-sold'), cash = $('#f-cash'), dens = $('#f-dens'), PRICE = 100;
    function fill(x) { x.style.setProperty('--p', ((x.value - x.min) / (x.max - x.min) * 100) + '%'); }
    function rs(n) { return '\u20b9' + fmt(n); }
    function run() {
      var a = +inv.value, b = +rec.value, c = +sold.value, m = +cash.value * 100000, dn = +dens.value;
      $('#fo-inv').textContent = fmt(a); $('#fo-rec').textContent = fmt(b); $('#fo-sold').textContent = fmt(c); $('#fo-cash').textContent = '\u20b9' + (+cash.value).toFixed(2) + ' L'; $('#fo-dens').textContent = dn.toFixed(1);
      var rows = [['Invoiced', a, fmt(a) + ' L'], ['Received', b, fmt(b) + ' L'], ['Sold', c, fmt(c) + ' L'], ['Collected', m / PRICE, '\u20b9' + (m / 100000).toFixed(2) + 'L']];
      var mx = Math.max(a, b, c, m / PRICE);
      $('#fSteps').innerHTML = rows.map(function (r) { return '<div class="fl-row"><span>' + r[0] + '</span><div class="ft"><i style="width:' + (r[1] / mx * 100).toFixed(1) + '%"></i></div><b>' + r[2] + '</b></div>'; }).join('');
      var flags = [], tr = a - b, st = b - c, pay = c * PRICE - m;
      if (tr > a * .003) flags.push(['bad', 'Transit gap ' + fmt(tr) + ' L', rs(tr * PRICE), 'Check transporter: seals and dip at decanting']);
      if (st > b * .006) flags.push(['bad', 'Stock gap ' + fmt(st) + ' L', rs(st * PRICE), 'Check night-time tank level drops and nozzle calibration']);
      if (pay > c * PRICE * .002) flags.push(['bad', 'Payment shortfall', rs(pay), 'Reconcile cash deposit and card settlements with the dealer']);
      if (dn > 3) flags.push(['bad', 'Density off by ' + dn.toFixed(1) + ' kg/m\u00b3', 'Quality', 'Hold sales from this tank and test a sample']);
      var ul = $('#fFlags'); ul.innerHTML = '';
      if (!flags.length) flags.push(['ok', 'All four steps within tolerance', '\u2713', 'No action needed today']);
      flags.forEach(function (fl) {
        var li = document.createElement('li'); li.className = fl[0];
        var t = document.createElement('span'); t.innerHTML = '<strong style="color:#fff;font-weight:600">' + fl[1] + '</strong><br><small style="color:var(--signal)">' + fl[3] + '</small>';
        var v = document.createElement('b'); v.textContent = fl[2];
        li.appendChild(t); li.appendChild(v); ul.appendChild(li);
      });
      [inv, rec, sold, cash, dens].forEach(fill);
    }
    [inv, rec, sold, cash, dens].forEach(function (x) { x.addEventListener('input', run); });
    run();
  })();

  /* Product value estimators */
  $$('form.roi').forEach(function (f) {
    var kind = f.dataset.roi, ins = $$('input[type=range]', f);
    function v(k) { return +$('#ri-' + k, f).value; }
    function cr(n) { return n >= 1e7 ? '\u20b9' + (n / 1e7).toLocaleString('en-IN', { maximumFractionDigits: 1 }) + ' crore' : '\u20b9' + (n / 1e5).toLocaleString('en-IN', { maximumFractionDigits: 1 }) + ' lakh'; }
    function run() {
      ins.forEach(function (x) {
        var u = x.dataset.unit, val = +x.value, t = u === '\u20b9' ? '\u20b9' + val.toLocaleString('en-IN') : (u === '%' ? val + '%' : val.toLocaleString('en-IN'));
        $('#ro-' + x.dataset.k, f).textContent = t;
        x.style.setProperty('--p', ((x.value - x.min) / (x.max - x.min) * 100) + '%');
      });
      var a = 0;
      if (kind === 'paysentinel') a = v('tx') * 1e5 * 12 * v('tk') * v('fr') / 1e4;
      if (kind === 'gridsentinel') a = v('mu') * 1e6 * v('cl') / 100 * v('tf');
      if (kind === 'fuelledger') a = v('ol') * v('kl') * 1000 * 365 * v('lp') / 100 * v('pr');
      $('#rr-a', f).textContent = cr(a);
      $('#rr-b', f).textContent = cr(a * v('sh') / 100);
    }
    ins.forEach(function (x) { x.addEventListener('input', run); });
    run();
  });

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
