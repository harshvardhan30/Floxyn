"""Generate 2-page PDF brochures for each product:  python3 _src/build/brochures.py"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from products import PRODUCTS
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("D", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
NIGHT = colors.HexColor("#0a0f2c"); FLUX = colors.HexColor("#ff7a1a"); SIG = colors.HexColor("#0a7aa2"); MUT = colors.HexColor("#5a627f"); LINE = colors.HexColor("#e2e5ee"); PAPER = colors.HexColor("#f5f6fa")
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "downloads"))
def clean(t): return re.sub(r"&amp;", "&", t).replace("\u2019", "'")
H2 = ParagraphStyle("h2", fontName="DB", fontSize=13.5, leading=18, textColor=NIGHT, spaceBefore=12, spaceAfter=6)
B = ParagraphStyle("b", fontName="D", fontSize=9.6, leading=14.5, textColor=colors.HexColor("#2b3253"))
FT = ParagraphStyle("ft", fontName="DB", fontSize=10, leading=13, textColor=NIGHT)
FD = ParagraphStyle("fd", fontName="D", fontSize=9, leading=13, textColor=MUT)
data_needed = {
 "paysentinel": ["12-24 months of transaction records", "Fraud and chargeback outcomes", "Device, merchant, amount and timestamp fields", "Current rules or decisions, for comparison"],
 "gridsentinel": ["12+ months of smart meter readings", "Transformer-level energy input", "Consumer master and billing records", "Past inspection outcomes, if available"],
 "fuelledger": ["Depot dispatch and invoice records", "Tank level (ATG) and density readings", "Nozzle or dispenser sales", "Cash deposit and fleet card records"]}
for p in PRODUCTS:
    def head(c, d, p=p):
        w, h = A4
        if d.page == 1:
            c.setFillColor(NIGHT); c.rect(0, h - 78 * mm, w, 78 * mm, fill=1, stroke=0)
            c.setFillColor(FLUX); c.rect(18 * mm, h - 22 * mm, 22 * mm, 1.6 * mm, fill=1, stroke=0)
            c.setFillColor(colors.HexColor("#4fe3ff")); c.setFont("DB", 10); c.drawString(18 * mm, h - 32 * mm, clean(p["cat"]).upper())
            c.setFillColor(colors.white); c.setFont("DB", 30); c.drawString(18 * mm, h - 47 * mm, p["name"])
            c.setFont("D", 15); c.setFillColor(colors.HexColor("#dfe4ff")); c.drawString(18 * mm, h - 58 * mm, clean(p["tagline"]))
            if p["stage"]:
                c.setFillColor(colors.HexColor("#4fe3ff")); c.setFont("DB", 9); c.drawString(18 * mm, h - 68 * mm, "\u25cf " + p["stage"].upper())
            c.setFont("DB", 10); c.setFillColor(colors.white); c.drawRightString(w - 18 * mm, h - 22 * mm, "Auto Solution")
        c.setStrokeColor(LINE); c.line(18 * mm, 15 * mm, w - 18 * mm, 15 * mm)
        c.setFont("D", 8); c.setFillColor(MUT)
        c.drawString(18 * mm, 10 * mm, f"{p['name']}  |  Auto Solution  |  info@autosoluation.com  |  Noida, India")
        c.drawRightString(w - 18 * mm, 10 * mm, f"{d.page} / 2")
    st = [Spacer(1, 66 * mm), Paragraph(clean(p["lede"]), ParagraphStyle("l", parent=B, fontSize=11, leading=17)), Paragraph("Capabilities", H2)]
    rows = [[Paragraph(clean(t), FT), Paragraph(clean(d), FD)] for t, d in p["features"]]
    tb = Table(rows, colWidths=[52 * mm, 122 * mm])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .5, LINE), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    st += [tb, Paragraph("How it works", H2)]
    st += [Paragraph(f"<b>{i+1}. {clean(t)}.</b> {clean(d)}", B) for i, (t, d) in enumerate(p["how"])]
    st += [PageBreak(), Paragraph("Built for", H2), Paragraph(", ".join(clean(x) for x in p["for_"]) + ".", B), Paragraph("Data we'll need for a pilot", H2)]
    st += [Paragraph("\u2022 " + x, B) for x in data_needed[p["slug"]]]
    st += [Paragraph("How we work", H2)] + [Paragraph("\u2022 " + x, B) for x in [
        "Learns from your own data and explains every flag it raises.",
        "Runs in your environment or a cloud account you approve.",
        "Humans stay in charge: borderline cases go to review, every decision is logged.",
        "Versioned models with monitoring, retraining and rollback."]]
    st += [Paragraph("Pilot program", H2), Paragraph("6-8 weeks on your own historical data, in shadow mode with no impact on live systems. Success criteria are agreed upfront and you get a clear go or no-go at the end. Fixed fee, credited in full against year one if you roll out.", B), Spacer(1, 14)]
    cta = Table([[Paragraph(f"<b>See {p['name']} in action</b><br/>Request a demo or a pilot: autosoluation.com/request-demo<br/>Book a call: calendly.com/autosoluationai/30min<br/>Email: info@autosoluation.com  |  Phone: +91 73038 97496",
                 ParagraphStyle("c", parent=B, textColor=colors.white, fontSize=10.5, leading=16))]], colWidths=[174 * mm])
    cta.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NIGHT), ("LEFTPADDING", (0, 0), (-1, -1), 16), ("TOPPADDING", (0, 0), (-1, -1), 14), ("BOTTOMPADDING", (0, 0), (-1, -1), 14)]))
    st += [cta]
    doc = SimpleDocTemplate(os.path.join(OUT, f"{p['slug']}-brochure.pdf"), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=14 * mm, bottomMargin=22 * mm, title=f"{p['name']} brochure", author="Auto Solution")
    doc.build(st, onFirstPage=head, onLaterPages=head)
    print("built", p["slug"])
