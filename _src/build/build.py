"""Build the Auto Solution site:  python3 build/build.py  -> writes into site/"""
import os, json
from layout import *
from content import SERVICES, INDUSTRIES, CASES, CASE_BY, SERVICE_BY
from posts import POSTS
from products import PRODUCTS, PRODUCT_BY

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))  # repo root
PAGES = []

def write(path, html):
    fp = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    if path.endswith(".html"):
        fp = os.path.join(OUT, path.strip("/"))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(html)
    if not path.endswith(".html"):
        PAGES.append(path)

def case_card(c, cls="card case-card rv"):
    return f'''<a class="{cls}" href="/case-studies/{c["slug"]}/"><p class="metric">{c["metric"]}</p>
<ul class="tags"><li class="tag">{c["tagind"]}</li><li class="tag">{c["loc"]}</li></ul>
<h3 class="h3">{c["title"]}</h3><p>{c["short"]}</p><span class="tlink">Read the case study</span></a>'''

def svc_card(s):
    return f'''<a class="card svc-card rv" href="/services/{s["slug"]}/">{UI[s["ui"]]()}<div class="body">
<h3 class="h3">{s["name"]}</h3><p>{s["short"]}</p><span class="tlink">Explore</span></div></a>'''

QUOTES = [
 ("Our monthly GST reconciliation used to eat an entire day. Now it runs itself before we\u2019ve even had coffee.", "Operations head", "CA firm, India"),
 ("The forecasting model paid for itself in the first quarter through reduced overstock alone.", "Supply chain manager", "D2C brand, India"),
 ("We were nervous about handing financial workflows to a script. Zero errors since launch changed our minds fast.", "Finance lead", "Logistics company, UAE"),
]
def quotes():
    return '<div class="quotes">' + "".join(
        f'<figure class="card quote rv"><blockquote>\u201c{q}\u201d</blockquote><figcaption><b>{n}</b>{r}</figcaption></figure>' for q, n, r in QUOTES) + "</div>"

TOOLS = ["Tally","SAP","Salesforce","Zoho","HubSpot","QuickBooks","Shopify","Google Sheets","Slack","WhatsApp","OpenAI","Claude","n8n","Make","Zapier","Python"]
def stack():
    li = "".join(f"<li>{t}</li>" for t in TOOLS) + "".join(f'<li aria-hidden="true">{t}</li>' for t in TOOLS)
    return f'<section class="stack" aria-label="Tools we integrate with"><p>Plugs into the tools your team already runs on</p><div class="mq"><ul>{li}</ul></div></section>'

MODELS = [
 ("Pilot","For teams trying automation for the first time","One workflow automated end to end in 1\u20132 weeks. See it run on your own data before deciding on anything bigger.",["One high-impact workflow","Fixed price, agreed upfront","Handover and training"]),
 ("Project","For a set of connected workflows","A fixed-scope build across several processes, with integrations, dashboards and documentation.",["Written scope in 3 business days","Weekly progress updates","15 days of free support after launch"]),
 ("Care plan","For automations that must never stop","Monthly monitoring, fixes and small improvements once your automations are live.",["Run monitoring and alerts","Fixes when your tools change","Small upgrades each month"]),
]
def models():
    out = '<div class="grid-3">'
    for i,(n,f,d,pts) in enumerate(MODELS):
        flag = '<span class="tag" style="align-self:flex-start;background:var(--flux);color:var(--flux-ink);border-color:var(--flux);font-weight:600">Recommended</span>' if i==1 else ""
        border = ' style="border-color:var(--flux);display:flex;flex-direction:column;gap:12px"' if i==1 else ' style="display:flex;flex-direction:column;gap:12px"'
        out += f'<article class="card rv"{border}>{flag}<h3 class="h3">{n}</h3><p style="color:var(--signal-ink);font-size:.93rem">{f}</p><p>{d}</p><div style="margin-top:auto;padding-top:12px">{checks(pts)}</div></article>'
    return out + "</div>"

PROCESS = [("Free 30-min call","We map your manual work and spot what\u2019s worth automating."),
           ("Scope in 3 days","A written scope, timeline and fixed price within three business days."),
           ("Build","Usually 3 days to 4 weeks, with weekly progress updates."),
           ("Handover","Training for your team and complete documentation."),
           ("15 days of support","Free fixes for edge cases while your team settles in.")]

ZONES = [("India (HQ, Noida)","Asia/Kolkata"),("Dubai","Asia/Dubai"),("Singapore","Asia/Singapore"),("London","Europe/London"),("New York","America/New_York")]
def zones():
    return '<ul class="zones">' + "".join(f'<li data-tz="{tz}"><span>{n}</span><b>--:--</b></li>' for n, tz in ZONES) + '</ul><p class="muted" style="font-size:.9rem;margin-top:12px">Highlighted cities are in business hours right now.</p>'

SECURITY = [("shield","NDA before anything else","Signed before we see a single file or system."),
            ("server","Runs in your environment","Your servers or your approved cloud account, not ours."),
            ("key","Least-privilege access","Only the access a task needs, revoked at handover."),
            ("list","Every run is logged","See exactly what ran, when, and on what data.")]
def security(dark=False):
    return '<div class="grid-4">' + "".join(f'<div class="card rv"><div class="ico">{ic(i)}</div><h3 class="h3">{t}</h3><p>{d}</p></div>' for i,t,d in SECURITY) + "</div>"

FOUNDER_NOTE = ("We started Auto Solution after watching skilled people lose whole days to copy-paste and spreadsheet chores. Every automation we ship is judged by one question: did someone get their time back?",
                "If the call shows automation isn\u2019t worth it for you, we\u2019ll say so.")
def founder_block():
    return f'''<figure class="founder rv"><img src="/assets/img/founder-1-800.webp" srcset="/assets/img/founder-1-400.webp 400w, /assets/img/founder-1-800.webp 800w" sizes="(max-width:960px) 280px, 320px" width="800" height="800" alt="Harsh Vardhan, founder of Auto Solution" loading="lazy">
<div><p class="kicker">A note from our founder</p><blockquote><p>{FOUNDER_NOTE[0]}</p><p>{FOUNDER_NOTE[1]}</p></blockquote><figcaption><b>Harsh Vardhan</b>Founder, Auto Solution</figcaption></div></figure>'''

def checklist_promo():
    return f'''<section class="sec tight"><div class="wrap"><div class="card rv promo"><div><p class="kicker">Free download</p><h2 class="h2" style="font-size:clamp(1.5rem,2.6vw,2.1rem)">The AI Automation Checklist</h2><p style="margin-top:10px">Find the work worth automating first, score it in 20 minutes, and avoid the mistakes that sink most first projects. 5 pages, PDF.</p></div><a class="btn btn-primary" href="/ai-automation-checklist/">Get the free checklist</a></div></div></section>'''

def stage_tag(p, light=False):
    return f'<span class="stage">{p["stage"]}</span>' if p["stage"] else ""

def prod_card(p):
    return f'''<a class="card prod-card rv" href="/products/{p["slug"]}/">{UI[p["ui"]]()}<div class="body">
<div class="prod-row"><span class="pname">{p["name"]}</span>{stage_tag(p)}</div><p class="ptag">{p["tagline"]}</p><p>{p["short"]}</p>
<p style="font-size:.92rem">For {", ".join(x.split(" (")[0].lower() for x in p["for_"][:3])}</p><span class="tlink">Explore {p["name"]}</span></div></a>'''

def products_grid():
    return '<div class="grid-3">' + "".join(prod_card(p) for p in PRODUCTS) + "</div>"

def demo_btn(label="Request a demo", cls="btn btn-primary", product=""):
    q = f"?product={product}" if product else ""
    return f'<a class="{cls}" href="/request-demo/{q}">{label}</a>'

TABS = [
 ("paysentinel","PaySentinel","pay","Real-time payment fraud detection","Stop fraud before the money moves.",["Fraud score and approve, review or decline on every transaction","Learns from your own transaction history","Drift monitoring with versioned models and rollback"],"/products/paysentinel/"),
 ("gridsentinel","GridSentinel","grid","Energy theft and loss analytics","Find where energy goes missing.",["Transformer-level energy balance","Separates theft from faulty meters and data gaps","Explainable, ranked leads for field teams"],"/products/gridsentinel/"),
 ("fuelledger","FuelLedger","fuel","Retail outlet integrity for fuel retail","Every litre, accounted for.",["Four-way reconciliation for every outlet, every day","Density, leak and short-dispensing checks","Transporter and fleet card scorecards"],"/products/fuelledger/"),
 ("agents","AI agents","chat","AI agents &amp; chatbots","Agents that get the work done.",["Answer customers 24/7 on WhatsApp and web","Qualify leads and book meetings","Update your CRM and systems automatically"],"/services/ai-agents/"),
 ("workflow","Automation","flow","Workflow automation","Your busywork, running on its own.",["Excel, Python and integration automation","Reconciliations and reports on schedule","Built around the tools you already use"],"/services/workflow-automation/"),
]
def simulator():
    cats = [("groceries","Groceries"),("travel","Travel"),("electronics","Electronics"),("gaming","Gaming"),("giftcards","Gift cards"),("crypto","Crypto exchange")]
    opts = "".join(f'<option value="{k}"{" selected" if k=="electronics" else ""}>{n}</option>' for k,n in cats)
    return f'''<section class="sec sim-sec" id="try" aria-labelledby="sim-h"><div class="wrap">
  <div class="sec-head center"><p class="kicker">Try it yourself</p><h2 class="h2" id="sim-h">Score a payment the way PaySentinel does</h2><p class="lede">Change the transaction and watch the fraud score, the decision and the reasons update instantly.</p></div>
  <div class="sim">
    <form class="sim-in" id="sim" onsubmit="return false">
      <div><label for="s-amt">Amount <output id="so-amt">₹24,999</output></label><input type="range" id="s-amt" min="100" max="200000" step="100" value="24999"></div>
      <div><label for="s-hr">Time of day <output id="so-hr">14:00</output></label><input type="range" id="s-hr" min="0" max="23" value="14"></div>
      <div><label for="s-vel">Payments from this device, last hour <output id="so-vel">2</output></label><input type="range" id="s-vel" min="1" max="20" value="2"></div>
      <div class="sim-row"><div class="f"><label for="s-cat">Merchant category</label><select id="s-cat">{opts}</select></div></div>
      <div class="sim-toggles">
        <label class="tg"><input type="checkbox" id="s-new"><span></span>New device</label>
        <label class="tg"><input type="checkbox" id="s-geo"><span></span>Card country differs</label>
      </div>
    </form>
    <div class="sim-out" aria-live="polite">
      <div class="gauge"><svg viewBox="0 0 200 110" aria-hidden="true"><path d="M15 100 A85 85 0 0 1 185 100" fill="none" stroke="rgba(150,170,255,.18)" stroke-width="14" stroke-linecap="round"/><path id="gArc" d="M15 100 A85 85 0 0 1 185 100" fill="none" stroke="url(#gg)" stroke-width="14" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"/><defs><linearGradient id="gg" x1="0" x2="1"><stop offset="0" stop-color="#25d366"/><stop offset=".5" stop-color="#ffc14d"/><stop offset="1" stop-color="#ff5a5a"/></linearGradient></defs></svg>
        <div class="g-val"><b class="mono" id="sScore">0.12</b><span>fraud score</span></div></div>
      <p class="sim-dec"><span class="dec ok" id="sDec">Approve</span></p>
      <h3 class="sim-h3">Why</h3>
      <ul class="why" id="sWhy"></ul>
      <p class="sim-note">Simplified demo model for illustration. PaySentinel learns these patterns from your own transaction history.</p>
    </div>
  </div>
  <p style="text-align:center;margin-top:28px"><a class="tlink" href="/products/paysentinel/">How PaySentinel works</a></p>
</div></section>'''

def architecture():
    return f'''<section class="sec dark arch-sec" aria-labelledby="arch-h"><div class="wrap">
  <div class="sec-head center"><p class="kicker">Under the hood</p><h2 class="h2" id="arch-h">From raw data to a decision you can trust</h2><p class="lede">Every Auto Solution product runs on the same production pipeline, built to be explainable, monitored and safe to change.</p></div>
  <div class="arch" aria-label="Pipeline: data sources, validation, features, versioned models, decisions, monitoring and feedback">
    <svg class="arch-wires" viewBox="0 0 1000 120" preserveAspectRatio="none" aria-hidden="true"><path d="M60 60 H940" class="aw"/><path d="M60 60 H940" class="aw on"/></svg>
    <ol class="arch-nodes">
      <li><span class="an-ic">{ic("server")}</span><b>Your data</b><span>Payments, meters, outlets, ERP</span></li>
      <li><span class="an-ic">{ic("shield")}</span><b>Validate</b><span>Schema checks, bad-data alerts</span></li>
      <li><span class="an-ic">{ic("flow")}</span><b>Features</b><span>Behaviour, timing, balance</span></li>
      <li><span class="an-ic">{ic("target")}</span><b>Models</b><span>Versioned, with rollback</span></li>
      <li><span class="an-ic">{ic("zap")}</span><b>Decisions</b><span>API, dashboards, alerts</span></li>
      <li><span class="an-ic">{ic("eye")}</span><b>Monitor</b><span>Drift, accuracy, feedback</span></li>
    </ol>
    <p class="arch-loop">{ic("list")}Field outcomes and reviews feed back into the next model version</p>
  </div>
  <div class="grid-3 arch-cards">
    <div class="card"><h3 class="h3">Explainable by default</h3><p>Every flag carries the reasons behind it, so analysts and field teams can check it, not just trust it.</p></div>
    <div class="card"><h3 class="h3">Humans stay in charge</h3><p>Borderline cases go to review. You decide the thresholds, and every automated decision is logged.</p></div>
    <div class="card"><h3 class="h3">Deploy where your data lives</h3><p>On-premise, in your own cloud account, or isolated from the internet when your security team requires it.</p></div>
  </div>
</div></section>'''

def tabs():
    btns = "".join(f'<button role="tab" type="button" id="t-{k}" aria-controls="tp-{k}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}">{n}</button>' for i,(k,n,*_) in enumerate(TABS))
    panels = ""
    for i,(k,n,ui,cat,tag,pts,href) in enumerate(TABS):
        st = PRODUCT_BY.get(k)
        badge = stage_tag(st) if st else ""
        panels += f'''<div class="tpanel" role="tabpanel" id="tp-{k}" aria-labelledby="t-{k}"{"" if i==0 else " hidden"}><div class="tp-copy"><p class="pcat">{cat}</p><h3 class="h2" style="font-size:clamp(1.6rem,2.6vw,2.2rem)">{tag}</h3><div class="prod-row" style="margin:14px 0 4px">{badge}</div><div style="margin-top:18px">{checks(pts)}</div><div class="btns">{demo_btn(product=k) if st else btn_book("Book a free call","btn btn-primary")}<a class="tlink" href="{href}">Learn more about {n}</a></div></div><div class="tp-ui">{UI[ui]()}</div></div>'''
    return f'<div class="tabs"><div class="tablist" role="tablist" aria-label="Products and services">{btns}</div>{panels}</div>'

def product_pages():
    body = phero("AI that finds where money goes missing", "Three products that catch loss before it hits the books: payment fraud, energy theft and fuel loss. Each one learns from your own data and explains every flag it raises.", [("Home","/"),("Products",None)], actions=demo_btn() + '<a class="btn btn-outline" href="/pilot/">See the pilot program</a>')
    body += f'<section class="sec"><div class="wrap">{products_grid()}</div></section>'
    body += f'''<section class="sec white"><div class="wrap"><div class="sec-head"><p class="kicker">How every product works</p><h2 class="h2">Built the same careful way</h2></div><div class="grid-4">
<div class="card rv"><div class="ico">{ic("target")}</div><h3 class="h3">Learns from your data</h3><p>Models are trained on your own history, not generic rules.</p></div>
<div class="card rv"><div class="ico">{ic("eye")}</div><h3 class="h3">Explains every flag</h3><p>Each alert comes with reasons a person can check.</p></div>
<div class="card rv"><div class="ico">{ic("server")}</div><h3 class="h3">Runs in your environment</h3><p>Your data stays on your servers or approved cloud.</p></div>
<div class="card rv"><div class="ico">{ic("zap")}</div><h3 class="h3">Improves over time</h3><p>Outcomes feed back so the model gets sharper.</p></div></div></div></section>'''
    body += architecture()
    body += cta_band("See a product run on sample data", "Book a demo and we\u2019ll walk you through it on realistic sample data, then talk about a pilot on yours.")
    write("/products/", page("/products/", "Products: PaySentinel, GridSentinel, FuelLedger", "AI products from Auto Solution: PaySentinel for payment fraud, GridSentinel for energy theft and losses, FuelLedger for fuel retail integrity.", body, active="products"))
    for p in PRODUCTS:
        hero = f'''<section class="phero has-ui"><div class="wrap"><div class="duo"><div>
<ol class="crumbs"><li><a href="/">Home</a></li><li><a href="/products/">Products</a></li><li aria-current="page">{p["name"]}</li></ol>
<p class="pcat">{p["name"]}: {p["cat"]}</p><h1 class="h1">{p["tagline"]}</h1><p class="lede">{p["lede"]}</p>
<div class="prod-row" style="margin-top:22px">{stage_tag(p)}</div>
<div class="btns">{demo_btn(product=p["slug"])}{btn_book("Book a call","btn btn-outline")}</div></div><div>{UI[p["ui"]]()}</div></div></div></section>'''
        feats = "".join(f'<div class="card rv"><div class="ico">{ic("check")}</div><h3 class="h3">{t}</h3><p>{d}</p></div>' for t, d in p["features"])
        b = hero + f'<section class="sec"><div class="wrap"><div class="sec-head"><p class="kicker">Capabilities</p><h2 class="h2">What {p["name"]} does</h2></div><div class="feat">{feats}</div></div></section>'
        how_title = "Four-way reconciliation, every outlet, every day" if p["slug"]=="fuelledger" else "How it works"
        if p["slug"] == "paysentinel": b += simulator()
        b += f'<section class="sec dark"><div class="wrap"><div class="sec-head"><p class="kicker">How it works</p><h2 class="h2">{how_title}</h2></div>{steps(p["how"])}</div></section>'
        who = "".join(f"<li>{x}</li>" for x in p["for_"])
        b += f'''<section class="sec white"><div class="wrap duo" style="align-items:start">
<div class="rv"><p class="kicker">Built for</p><h2 class="h2">Who it\u2019s for</h2><ul class="who" style="margin-top:24px">{who}</ul></div>
<div class="rv"><p class="kicker">Getting started</p><h2 class="h2">What a pilot looks like</h2><div style="margin-top:24px">{checks(["6\u20138 weeks on your own historical data, inside your environment","Shadow mode: no impact on live systems","Success criteria agreed upfront, with a clear go or no-go at the end","Fixed fee, credited in full if you roll out"])}</div><a class="tlink" style="margin-top:20px" href="/pilot/">See the pilot program</a></div></div></section>'''
        b += f'<section class="sec"><div class="wrap faq-wrap"><div><p class="kicker">FAQ</p><h2 class="h2">Questions about {p["name"]}</h2></div>{faq(p["faq"])}</div></section>'
        others = [o for o in PRODUCTS if o["slug"] != p["slug"]]
        b += f'<section class="sec white tight"><div class="wrap"><div class="sec-head"><p class="kicker">More products</p><h2 class="h2" style="font-size:1.8rem">Also from Auto Solution</h2></div><div class="grid-2">{"".join(prod_card(o) for o in others)}</div></div></section>'
        b += cta_band(f"See {p['name']} in action", "We\u2019ll walk you through it on sample data, then talk about a pilot on your own.")
        prod_schema = json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":p["name"],"applicationCategory":"BusinessApplication","description":p["lede"],"publisher":{"@type":"Organization","name":"Auto Solution"}})
        write(f"/products/{p['slug']}/", page(f"/products/{p['slug']}/", f"{p['name']}: {p['cat']}", p["lede"][:158], b, active="products", schema=f'<script type="application/ld+json">{prod_schema}</script>' + faq_schema(p["faq"])))

# ============================ PILOT PROGRAM ============================
PILOT = dict(
  weeks="6\u20138 weeks",
  phases=[("Weeks 1\u20132","Scope and data","Agree success criteria, sign the NDA, connect to a historical data extract in your environment and validate it."),
          ("Weeks 2\u20134","Model on your data","Train and tune the model on your own history, and set thresholds with your team."),
          ("Weeks 4\u20137","Shadow mode","Run alongside your current process without touching live decisions, and compare results case by case."),
          ("Weeks 7\u20138","Findings and decision","Present results against the agreed criteria, with a clear go or no-go recommendation and a rollout plan.")],
  data={"paysentinel":["12\u201324 months of transaction records","Fraud and chargeback outcomes","Device, merchant, amount and timestamp fields","Your current rules or decisions, to compare against"],
        "gridsentinel":["12+ months of smart meter readings","Transformer-level energy input","Consumer master and billing records","Past inspection outcomes, if available"],
        "fuelledger":["Depot dispatch and invoice records","Tank level (ATG) and density readings","Nozzle or dispenser sales","Cash deposit and fleet card records"]},
  gets=["A findings report: what the model caught, missed and why","Ranked, explainable leads or decisions you can verify","Performance measured on your data against the agreed criteria","An estimate of the annual value at stake, based on your numbers","A go or no-go recommendation and a rollout plan if it\u2019s a go"],
  faq=[("Is the pilot free?","No. It\u2019s a fixed-fee pilot, agreed before we start. If you go on to roll the product out, the full pilot fee is credited against your first year."),
       ("Will it affect our live systems?","No. During the pilot the product runs in shadow mode on a copy of your data. Live approvals, billing and operations don\u2019t change."),
       ("Where does our data go?","It stays in your environment or a cloud account you approve. At the end we return or delete any extracts, as you prefer, and revoke our access."),
       ("What do you need from our team?","One owner on your side, a few hours a week from someone who knows the data, and a review session at each phase."),
       ("What if the results aren\u2019t good enough?","Then the recommendation is no-go, and you\u2019re under no obligation to continue. Success criteria are agreed at the start, so there\u2019s no ambiguity."),
       ("Can the pilot be shorter?","Sometimes. If your data is clean and easy to access, the first phases move faster. We\u2019ll give you a firm plan during scoping.")])

def pilot_page():
    P = PILOT
    body = phero("Pilot program", "Prove the value on your own data before you commit. A fixed-scope, low-risk pilot of PaySentinel, GridSentinel or FuelLedger, run inside your environment.", [("Home","/"),("Products","/products/"),("Pilot program",None)], actions='<a class="btn btn-primary" href="/request-demo/?type=pilot">Apply for a pilot</a>' + btn_book("Talk to us first","btn btn-outline"))
    glance = [(P["weeks"],"from kickoff to decision"),("Fixed fee","credited in full if you roll out"),("Shadow mode","no impact on live systems"),("No obligation","to continue after the pilot")]
    body += '<section class="sec tight"><div class="wrap"><div class="stats rv" style="grid-template-columns:repeat(4,1fr)">' + "".join(f"<div><b style=\"font-size:clamp(1.5rem,2.6vw,2.2rem)\">{a}</b><span>{b}</span></div>" for a,b in glance) + "</div></div></section>"
    ph = "".join(f'<li><span class="n">{i+1}</span><p class="ph-w">{w}</p><h3>{t}</h3><p>{d}</p></li>' for i,(w,t,d) in enumerate(P["phases"]))
    body += f'<section class="sec dark"><div class="wrap"><div class="sec-head"><p class="kicker">How it runs</p><h2 class="h2">Four phases, one clear decision</h2></div><ol class="steps pilot-steps" style="--n:4">{ph}</ol></div></section>'
    cards = "".join(f'<div class="card rv"><p class="pcat">{PRODUCT_BY[k]["name"]}</p><h3 class="h3">Data we\u2019ll need</h3><div style="margin-top:14px">{checks(v)}</div><a class="tlink" style="margin-top:18px" href="/request-demo/?product={k}&amp;type=pilot">Apply for a {PRODUCT_BY[k]["name"]} pilot</a></div>' for k,v in P["data"].items())
    body += f'<section class="sec white"><div class="wrap"><div class="sec-head"><p class="kicker">What we need</p><h2 class="h2">Data for each product</h2><p class="lede">A historical extract is enough to start. We help your team prepare it, and it never has to leave your environment.</p></div><div class="grid-3">{cards}</div></div></section>'
    body += f'''<section class="sec"><div class="wrap duo" style="align-items:start">
<div class="rv"><p class="kicker">What you get</p><h2 class="h2">At the end of the pilot</h2><div style="margin-top:24px">{checks(P["gets"])}</div></div>
<div class="card rv" style="padding:36px"><p class="kicker">Ground rules</p><h2 class="h3" style="font-size:1.4rem;margin-bottom:18px">How we keep it safe and fair</h2>{checks(["Success criteria agreed in writing before we start","NDA signed before any data is shared","Runs in your environment, read-only, in shadow mode","Weekly check-ins and a review at every phase","Data extracts returned or deleted at the end","Pilot fee credited in full against year one if you roll out"])}</div></div></section>'''
    body += f'<section class="sec white"><div class="wrap faq-wrap"><div><p class="kicker">FAQ</p><h2 class="h2">Pilot questions</h2></div>{faq(P["faq"])}</div></section>'
    body += cta_band("Ready to test it on your data?", "Tell us which product and a little about your setup. We\u2019ll come back within one business day with a pilot outline.").replace('href="/request-demo/">Request a demo', 'href="/request-demo/?type=pilot">Apply for a pilot')
    write("/pilot/", page("/pilot/", "Pilot program", "Run a fixed-scope pilot of PaySentinel, GridSentinel or FuelLedger on your own data, in shadow mode, with the fee credited if you roll out.", body, active="products", schema=faq_schema(P["faq"])))

def request_demo():
    opts = "".join(f'<option value="{p["slug"]}">{p["name"]}: {p["cat"]}</option>' for p in PRODUCTS) + '<option value="custom">Custom automation or AI agent</option>'
    body = phero("Request a demo", "Tell us a little about your organisation and we\u2019ll set up a walkthrough on realistic sample data. We reply within one business day.", [("Home","/"),("Request a demo",None)], actions=False)
    body += f'''<section class="sec no-mbar"><div class="wrap duo" style="align-items:start">
<form class="card form" id="demoForm" novalidate data-endpoint="{FORM_ENDPOINT}" style="padding:32px">
  <input type="text" name="_honey" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
  <div class="two"><div class="f"><label for="r-type-req">I\u2019d like</label><select id="r-type-req" name="request_type"><option value="demo">A demo</option><option value="pilot">A pilot on our data</option></select></div>
  <div class="f"><label for="r-product">Product</label><select id="r-product" name="product">{opts}</select></div></div>
  <div class="two"><div class="f"><label for="r-name">Name</label><input id="r-name" name="name" autocomplete="name" required aria-describedby="r-name-e"><span class="err" id="r-name-e"></span></div>
  <div class="f"><label for="r-role">Role</label><input id="r-role" name="role" autocomplete="organization-title" placeholder="e.g. Head of Risk"></div></div>
  <div class="two"><div class="f"><label for="r-email">Work email</label><input id="r-email" name="email" type="email" autocomplete="email" required aria-describedby="r-email-e"><span class="err" id="r-email-e"></span></div>
  <div class="f"><label for="r-phone">Phone <span class="opt">(optional)</span></label><input id="r-phone" name="phone" type="tel" autocomplete="tel"></div></div>
  <div class="f"><label for="r-org">Organisation</label><input id="r-org" name="organisation" autocomplete="organization" required aria-describedby="r-org-e"><span class="err" id="r-org-e"></span></div>
  <div class="f"><label for="r-type">Organisation type</label><select id="r-type" name="org_type"><option>Payment gateway or aggregator</option><option>Bank or fintech</option><option>Power distribution company (DISCOM)</option><option>Oil marketing company or fuel retailer</option><option>Fleet operator</option><option>Other</option></select></div>
  <div class="f"><label for="r-msg">What would you like to see? <span class="opt">(optional)</span></label><textarea id="r-msg" name="message" rows="3"></textarea></div>
  <button class="btn btn-primary btn-block" type="submit">Request demo</button>
  <p class="ok-note" id="demoStatus" role="status" aria-live="polite"></p>
</form>
<div class="rv"><h2 class="h3" style="font-size:1.5rem">What happens next</h2><div style="margin-top:20px">{steps([("We reply within a day","To confirm a time and what you\u2019d like to see."),("Demo on sample data","A walkthrough of the product on realistic sample data."),("Pilot conversation","If it fits, we scope a pilot on your own data, in your environment.")])}</div>
<p class="muted" style="margin-top:8px">Prefer to pick a time yourself? <a href="{CAL}" target="_blank" rel="noopener">Book a call on our calendar</a>.</p></div></div></section>'''
    write("/request-demo/", page("/request-demo/", "Request a demo", "Request a demo of PaySentinel, GridSentinel or FuelLedger from Auto Solution.", body, active="products"))

# ============================ HOME ============================
def home():
    gst = CASE_BY["gst-reconciliation"]
    body = f"""
<section class="hero-l" aria-labelledby="hero-h">
  <div class="mesh" aria-hidden="true"></div>
  <div class="wrap hero-l-in">
    <a class="pill-l fade-up" href="/products/"><span class="pill-new">AI products</span>PaySentinel, GridSentinel and FuelLedger stop revenue leaks <span aria-hidden="true">\u2192</span></a>
    <h1 class="display" id="hero-h">Your busywork,<br><span class="grad">running on its own.</span></h1>
    <p class="lede fade-up d1">We build AI agents and automation that take repetitive work off your team, and AI products that catch payment fraud, energy theft and fuel loss before they hit the books.</p>
    <div class="btns fade-up d2">{demo_btn()}{btn_book("Book a free 30-min call","btn btn-outline")}</div>
    <p class="hero-note fade-up d3">No commitment. We reply within one business day.</p>
    <div class="collage fade-up d3" aria-hidden="true">
      <div class="c-side c-left">{ui_chat("WhatsApp agent")}</div>
      <div class="c-main">{ui_pay(True)}</div>
      <div class="c-side c-right">{ui_grid()}</div>
    </div>
  </div>
</section>
{stack()}

<section class="sec" aria-labelledby="tabs-h"><div class="wrap">
  <div class="sec-head center"><p class="kicker">What we build</p><h2 class="h2" id="tabs-h">AI products and automation, built around your data</h2><p class="lede">Three products for revenue protection, and custom AI for everything your team does by hand.</p></div>
  {tabs()}
</div></section>
{simulator()}
{architecture()}
<section class="sec white" aria-labelledby="svc-h"><div class="wrap">
  <div class="split"><div class="sec-head"><p class="kicker">Custom solutions</p><h2 class="h2" id="svc-h">Your busywork, automated</h2><p class="lede">Alongside our products, we build custom AI agents and automation around the tools your team already uses.</p></div><a class="tlink" href="/services/">All services</a></div>
  <div class="grid-2">{"".join(svc_card(s) for s in SERVICES)}</div>
</div></section>

<section class="story dark" id="how" aria-labelledby="story-h"><div class="story-pin"><div class="wrap duo">
  <div>
    <p class="kicker">See it run</p>
    <h2 class="h2" id="story-h">Watch a month-end GST reconciliation finish itself.</h2>
    <p class="lede">A job that used to take someone three hours, every month. Scroll to run it.</p>
    <ol class="st-steps">
      <li class="st"><span class="n">1</span><div><h3>Pull the books</h3><p>Every transaction comes straight out of Tally. No exports, no copy-paste.</p></div></li>
      <li class="st"><span class="n">2</span><div><h3>Match against the GST portal</h3><p>Each entry is checked against GSTR-2B, line by line.</p></div></li>
      <li class="st"><span class="n">3</span><div><h3>Flag only what needs a human</h3><p>Mismatches go to a short review list. Everything else is cleared.</p></div></li>
      <li class="st"><span class="n">4</span><div><h3>File-ready reports, delivered</h3><p>GSTR-1 and GSTR-3B drafts land on WhatsApp and email.</p></div></li>
    </ol>
  </div>
  <div class="ui console" aria-label="Sample automation run">
    <div class="ui-bar"><i></i><i></i><i></i><span>Sample run: gst_reconciliation</span><span class="r" id="timer">0.0s</span></div>
    <svg class="pipe" viewBox="0 0 520 120" aria-hidden="true">
      <defs><linearGradient id="pg" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="490" y2="0"><stop offset="0" stop-color="#4fe3ff"/><stop offset="1" stop-color="#ff7a1a"/></linearGradient></defs>
      <path id="pipePath" d="M30 60 H490" fill="none" stroke="rgba(160,180,255,.2)" stroke-width="2"/>
      <path id="pipeLit" d="M30 60 H490" fill="none" stroke="url(#pg)" stroke-width="3" stroke-linecap="round"/>
      <g class="pnode" data-at="0"><circle cx="30" cy="60" r="16"/><text x="30" y="102">Tally</text></g>
      <g class="pnode" data-at=".3"><circle cx="183" cy="60" r="16"/><text x="183" y="102">Match</text></g>
      <g class="pnode" data-at=".58"><circle cx="337" cy="60" r="16"/><text x="337" y="102">Review</text></g>
      <g class="pnode" data-at=".86"><circle cx="490" cy="60" r="16"/><text x="490" y="102">Deliver</text></g>
      <circle id="packet" r="6" cx="30" cy="60" fill="#fff"/>
    </svg>
    <dl class="readout">
      <div><dt>Transactions loaded</dt><dd data-to="1247" data-at="0">0</dd></div>
      <div><dt>Matched automatically</dt><dd data-to="1238" data-at=".3">0</dd></div>
      <div><dt>Sent for review</dt><dd class="warn" data-to="9" data-at=".58">0</dd></div>
      <div><dt>Reports ready</dt><dd class="ok" data-text="GSTR-1, GSTR-3B" data-at=".86">–</dd></div>
    </dl>
    <p class="cfoot" id="cfoot">Waiting to start.</p>
  </div>
</div></div></section>

<section class="sec white" aria-labelledby="res-h"><div class="wrap">
  <div class="sec-head"><p class="kicker">Results</p><h2 class="h2" id="res-h">Measured in hours given back</h2></div>
  <div class="stats rv"><div><b><span class="count" data-to="11">11</span>+</b><span>projects delivered since 2026</span></div><div><b>3</b><span>AI products for revenue protection</span></div><div><b><span class="count" data-to="20">20</span>+</b><span>hours a week saved for most clients</span></div><div><b>&lt;5 min</b><span>for a GST report that took 3 hours</span></div></div>
</div></section>

<section class="sec" aria-labelledby="cs-h"><div class="wrap">
  <div class="split"><div class="sec-head"><p class="kicker">Case studies</p><h2 class="h2" id="cs-h">What clients got back</h2><p class="lede">Real projects. Client names stay private under NDA.</p></div><a class="tlink" href="/case-studies/">All case studies</a></div>
  <a class="card feature-case rv" href="/case-studies/{gst["slug"]}/" style="text-decoration:none;margin-bottom:24px"><div class="body"><p class="metric" style="font-weight:640;font-size:clamp(2.4rem,4.5vw,3.6rem);letter-spacing:-.04em;line-height:1">3 hrs \u2192 &lt;5 min</p><ul class="tags"><li class="tag">Finance &amp; CA</li><li class="tag">India</li></ul><h3 class="h3" style="margin-top:18px">{gst["title"]}</h3><p style="margin-top:8px">{gst["challenge"]}</p><span class="tlink" style="margin-top:18px">Read the case study</span></div>{ui_flow()}</a>
  <div class="grid-3">{"".join(case_card(CASE_BY[s]) for s in ["shipment-tracking","demand-forecasting","invoice-ocr"])}</div>
</div></section>

<section class="sec dark" aria-labelledby="agent-h"><div class="wrap duo">
  <div>
    <p class="kicker">AI agents</p>
    <h2 class="h2" id="agent-h">An AI agent doesn\u2019t just reply. It gets the work done.</h2>
    <p class="lede">A property enquiry on WhatsApp at 11pm. Nobody from the team is awake. The agent checks what\u2019s available, qualifies the buyer, books the visit and updates the CRM.</p>
    <ul class="did" id="agentDid">
      <li data-s="1"><span class="tk">{ic("check")}</span>Checked live inventory</li>
      <li data-s="2"><span class="tk">{ic("check")}</span>Qualified the lead: budget and timeline</li>
      <li data-s="3"><span class="tk">{ic("check")}</span>Booked the visit in the sales calendar</li>
      <li data-s="4"><span class="tk">{ic("check")}</span>Logged the lead and summary in the CRM</li>
    </ul>
    <div class="btns" style="margin-top:0"><button type="button" class="btn btn-ghost btn-sm" id="agentReplay">Replay</button><a class="tlink" href="/services/ai-agents/">How we build AI agents</a></div>
  </div>
  <div class="chat" aria-label="Example WhatsApp conversation">
    <div class="chat-top"><span class="chat-av">{ic("bot")}</span><div><strong>Skyline Homes</strong><span class="chat-sub" id="chatSub">AI assistant, online</span></div><span class="chat-badge">Example</span></div>
    <ol class="chat-body" id="chatBody"></ol>
  </div>
</div></section>

<section class="sec" aria-labelledby="ind-h"><div class="wrap">
  <div class="split"><div class="sec-head"><p class="kicker">Industries</p><h2 class="h2" id="ind-h">Built for how your industry actually works</h2></div><a class="tlink" href="/industries/">All industries</a></div>
  <div class="grid-3">{"".join(f'<a class="card rv" href="/industries/{i["slug"]}/"><h3 class="h3">{i["name"]}</h3><p>{i["short"]}</p><span class="tlink">See use cases</span></a>' for i in INDUSTRIES)}</div>
</div></section>

<section class="sec white" aria-labelledby="ways-h"><div class="wrap">
  <div class="sec-head"><p class="kicker">Working with us</p><h2 class="h2" id="ways-h">Start small, or go straight to a full build</h2><p class="lede">Every option starts with a free 30-minute call. Nothing is billed until you approve a written scope.</p></div>
  {models()}
  <p style="margin-top:28px"><a class="tlink" href="/how-we-work/">How we work, step by step</a></p>
</div></section>

<section class="sec" aria-labelledby="q-h"><div class="wrap">
  <div class="sec-head"><p class="kicker">Clients</p><h2 class="h2" id="q-h">In their words</h2></div>
  {quotes()}
</div></section>

<section class="sec white" aria-labelledby="sec-h"><div class="wrap">
  <div class="sec-head"><p class="kicker">Security</p><h2 class="h2" id="sec-h">Your data stays yours</h2><p class="lede">Your workflows touch financial and customer data. Here\u2019s how we handle it on every project.</p></div>
  {security()}
</div></section>
<section class="sec"><div class="wrap">{founder_block()}</div></section>
{checklist_promo()}
{cta_band()}"""
    org = json.dumps({"@context":"https://schema.org","@type":"ProfessionalService","name":"Auto Solution","url":SITE+"/","logo":SITE+"/favicon.svg","image":SITE+"/assets/img/og-cover.png","email":EMAIL,"telephone":TEL,"foundingDate":"2026","address":{"@type":"PostalAddress","addressLocality":"Noida","addressRegion":"Uttar Pradesh","addressCountry":"IN"},"areaServed":"Worldwide","founder":[{"@type":"Person","name":"Harsh Vardhan"},{"@type":"Person","name":"Anurag Maurya"}]})
    write("/", page("/", "Auto Solution \u2014 Your busywork, running on its own",
        "Auto Solution builds AI agents and automation that take repetitive work off your team, plus AI products for payment fraud (PaySentinel), energy theft (GridSentinel) and fuel loss (FuelLedger).",
        body, schema=f'<script type="application/ld+json">{org}</script>'))

# ============================ SERVICES ============================
def services():
    body = phero("Services", "Four kinds of automation, all built around the tools your team already uses, and all running in your environment.", [("Home","/"),("Services",None)], h="h1")
    body += f'<section class="sec"><div class="wrap"><div class="grid-2">{"".join(svc_card(s) for s in SERVICES)}</div></div></section>'
    body += f'<section class="sec white"><div class="wrap"><div class="sec-head"><p class="kicker">Process</p><h2 class="h2">How every project runs</h2></div>{steps(PROCESS)}</div></section>' + cta_band()
    write("/services/", page("/services/", "Services: AI agents, workflow automation, document AI, analytics", "AI agents and chatbots, workflow automation, document AI and OCR, and data and forecasting services from Auto Solution.", body, active="services"))
    for s in SERVICES:
        b = phero(s["title"], s["lede"], [("Home","/"),("Services","/services/"),(s["name"],None)], right=UI[s["ui"]]())
        uses = "".join(f'<div class="card rv"><h3 class="h3">{t}</h3><p>{d}</p></div>' for t, d in s["uses"])
        b += f'<section class="sec"><div class="wrap"><div class="sec-head"><p class="kicker">Use cases</p><h2 class="h2">What we build</h2></div><div class="grid-3">{uses}</div></div></section>'
        b += f'<section class="sec dark"><div class="wrap"><div class="sec-head"><p class="kicker">How it works</p><h2 class="h2">From first call to running in production</h2></div>{steps(s["how"])}<p class="muted" style="margin-top:40px"><b style="color:#fff">Tools we use:</b> {s["tools"]}</p></div></section>'
        if s["cases"]:
            b += f'<section class="sec"><div class="wrap"><div class="sec-head"><p class="kicker">Proof</p><h2 class="h2">Related case studies</h2></div><div class="grid-3">{"".join(case_card(CASE_BY[c]) for c in s["cases"])}</div></div></section>'
        b += f'<section class="sec white"><div class="wrap faq-wrap"><div><p class="kicker">FAQ</p><h2 class="h2">Common questions</h2></div>{faq(s["faq"])}</div></section>' + cta_band()
        write(f"/services/{s['slug']}/", page(f"/services/{s['slug']}/", s["name"].replace("&amp;","&"), s["lede"], b, active="services", schema=faq_schema(s["faq"])))

# ============================ INDUSTRIES ============================
def industries():
    cards = "".join(f'<a class="card rv" href="/industries/{i["slug"]}/"><h3 class="h3">{i["name"]}</h3><p>{i["short"]}</p><span class="tlink">See use cases</span></a>' for i in INDUSTRIES)
    body = phero("Industries we automate", "The tools differ by industry. The manual pain doesn\u2019t. Here\u2019s what automation looks like in the sectors we work in most.", [("Home","/"),("Industries",None)])
    body += f'<section class="sec"><div class="wrap"><div class="grid-3">{cards}</div><p class="muted" style="margin-top:36px">We\u2019ve also worked with NBFCs, EdTech, legal, agri-business, hospitality, SaaS and public-sector teams. If the work is repetitive and rule-based, we can probably automate it.</p></div></section>' + cta_band()
    write("/industries/", page("/industries/", "Industries", "Automation for finance, logistics, e-commerce, real estate, manufacturing and healthcare teams.", body, active="industries"))
    for i in INDUSTRIES:
        b = phero(i["title"], i["lede"], [("Home","/"),("Industries","/industries/"),(i["name"],None)], right=UI[i["ui"]]())
        b += f'''<section class="sec"><div class="wrap duo" style="align-items:start">
<div class="rv"><p class="kicker">Sound familiar?</p><h2 class="h2">Where the hours go today</h2><div style="margin-top:28px">{checks(i["pains"])}</div></div>
<div class="card rv" style="padding:36px"><p class="kicker">What we automate</p><h2 class="h3" style="font-size:1.5rem;margin-bottom:22px">Typical automations we build</h2>{checks(i["uses"])}</div></div></section>'''
        if i["cases"]:
            b += f'<section class="sec white"><div class="wrap"><div class="sec-head"><p class="kicker">Proof</p><h2 class="h2">Results in {i["name"].split(" &amp;")[0].lower()}</h2></div><div class="grid-3">{"".join(case_card(CASE_BY[c]) for c in i["cases"])}</div></div></section>'
        else:
            b += f'<section class="sec white"><div class="wrap duo"><div><p class="kicker">See it in action</p><h2 class="h2">An AI agent that works the night shift</h2><p class="lede">Our AI agents answer enquiries, qualify, book and update your systems at any hour. See an example conversation on our home page.</p><div class="btns"><a class="btn btn-outline" href="/services/ai-agents/">AI agents</a><a class="btn btn-outline" href="/#agent-h">See the example</a></div></div><div>{ui_chat("Enquiry agent")}</div></div></section>'
        b += cta_band(f"Let\u2019s look at your {i['name'].split(' &amp;')[0].lower()} workflows")
        write(f"/industries/{i['slug']}/", page(f"/industries/{i['slug']}/", i["title"], i["lede"], b, active="industries"))

# ============================ CASE STUDIES ============================
def cases():
    body = phero("Case studies", "Real projects, measured in hours given back. Client names are kept private under NDA.", [("Home","/"),("Case studies",None)])
    body += f'<section class="sec"><div class="wrap"><div class="grid-3">{"".join(case_card(c) for c in CASES)}</div></div></section>' + cta_band()
    write("/case-studies/", page("/case-studies/", "Case studies", "How Auto Solution clients automated GST reconciliation, shipment tracking, invoice entry, forecasting and more.", body, active="cases"))
    for idx, c in enumerate(CASES):
        nxt = CASES[(idx + 1) % len(CASES)]
        b = phero(c["title"], c["client"] + ". " + c["short"], [("Home","/"),("Case studies","/case-studies/"),(c["tagind"],None)], actions=False, tags=[c["tagind"], c["loc"]])
        res = "".join(f'<div><b>{v}</b><span>{l}</span></div>' for v, l in c["results"])
        sol = "".join(f'<li><span class="n">{n+1}</span><p>{s}</p></li>' for n, s in enumerate(c["solution"]))
        q = ""
        if c["quote"]:
            q = f'<figure class="card quote rv" style="margin-top:40px;padding:36px"><blockquote style="font-size:1.35rem">\u201c{c["quote"][0]}\u201d</blockquote><figcaption>{c["quote"][1]}</figcaption></figure>'
        b += f'''<section class="sec white tight"><div class="wrap"><div class="stats" style="grid-template-columns:repeat(3,1fr)">{res}</div></div></section>
<section class="sec"><div class="wrap duo" style="align-items:start">
<div class="rv"><p class="kicker">The challenge</p><h2 class="h2" style="font-size:1.8rem">What wasn\u2019t working</h2><p class="lede" style="margin-top:16px">{c["challenge"]}</p></div>
<div class="rv"><p class="kicker">What we built</p><h2 class="h2" style="font-size:1.8rem">The solution</h2><ol class="vsteps">{sol}</ol><p class="muted" style="margin-top:8px"><b style="color:var(--ink)">Built with:</b> {c["stack"]}</p></div></div>
<div class="wrap">{q}</div></section>
<section class="sec white tight"><div class="wrap split"><div><p class="muted">Next case study</p><a class="h3" style="text-decoration:none" href="/case-studies/{nxt["slug"]}/">{nxt["title"]}</a></div><a class="tlink" href="/case-studies/{nxt["slug"]}/">Read next</a></div></section>'''
        b += cta_band("Want results like these?")
        write(f"/case-studies/{c['slug']}/", page(f"/case-studies/{c['slug']}/", c["title"].replace("&lt;", "<"), c["challenge"][:155], b, active="cases"))

# ============================ ROI CALCULATOR ============================
def roi():
    body = phero("How many hours could your team get back?", "Move the sliders to match your team. We assume about 60% of repetitive work can be automated. Your free call gives the real number.", [("Home","/"),("ROI calculator",None)], actions=False)
    body += f'''<section class="sec"><div class="wrap duo" style="align-items:start">
<form class="calc" id="calc" aria-describedby="calcNote">
  <div><label for="c-people">People doing repetitive work <output id="o-people" for="c-people">5</output></label><input type="range" id="c-people" min="1" max="50" value="5"></div>
  <div><label for="c-hours">Hours each, per week <output id="o-hours" for="c-hours">10</output></label><input type="range" id="c-hours" min="1" max="40" value="10"></div>
  <div><label for="c-rate">Cost per hour <output id="o-rate" for="c-rate">₹400</output></label><div class="rate-row"><input type="range" id="c-rate" min="100" max="3000" step="50" value="400"><select id="c-cur" aria-label="Currency"><option value="INR" selected>₹ INR</option><option value="USD">$ USD</option><option value="AED">AED</option><option value="GBP">£ GBP</option></select></div></div>
  <div class="calc-out" aria-live="polite"><div><p class="v" id="r-hours">1,560</p><p>hours back per year</p></div><div><p class="v" id="r-money">₹6,24,000</p><p>in team time, per year</p></div></div>
  <button type="submit" class="btn btn-primary btn-block">Send me this estimate</button>
  <p class="note" id="calcNote">Opens WhatsApp with your numbers filled in.</p>
</form>
<div class="rv"><h2 class="h3" style="font-size:1.5rem">How the estimate works</h2>
<div style="margin-top:20px">{checks(["Hours per year = people \u00d7 hours per week \u00d7 52 weeks \u00d7 60%.","60% is a conservative share of repetitive work we typically automate. Some workflows reach far higher, some lower.","Cost uses the hourly figure you enter, so it reflects your team, not an average."])}</div>
<p class="muted" style="margin-top:24px">Prefer to talk it through? We\u2019ll walk your real workflows on a free call and give you a proper number.</p><div class="btns">{btn_book()}</div></div></div></section>'''
    write("/roi-calculator/", page("/roi-calculator/", "Automation ROI calculator", "Estimate how many hours and how much money your team could save by automating repetitive work.", body))

# ============================ HOW WE WORK ============================
HOW_FAQ = [("What does a project cost?","It depends on what\u2019s being automated, so we quote after the free call. You approve a fixed scope and price before any work is billed."),
           ("How long does a project take?","Simple scripts take 3\u20137 days. Integrations and dashboards take 1\u20132 weeks. ML pipelines take 2\u20134 weeks. You get a firm timeline in the written scope."),
           ("Do we need anyone technical?","No. Automations fit into what your team already uses, and we train them at handover."),
           ("How do we pay?","Bank transfer, UPI, Stripe or PayPal. International clients can pay in their own currency."),
           ("Who owns the code?","You do. It runs in your environment and you get the code and documentation at handover.")]
def how():
    body = phero("How we work", "A low-risk path from first call to a live, supported automation. You see value before you commit to anything big.", [("Home","/"),("How we work",None)])
    body += f'<section class="sec"><div class="wrap"><div class="sec-head"><p class="kicker">Engagement models</p><h2 class="h2">Three ways to work with us</h2></div>{models()}</div></section>'
    body += f'<section class="sec dark"><div class="wrap"><div class="sec-head"><p class="kicker">Process</p><h2 class="h2">Five steps, no surprises</h2></div>{steps(PROCESS)}</div></section>'
    body += f'<section class="sec white"><div class="wrap"><div class="sec-head"><p class="kicker">Security</p><h2 class="h2">How we handle your data</h2></div>{security()}</div></section>'
    body += f'<section class="sec"><div class="wrap faq-wrap"><div><p class="kicker">FAQ</p><h2 class="h2">Questions before you start</h2></div>{faq(HOW_FAQ)}</div></section>' + cta_band()
    write("/how-we-work/", page("/how-we-work/", "How we work", "Pilots, fixed-scope projects and care plans. How Auto Solution runs automation projects from first call to support.", body, active="company", schema=faq_schema(HOW_FAQ)))

# ============================ ABOUT ============================
def about():
    body = phero("We give people their time back", "Auto Solution is an AI company founded in 2026 and based in Noida, India. We build the agents and automations that take repetitive work off busy teams, for clients across India, the Middle East, Southeast Asia, Europe and the US.", [("Home","/"),("About",None)])
    body += f'''<section class="sec"><div class="wrap duo" style="align-items:start">
<div class="rv"><p class="kicker">Our story</p><h2 class="h2">It started with a spreadsheet</h2></div>
<div class="rv" style="color:var(--ink-2);font-size:1.1rem;line-height:1.75"><p>Our founders kept watching skilled people lose whole days to copy-paste reporting, manual reconciliation and Excel busywork, tasks a script could finish in seconds. So they built one. Then another. Then a studio around it.</p><p style="margin-top:18px">Today our team designs and ships AI agents, workflow automation, document AI and forecasting for finance, logistics, e-commerce, real estate and manufacturing teams. We measure ourselves the way our clients do: hours saved, errors removed, and how quickly a project goes from \u201cmanual mess\u201d to \u201cit just runs now.\u201d</p></div></div></section>
<section class="sec white"><div class="wrap">{founder_block()}</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><p class="kicker">Leadership</p><h2 class="h2">The people behind it</h2></div>
  <div class="grid-3">
    <div class="card rv"><div class="person"><img src="/assets/img/founder-1-400.webp" width="72" height="72" alt="Harsh Vardhan" loading="lazy"><div><b>Harsh Vardhan</b><span>Founder</span></div></div><p style="margin-top:18px">Leads engineering and ML strategy. Focused on turning messy manual workflows into automation that just works.</p></div>
    <div class="card rv"><div class="person"><span class="av">AM</span><div><b>Anurag Maurya</b><span>Co-founder</span></div></div><p style="margin-top:18px">Leads client delivery and global partnerships, making sure every automation fits how a business actually runs.</p></div>
    <div class="card rv"><div class="person"><span class="av">MC</span><div><b>Mohit Chowdhary</b><span>Member of technical staff</span></div></div><p style="margin-top:18px">Builds automations and integrations, from scoping through deployment.</p></div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="sec-head"><p class="kicker">Team</p><h2 class="h2">20 senior engineers under one roof</h2><p class="lede">Alumni of IIT, NIT and BITS Pilani, with prior work at PayPal India, Paytm, Pine Labs, Automation Anywhere and Infosys, TCS and HCL. Average experience: 4\u20139 years.</p></div>
  <div class="stats" style="grid-template-columns:repeat(3,1fr)"><div><b>8</b><span>Python &amp; backend automation engineers</span></div><div><b>4</b><span>ML &amp; AI engineers</span></div><div><b>3</b><span>Integration engineers</span></div><div><b>2</b><span>OCR &amp; document AI specialists</span></div><div><b>2</b><span>Dashboard &amp; data visualisation experts</span></div><div><b>1</b><span>Business analyst &amp; QA lead</span></div></div>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><p class="kicker">Values</p><h2 class="h2">How we work</h2></div><div class="grid-3">
<div class="card rv"><div class="ico">{ic("target")}</div><h3 class="h3">Outcomes over output</h3><p>We\u2019re judged by hours saved and errors removed, not lines of code.</p></div>
<div class="card rv"><div class="ico">{ic("eye")}</div><h3 class="h3">Honest scoping</h3><p>Clear timelines, fixed prices, and we\u2019ll tell you when automation isn\u2019t worth it.</p></div>
<div class="card rv"><div class="ico">{ic("shield")}</div><h3 class="h3">Your data, your systems</h3><p>NDA first, least-privilege access, and everything runs in your environment.</p></div></div></div></section>
<section class="sec white"><div class="wrap duo">
<div class="rv"><p class="kicker">Global</p><h2 class="h2">Headquartered in Noida. Working in your time zone.</h2><p class="lede">We\u2019re remote-first, with overlap across India, the Gulf, Southeast Asia, the UK and the US.</p><p style="margin-top:22px;display:flex;gap:10px;align-items:center;color:var(--ink-2)"><span class="ico" style="margin:0;width:38px;height:38px">{ic("pin")}</span>{ADDRESS}</p></div>
<div class="rv">{zones()}</div></div></section>''' + cta_band("Work with us")
    write("/about/", page("/about/", "About us", "Auto Solution is an AI company founded in 2026 in Noida, India, building PaySentinel, GridSentinel and FuelLedger.", body, active="company"))

# ============================ INSIGHTS ============================
def insights():
    cards = "".join(f'<a class="card post-card rv" href="/insights/{p["slug"]}/"><p class="cat">{p["cat"]}</p><h2 class="h3">{p["title"]}</h2><p style="margin-top:8px">{p["desc"]}</p><p class="meta-l">{p["mins"]} min read</p><span class="tlink">Read</span></a>' for p in POSTS)
    body = phero("Insights", "Practical guides on automation and AI from the projects we ship. No hype.", [("Home","/"),("Insights",None)], actions=False)
    body += f'<section class="sec"><div class="wrap"><div class="grid-3">{cards}</div></div></section>' + cta_band()
    write("/insights/", page("/insights/", "Insights", "Practical guides on workflow automation and AI agents from Auto Solution.", body, active="resources"))
    for p in POSTS:
        art = json.dumps({"@context":"https://schema.org","@type":"Article","headline":p["title"],"description":p["desc"],"author":{"@type":"Organization","name":"Auto Solution"},"publisher":{"@type":"Organization","name":"Auto Solution"}})
        b = f'''<section class="phero"><div class="wrap" style="max-width:820px"><ol class="crumbs"><li><a href="/">Home</a></li><li><a href="/insights/">Insights</a></li><li aria-current="page">{p["cat"]}</li></ol>
<h1 class="h1">{p["title"]}</h1><p class="lede">{p["desc"]}</p><p class="meta"><span>Auto Solution team</span><span>{p["date"]}</span><span>{p["mins"]} min read</span></p></div></section>
<section class="sec white"><article class="wrap prose">{p["body"]}</article></section>''' + cta_band()
        write(f"/insights/{p['slug']}/", page(f"/insights/{p['slug']}/", p["title"], p["desc"], b, active="resources", schema=f'<script type="application/ld+json">{art}</script>'))

# ============================ CAREERS ============================
JOBS = [("Python Automation Engineer","Full-time","Remote, 1\u20133 years","Build and ship Python and Excel automation pipelines directly with clients, from scoping to deployment."),
        ("ML Engineer (NLP / OCR)","Full-time","Remote, 2+ years","Design forecasting, classification and document-extraction models that plug straight into client workflows."),
        ("Business Development (Automation)","Full-time or contract","Remote, global clients","Find and close automation projects worldwide, and own the conversation from first chat to signed scope.")]
def careers():
    jobs = "".join(f'<article class="card rv" style="display:flex;flex-direction:column"><ul class="tags" style="margin:0 0 14px"><li class="tag">{t}</li><li class="tag">{m}</li></ul><h2 class="h3">{n}</h2><p style="margin-top:8px">{d}</p><a class="tlink" style="margin-top:auto;padding-top:20px" href="mailto:{EMAIL}?subject=Application:%20{n.replace(" ","%20")}">Apply by email</a></article>' for n,t,m,d in JOBS)
    body = phero("Build automation that matters", "We\u2019re a remote-first team of senior engineers. Real client ownership, a flat structure and no busywork, which would be ironic.", [("Home","/"),("Careers",None)], actions=False)
    body += f'''<section class="sec"><div class="wrap"><div class="sec-head"><p class="kicker">Open roles</p><h2 class="h2">Current openings</h2></div><div class="grid-3">{jobs}</div></div></section>
<section class="sec white"><div class="wrap duo"><div><p class="kicker">Why join</p><h2 class="h2">What you get</h2></div>{checks(["100% remote, flexible hours","Work directly with clients, not through layers","A learning budget for courses and conferences","Ship to production within your first weeks","A flat team where good ideas win"], "checks")}</div></section>
<section class="sec tight"><div class="wrap"><div class="card" style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;padding:32px"><div><h2 class="h3">Don\u2019t see the right role?</h2><p>We\u2019re always glad to meet good automation engineers, ML builders and closers.</p></div><a class="btn btn-outline" href="mailto:{EMAIL}?subject=Careers%20at%20Auto%20Solution">Email your CV</a></div></div></section>'''
    write("/careers/", page("/careers/", "Careers", "Remote roles at Auto Solution: Python automation engineers, ML engineers and business development.", body, active="company"))

# ============================ CONTACT ============================
def contact():
    opts = "".join(f"<option>{s['name'].replace('&amp;','&')}</option>" for s in SERVICES) + "<option>Not sure yet</option>"
    body = phero("Let\u2019s talk about your work", "Book a free 30-minute call, message us on WhatsApp, or send the form. We reply within 24 hours.", [("Home","/"),("Contact",None)], actions=False)
    body += f'''<section class="sec no-mbar" id="book"><div class="wrap duo" style="align-items:start">
<div>
  <h2 class="h2" style="font-size:1.8rem">Book a free 30-minute call</h2>
  <p class="muted" style="margin:12px 0 24px">Pick a time that suits you. You\u2019ll get a Google Meet link by email.</p>
  <div class="calendly-inline-widget" data-url="{CAL}?hide_gdpr_banner=1&amp;primary_color=ff7a1a"></div>
  <p class="note" style="margin-top:12px">Calendar not loading? <a href="{CAL}" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
</div>
<div>
  <ul class="contact-lines" style="margin-bottom:40px">
    <li><span class="ico">{ic("cal")}</span><div><a href="{CAL}" target="_blank" rel="noopener">Book a 30-minute call</a><small>Pick a time that suits you.</small></div></li>
    <li><span class="ico">{ic("mail")}</span><div><a href="mailto:{EMAIL}">{EMAIL}</a><small>For detailed briefs and documents.</small></div></li>
    <li><span class="ico">{ic("phone")}</span><div><a href="tel:{TEL}">{PHONE}</a><small>Mon\u2013Sat, 10am\u20137pm IST.</small></div></li>
    <li><span class="ico">{ic("pin")}</span><div><b>{ADDRESS}</b><small>Remote-first, working worldwide.</small></div></li>
  </ul>
  <h2 class="h3" style="font-size:1.4rem;margin-bottom:18px">Or send us a message</h2>
  <form class="form" id="leadForm" novalidate data-endpoint="{FORM_ENDPOINT}">
    <input type="text" name="_honey" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
    <div class="two"><div class="f"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required aria-describedby="f-name-e"><span class="err" id="f-name-e"></span></div>
    <div class="f"><label for="f-company">Company <span class="opt">(optional)</span></label><input id="f-company" name="company" autocomplete="organization"></div></div>
    <div class="two"><div class="f"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" autocomplete="email" required aria-describedby="f-email-e"><span class="err" id="f-email-e"></span></div>
    <div class="f"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div></div>
    <div class="f"><label for="f-service">Interested in</label><select id="f-service" name="service">{opts}</select></div>
    <div class="f"><label for="f-msg">What do you want automated?</label><textarea id="f-msg" name="message" rows="4" required aria-describedby="f-msg-e" placeholder="e.g. We build 50 Excel reports from ERP data every month."></textarea><span class="err" id="f-msg-e"></span></div>
    <button class="btn btn-primary btn-block" type="submit" id="sendBtn">Send message</button>
    <p class="note">Goes straight to our inbox. We reply within 24 hours. Prefer to talk? <a href="{CAL}" target="_blank" rel="noopener">Book a call</a>.</p>
    <p class="ok-note" id="formStatus" role="status" aria-live="polite"></p>
  </form>
</div></div></section>'''
    write("/contact/", page("/contact/", "Contact us", "Book a free 30-minute call with Auto Solution, message us on WhatsApp, or email info@autosoluation.com.", body, active="company",
        extra_js='<script src="https://assets.calendly.com/assets/external/widget.js" async></script>'))

# ============================ SECURITY ============================
SEC_FAQ=[("Do you sign an NDA?","Yes, on every engagement, before we see any data or systems."),
 ("Where does our data go?","Automations run in your environment or a cloud account you approve. We don\u2019t copy your data to our own servers."),
 ("Do you use AI models on our data?","Only where the project needs it, and only with providers and settings you approve. For sensitive work we can use models that don\u2019t retain or train on your data, or run models inside your environment."),
 ("What happens to our access at the end?","We hand over all credentials and revoke our own access at handover, unless you\u2019ve chosen a care plan.")]
def security_page():
    body = phero("Security &amp; trust", "Our automations touch financial records, customer data and core systems. Here\u2019s exactly how we protect them.", [("Home","/"),("Security",None)])
    body += f'<section class="sec"><div class="wrap"><div class="sec-head"><p class="kicker">Principles</p><h2 class="h2">Four rules on every project</h2></div>{security()}</div></section>'
    body += f'''<section class="sec white"><div class="wrap duo" style="align-items:start">
<div class="rv"><p class="kicker">In practice</p><h2 class="h2">How a project is secured</h2></div>
<div class="rv">{checks(["An NDA is signed before discovery begins.","We request read-only access first, and write access only where the automation needs it.","Credentials are stored in your secret manager or environment, never in code or chat.","Every automated run is logged with what it read, what it changed and when.","AI agents get the narrowest permissions that let them do the job, and every action they take is recorded.","Inputs are validated; when something looks wrong, the automation stops and alerts a person.","At handover you receive the code, documentation and all credentials, and we revoke our access."])}</div></div></section>'''
    body += f'''<section class="sec"><div class="wrap duo" style="align-items:start">
<div class="rv"><p class="kicker">Compliance</p><h2 class="h2">Built for regulated teams</h2><p class="lede">We design with India\u2019s Digital Personal Data Protection Act and GDPR principles in mind: collect only what\u2019s needed, keep it where you control it, and make it easy to delete.</p></div>
<div class="faq rv">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in SEC_FAQ)}</div></div></section>''' + cta_band("Have a security question before you start?", "Ask us on a free call. We\u2019re happy to walk your IT or compliance team through our approach.")
    write("/security/", page("/security/", "Security & trust", "How Auto Solution protects client data: NDAs, least-privilege access, logging and automations that run in your environment.", body, active="company", schema=faq_schema(SEC_FAQ)))

# ============================ CHECKLIST (lead magnet) ============================
def checklist():
    body = phero("The AI Automation Checklist", "A free 5-page guide to finding the work worth automating first, scoring it in 20 minutes, and avoiding the mistakes that sink most first projects.", [("Home","/"),("Free checklist",None)], actions=False)
    body += f'''<section class="sec no-mbar"><div class="wrap duo" style="align-items:start">
<div class="rv"><h2 class="h3" style="font-size:1.5rem">What\u2019s inside</h2><div style="margin-top:20px">{checks(["A list of 20 repetitive tasks to check across finance, sales, operations and HR","A five-question scoring method, with a printable scoring sheet","A readiness checklist covering process, data, people and measurement","Six common mistakes and how to avoid them"])}</div></div>
<form class="card form" id="dlForm" novalidate data-endpoint="{FORM_ENDPOINT}" data-file="/assets/downloads/ai-automation-checklist.pdf" style="padding:32px">
  <input type="text" name="_honey" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
  <h2 class="h3">Get the PDF</h2>
  <div class="f"><label for="d-name">Name <span class="opt">(optional)</span></label><input id="d-name" name="name" autocomplete="name"></div>
  <div class="f"><label for="d-email">Work email</label><input id="d-email" name="email" type="email" autocomplete="email" required aria-describedby="d-email-e"><span class="err" id="d-email-e"></span></div>
  <button class="btn btn-primary btn-block" type="submit">Download the checklist</button>
  <p class="note">We\u2019ll occasionally email practical automation tips. Unsubscribe any time.</p>
  <p class="ok-note" id="dlStatus" role="status" aria-live="polite"></p>
</form></div></section>'''
    write("/ai-automation-checklist/", page("/ai-automation-checklist/", "Free AI Automation Checklist (PDF)", "Download a free 5-page checklist to find the work worth automating first and avoid common automation mistakes.", body, active="resources"))

# ============================ LEGAL + 404 ============================
def legal(path, title, html):
    body = phero(title, "Last updated October 2026.", [("Home","/"),(title,None)], actions=False)
    body += f'<section class="sec white"><div class="wrap prose">{html}</div></section>'
    write(path, page(path, title, f"{title} for the Auto Solution website.", body))

PRIVACY = f"""<p>This policy explains what information the Auto Solution website handles and why. Client projects are covered by the NDA and contract signed for each engagement.</p>
<h2>What we collect</h2><ul><li><strong>Contact and download forms.</strong> When you submit a form, your details are emailed to us through FormSubmit, a form-delivery service. We use them only to reply and, for the checklist, to send occasional automation tips you can unsubscribe from.</li><li><strong>Calculator and WhatsApp links.</strong> These open WhatsApp with details pre-filled; nothing reaches us until you press send. WhatsApp's privacy policy applies.</li><li><strong>Call bookings.</strong> Booking through Calendly shares the details you enter with us and with Calendly, under Calendly's privacy policy.</li><li><strong>Email and phone.</strong> Whatever you choose to share when you contact us.</li></ul>
<h2>Cookies, storage and analytics</h2><p>We don't use advertising or tracking cookies. We use Vercel Web Analytics to count visits and see which pages are useful; it doesn't use cookies or identify individual visitors. The embedded Calendly booking calendar on our contact page may set its own cookies.</p>
<h2>Service providers</h2><p>Our hosting provider (Vercel) may keep standard server logs (IP address, browser, pages requested) for security and reliability. FormSubmit, Calendly and WhatsApp (Meta) process data when you use them.</p>
<h2>How we use information</h2><p>Only to reply to your enquiry, scope and deliver work you ask for, and stay in touch about that work. We do not sell or rent personal data.</p>
<h2>Your choices</h2><p>To ask what we hold about you, or to have it corrected or deleted, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Contact</h2><p>Auto Solution, {ADDRESS}. <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""

TERMS = f"""<p>These terms cover your use of the Auto Solution website. Project work is governed by the separate contract and scope agreed for each engagement.</p>
<h2>Use of this website</h2><p>You may browse and share content from this site for personal or internal business use. Please don't copy substantial parts of it for commercial use without asking.</p>
<h2>No professional advice</h2><p>Articles, examples and calculator results are for general information. They aren't financial, legal or tax advice, and calculator figures are estimates, not guarantees.</p>
<h2>Examples and case studies</h2><p>Client names are withheld under NDA. Example conversations and sample runs are illustrations of how our systems work.</p>
<h2>Links to other services</h2><p>We link to WhatsApp, Calendly and other services we don't control, and aren't responsible for their content or practices.</p>
<h2>Liability</h2><p>We work to keep this site accurate and available but can't guarantee it will always be either. To the extent the law allows, we aren't liable for losses arising from use of the website.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of India, with courts in Uttar Pradesh having jurisdiction.</p>
<h2>Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>"""

def notfound():
    body = f'<section class="phero" style="min-height:80vh;display:flex;align-items:center"><div class="wrap" style="max-width:720px"><p class="kicker">404</p><h1 class="h1">This page doesn\u2019t exist</h1><p class="lede">The link may be old or mistyped. Try one of these instead.</p><div class="btns"><a class="btn btn-primary" href="/">Go to homepage</a><a class="btn btn-outline" href="/products/">Our products</a><a class="btn btn-outline" href="/contact/">Contact us</a></div></div></section>'
    write("/404.html", page("/404.html", "Page not found", "This page doesn't exist.", body))

# ============================ RUN ============================
if __name__ == "__main__":
    home(); product_pages(); pilot_page(); request_demo(); services(); industries(); cases(); roi(); how(); about(); insights(); careers(); contact(); security_page(); checklist()
    legal("/privacy/", "Privacy policy", PRIVACY); legal("/terms/", "Terms of use", TERMS); notfound()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}{p}</loc></url>\n" for p in PAGES) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(OUT, "vercel.json"), "w").write(json.dumps({"trailingSlash": True, "headers": [{"source": "/assets/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}]}, indent=2))
    print(f"Built {len(PAGES)} pages")
