"""Shared layout + components for the Auto Solution static site."""
from html import escape as e

SITE = "https://autosoluation.com"
CAL = "https://calendly.com/autosoluationai/30min"
WA_NUM = "917303897496"
WA = f"https://wa.me/{WA_NUM}?text=Hi%20Auto%20Solution!%20I%27d%20like%20to%20talk%20about%20automating%20some%20work."
EMAIL = "info@autosoluation.com"
PHONE = "+91 73038 97496"
TEL = "+917303897496"
ADDRESS = "Noida, Uttar Pradesh, India"
FORM_ENDPOINT = f"https://formsubmit.co/ajax/{EMAIL}"   # free email delivery for forms (activate once via email)

SPRITE = """<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">
<symbol id="i-wa" viewBox="0 0 448 512"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67-157zM224 438.7c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3 18.6-68-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
<symbol id="i-chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-bot" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V4M9 13h.01M15 13h.01M9 17h6"/></symbol>
<symbol id="i-flow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="6" cy="6" r="3"/><circle cx="18" cy="18" r="3"/><circle cx="18" cy="6" r="3"/><path d="M9 6h6M6 9v3a3 3 0 0 0 3 3h6"/></symbol>
<symbol id="i-doc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></symbol>
<symbol id="i-chart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></symbol>
<symbol id="i-cal" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></symbol>
<symbol id="i-server" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><path d="M6 6h.01M6 18h.01"/></symbol>
<symbol id="i-key" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/></symbol>
<symbol id="i-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></symbol>
<symbol id="i-target" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></symbol>
<symbol id="i-eye" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></symbol>
<symbol id="i-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></symbol>
<symbol id="i-zap" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></symbol>
<symbol id="i-in" viewBox="0 0 24 24"><path fill="currentColor" d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.4V9h3.4v1.6h.1c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.6V9h3.5v11.5zM22.2 0H1.8C.8 0 0 .8 0 1.7v20.6c0 .9.8 1.7 1.8 1.7h20.4c1 0 1.8-.8 1.8-1.7V1.7C24 .8 23.2 0 22.2 0z"/></symbol>
</svg>"""

LOGO = """<svg viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff8a00"/><stop offset="1" stop-color="#ff3d68"/></linearGradient></defs><rect width="64" height="64" rx="14" fill="#0a0f2c" stroke="url(#lg)" stroke-width="1.5"/><path d="M14 46 L26 18 L38 46 M19 38 L33 38" stroke="url(#lg)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="48" cy="22" r="6" fill="none" stroke="url(#lg)" stroke-width="2.6"/><circle cx="48" cy="22" r="2" fill="url(#lg)"/><path d="M42 30 Q48 36 54 30" stroke="url(#lg)" stroke-width="2.6" fill="none" stroke-linecap="round"/></svg>"""

def ic(name, cls=""):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def wa_ic(size=18):
    return ""  # WhatsApp logo removed site-wide by request

def btn_book(label="Book a free 30-min call", cls="btn btn-primary"):
    return f'<a class="{cls}" href="{CAL}" target="_blank" rel="noopener">{e(label)}</a>'

def btn_wa(label="Chat on WhatsApp", cls="btn btn-ghost"):
    return f'<a class="{cls}" href="{WA}" target="_blank" rel="noopener">{wa_ic()}{e(label)}</a>'

# ---------------- navigation data ----------------
NAV_PRODUCTS = [
    ("/products/paysentinel/", "PaySentinel", "Real-time payment fraud detection."),
    ("/products/gridsentinel/", "GridSentinel", "Energy theft and loss analytics for DISCOMs."),
    ("/products/fuelledger/", "FuelLedger", "Retail outlet integrity for fuel retail."),
    ("/pilot/", "Pilot program", "Prove the value on your own data in 6\u20138 weeks."),
    ("/products/", "All products", "Compare all three, and request a demo."),
]
NAV_SERVICES = [
    ("/services/ai-agents/", "AI agents &amp; chatbots", "Agents that answer, qualify, book and update your systems."),
    ("/services/workflow-automation/", "Workflow automation", "Excel, Python and integrations that run your busywork."),
    ("/services/document-ai/", "Document AI &amp; OCR", "Invoices, contracts and scans turned into clean data."),
    ("/services/data-analytics/", "Data, forecasting &amp; dashboards", "Predict demand, catch anomalies, see numbers live."),
]
NAV_INDUSTRIES = [
    ("/industries/finance/", "Finance &amp; CA firms", "GST, reconciliation and client reporting."),
    ("/industries/logistics/", "Logistics", "Tracking, alerts and courier integrations."),
    ("/industries/ecommerce/", "D2C &amp; e-commerce", "Forecasting, catalog and order sync."),
    ("/industries/real-estate/", "Real estate", "Enquiry agents, follow-ups and site visits."),
    ("/industries/manufacturing/", "Manufacturing", "Live production and downtime dashboards."),
    ("/industries/healthcare/", "Healthcare &amp; clinics", "Records, reminders and billing."),
]
NAV_RESOURCES = [
    ("/case-studies/", "Case studies", "How clients got hours back."),
    ("/insights/", "Insights", "Practical guides on automation and AI."),
    ("/roi-calculator/", "ROI calculator", "Estimate the hours your team could save."),
    ("/ai-automation-checklist/", "Free checklist (PDF)", "Find the work worth automating first."),
]
NAV_COMPANY = [
    ("/about/", "About us", "Who we are and how we think."),
    ("/how-we-work/", "How we work", "Pilots, projects and care plans."),
    ("/security/", "Security &amp; trust", "How we protect your data and systems."),
    ("/careers/", "Careers", "Join a remote, senior team."),
    ("/contact/", "Contact", "Book a call or message us."),
]

def mm_panel(pid, items, foot=""):
    links = "".join(f'<a href="{h}"><strong>{t}</strong><span>{d}</span></a>' for h, t, d in items)
    return f'<div class="mm" id="{pid}"><div class="mm-in">{links}{foot}</div></div>'

def header(active=""):
    def mb(pid, label):
        cur = ' aria-current="page"' if active == pid else ""
        return f'<button class="mm-btn" type="button" aria-expanded="false" aria-controls="mm-{pid}"{cur}>{label}<svg aria-hidden="true"><use href="#i-chev"/></svg></button>'
    def ln(href, label, key):
        cur = ' aria-current="page"' if active == key else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    foot_s = f'<div class="mm-foot"><span>Not sure where to start? We\u2019ll map it with you on a free call.</span><a class="tlink" href="{CAL}" target="_blank" rel="noopener">Book a free 30-min call</a></div>'
    foot_i = '<div class="mm-foot"><span>Don\u2019t see your industry? If the work is repetitive and rule-based, we can probably automate it.</span><a class="tlink" href="/contact/">Tell us about your work</a></div>'
    def dsec(title, items):
        return f'<details><summary>{title}</summary>' + "".join(f'<a href="{h}">{t}</a>' for h, t, _ in items) + "</details>"
    return f"""{SPRITE}
<a class="skip" href="#main">Skip to content</a>
<header class="hdr" id="hdr">
  <a class="annc" href="/pilot/"><span class="annc-tag">New</span>GridSentinel and FuelLedger are now pilot-ready. <u>Apply for a pilot</u></a>
  <div class="hdr-in">
    <a class="brand" href="/" aria-label="Auto Solution home">{LOGO}<span>Auto Solution</span></a>
    <nav class="mainnav" aria-label="Main">
      {mb("products","Products")}{mb("services","Services")}{mb("industries","Industries")}{mb("resources","Resources")}{mb("company","Company")}
      {ln("/case-studies/","Case studies","cases")}
    </nav>
    <div class="hdr-cta">{btn_book("Book a call","btn btn-outline btn-sm")}<a class="btn btn-primary btn-sm" href="/request-demo/">Request a demo</a></div>
    <button class="menu-btn" id="menuBtn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><svg width="24" height="24"><use href="#i-menu"/></svg></button>
  </div>
  {mm_panel("mm-products", NAV_PRODUCTS, '<div class="mm-foot"><span>See any product running on sample data.</span><a class="tlink" href="/request-demo/">Request a demo</a></div>')}
  {mm_panel("mm-services", NAV_SERVICES, foot_s)}
  {mm_panel("mm-industries", NAV_INDUSTRIES, foot_i)}
  {mm_panel("mm-resources", NAV_RESOURCES)}
  {mm_panel("mm-company", NAV_COMPANY)}
</header>
<nav class="drawer" id="drawer" aria-label="Mobile">
  {dsec("Products", NAV_PRODUCTS)}{dsec("Services", NAV_SERVICES)}{dsec("Industries", NAV_INDUSTRIES)}{dsec("Resources", NAV_RESOURCES)}{dsec("Company", NAV_COMPANY)}
  <a class="btn btn-primary" href="/request-demo/">Request a demo</a>
  {btn_book(cls="btn btn-outline")}
</nav>"""

def footer():
    def col(title, items):
        return f'<nav aria-label="{title}"><h2>{title}</h2>' + "".join(f'<a href="{h}">{t}</a>' for h, t, _ in items) + "</nav>"
    return f"""<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <div>
        <a class="brand" href="/">{LOGO}<span>Auto Solution</span></a>
        <p>AI that finds where money goes missing: payment fraud, energy theft and fuel loss. Plus custom automation for busy teams. Founded 2026, Noida.</p>
        <div class="ftr-contact">
          <a href="tel:{TEL}">{ic("phone")}{PHONE}</a>
          <a href="mailto:{EMAIL}">{ic("mail")}{EMAIL}</a>
          <span style="color:var(--d-muted)">{ADDRESS}</span>
        </div>
      </div>
      {col("Products", NAV_PRODUCTS[:4])}{col("Services", NAV_SERVICES)}{col("Resources", NAV_RESOURCES)}{col("Company", NAV_COMPANY)}
    </div>
    <div class="ftr-bot"><span>© <span class="yr">2026</span> Auto Solution. All rights reserved.</span><span><a href="/privacy/">Privacy policy</a><a href="/terms/">Terms of use</a></span></div>
  </div>
</footer>
<div class="mbar" id="mbar">{btn_book("Book a call","btn btn-ghost")}<a class="btn btn-primary" href="/request-demo/">Request a demo</a></div>"""

def page(path, title, desc, body, active="", extra_js="", schema=""):
    canon = SITE + path
    full_title = title if "Auto Solution" in title else f"{title} | Auto Solution"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0a0f2c">
<meta property="og:type" content="website"><meta property="og:site_name" content="Auto Solution">
<meta property="og:title" content="{e(full_title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/geist-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">
<script defer src="/_vercel/insights/script.js"></script>
{schema}
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
{extra_js}<script src="/assets/js/site.js" defer></script>
</body>
</html>"""

# ---------------- components ----------------
def phero(title, lede, crumbs, actions=True, right="", tags=None, h="h1"):
    cr = '<ol class="crumbs">' + "".join(
        (f'<li><a href="{u}">{t}</a></li>' if u else f'<li aria-current="page">{t}</li>') for t, u in crumbs) + "</ol>"
    tg = ('<ul class="tags">' + "".join(f'<li class="tag">{t}</li>' for t in tags) + "</ul>") if tags else ""
    if isinstance(actions, str):
        act = f'<div class="btns">{actions}</div>'
    else:
        act = f'<div class="btns">{btn_book()}<a class="btn btn-outline" href="/request-demo/">Request a demo</a></div>' if actions else ""
    left = f'<div>{cr}<h1 class="{h}">{title}</h1><p class="lede">{lede}</p>{tg}{act}</div>'
    inner = f'<div class="duo">{left}<div>{right}</div></div>' if right else f'<div style="max-width:860px">{left}</div>'
    return f'<section class="phero{" has-ui" if right else ""}"><div class="wrap">{inner}</div></section>'

def cta_band(title="Find out what you could automate", lede="A free 30-minute call. We look at how your team works today and show you what\u2019s worth automating, with no obligation."):
    return f"""<section class="sec tight"><div class="wrap"><div class="cta-band rv no-mbar"><div class="row">
<div style="max-width:620px"><h2 class="h2">{title}</h2><p class="lede">{lede}</p></div>
<div class="btns" style="margin:0"><a class="btn btn-primary" href="/request-demo/">Request a demo</a>{btn_book("Book a free 30-min call","btn btn-ghost")}</div></div></div></div></section>"""

def checks(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f'<li>{ic("check")}<span>{t}</span></li>' for t in items) + "</ul>"

def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"

def faq_schema(items):
    import json, re
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub("<[^>]+>", "", q), "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in items]}
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"

def steps(items, n=None):
    n = n or len(items)
    return f'<ol class="steps" style="--n:{n}">' + "".join(
        f'<li><span class="n">{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(items)) + "</ol>"

# ---------------- product UI mockups ----------------
def ui_chat(name="Support agent"):
    return f"""<div class="ui ui-chat" aria-hidden="true"><div class="ui-bar"><i></i><i></i><i></i><span>{name}</span><span class="r">online</span></div>
<div class="b u">Is order #4821 shipped yet?</div>
<div class="act">{ic("check")} Looked up order in Shopify</div>
<div class="b a">Yes, it left our warehouse today. Tracking: BD48211. Expected Thursday.</div>
<div class="b u">Can I change the address?</div>
<div class="act">{ic("check")} Updated address with courier</div>
<div class="b a">Done. New address saved and the courier has it.</div></div>"""

def ui_flow():
    return """<div class="ui ui-flow" aria-hidden="true"><div class="ui-bar"><i></i><i></i><i></i><span>month_end_reports</span><span class="r">running</span></div>
<svg viewBox="0 0 360 170"><path class="wire on" d="M92 40 H130"/><path class="wire on" d="M228 40 H262"/><path class="wire" d="M180 58 V96"/><path class="wire" d="M228 120 H262"/>
<g class="nd on"><rect x="8" y="20" width="84" height="40" rx="8"/><text x="18" y="38">Tally</text><text class="sub" x="18" y="52">1,247 rows</text></g>
<g class="nd on"><rect x="130" y="20" width="98" height="40" rx="8"/><text x="140" y="38">Clean &amp; match</text><text class="sub" x="140" y="52">Python</text></g>
<g class="nd on"><rect x="262" y="20" width="90" height="40" rx="8"/><text x="272" y="38">Excel report</text><text class="sub" x="272" y="52">50 sheets</text></g>
<g class="nd"><rect x="130" y="96" width="98" height="44" rx="8"/><text x="140" y="115">Exceptions</text><text class="sub" x="140" y="129">9 for review</text></g>
<g class="nd"><rect x="262" y="96" width="90" height="44" rx="8"/><text x="272" y="115">Email + WhatsApp</text><text class="sub" x="272" y="129">to finance team</text></g></svg></div>"""

def ui_doc():
    return """<div class="ui ui-doc" aria-hidden="true"><div class="ui-bar"><i></i><i></i><i></i><span>invoice_0482.pdf</span><span class="r">extracting</span></div>
<div class="cols"><div class="paper"><span class="scan"></span><b>TAX INVOICE</b><div class="ln" style="width:70%"></div>Vendor: <span class="hl">Mehta Traders</span><div class="ln"></div>GSTIN: <span class="hl">09AAB…1Z5</span><div class="ln" style="width:60%"></div>Total: <span class="hl">₹48,260</span><div class="ln" style="width:80%"></div>Due: <span class="hl">12 Nov</span></div>
<div class="json">{<br>&nbsp;"vendor": <b>"Mehta Traders"</b>,<br>&nbsp;"gstin": <b>"09AAB…1Z5"</b>,<br>&nbsp;"total": <b>48260</b>,<br>&nbsp;"due": <b>"2026-11-12"</b>,<br>&nbsp;"status": <b>"posted"</b><br>}</div></div></div>"""

def ui_dash():
    return """<div class="ui ui-dash" aria-hidden="true"><div class="ui-bar"><i></i><i></i><i></i><span>demand_forecast</span><span class="r">live</span></div>
<div class="kp"><div><small>Next 30 days</small><b>18,420</b></div><div><small>Overstock risk</small><b class="up">−23%</b></div><div><small>Accuracy</small><b>94%</b></div></div>
<svg viewBox="0 0 320 110"><defs><linearGradient id="dg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4fe3ff" stop-opacity=".35"/><stop offset="1" stop-color="#4fe3ff" stop-opacity="0"/></linearGradient></defs>
<path d="M0 80 L30 72 L60 76 L90 60 L120 64 L150 48 L180 54 L200 40" fill="none" stroke="#a3abcf" stroke-width="2"/>
<path d="M200 40 L230 34 L260 38 L290 24 L320 28 L320 110 L200 110 Z" fill="url(#dg)"/><path d="M200 40 L230 34 L260 38 L290 24 L320 28" fill="none" stroke="#4fe3ff" stroke-width="2.4" stroke-dasharray="5 4"/>
<line x1="200" y1="0" x2="200" y2="110" stroke="rgba(150,170,255,.3)" stroke-dasharray="3 3"/><text x="206" y="12" fill="#a3abcf" font-size="9">forecast</text></svg></div>"""

def ui_pay(live=False):
    rows=[("TXN 8F21A","₹2,450","UPI","0.04","ok","Approve"),("TXN 8F21B","₹98,000","Card","0.91","bad","Decline"),
          ("TXN 8F21C","₹14,999","Card","0.58","mid","Review"),("TXN 8F21D","₹640","UPI","0.02","ok","Approve"),("TXN 8F21E","₹49,500","Netbank","0.73","mid","Review")]
    tr="".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class="mono">{d}</td><td><span class="dec {e}">{f}</span></td></tr>' for a,b,c,d,e,f in rows)
    return f"""<div class="ui ui-pay" aria-hidden="true"><div class="ui-bar"><i></i><i></i><i></i><span>PaySentinel: live scoring</span><span class="r">{'<span class="livedot"></span>live demo' if live else 'sample data'}</span></div>
<table class="utbl"><thead><tr><th>Transaction</th><th>Amount</th><th>Rail</th><th>Score</th><th>Decision</th></tr></thead><tbody{' id="liveTbl"' if live else ''}>{tr}</tbody></table>
<div class="drift"><span>Drift</span><b class="ok">Stable</b><span>Model</span><b>v14</b><span>Latency</span><b>38 ms</b></div></div>"""

def ui_grid():
    rows=[("DT-0417","Sector 12","18.6%","high"),("DT-0233","Industrial Rd","11.2%","mid"),("DT-0891","Old Market","9.4%","mid"),("DT-0152","Green Park","2.1%","ok")]
    tr="".join(f'<tr><td class="mono">{a}</td><td>{b}</td><td><span class="bar {d}" style="--w:{float(c[:-1])*4.5}%"></span><span class="mono">{c}</span></td></tr>' for a,b,c,d in rows)
    return f"""<div class="ui ui-grid" aria-hidden="true"><div class="ui-bar"><i></i><i></i><i></i><span>GridSentinel: transformer balance</span><span class="r">sample data</span></div>
<table class="utbl"><thead><tr><th>Transformer</th><th>Area</th><th>Unexplained loss</th></tr></thead><tbody>{tr}</tbody></table>
<div class="lead"><b>Top lead</b> Consumer #44817 on DT-0417: night load with zero billed units for 3 cycles. <span>Likely bypass. Inspect meter and incoming cable.</span></div></div>"""

def ui_fuel():
    steps=[("Invoiced","12,000 L",100),("Received","11,940 L",99.5),("Sold","11,610 L",96.75),("Collected","₹11.52L",95.4)]
    bars="".join(f'<div class="fs"><span>{a}</span><div class="ft"><i style="width:{w}%"></i></div><b class="mono">{v}</b></div>' for a,v,w in steps)
    return f"""<div class="ui ui-fuel" aria-hidden="true"><div class="ui-bar"><i></i><i></i><i></i><span>FuelLedger: Outlet RO-2291, today</span><span class="r">sample data</span></div>
{bars}<div class="gaps"><span class="g mid">Transit gap 60 L</span><span class="g bad">Stock gap 330 L</span><span class="g mid">Night level drop, Tank 2</span></div></div>"""

UI = {"chat": ui_chat, "flow": ui_flow, "doc": ui_doc, "dash": ui_dash, "pay": ui_pay, "grid": ui_grid, "fuel": ui_fuel}
