# Auto Solution — website

Multi-page marketing site for Auto Solution (AI agents & workflow automation).
Static HTML/CSS/JS, deployed on Vercel. No framework, no runtime dependencies.

## Structure

```
/                     ← built site (what Vercel serves)
├── index.html        Home
├── services/         Services + 4 detail pages
├── industries/       Industries + 6 detail pages
├── case-studies/     Case studies + 6 detail pages
├── insights/         Blog + articles
├── roi-calculator/  how-we-work/  about/  careers/  contact/  privacy/  terms/
├── assets/css/style.css   Design system
├── assets/js/site.js      Menus, animations, calculator, forms, chat demo
├── assets/js/field.js     Home page 3D particle hero (WebGL)
└── _src/build/       Page generator (not deployed — see .vercelignore)
    ├── content.py    Services, industries, case studies  ← edit text here
    ├── posts.py      Blog articles
    ├── layout.py     Header, footer, contact details, Calendly link
    └── build.py      Page templates
```

## Editing content

1. Change text in `_src/build/content.py`, `posts.py` or `layout.py`
   (email, phone, address and Calendly link are at the top of `layout.py`).
2. Rebuild: `python3 _src/build/build.py`
3. Commit and push. Vercel deploys automatically.

Header, footer and design changes apply to every page at once.

## Run locally

```bash
python3 _src/build/build.py
python3 -m http.server 8000   # open http://localhost:8000
```

## Contact & lead capture

- **Book a call** buttons open Calendly: https://calendly.com/autosoluationai/30min (embedded on /contact/).
- **Contact form** and **checklist download form** email leads to info@autosoluation.com via
  FormSubmit (free, no account). If FormSubmit is unreachable, the contact form falls back to WhatsApp.
  ⚠️ The first submission sends an *activation email* to info@autosoluation.com — click "Activate Form" once.
- **ROI calculator** sends the estimate via WhatsApp (+91 73038 97496).
- **Lead magnet:** /ai-automation-checklist/ → `assets/downloads/ai-automation-checklist.pdf`.

## Analytics

Vercel Web Analytics script is included on every page. Turn it on once in
Vercel → Project → Analytics → Enable. No cookies, so no cookie banner needed.

## Content to review

- [ ] Founder note (Home + About) is written in Harsh's voice — edit `FOUNDER_NOTE` in `build.py` so it sounds like him.
- [ ] Case study wording expands the original one-line descriptions — confirm each is accurate.
- [ ] The AI agent demo ("Skyline Homes") is an illustrative example and is labelled as such.
- [ ] Terms and privacy pages: have them reviewed for your jurisdiction.
- [ ] Add LinkedIn / social links in `layout.py` footer when available.
