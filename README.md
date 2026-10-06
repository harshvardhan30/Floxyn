# Auto Solution — Company Website

Marketing website for **Auto Solution**, an AI automation & analytics studio.
Static site: plain HTML, CSS and JavaScript. No build step, no dependencies.

## Project structure

```
.
├── index.html              # Main page (Home + Sectors / Analytics / AI Dashboard tabs)
├── privacy.html            # Privacy policy
├── 404.html                # Not-found page
├── favicon.svg
├── site.webmanifest
├── robots.txt
├── sitemap.xml
├── .nojekyll               # Lets GitHub Pages serve files as-is
└── assets/
    ├── css/style.css       # All styles (light + dark theme)
    ├── js/main.js          # Navigation, routing, FAQ, forms, popups
    ├── js/dashboard.js     # Live dashboard demo (runs only when that tab is open)
    └── img/                # OG share image, app icons
```

## Run locally

Any static server works:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Pages & routing

Everything lives in `index.html`. Hash links switch views:

| URL | Shows |
|---|---|
| `/#about`, `/#services`, `/#contact` … | Home page, scrolled to that section |
| `/#sectors` | Industries we serve |
| `/#analytics` | Analytics dashboard demo |
| `/#dashboard` | AI live dashboard demo |

## How the forms work

The contact form and checklist form don't use a backend. Submitting opens
WhatsApp (`wa.me/917303897496`) with the details pre-filled. To change the
number, edit `WA_NUMBER` at the top of `assets/js/main.js` and the `wa.me`
links in `index.html`.

## Deploy

**GitHub Pages:** repo → Settings → Pages → Source: *Deploy from a branch* →
Branch: `main` / root → Save. The site appears at
`https://<username>.github.io/<repo>/` within a minute or two.

**Custom domain (autosolution.com):** in the same Pages screen, add the domain,
then point DNS at GitHub Pages (A records to GitHub's IPs, or a CNAME for `www`).

**Netlify / Vercel / Cloudflare Pages:** import the repo, no build command,
publish directory = `/`.

## Before going live — content checklist

These need a decision from the team; the code can't verify them:

- [ ] **Email address:** site uses `info@autosoluation.com` (note "solu**a**tion")
      but the domain is `autosolution.com`. Confirm which is correct, then
      find-and-replace across `index.html` and `privacy.html`.
- [ ] **Numbers that don't match each other:** "100+ automations" vs "50+ projects";
      "Analytics: 142 active automations"; GST case "3 hr → 5 min" (Work section)
      vs "3 hr → 4.2 s" (ticker, Sectors).
- [ ] **Team size:** "small team" in About vs "20 senior engineers" in Team.
- [ ] **Claims to be able to back up:** IIT/NIT/BITS alumni, PayPal/Paytm/Pine Labs
      experience, 15+ countries, 99.9% accuracy, 98% retention.
- [ ] **Social links:** add real LinkedIn / X URLs in the footer (`.foot-social`).
- [ ] **Insights articles:** cards have no links yet; link them when posts exist.
- [ ] **Privacy policy:** have it reviewed for your jurisdiction (India DPDP Act,
      GDPR if you have EU clients).
- [ ] **Canonical / OG URLs:** if the final domain differs, update
      `https://www.autosolution.com` in `index.html`, `privacy.html`,
      `robots.txt` and `sitemap.xml`.
