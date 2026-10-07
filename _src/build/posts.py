"""Insights articles. Body is HTML inside .prose."""

POSTS = [
 dict(slug="what-to-automate-first", cat="Strategy", mins=6, date="October 2026",
  title="What to automate first: a simple scoring method",
  desc="Most teams automate the wrong thing first. A five-question score helps you pick the workflow that pays back fastest.",
  body="""
<p>Most teams that try automation start with whatever annoys the loudest person in the room. Sometimes that works. Often it doesn't, because the most annoying task isn't the one that pays back fastest.</p>
<p>Here's the scoring method we use in our free audits. It takes about 20 minutes with a spreadsheet.</p>

<h2>Step 1: List every repetitive task</h2>
<p>Ask each person on the team to write down anything they do at least weekly that follows roughly the same steps. Don't filter yet. Typical answers: building the same Excel report, reconciling two systems, copying data from emails or PDFs, sending reminders, updating a CRM.</p>

<h2>Step 2: Score each task on five questions</h2>
<p>Give each a score from 1 (low) to 5 (high).</p>
<table>
<tr><th>Question</th><th>Why it matters</th></tr>
<tr><td><strong>Hours per month</strong> spent on it, across everyone</td><td>The size of the prize.</td></tr>
<tr><td><strong>How rule-based</strong> is it?</td><td>Clear rules automate cleanly. Heavy judgement needs a person in the loop.</td></tr>
<tr><td><strong>How stable</strong> is the process?</td><td>If it changes every month, the automation will too.</td></tr>
<tr><td><strong>Cost of mistakes</strong> today</td><td>Errors in GST, payroll or invoices are expensive. Automation with checks removes them.</td></tr>
<tr><td><strong>Data access</strong>: is the input digital and reachable?</td><td>Data trapped in paper or a locked system adds work before automation can start.</td></tr>
</table>
<p>Add the five scores. Anything above 18 is a strong first candidate.</p>

<div class="callout"><strong>Rule of thumb:</strong> your first automation should be boring, frequent and visible. Boring means low risk. Frequent means fast payback. Visible means the team sees it working and asks for the next one.</div>

<h2>Step 3: Check the "last mile"</h2>
<p>Before committing, ask where the output goes. A reconciliation that produces a perfect file nobody opens hasn't saved anything. The best first projects end in something a person already uses: the report they send, the sheet they plan from, the WhatsApp message they'd otherwise type.</p>

<h2>Step 4: Start with a pilot, not a platform</h2>
<p>Automate one workflow end to end on real data. Measure hours before and after. That number becomes the business case for everything that follows, and it's far more convincing than any slide.</p>

<h2>Examples that usually score high</h2>
<ul>
<li>Monthly GST or bank reconciliation</li>
<li>Weekly management reports rebuilt from ERP exports</li>
<li>Invoice data entry from PDFs</li>
<li>Payslip generation and dispatch</li>
<li>Answering the same customer questions on WhatsApp</li>
</ul>
<p>If you want a second pair of eyes on your list, that's exactly what our free 30-minute call is for.</p>
"""),
 dict(slug="n8n-make-or-custom-python", cat="Tools", mins=7, date="October 2026",
  title="n8n, Make or custom Python: how to choose",
  desc="No-code tools are fast to start; custom code scales further. Here's how we decide which to use for each workflow.",
  body="""
<p>Clients often ask whether they should use a no-code tool like n8n or Make, or have something built in Python. The honest answer: it depends on the workflow, and many good setups use both.</p>

<h2>The short version</h2>
<table>
<tr><th></th><th>Make / Zapier</th><th>n8n</th><th>Custom Python</th></tr>
<tr><td><strong>Best for</strong></td><td>Simple app-to-app flows</td><td>Multi-step flows, self-hosting</td><td>Heavy data, complex logic</td></tr>
<tr><td><strong>Speed to first version</strong></td><td>Hours</td><td>Hours to days</td><td>Days</td></tr>
<tr><td><strong>Handles large files</strong></td><td>Poorly</td><td>Moderately</td><td>Well</td></tr>
<tr><td><strong>Runs on your servers</strong></td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td><strong>Cost at high volume</strong></td><td>Grows per task</td><td>Mostly fixed</td><td>Mostly fixed</td></tr>
<tr><td><strong>Who can edit it</strong></td><td>Ops team</td><td>Ops team with some help</td><td>Developers</td></tr>
</table>

<h2>When no-code wins</h2>
<p>If the job is "when X happens in one app, do Y in another", for example a new form entry creating a CRM contact and a Slack message, Make or Zapier is usually the right call. It's quick, your team can change it themselves, and volumes are low enough that per-task pricing doesn't hurt.</p>

<h2>When n8n wins</h2>
<p>n8n sits in the middle. It handles longer, branching workflows, can run on your own server (useful when data can't leave your environment), and its cost doesn't climb with every task. We use it a lot for integrations between CRMs, WhatsApp and internal tools.</p>

<h2>When custom Python wins</h2>
<p>Reach for code when the work involves large spreadsheets, reconciliations with fuzzy matching, OCR, machine learning, or logic that would turn into a tangle of boxes in a visual tool. Python also makes testing and version control straightforward, which matters for anything touching money.</p>

<div class="callout"><strong>A common pattern:</strong> Python does the heavy lifting (reading Tally, matching thousands of rows, building reports) and n8n handles the edges (triggering the job, sending WhatsApp alerts, updating the CRM).</div>

<h2>Questions to ask before you choose</h2>
<ol>
<li>How many runs per month, and how big is each input?</li>
<li>Does the data have to stay on your own servers?</li>
<li>Who will change this workflow in six months?</li>
<li>What happens if it fails silently? (If the answer is "something expensive", you want proper tests and alerts.)</li>
</ol>
<p>There's no prize for using the most advanced tool. The right choice is the simplest one that will still be running reliably a year from now.</p>
"""),
 dict(slug="what-ai-agents-can-and-cannot-do", cat="AI agents", mins=6, date="October 2026",
  title="What AI agents can and can\u2019t do for your business today",
  desc="AI agents are genuinely useful for some jobs and risky for others. A practical guide to where they work and where to keep a human.",
  body="""
<p>"AI agent" has become a buzzword, so it helps to be precise. An agent is a language model that can do more than chat: it can look things up, call your tools and take actions, such as booking a meeting or updating a record.</p>
<p>That's powerful, and it's also where the risk comes from. Here's where we've seen agents work well, and where we still keep a person in charge.</p>

<h2>Where agents work well today</h2>
<ul>
<li><strong>Answering repeat customer questions</strong> about orders, timings, prices and policies, using your real data.</li>
<li><strong>Qualifying leads</strong> by asking a few structured questions and routing serious buyers to sales.</li>
<li><strong>Booking and rescheduling</strong> against a real calendar.</li>
<li><strong>Reading documents</strong> and pulling out fields, with validation.</li>
<li><strong>Internal Q&amp;A</strong> over SOPs and policies, with links to the source.</li>
<li><strong>Drafting</strong> follow-ups, summaries and replies for a person to approve.</li>
</ul>

<h2>Where to keep a human in the loop</h2>
<ul>
<li><strong>Anything that moves money</strong>: refunds, payments, credit decisions. Let the agent prepare; let a person approve.</li>
<li><strong>Legal, medical or financial advice.</strong> Agents can find information; they shouldn't be the final word.</li>
<li><strong>Angry or sensitive conversations.</strong> A good agent recognises these and hands over quickly.</li>
<li><strong>Rare edge cases</strong> the agent has never seen. Build a clear "I don't know, let me get someone" path.</li>
</ul>

<div class="callout"><strong>The design rule we follow:</strong> give the agent the narrowest permissions that let it do its job, log every action it takes, and make handing over to a human easy for both the customer and the agent.</div>

<h2>How to tell if an agent is ready to launch</h2>
<ol>
<li>Test it on a few hundred real past conversations, not made-up ones.</li>
<li>Measure how often it answers correctly, hands over correctly, and gets something wrong.</li>
<li>Read the failures. If any would embarrass you or cost money, fix those before launch.</li>
<li>Launch to a slice of traffic first, and review conversations weekly.</li>
</ol>

<h2>The real benefit</h2>
<p>The best agents don't replace your team. They take the 60–70% of conversations that are routine, answer them instantly at any hour, and hand your people the ones that genuinely need them, with the context already gathered.</p>
"""),
 dict(slug="gst-reconciliation-automation", cat="Finance", mins=7, date="October 2026",
  title="GST reconciliation automation: a practical guide for Indian finance teams",
  desc="How to automate matching your purchase register against GSTR-2B, what to keep manual, and what a realistic setup looks like.",
  body="""
<p>For most Indian finance teams and CA firms, GST reconciliation is the most predictable pain of the month. The rules are clear, the data is digital, and the work repeats every cycle. That combination makes it one of the best first candidates for automation.</p>

<h2>What "reconciliation" actually involves</h2>
<p>The core job is comparing two lists that should agree:</p>
<ul>
<li><strong>Your purchase register</strong>, usually exported from Tally or your ERP.</li>
<li><strong>GSTR-2B</strong>, the auto-drafted statement of input tax credit built from what your suppliers have filed.</li>
</ul>
<p>Every invoice needs to be matched on supplier GSTIN, invoice number, date and tax amounts. Anything missing or different has to be investigated before you claim credit. On the outward side, sales data feeds GSTR-1, and the summary feeds GSTR-3B.</p>

<h2>Why it takes so long by hand</h2>
<ul>
<li>Invoice numbers are written differently in the books and on the portal (for example "INV/045" vs "45").</li>
<li>Dates, rounding and credit notes make exact matches fail.</li>
<li>Large registers mean thousands of rows, and filters and VLOOKUPs break easily.</li>
<li>The same steps are repeated for every GSTIN and every month.</li>
</ul>

<h2>What a good automation does</h2>
<ol>
<li><strong>Pulls both sides automatically</strong>: the purchase register from Tally or the ERP, and the GSTR-2B file.</li>
<li><strong>Normalises the data</strong>: cleans invoice numbers, standardises dates and GSTINs.</li>
<li><strong>Matches in layers</strong>: exact matches first, then near matches (small rounding differences, reformatted invoice numbers) flagged as "probable".</li>
<li><strong>Produces a short exception list</strong>: invoices in the books but missing from 2B, invoices in 2B but not in the books, and amount mismatches.</li>
<li><strong>Builds the outputs</strong> your team already uses: Excel workings and GSTR-1 and GSTR-3B drafts.</li>
<li><strong>Sends them</strong> to the right people by email or WhatsApp, and logs every run.</li>
</ol>

<div class="callout"><strong>What stays manual:</strong> deciding what to do about each exception. Following up with a supplier or deciding whether to claim credit is a judgement call, and it should stay with your team. Automation's job is to shrink that list to the few entries that truly need a person.</div>

<h2>What results look like</h2>
<p>For one CA firm we worked with, a reconciliation that took about three hours per report now runs in under five minutes, and the team only reviews the flagged entries. The bigger win was predictability: month-end stopped being a scramble.</p>

<h2>Before you start</h2>
<ul>
<li>Make sure you can export the purchase register in a consistent format each month.</li>
<li>Collect two or three months of past data with known answers to test against.</li>
<li>Agree who owns the exception list and how quickly it should be cleared.</li>
</ul>
<p>Automation supports your compliance process; it doesn't replace professional judgement. Your CA or tax advisor should still review what gets filed.</p>
"""),
 dict(slug="tally-automation", cat="Finance", mins=6, date="October 2026",
  title="Tally automation: what you can automate and how it connects",
  desc="Tally sits at the centre of many Indian businesses. Here are the ways to get data in and out of it automatically, and the workflows worth automating first.",
  body="""
<p>Tally is the accounting backbone for a huge number of Indian businesses. It's reliable, but getting data in and out of it often means manual exports, copy-paste and rebuilding the same Excel reports every month. The good news: most of that can be automated without replacing Tally.</p>

<h2>How automations connect to Tally</h2>
<table>
<tr><th>Method</th><th>Good for</th><th>Notes</th></tr>
<tr><td><strong>XML over HTTP</strong></td><td>Reading reports and posting vouchers</td><td>TallyPrime can act as a server on your local network. Scripts send XML requests and get data back. The most flexible option.</td></tr>
<tr><td><strong>ODBC</strong></td><td>Reading masters and transactions</td><td>Lets tools like Excel or Python query Tally data directly. Mostly read-oriented.</td></tr>
<tr><td><strong>Scheduled exports</strong></td><td>Simple, low-risk starts</td><td>Export to Excel or CSV on a schedule and process the file. Easy, but less real-time.</td></tr>
</table>
<p>Which method fits depends on your Tally version, where it runs, and whether the automation needs to write data back or only read it.</p>

<h2>Workflows worth automating</h2>
<ul>
<li><strong>Monthly MIS reports</strong>: P&amp;L, cash flow and ageing pulled from Tally and formatted the way management likes them.</li>
<li><strong>GST reconciliation</strong>: purchase register matched against GSTR-2B with an exception list.</li>
<li><strong>Bank reconciliation</strong>: statements matched to ledger entries, with only unmatched lines left for review.</li>
<li><strong>Voucher entry</strong>: invoices read by OCR and posted as purchase vouchers after validation.</li>
<li><strong>Receivables follow-up</strong>: overdue invoices identified daily and reminders sent on WhatsApp or email.</li>
<li><strong>Multi-company consolidation</strong>: data from several Tally companies combined into one report.</li>
</ul>

<div class="callout"><strong>Start read-only.</strong> The safest first automation reads from Tally and produces reports. Once the team trusts it, add workflows that write back, such as posting vouchers, with validation and a review step.</div>

<h2>Common questions</h2>
<h3>Do we have to move off Tally?</h3>
<p>No. Automation works around Tally. Your accountants keep using it exactly as they do today.</p>
<h3>Does Tally need to be on the cloud?</h3>
<p>Not necessarily. Automations can run on a machine in the same office network as Tally, or connect to a hosted Tally setup.</p>
<h3>Is it safe to let a script post entries?</h3>
<p>With the right safeguards, yes: validate every field, post to a review state where possible, log every entry, and alert a person on anything unusual.</p>

<h2>A realistic first step</h2>
<p>Pick the report your team rebuilds most often from Tally exports. Automate just that, measure the hours saved, and use the result to decide what comes next.</p>
"""), dict(slug="atc-losses-energy-theft-analytics", cat="Power distribution", mins=7, date="October 2026",
  title="AT&C losses explained: where electricity goes missing, and how analytics finds it",
  desc="A practical guide for distribution companies on separating technical losses, theft and billing errors using smart meter data.",
  body="""
<p>Every distribution company knows the gap between the energy it buys and the energy it gets paid for. The industry calls it AT&amp;C loss: aggregate technical and commercial loss. Reducing it is one of the fastest ways for a DISCOM to improve its finances, but only if you can tell what kind of loss you're looking at.</p>

<h2>Three different problems under one number</h2>
<ul>
<li><strong>Technical losses</strong> are the physics of moving power: heat in lines and transformers. They can be reduced with network upgrades, but never to zero.</li>
<li><strong>Commercial losses</strong> are energy that reached consumers but was never correctly billed: theft by hooking or meter bypass, tampering, wrong tariff categories, faulty meters and billing errors.</li>
<li><strong>Collection losses</strong> are bills issued but not paid.</li>
</ul>
<p>Each needs a different response. Sending vigilance teams after what is really a faulty meter wastes time and damages trust with honest consumers.</p>

<h2>Start at the distribution transformer</h2>
<p>The most useful unit of analysis is the distribution transformer. If you know how much energy entered it and how much was billed to every consumer it serves, the difference, minus a realistic technical loss, is the unexplained loss for that small area. Smart meters on transformers and consumer premises make this energy balance possible every billing cycle instead of once a year.</p>

<div class="callout"><strong>The key step:</strong> rank transformers by unexplained loss first, then look at individual consumers only on the worst ones. It turns a city-wide problem into a short, prioritised list.</div>

<h2>What separates theft from faults</h2>
<p>Within a high-loss transformer, consumer-level signals point to the likely cause:</p>
<ul>
<li>Load at night with very low billed units can suggest a bypass.</li>
<li>A sudden, lasting drop in consumption after a tamper event points to meter interference.</li>
<li>A load profile that looks commercial on a domestic connection suggests category misuse.</li>
<li>Gaps in readings followed by flat values usually mean a meter or communication fault, not theft.</li>
<li>Vacant premises explain low consumption without any wrongdoing.</li>
</ul>

<h2>Making leads field-ready</h2>
<p>Field teams need more than a risk score. A good lead says which consumer, why they were flagged, and what to check on site. Inspection results should flow back into the system, so the model learns which signals actually led to recoveries in your network.</p>

<h2>Where to begin</h2>
<p>A pilot on 12 months of historical meter and billing data for a few feeders is usually enough to show whether transformer-level analytics will pay off, before any change to live operations.</p>
<p><a href="/products/gridsentinel/">GridSentinel</a> is our product for exactly this workflow.</p>
"""),
 dict(slug="fuel-retail-loss-four-way-reconciliation", cat="Fuel retail", mins=6, date="October 2026",
  title="Where fuel goes missing between the depot and the nozzle",
  desc="Transit theft, tank leaks, short-dispensing, adulteration and cash shortfalls: how four-way reconciliation catches each one.",
  body="""
<p>A fuel retail outlet looks simple: fuel comes in, fuel goes out, money comes in. In practice there are several hand-offs between the depot and the customer, and loss can creep in at each of them. Small daily gaps add up quickly across a network of outlets.</p>

<h2>The four numbers that should agree</h2>
<ol>
<li><strong>Invoiced:</strong> what the depot dispatched and billed.</li>
<li><strong>Received:</strong> what actually reached the outlet's tanks.</li>
<li><strong>Sold:</strong> what the nozzles dispensed.</li>
<li><strong>Collected:</strong> what money and card payments came in.</li>
</ol>
<p>Comparing these every day, for every outlet, is what we mean by four-way reconciliation. Each gap points to a different problem and a different person to talk to.</p>

<h2>What each gap usually means</h2>
<table>
<tr><th>Gap</th><th>Common causes</th><th>First action</th></tr>
<tr><td>Invoiced vs received</td><td>Transit theft, short delivery</td><td>Check transporter seals and decanting records</td></tr>
<tr><td>Received vs sold</td><td>Tank leaks, theft from tanks, calibration errors</td><td>Review night-time tank level drops and dip readings</td></tr>
<tr><td>Sold vs dispensed correctly</td><td>Nozzle short-dispensing</td><td>Check dispenser calibration</td></tr>
<tr><td>Sold vs collected</td><td>Cash shortfalls, fleet card misuse</td><td>Reconcile deposits and card settlements</td></tr>
</table>

<h2>Quality is a loss too</h2>
<p>Adulteration doesn't show up as missing litres; it shows up as fuel that isn't what it should be. Monitoring density readings against expected values helps flag tanks that need a sample tested before more fuel is sold from them.</p>

<div class="callout"><strong>Patterns across outlets matter.</strong> A transporter who short-delivers a little at many outlets can stay under every single outlet's tolerance. Looking across the network surfaces patterns no individual outlet would notice.</div>

<h2>Making it practical</h2>
<ul>
<li>Use automatic tank gauge (ATG) data where available rather than manual dips alone.</li>
<li>Agree tolerances per product and outlet, so normal evaporation and temperature effects don't trigger alerts.</li>
<li>Give every flag a value in rupees and a specific next step, so area managers know what to do first.</li>
</ul>
<p><a href="/products/fuelledger/">FuelLedger</a> automates this reconciliation for every outlet, every day.</p>
"""),
 dict(slug="payment-fraud-detection-rules-vs-machine-learning", cat="Payments", mins=6, date="October 2026",
  title="Real-time payment fraud detection: rules vs machine learning",
  desc="Why static rules struggle with modern payment fraud, what machine learning adds, and how to introduce it without risking live approvals.",
  body="""
<p>Most payment businesses start fraud prevention with rules: block transactions above a limit, flag new devices, decline certain merchant categories at night. Rules are easy to understand and quick to deploy. They also have well-known limits.</p>

<h2>Where rules struggle</h2>
<ul>
<li><strong>They're blunt.</strong> A limit that stops fraud also stops good customers making large, legitimate payments.</li>
<li><strong>They're easy to learn.</strong> Fraudsters probe thresholds and stay just under them.</li>
<li><strong>They pile up.</strong> Over time, hundreds of overlapping rules become hard to maintain and nobody is sure which ones still help.</li>
</ul>

<h2>What machine learning adds</h2>
<p>A model looks at many signals together instead of one at a time, and weighs them based on your own history of good and fraudulent transactions:</p>
<ul>
<li>How many payments this device has made in the last hour</li>
<li>Whether the amount is unusual for this customer or merchant</li>
<li>Time of day and location consistency</li>
<li>The risk history of the merchant category</li>
</ul>
<p>The result is a score for every transaction, which maps to approve, review or decline. Because the model sees combinations, a large payment from a trusted device at a normal hour can sail through while a modest one with several weak warning signs goes to review.</p>

<div class="callout"><strong>Explainability matters.</strong> Every decision should come with the top reasons behind it, so analysts can review cases quickly and customers can be given a clear explanation.</div>

<h2>Keeping models healthy</h2>
<p>Fraud patterns change. A model that was accurate six months ago may drift as customer behaviour and attack methods shift. Production systems need monitoring for data drift and performance drift, versioned models, and the ability to roll back quickly if a new version misbehaves.</p>

<h2>Introducing ML safely</h2>
<ol>
<li>Train on your historical transactions and known fraud outcomes.</li>
<li>Run the model in shadow mode next to your current rules, without affecting approvals.</li>
<li>Compare decisions: what it caught that rules missed, and where it would have blocked good customers.</li>
<li>Agree thresholds, then roll out gradually.</li>
</ol>
<p>Rules don't have to disappear. Many teams keep a small set of hard rules for clear-cut cases and let the model handle the grey areas.</p>
<p>Try our <a href="/#try">interactive fraud score demo</a>, or read about <a href="/products/paysentinel/">PaySentinel</a>.</p>
"""),
]