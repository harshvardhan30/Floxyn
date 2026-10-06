# Auto Solution — Company Website

Marketing website for **Auto Solution**, an AI automation & analytics studio.
Static site: plain HTML, CSS and JavaScript. No build step, no dependencies.

## Project structure

```
.
├── index.html              # Single landing page
├── privacy.html            # Privacy policy
├── 404.html                # Not-found page
├── favicon.svg
├── site.webmanifest
├── robots.txt
├── sitemap.xml
├── .nojekyll               # Lets GitHub Pages serve files as-is
└── assets/
    ├── css/style.css       # All styles
    ├── js/field.js         # Hero 3D particle field (plain WebGL, no libraries)
    ├── js/main.js          # Header, scroll story, counters, savings estimate, forms
    ├── fonts/              # Self-hosted Unbounded + Geist (no Google Fonts call)
    └── img/                # OG share image, app icons
```

## Run locally

Any static server works:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Page structure

Hero (3D field) → integrations strip → scroll-driven automation run → results
with case studies → AI agent demo → savings estimate → services → industries →
engagement models → process → team & security → founder note & time zones →
quotes → FAQ → contact.

The 3D field pauses when off-screen, and everything falls back to a static
layout for visitors who set "reduce motion" in their OS.

## How the forms work

The contact form and savings estimate don't use a backend. Submitting opens
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
- [ ] **Savings estimate assumption:** assumes 60% of repetitive work is automatable
      (`SHARE` in `assets/js/main.js`). Adjust to what your projects actually show.
- [ ] **Founder note** is a draft written in Harsh's voice. Edit it so it sounds like him.
- [ ] **Case study wording** ("The problem / What we built / The result") expands the
      original one-line project descriptions. Check each matches what really happened.
- [ ] **AI agent demo** uses a made-up property company ("Skyline Homes") and is labelled
      "Example". Swap in a real (anonymised) conversation if you have one.
- [ ] **"Recommended" badge** on the Project plan: change or remove if another plan suits most clients.
- [ ] **Sample GST run figures** (1,247 / 1,238 / 9) are illustrative; swap in a real run if you have one.
- [ ] **Claims to be able to back up:** IIT/NIT/BITS alumni, PayPal/Paytm/Pine Labs
      experience, 15+ countries, 99.9% accuracy, 98% retention.
- [ ] **Social links:** add real LinkedIn / X URLs in the footer (`.foot-social`).
- [ ] **Insights articles:** cards have no links yet; link them when posts exist.
- [ ] **Privacy policy:** have it reviewed for your jurisdiction (India DPDP Act,
      GDPR if you have EU clients).
- [ ] **Canonical / OG URLs:** if the final domain differs, update
      `https://www.autosolution.com` in `index.html`, `privacy.html`,
      `robots.txt` and `sitemap.xml`.
