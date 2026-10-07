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
"""),
]