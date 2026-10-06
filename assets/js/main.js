/* =========================================================
   Auto Solution — main site script
   ========================================================= */
(function () {
  'use strict';

  var WA_NUMBER = '917303897496';
  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  root.classList.remove('no-js');

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function store(type, key, val) {
    try {
      var s = window[type];
      if (val === undefined) return s.getItem(key);
      s.setItem(key, val);
    } catch (e) { return null; }
  }
  function waLink(text) { return 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(text); }

  /* ---------- Year ---------- */
  var yr = $('#yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- Progress bar + back-to-top ---------- */
  var pbar = $('#pbar');
  var totopBtn = $('#totopBtn');
  var ticking = false;
  function onScroll() {
    var h = root;
    var max = h.scrollHeight - h.clientHeight;
    if (pbar) pbar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    if (totopBtn) totopBtn.classList.toggle('show', h.scrollTop > 500);
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  if (totopBtn) totopBtn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
  });

  /* ---------- Theme ---------- */
  function toggleTheme() {
    var dark = root.getAttribute('data-theme') === 'dark';
    root.setAttribute('data-theme', dark ? 'light' : 'dark');
    store('localStorage', 'as-theme', dark ? 'light' : 'dark');
    $$('.theme-toggle').forEach(function (b) { b.setAttribute('aria-pressed', String(!dark)); });
  }
  $$('.theme-toggle').forEach(function (b) {
    b.setAttribute('aria-pressed', String(root.getAttribute('data-theme') === 'dark'));
    b.addEventListener('click', toggleTheme);
  });

  /* ---------- Desktop dropdowns ---------- */
  var dds = $$('.navdd');
  function closeDropdowns(except) {
    dds.forEach(function (dd) {
      if (dd === except) return;
      dd.classList.remove('open');
      var b = $('.navdd-btn', dd);
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  dds.forEach(function (dd) {
    var btn = $('.navdd-btn', dd);
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = !dd.classList.contains('open');
      closeDropdowns(dd);
      dd.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
    $$('a', dd).forEach(function (a) { a.addEventListener('click', function () { closeDropdowns(); }); });
  });
  document.addEventListener('click', function () { closeDropdowns(); });

  /* ---------- Mobile menu ---------- */
  var hambBtn = $('#hambBtn'), mmenu = $('#mmenu'), mbackdrop = $('#mbackdrop'), mcloseBtn = $('#mcloseBtn');
  function openMenu() {
    mmenu.classList.add('open'); mbackdrop.classList.add('open');
    hambBtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    mcloseBtn.focus();
  }
  function closeMenu() {
    if (!mmenu.classList.contains('open')) return;
    mmenu.classList.remove('open'); mbackdrop.classList.remove('open');
    hambBtn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    hambBtn.focus();
  }
  if (hambBtn) {
    hambBtn.addEventListener('click', openMenu);
    mcloseBtn.addEventListener('click', closeMenu);
    mbackdrop.addEventListener('click', closeMenu);
    $$('a', mmenu).forEach(function (a) { a.addEventListener('click', closeMenu); });
  }

  /* ---------- WhatsApp widget ---------- */
  (function () {
    var widget = $('#waWidget'), fab = $('#waFabBtn'), typing = $('#waTyping'), msg = $('#waMsg');
    if (!widget || !fab) return;
    var shown = false;
    fab.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = !widget.classList.contains('open');
      widget.classList.toggle('open', open);
      fab.setAttribute('aria-expanded', String(open));
      if (open && !shown) {
        shown = true;
        setTimeout(function () { typing.hidden = true; msg.hidden = false; }, reduceMotion ? 0 : 1000);
      }
    });
    document.addEventListener('click', function (e) {
      if (widget.classList.contains('open') && !widget.contains(e.target)) {
        widget.classList.remove('open'); fab.setAttribute('aria-expanded', 'false');
      }
    });
  })();

  /* ---------- Exit-intent popup (once per session) ---------- */
  // Programmatic scrolls (tab switches, anchor jumps) must not look like "leaving"
  var suppressExitUntil = 0;
  var exitApi = (function () {
    var backdrop = $('#exitBackdrop'), popup = $('#exitPopup');
    if (!popup) return { close: function () {}, isOpen: function () { return false; } };
    var shown = store('sessionStorage', 'as-exit-seen') === '1';
    var lastFocus = null;
    function open() {
      if (shown || Date.now() < suppressExitUntil || mmenu.classList.contains('open')) return;
      shown = true;
      lastFocus = document.activeElement;
      backdrop.classList.add('show'); popup.classList.add('show');
      popup.setAttribute('aria-hidden', 'false');
      store('sessionStorage', 'as-exit-seen', '1');
      $('#exitCta').focus();
    }
    function close() {
      if (!popup.classList.contains('show')) return;
      backdrop.classList.remove('show'); popup.classList.remove('show');
      popup.setAttribute('aria-hidden', 'true');
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    ['#exitClose', '#exitSkip', '#exitCta'].forEach(function (s) { $(s).addEventListener('click', close); });
    backdrop.addEventListener('click', close);
    document.addEventListener('mouseout', function (e) { if (!e.relatedTarget && e.clientY < 10) open(); });
    var maxY = 0, lastY = window.scrollY;
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      maxY = Math.max(maxY, y);
      if (maxY > 900 && y < lastY - 40 && y < 250) open();
      lastY = y;
    }, { passive: true });
    setTimeout(open, 45000);
    return { close: close, isOpen: function () { return popup.classList.contains('show'); } };
  })();

  /* ---------- Escape closes overlays ---------- */
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    exitApi.close(); closeMenu(); closeDropdowns();
    var w = $('#waWidget');
    if (w && w.classList.contains('open')) { w.classList.remove('open'); $('#waFabBtn').setAttribute('aria-expanded', 'false'); }
  });

  /* ---------- Cookie notice ---------- */
  (function () {
    var banner = $('#cookieBanner');
    if (!banner) return;
    if (!store('localStorage', 'as_cookie_choice')) setTimeout(function () { banner.classList.add('show'); }, 800);
    function choose(v) { store('localStorage', 'as_cookie_choice', v); banner.classList.remove('show'); }
    $('#cookieAccept').addEventListener('click', function () { choose('accepted'); });
    $('#cookieDeny').addEventListener('click', function () { choose('declined'); });
  })();

  /* ---------- Tab routing (#home sections, #sectors, #analytics, #dashboard) ---------- */
  var TABS = ['dashboard', 'analytics', 'sectors'];
  var panels = $$('.tab-panel');
  var currentTab = null;
  function activateTab(name) {
    if (name === currentTab) return;
    currentTab = name;
    panels.forEach(function (p) {
      var on = p.id === 'tab-' + name;
      p.classList.toggle('active', on);
      p.hidden = !on;
    });
    $$('[data-tab]').forEach(function (a) {
      var on = a.getAttribute('data-tab') === name;
      a.classList.toggle('active-link', on);
      if (on) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    var titles = {
      home: 'Auto Solution — AI Automation, Chatbots & Workflow Automation Studio',
      sectors: 'Industries We Serve — Auto Solution',
      analytics: 'Analytics Dashboard Demo — Auto Solution',
      dashboard: 'AI Live Dashboard Demo — Auto Solution'
    };
    document.title = titles[name] || titles.home;
    document.dispatchEvent(new CustomEvent('as:tabchange', { detail: { tab: name } }));
  }
  function route(initial) {
    suppressExitUntil = Date.now() + 2000;
    var hash = decodeURIComponent((location.hash || '').slice(1));
    if (TABS.indexOf(hash) > -1) {
      activateTab(hash);
      window.scrollTo(0, 0);
      return;
    }
    activateTab('home');
    if (hash && hash !== 'home') {
      var el = document.getElementById(hash);
      if (el) requestAnimationFrame(function () { el.scrollIntoView({ behavior: initial || reduceMotion ? 'auto' : 'smooth' }); });
    } else if (!initial) {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    }
  }
  window.addEventListener('hashchange', function () { route(false); });
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (a) suppressExitUntil = Date.now() + 2000;
  });
  route(true);

  /* ---------- Reveal on scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('show'); io.unobserve(e.target); } });
    }, { threshold: 0.1 });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('show'); });
  }

  function onceVisible(els, fn, threshold) {
    if (!('IntersectionObserver' in window)) { els.forEach(fn); return; }
    var o = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { fn(e.target); o.unobserve(e.target); } });
    }, { threshold: threshold || 0.3 });
    els.forEach(function (el) { o.observe(el); });
  }

  /* ---------- Count-up numbers ---------- */
  onceVisible($$('.countup'), function (el) {
    var target = parseFloat(el.dataset.target);
    var dec = parseInt(el.dataset.decimal || '0', 10);
    var suffix = el.dataset.suffix || '';
    var comma = el.dataset.comma === '1';
    function fmt(v) { return comma ? Math.round(v).toLocaleString('en-IN') : (dec ? v.toFixed(dec) : String(Math.round(v))); }
    if (reduceMotion) { el.textContent = fmt(target) + suffix; return; }
    var t0 = performance.now();
    (function frame(now) {
      var p = Math.min((now - t0) / 1400, 1);
      el.textContent = fmt(target * (1 - Math.pow(1 - p, 3))) + suffix;
      if (p < 1) requestAnimationFrame(frame);
    })(t0);
  }, 0.4);

  /* ---------- Rings, bars, sector bars ---------- */
  onceVisible($$('.outcome-charts'), function (el) {
    $$('.ring-fill', el).forEach(function (r) { r.style.strokeDashoffset = r.dataset.offset; });
  });
  onceVisible($$('#barChart'), function (el) {
    $$('.mbar', el).forEach(function (b, i) { setTimeout(function () { b.style.height = b.dataset.h + '%'; }, i * 120); });
  });
  onceVisible($$('.ring-stats'), function (el) {
    $$('.rstat-fill', el).forEach(function (f, i) { setTimeout(function () { f.style.width = f.dataset.w + '%'; }, i * 200); });
  });
  onceVisible($$('.sector-bars'), function (el) {
    $$('.sbr-fill', el).forEach(function (f, i) { setTimeout(function () { f.style.width = f.dataset.w + '%'; }, i * 90); });
  }, 0.2);

  /* ---------- FAQ accordion + search ---------- */
  (function () {
    var items = $$('.faq-item');
    items.forEach(function (item) {
      var btn = $('.faq-q', item);
      btn.addEventListener('click', function () {
        var open = !item.classList.contains('active');
        items.forEach(function (f) { f.classList.remove('active'); $('.faq-q', f).setAttribute('aria-expanded', 'false'); });
        item.classList.toggle('active', open);
        btn.setAttribute('aria-expanded', String(open));
      });
    });
    var input = $('#faqSearch'), empty = $('#faqEmpty');
    if (!input) return;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase(), n = 0;
      items.forEach(function (item) {
        var match = !q || item.textContent.toLowerCase().indexOf(q) > -1;
        item.hidden = !match;
        if (match) n++;
      });
      empty.hidden = n > 0;
    });
  })();

  /* ---------- Testimonial slider ---------- */
  (function () {
    var wrap = $('#tSlides');
    if (!wrap) return;
    var slides = $$('.t-slide', wrap), dotsWrap = $('#tDots'), idx = 0, timer = null;
    slides.forEach(function (s, i) {
      s.setAttribute('role', 'group');
      s.setAttribute('aria-roledescription', 'slide');
      s.setAttribute('aria-label', (i + 1) + ' of ' + slides.length);
      var d = document.createElement('button');
      d.type = 'button';
      d.className = 't-dot';
      d.setAttribute('aria-label', 'Show testimonial ' + (i + 1));
      d.addEventListener('click', function () { goTo(i); });
      dotsWrap.appendChild(d);
    });
    var dots = $$('.t-dot', dotsWrap);
    function goTo(i) {
      idx = (i + slides.length) % slides.length;
      slides.forEach(function (s, j) { s.classList.toggle('active', j === idx); s.setAttribute('aria-hidden', String(j !== idx)); });
      dots.forEach(function (d, j) { d.classList.toggle('active', j === idx); d.setAttribute('aria-current', String(j === idx)); });
      restart();
    }
    function stop() { if (timer) clearInterval(timer); timer = null; }
    function restart() { stop(); if (!reduceMotion) timer = setInterval(function () { goTo(idx + 1); }, 6000); }
    $('#tNext').addEventListener('click', function () { goTo(idx + 1); });
    $('#tPrev').addEventListener('click', function () { goTo(idx - 1); });
    var slider = $('#tSlider');
    slider.addEventListener('mouseenter', stop);
    slider.addEventListener('mouseleave', restart);
    slider.addEventListener('focusin', stop);
    slider.addEventListener('focusout', restart);
    goTo(0);
  })();

  /* ---------- Terminal typing ---------- */
  (function () {
    var body = $('#termBody');
    if (!body) return;
    var lines = [
      ['cmt', '# Auto Solution automation engine'],
      ['prompt', '$ python automate.py --task gst_reconciliation'],
      ['out', '[ok] Loading 1,247 transactions from Tally...'],
      ['out', '[ok] Validation passed: 99.9% match rate'],
      ['out', '[ok] Generating GSTR-1, GSTR-3B reports...'],
      ['out', '[ok] Sent via WhatsApp + Email'],
      ['cmt', '# Done in 4.2s, saved 3h 12m'],
      ['prompt', '$ _']
    ];
    var i = 0;
    function next() {
      if (i >= lines.length) return;
      var div = document.createElement('div');
      div.className = 'line';
      var s = document.createElement('span');
      s.className = lines[i][0];
      s.textContent = lines[i][1];
      div.appendChild(s);
      body.appendChild(div);
      i++;
      setTimeout(next, reduceMotion ? 0 : 600);
    }
    onceVisible([body], next);
  })();

  /* ---------- Lead form → WhatsApp ---------- */
  (function () {
    var form = $('#leadForm');
    if (!form) return;
    var fields = $$('[required]', form);
    function validate(el) {
      var err = $('#' + el.id + '-err');
      var ok = el.checkValidity();
      el.setAttribute('aria-invalid', String(!ok));
      if (err) err.textContent = ok ? '' : (el.validity.typeMismatch ? 'Enter a valid email address.' : 'This field is required.');
      return ok;
    }
    fields.forEach(function (el) {
      el.addEventListener('blur', function () { if (el.value) validate(el); });
      el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') validate(el); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var firstBad = null;
      fields.forEach(function (el) { if (!validate(el) && !firstBad) firstBad = el; });
      if (firstBad) { firstBad.focus(); return; }
      var fd = new FormData(form);
      function v(k, d) { var x = (fd.get(k) || '').toString().trim(); return x || d; }
      var text =
        '*New lead from autosolution website*\n\n' +
        'Name: ' + v('name', '') + '\n' +
        'Company: ' + v('company', '-') + '\n' +
        'Email: ' + v('email', '') + '\n' +
        'Phone: ' + v('phone', '-') + '\n' +
        'Country: ' + v('country', '-') + '\n' +
        'Service: ' + v('service', '') + '\n\n' +
        'Message:\n' + v('message', '');
      var btn = $('#submitBtn');
      var label = $('.fsub-label', btn);
      var original = label.textContent;
      btn.disabled = true;
      label.textContent = 'Opening WhatsApp...';
      window.open(waLink(text), '_blank', 'noopener');
      setTimeout(function () {
        btn.disabled = false;
        label.textContent = original;
        form.reset();
        $('#formStatus').textContent = 'WhatsApp opened with your details. Press send there to reach our team.';
      }, 600);
    });
  })();

  /* ---------- Checklist request → WhatsApp (no fake "subscribed") ---------- */
  (function () {
    var f = $('#newsForm');
    if (!f) return;
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = $('#newsEmail');
      if (!email.checkValidity()) { email.reportValidity(); return; }
      window.open(waLink('Hi Auto Solution! Please send the 2026 AI Automation Checklist to ' + email.value.trim()), '_blank', 'noopener');
      $('#newsStatus').textContent = 'WhatsApp opened. Send the message and we will share the checklist.';
      f.reset();
    });
  })();
})();
