#!/usr/bin/env python3
"""Generates the static pages of amrinderjakhar.com into OUT. Edit content here, re-run."""
import pathlib, sys, datetime
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
OUT.mkdir(parents=True, exist_ok=True)

SITE = "https://amrinderjakhar.com"
EMAIL = "aj01359@uga.edu"
YEAR = datetime.date.today().year
LINKS = {
    "ORCID": "https://orcid.org/0009-0001-9110-8118",
    "Google Scholar": "https://scholar.google.com/citations?user=-YphPCoAAAAJ",
    "GitHub": "https://github.com/AmrinderJakhar98",
    "LinkedIn": "https://www.linkedin.com/in/amrinder-jakhar-272b331a4/",
}
LOGO = ('<svg viewBox="0 0 100 100" aria-hidden="true" focusable="false"><mask id="aj-cut"><rect width="100" height="100" fill="#fff"/>'
        '<g stroke="#000" fill="none" stroke-width="6.5"><path d="M62 -4V64a16 16 0 0 1-16 16a16 16 0 0 1-14.5-9.2" stroke-linecap="round"/>'
        '<path d="M62 5L-2 73"/><path d="M27 42H62"/></g></mask><circle fill="currentColor" cx="50" cy="50" r="50" mask="url(#aj-cut)"/></svg>')

ICON = {  # small inline line icons
 "sensor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 20c3-6 13-6 16 0"/><path d="M12 14V4"/><path d="M8 7l4-3 4 3"/><circle cx="12" cy="14" r="1.5"/></svg>',
 "drone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 3l9 4.5-9 4.5-9-4.5z"/><path d="M3 12l9 4.5 9-4.5"/><path d="M3 16.5L12 21l9-4.5"/></svg>',
 "ml": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="5" cy="6" r="2"/><circle cx="5" cy="18" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 7l3 4M7 17l3-4M14 11l3-4M14 13l3 4"/></svg>',
 "water": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/><path d="M9 15a3 3 0 0 0 3 3"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 "link": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M10 14a4 4 0 0 0 6 0l3-3a4 4 0 0 0-6-6l-1 1"/><path d="M14 10a4 4 0 0 0-6 0l-3 3a4 4 0 0 0 6 6l1-1"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
 "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/></svg>',
 "teach": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg>',
 "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6M15 14c3 0 6 2 6 5"/></svg>',
}
# icons are decoration: keep them out of the screen-reader tree
ICON = {k: v.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1) for k, v in ICON.items()}

NAV = [("index.html", "Home"), ("research.html", "Research"), ("publications.html", "Publications"),
       ("teaching.html", "Teaching"), ("cv.html", "CV"), ("contact.html", "Contact")]

import json, csv, re, html as _html, urllib.request, urllib.parse, time
esc = _html.escape

def write(name, text):
    (OUT / name).write_text(text, encoding="utf-8", newline="\n")

# ---------------------------------------------------------------- structured data (schema.org)
def ld(*nodes):
    js = json.dumps({"@context": "https://schema.org", "@graph": list(nodes)}, separators=(",", ":"))
    # keep text from the CSV from closing the script block
    js = js.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return '<script type="application/ld+json">' + js + '</script>'

PERSON = {
  "@type": "Person", "@id": SITE + "/#person",
  "name": "Amrinder Jakhar",
  "url": SITE + "/", "image": SITE + "/assets/img/amrinder-jakhar.jpg",
  "email": EMAIL,
  "jobTitle": "Ph.D. Candidate, Crop and Soil Sciences",
  "description": "Agronomist and applied data scientist working on precision agriculture, remote sensing, machine learning and water quality.",
  "affiliation": {"@type": "CollegeOrUniversity", "name": "University of Georgia", "url": "https://www.uga.edu"},
  "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Mississippi State University"},
               {"@type": "CollegeOrUniversity", "name": "Punjab Agricultural University"}],
  "hasCredential": [
    {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": "M.S., Agronomy",
     "recognizedBy": {"@type": "CollegeOrUniversity", "name": "Mississippi State University"}},
    {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": "B.Sc. (Hons.), Agriculture",
     "recognizedBy": {"@type": "CollegeOrUniversity", "name": "Punjab Agricultural University"}}],
  "award": ["Outstanding Graduate Student Award, International Society of Precision Agriculture, 2024",
            "1st Place, Bayer Graduate Hackathon Challenge, CANVAS 2025",
            "1st Place, Graduate Poster Competition, 16th International Conference on Precision Agriculture, 2024"],
  "knowsAbout": ["Precision agriculture", "Remote sensing", "Machine learning", "Nitrogen management", "Water quality", "Agricultural data science"],
  "sameAs": list(LINKS.values()),
  "address": {"@type": "PostalAddress", "addressLocality": "Athens", "addressRegion": "GA", "addressCountry": "US"},
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Amrinder Jakhar",
           "inLanguage": "en", "publisher": {"@id": SITE + "/#person"}}
LD = {"index.html": ld(WEBSITE, {"@type": "ProfilePage", "@id": SITE + "/#profile", "url": SITE + "/",
                                 "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": PERSON})}

OG_ALT = "Amrinder Jakhar, precision agriculture and data science. AJ monogram on a dark background."

CUR = ' aria-current="page"'
def page(fn, title, desc, body):
    nf = fn == "404.html"            # the 404 page is served from any path, so it needs absolute URLs
    P = "/" if nf else ""
    menu = "".join(f'<li><a href="{"/" if nf and h == "index.html" else P + h}"{CUR if h == fn else ""}>{t}</a></li>' for h, t in NAV)
    social = " ".join(f'<a href="{u}">{k}</a>' for k, u in LINKS.items())
    full = "Amrinder Jakhar | Precision Agriculture & Data Science" if fn == "index.html" else f"{title} | Amrinder Jakhar"
    canon = SITE + ("/" if fn == "index.html" else "/" + fn)
    t_e, d_e, alt = esc(full), esc(desc), esc(OG_ALT)
    if nf:
        seo = '<meta name="robots" content="noindex">'
    else:
        og_type = ('<meta property="og:type" content="profile"><meta property="profile:first_name" content="Amrinder">'
                   '<meta property="profile:last_name" content="Jakhar">') if fn == "index.html" else '<meta property="og:type" content="website">'
        img = SITE + "/assets/icons/social-preview.png"
        seo = f"""<link rel="canonical" href="{canon}">
{og_type}<meta property="og:site_name" content="Amrinder Jakhar"><meta property="og:locale" content="en_US">
<meta property="og:title" content="{t_e}"><meta property="og:description" content="{d_e}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{img}"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{alt}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t_e}"><meta name="twitter:description" content="{d_e}"><meta name="twitter:image" content="{img}"><meta name="twitter:image:alt" content="{alt}">"""
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t_e}</title>
<meta name="description" content="{d_e}">
{seo}
<link rel="icon" href="{P}assets/icons/favicon.ico" sizes="any"><link rel="icon" href="{P}assets/icons/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{P}assets/icons/apple-touch-icon.png">
<meta name="theme-color" content="#0f1913">
<link rel="stylesheet" href="{P}assets/css/style.css">
<noscript><style>.burger{{display:none}}.nav .wrap{{height:auto;flex-wrap:wrap;padding-top:8px;padding-bottom:8px}}.menu{{display:flex;flex-direction:row;flex-wrap:wrap;position:static;padding:0;box-shadow:none}}.menu a{{border-bottom:0;padding:8px 10px}}.nav{{position:static}}</style></noscript>
{LD.get(fn, "")}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
<a class="brand" href="{"/" if nf else "index.html"}">{LOGO}<span>Amrinder Jakhar<small>Precision Ag &amp; Data Science</small></span></a>
<button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span aria-hidden="true">&#9776;</span></button>
<nav aria-label="Main"><ul class="menu" id="menu">{menu}</ul></nav>
</div></header>
<main id="main" tabindex="-1">
<p class="printhead">Amrinder Jakhar &middot; Ph.D. candidate, Crop and Soil Sciences, University of Georgia &middot; {EMAIL} &middot; amrinderjakhar.com</p>
{body}
</main>
<footer><div class="wrap">
<span>&copy; <span id="yr">{YEAR}</span> Amrinder Jakhar &middot; Athens, Georgia &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
<nav class="social" aria-label="Profiles">{social}</nav>
</div></footer>
<script src="{P}assets/js/site.js" defer></script>
</body>
</html>
"""
    write(fn, html)

def phead(h, p):
    return f'<div class="phead"><div class="wrap"><h1>{h}</h1><p>{p}</p></div></div>'

# ---------------------------------------------------------------- data
XGB_REPO = "https://github.com/AmrinderJakhar98/XgBoost_2025_dsa"
THEMES = [
 ("sensor", "Sensor-based nitrogen management",
  "Using canopy sensors to set side-dress nitrogen rates in irrigated corn.",
  ["Six site-years of irrigated corn trials across Georgia (Tifton, Midville, Watkinsville)",
   "Side-dress timing, at-planting rate and sensor prescriptions against uniform-rate controls",
   "Agronomic and economic optimum N rates, nitrogen use efficiency and partial profit",
   "Global meta-analysis: 235 paired comparisons from 25 studies in nine countries, with an economic sensitivity analysis across six nitrogen-to-maize price scenarios"],
  ["Corn", "Nitrogen", "On-farm trials", "Meta-analysis"]),
 ("drone", "Remote sensing",
  "Comparing proximal canopy sensors, UAV multispectral and satellite imagery over the same plots.",
  ["Proximal active sensors (Crop Circle, GreenSeeker), MicaSense UAV multispectral, PlanetScope",
   "Canopy cover and soil background explain why platforms disagree (manuscript in revision)",
   "Vegetation-index and normalization choices for in-season N prescriptions",
   "UAV LiDAR in cotton: flight settings, plant height and yield prediction (co-author)"],
  ["UAV", "Satellite", "LiDAR", "Vegetation indices"]),
 ("ml", "Machine learning",
  "Yield prediction and image models built from field, weather and sensor data.",
  ["Gradient boosting (XGBoost) and random forests with tidymodels resampling and tuning",
   "Explainable AI for peanut yield and grade prediction (co-author; Computers and Electronics in Agriculture, 2026)",
   "Within-field cotton yield prediction and model generalizability (co-author)",
   "Random forest / XGBoost soil-pixel removal from UAV imagery; YOLO kernel counting (class project)",
   f'Open lesson code: <a href="{XGB_REPO}">gradient boosting with XGBoost and tidymodels</a>'],
  ["XGBoost", "Random forest", "XAI", "R &amp; Python"]),
 ("water", "Soil and water quality",
  "My M.S. work on biochar and gypsum and on nutrient losses in Mississippi Delta soils.",
  ["Sugarcane biochar and FGD gypsum in rainfed Mississippi Delta cotton and soybean",
   "Soil solution sampled with suction-cup lysimeters at two depths to track nutrient movement",
   "Nutrients by ion chromatography, Lachat flow injection and ICP-OES",
   "Bulk density, infiltration, aggregate stability and soil carbon responses"],
  ["Biochar", "Gypsum", "Nutrient leaching", "Mississippi Delta"]),
]

# ---------------------------------------------------------------- publications
# Publications live in publications.csv (edit that file, not this one).
# Columns: doi, type, year, title, authors, journal, topics, note
#   type   = journal | review | proc | ext   (blank = journal)
#   topics = any of, separated by ";": nitrogen; remote sensing; machine learning; soil and water; decision tools
# A row with only a DOI is enough: a missing title, authors, journal or year is filled
# from Crossref when the site is rebuilt, and written back into publications.csv.
PUB_CSV = pathlib.Path(__file__).with_name("publications.csv")
FIELDS = ["doi", "type", "year", "title", "authors", "journal", "topics", "note"]
TOPIC_KEYS = {"nitrogen": "nitrogen", "remote sensing": "sensing", "machine learning": "ml",
              "soil and water": "water", "decision tools": "tools"}
FILTERS = [("nitrogen", "Nitrogen"), ("sensing", "Remote sensing"), ("ml", "Machine learning"),
           ("water", "Soil and water"), ("tools", "Decision tools")]
ME = "Jakhar"

def clean_doi(d):
    d = (d or "").strip()
    for p in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "doi:"):
        if d.lower().startswith(p):
            d = d[len(p):]
    return d.strip()

def crossref(doi):
    """Metadata for a DOI from Crossref, or {} when offline or unknown."""
    m = None
    for attempt in (1, 2):
        try:
            req = urllib.request.Request("https://api.crossref.org/works/" + urllib.parse.quote(doi),
                                         headers={"User-Agent": "academic-website-builder/1.0"})
            m = json.load(urllib.request.urlopen(req, timeout=20))["message"]
            break
        except Exception as e:
            print("  Crossref lookup failed for", doi, "-", e)
            if attempt == 1:
                time.sleep(5)
    if m is None:
        return {}
    def initials(g):
        return " ".join(p[0] + "." for p in g.replace("-", " ").split() if p)
    auth = [f"{a.get('family', '')}, {initials(a.get('given', ''))}".strip(", ") or a.get("name", "") for a in m.get("author", [])]
    auth = [a for a in auth if a]
    authors = (", ".join(auth[:-1]) + ", & " + auth[-1]) if len(auth) > 2 else " & ".join(auth)
    bits = [(m.get("container-title") or [""])[0]]
    if m.get("volume"):
        bits.append(m["volume"] + (f"({m['issue']})" if m.get("issue") else ""))
    if m.get("article-number") or m.get("page"):
        bits.append(m.get("article-number") or m.get("page"))
    year = ""
    for k in ("published-print", "published-online", "issued"):
        dp = (m.get(k) or {}).get("date-parts")
        if dp and dp[0] and dp[0][0]:
            year = str(dp[0][0]); break
    return {"title": _html.unescape(re.sub(r"<[^>]+>", "", (m.get("title") or [""])[0])),
            "authors": authors, "journal": ", ".join(b for b in bits if b), "year": year}

def load_pubs():
    try:
        with PUB_CSV.open(newline="", encoding="utf-8-sig") as fh:
            rd = csv.DictReader(fh)
            lost = [f for f in FIELDS if f not in (rd.fieldnames or [])]
            if lost:
                sys.exit(f"ERROR: publications.csv is missing the column(s) {lost}. Save it as a comma-separated CSV (UTF-8).")
            rows = list(rd)
    except UnicodeDecodeError:
        sys.exit("ERROR: publications.csv must be saved as CSV UTF-8.")
    changed = False
    for r in rows:
        for f in FIELDS:
            r[f] = (r.get(f) or "").strip()
        if r["doi"] != clean_doi(r["doi"]):
            r["doi"] = clean_doi(r["doi"]); changed = True
        if r["doi"] and not all(r[f] for f in ("title", "authors", "journal", "year")):
            for f, v in crossref(r["doi"]).items():
                if v and not r[f]:
                    r[f] = v; changed = True
    # stop instead of quietly publishing a page that is missing a paper
    lost = [r["doi"] for r in rows if r["doi"] and not r["title"]]
    if lost:
        sys.exit("ERROR: no details found for DOI(s): " + ", ".join(lost)
                 + ". Check the DOI, or fill in title, authors, journal and year by hand.")
    if changed:
        tmp = PUB_CSV.with_suffix(".tmp")
        with tmp.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            w.writeheader()
            w.writerows({f: r[f] for f in FIELDS} for r in rows)
        tmp.replace(PUB_CSV)
        print("publications.csv updated")
    rows = [r for r in rows if r["title"]]
    if not rows:
        sys.exit("ERROR: publications.csv has no publications.")
    def yr(r):
        m = re.match(r"\d{4}", r["year"])
        return int(m.group()) if m else 0
    rows.sort(key=yr, reverse=True)
    return rows

PUBS = load_pubs()

def kind(r):
    return (r["type"] or "journal").lower()

def topic_tags(s):
    out = []
    for t in re.split(r"[;,]", s):
        k = TOPIC_KEYS.get(t.strip().lower())
        if k and k not in out:
            out.append(k)
    return out

def venue_html(j):
    """Journal name (and volume) in italics; a status such as (in revision) as a small label."""
    st = ""
    m = re.match(r"^(.*?)\s*\((in revision|submitted|under review|in press|accepted)\)$", j, re.I)
    if m:
        j, st = m.group(1), f' <span class="st">{esc(m.group(2).capitalize())}</span>'
    m = re.match(r"^(.*?(?:, \d+)?)(\(\d+\))?(, (?:\d|p\.).*)?$", j)
    name, rest = (m.group(1), (m.group(2) or "") + (m.group(3) or "")) if m else (j, "")
    return f"<i>{esc(name)}</i>{esc(rest)}{st}"

def pub_html(r):
    tags = " ".join(topic_tags(r["topics"]))
    note = r["note"] or ("First author" if re.match(re.escape(ME) + r",", r["authors"]) else "")
    b = f' <span class="badge">{esc(note)}</span>' if note else ""
    authors = re.sub(r"\b(" + re.escape(ME) + r", [A-Z]\.?(?:[ -]?[A-Z]\.?)*)(?![A-Za-z])", r"<b>\1</b>", esc(r["authors"]))
    l = ""
    if r["doi"]:
        href = "https://doi.org/" + urllib.parse.quote(r["doi"], safe="/:()<>;")
        l = f'<div class="links"><a href="{esc(href)}" aria-label="DOI for {esc(r["title"])}">DOI</a></div>'
    return (f'<li class="pub" data-tags="{tags}"><div class="yr">{esc(r["year"])}</div><div>'
            f'<div class="t">{esc(r["title"])}{b}</div><div class="a">{authors}</div>'
            f'<div class="v">{venue_html(r["journal"])}</div>{l}</div></li>')

def article_ld(r):
    names = re.findall(r"([^,&]+), ((?:[A-Z]\.\s?)+)", r["authors"])
    authors = [{"@type": "Person", "name": "Amrinder Jakhar", "url": SITE + "/"} if f.strip() == ME
               else {"@type": "Person", "name": g.strip() + " " + f.strip()} for f, g in names]
    a = {"@type": "ScholarlyArticle", "headline": r["title"], "name": r["title"], "datePublished": r["year"],
         "author": authors, "isPartOf": {"@type": "Periodical", "name": re.split(r",\s*\d", r["journal"])[0]}}
    if r["doi"]:
        a["sameAs"] = "https://doi.org/" + r["doi"]
        a["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": r["doi"]}
    return a
LD["publications.html"] = ld(*[article_ld(p) for p in PUBS if kind(p) == "journal"])

# UPDATE AT GRADUATION (May 2027): "Ph.D. candidate" / "will graduate" appear in PERSON jobTitle, the print header
# in page(), the home hero and About text, the meta descriptions, the CV education rows and the Contact intro.
NEWS = [
 ("Nov 2026", "Presented an oral talk and a poster at CANVAS 2026 in Portland, OR."),
 ("Oct 2026", "Defended my Ph.D. dissertation at the University of Georgia."),
 ("Aug 2026", "2nd place, NxS Hackathon, and 3rd place poster at the Nitrogen Use Efficiency Workshop."),
 ("Jul 2026", "Invited speaker, Brazil-Global Digital Agriculture Workshop, UNESP Jaboticabal."),
 ("2026", "Meta-analysis on sensor-based variable-rate nitrogen published in <i>Precision Agriculture</i>."),
 ("Nov 2025", "1st place, Bayer Graduate Hackathon Challenge (Team DataGenix), CANVAS 2025."),
]
MONTHS = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
def iso(d):
    p = d.split()
    return d if len(p) == 1 else f"{p[1]}-{MONTHS[p[0]]:02d}"

# ---------------------------------------------------------------- pages
cards = "".join(f'<a class="card reveal" href="research.html#theme-{n}"><div class="icon">{ICON[i]}</div><h3>{h}</h3><p>{d}</p></a>' for n, (i, h, d, _, _) in enumerate(THEMES, 1))
news = "".join(f'<li><time datetime="{iso(d)}">{d}</time><span>{t}</span></li>' for d, t in NEWS)
sel = "".join(pub_html(p) for p in PUBS if kind(p) == "journal")
META_DOI = "https://doi.org/10.1007/s11119-026-10447-1"

page("index.html", "Home",
 "Amrinder Jakhar is a Ph.D. candidate at the University of Georgia working on precision agriculture, remote sensing, machine learning and water quality.",
 f"""
<section class="hero"><picture><source media="(max-width:820px)" srcset="assets/img/field-whole-tall.webp"><img class="bg" src="assets/img/field-whole-900.webp" srcset="assets/img/field-whole-900.webp 900w, assets/img/field-whole-1600.webp 1600w" sizes="100vw" alt="" width="1600" height="900" decoding="async"></picture>
<div class="wrap">
 <div>
  <div class="eyebrow">Crop and Soil Sciences &middot; University of Georgia</div>
  <h1>Amrinder Jakhar</h1>
  <p class="lead">I am a Ph.D. candidate at the University of Georgia. I study in-season nitrogen management in corn using canopy sensors, drone and satellite imagery, and machine learning.</p>
  <ul class="tags"><li>Ph.D. candidate, Crop and Soil Sciences, UGA</li><li>Remote sensing</li><li>Machine learning</li><li>Water quality</li><li>FAA Part 107 pilot</li></ul>
  <div class="btns"><a class="btn btn-primary" href="cv.html">View CV</a><a class="btn btn-ghost" href="publications.html">Publications</a><a class="btn btn-ghost" href="contact.html">Get in touch</a></div>
  <p class="mail"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
 </div>
 <div class="portrait"><picture><source srcset="assets/img/amrinder-jakhar.webp" type="image/webp"><img src="assets/img/amrinder-jakhar.jpg" alt="Portrait of Amrinder Jakhar" width="320" height="320" fetchpriority="high"></picture></div>
</div></section>

<div class="wrap"><ul class="stats" aria-label="At a glance">
 <li class="stat reveal"><b>{sum(kind(p) == "journal" for p in PUBS)}</b><span>peer-reviewed articles</span></li>
 <li class="stat reveal"><b>6</b><span>site-years of corn N trials</span></li>
 <li class="stat reveal"><b>3</b><span>sensing platforms compared</span></li>
 <li class="stat reveal"><b>12+</b><span>research and hackathon awards</span></li>
</ul></div>

<section><div class="wrap two">
 <div>
  <h2>About me</h2>
  <p>I work in Dr. Leonardo M. Bastos's lab in the Department of Crop and Soil Sciences. I defended my dissertation in October 2026 and will graduate in May 2027.</p>
  <p>Most of my Ph.D. has been in corn fields in Georgia. I compare handheld canopy sensors, drone imagery and satellite imagery for deciding how much nitrogen to side-dress, and I led a meta-analysis on sensor-based variable-rate nitrogen in maize that came out in <a href="{META_DOI}"><i>Precision Agriculture</i></a> in 2026.</p>
  <p>I also fit machine learning models, mostly gradient boosting and random forests in R, and have worked with lab mates on yield prediction for peanut and cotton. For my M.S. at Mississippi State University I studied biochar and gypsum in Delta cotton and soybean, including how they change nutrient losses in soil water.</p>
  <p>I am looking for positions in precision agriculture and agricultural data science starting in 2027.</p>
 </div>
 <div>
  <h2>News</h2>
  <ul class="news">{news}</ul>
 </div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head"><h2>Research</h2><a href="research.html">All research <span aria-hidden="true">&rarr;</span></a></div>
 <div class="grid g4">{cards}</div>
</div></section>

<section><div class="wrap">
 <div class="sec-head"><h2>Peer-reviewed journal articles</h2><a href="publications.html">Full list <span aria-hidden="true">&rarr;</span></a></div>
 <ul class="plist">{sel}</ul>
</div></section>
""")

# field photos (720 px WebP, loaded only when scrolled to)
PHOTOS = '<ul class="photos">' + "".join(
 f'<li><img src="assets/img/{f}.webp" alt="{a}" width="720" height="540" loading="lazy" decoding="async"></li>' for f, a in [
  ("field-plots", "Drone view straight down on rectangular crop plots in a research field"),
  ("field-corn-contrast", "Tall dark green corn beside shorter, lighter green corn in the next plot"),
  ("field-rows", "Rows of young corn in a research field under a blue sky")]) + "</ul>"
themes = "".join(
 f'<div class="theme reveal" id="theme-{n}"><div><div class="icon">{ICON[i]}</div><h2>{h}</h2><p>{d}</p>'
 + '<ul class="pills" aria-label="Topics">' + "".join(f'<li class="pill">{t}</li>' for t in tags) + "</ul>"
 + "<ul>" + "".join(f"<li>{x}</li>" for x in pts) + "</ul></div></div>"
 for n, (i, h, d, pts, tags) in enumerate(THEMES, 1))
page("research.html", "Research", "Research by Amrinder Jakhar at the University of Georgia on sensor-based nitrogen management, remote sensing, machine learning and water quality.",
 phead("Research", "My Ph.D. is on nitrogen management and crop sensing in Georgia corn. My M.S. was on soil amendments and water quality.")
 + f'<section><div class="wrap">{PHOTOS}{themes}</div></section>'
 + """<section class="alt"><div class="wrap two">
 <div><h2>Field sites</h2>
 <p>Replicated corn nitrogen trials at UGA research farms in Tifton (Ponder and Rigdon Farms), Midville and Watkinsville (Iron Horse Farm), plus on-farm trials with Georgia growers. M.S. field work in the Mississippi Delta.</p></div>
 <div><h2>Equipment and methods</h2>
 <div class="chips"><span>Crop Circle ACS-435</span><span>GreenSeeker</span><span>MicaSense Altum-PT</span><span>DJI M300 RTK</span><span>Zenmuse L1 LiDAR</span><span>PlanetScope</span><span>Veris MSP3</span><span>Mixed-effects models</span><span>Meta-analysis</span><span>EONR / AONR</span><span>XGBoost</span><span>tidymodels</span><span>QGIS</span><span>Pix4D</span><span>Sapelo2 HPC</span></div></div>
</div></section>""")

groups = [("journal","Peer-reviewed journal articles"),("review","Submitted and under review"),("proc","Conference proceedings"),("ext","Extension and outreach")]
pubs = "".join(
 f'<div class="pgroup"><h2>{g} <span class="n">({sum(kind(p) == k for p in PUBS)})</span></h2><ul class="plist">'
 + "".join(pub_html(p) for p in PUBS if kind(p) == k) + "</ul></div>"
 for k, g in groups if any(kind(p) == k for p in PUBS))
fbtns = '<button type="button" class="on" aria-pressed="true" data-f="all">All</button>' + "".join(
 f'<button type="button" aria-pressed="false" data-f="{k}">{t}</button>'
 for k, t in FILTERS if any(k in topic_tags(p["topics"]) for p in PUBS))
page("publications.html", "Publications", "Publications by Amrinder Jakhar, University of Georgia, in precision agriculture, remote sensing, machine learning and water quality.",
 phead("Publications", 'Everything I have published or submitted, newest first in each group. The same list is on my <a href="'+LINKS["Google Scholar"]+'">Google Scholar</a> and <a href="'+LINKS["ORCID"]+'">ORCID</a> pages.')
 + f"""<section><div class="wrap">
 <div class="filters" role="group" aria-label="Filter publications by topic">{fbtns}</div>
 <p id="pubcount" class="count" role="status" aria-live="polite"></p>
 <div class="pubs">{pubs}</div></div></section>""")

page("teaching.html", "Teaching & Mentoring", "Teaching, mentoring, open-source code and outreach by Amrinder Jakhar, Ph.D. candidate in Crop and Soil Sciences at the University of Georgia.",
 phead("Teaching &amp; Mentoring", "I was a teaching assistant at the University of Georgia and have mentored graduate and high school students.")
 + f"""<section><div class="wrap two">
 <div><h2>CRSS 8030: Data Science and Statistical Programming Applied to Agriculture</h2>
 <p class="meta">Teaching Assistant &middot; University of Georgia &middot; Spring 2025</p>
 <p>I held weekly office hours and helped graduate students with R and statistical modeling. I had taken the course myself in 2024.</p>
 <p>I also taught one lecture and lab on gradient boosting with XGBoost and tidymodels. The code and recording are public.</p>
 <div class="btns"><a class="btn btn-dark" href="{XGB_REPO}">Lesson code</a><a class="btn btn-dark" href="https://www.youtube.com/watch?v=64FaToOxLLo">Watch the recording</a></div></div>
 <div><h2>Students I have mentored</h2>
 <ul class="tl">
  <li><div class="when">2024 &middot; 8 months</div><h3>Visiting graduate researcher, USP / ESALQ</h3><p>Co-supervised a project on nitrogen rate effects on corn grain quality for dairy nutrition.</p></li>
  <li><div class="when">2024 &middot; Young Scholars Program</div><h3>High school student</h3><p>Using drone and satellite imagery to prescribe nitrogen fertilizer in corn.</p></li>
  <li><div class="when">2023 &middot; Young Scholars Program</div><h3>High school student</h3><p>Drone imagery processing and analysis; featured in a UGA CAES article.</p></li>
 </ul></div>
</div></section>
<section class="alt"><div class="wrap">
 <h2>Code and tools</h2>
 <div class="grid g3">
  <div class="card reveal"><h3><a href="{XGB_REPO}">XGBoost teaching module</a></h3><p>Annotated, reproducible R lesson on gradient boosting with tidymodels (2025).</p></div>
  <div class="card reveal"><h3>PGRx dashboard</h3><p>Co-developer of a cotton plant growth regulator recommender; manuscript under review.</p></div>
  <div class="card reveal"><h3>Cotton variety selector</h3><p>Co-developer of a dashboard that helps choose cotton varieties from Georgia variety trial results (2025).</p></div>
  <div class="card reveal"><h3>NxS Advisor</h3><p>Nitrogen-by-sulfur decision tool built with Team Georgia, 2nd place at the NxS Hackathon, 2026 Nitrogen Use Efficiency Workshop. Prototype, not yet public.</p></div>
  <div class="card reveal"><h3>Optical-sensor N algorithm library</h3><p>Reproducible R implementations of published in-season N algorithms (in progress).</p></div>
  <div class="card reveal"><h3>Outreach</h3><p>Field-day sensor demos for about 100 growers, consultants, students and faculty, and drone and data science sessions for school students.</p></div>
 </div>
</div></section>""")

CVBTN = '<p><a class="btn btn-dark" href="assets/Amrinder_Jakhar_CV.pdf">Download full CV (PDF)</a></p>' if (OUT / "assets/Amrinder_Jakhar_CV.pdf").exists() else ""

SD = '<div class="s">{}</div>'
def rows(items):
    return "".join(f'<div class="row"><div><b>{a}</b>{"<br>"+b if b else ""}</div><div class="d">{d}</div>{SD.format(s) if s else ""}</div>' for a, b, d, s in items)

page("cv.html", "CV", "Curriculum vitae of Amrinder Jakhar, Ph.D. candidate in Crop and Soil Sciences at the University of Georgia: education, research, honors, talks and skills.",
 phead("Curriculum Vitae", "Ph.D. candidate in Crop and Soil Sciences at the University of Georgia.")
 + f"""<section><div class="wrap">
 {CVBTN}
 <div class="cvsec"><h2>Education</h2>{rows([
  ("Ph.D., Crop and Soil Sciences","University of Georgia, Athens, GA","Jan 2023 &ndash; May 2027 (expected)","Dissertation on in-season sensor-based corn nitrogen management in Georgia. Advisor: Dr. Leonardo M. Bastos. Defended October 30, 2026; degree conferral expected May 2027."),
  ("Graduate Certificate in Agricultural Data Science","University of Georgia","Award May 2027","Coursework completed."),
  ("M.S., Agronomy","Mississippi State University, MS","2021 &ndash; 2022","Thesis: Biochar and gypsum effects on soil properties and water quality in cotton and soybean production systems in the Mississippi Delta. Advisor: Dr. Jagmandeep Dhillon. Defended December 2022; degree conferred December 2023."),
  ("B.Sc. (Hons.), Agriculture","Punjab Agricultural University, Ludhiana, India","2013 &ndash; 2019","")])}</div>
 <div class="cvsec"><h2>Research experience</h2>{rows([
  ("Graduate Research Assistant","Crop and Soil Sciences, University of Georgia","2023 &ndash; present","Multi-site-year corn N trials; proximal, UAV and satellite sensing; optimum N rate models; global meta-analysis; collaborative ML and UAV LiDAR studies."),
  ("Graduate Research Assistant","Mississippi State University","2021 &ndash; 2022","Biochar and gypsum effects on soil physical properties and water quality, with lysimeter soil-solution monitoring and IC, Lachat and ICP-OES analysis."),
  ("Intern, Cotton Development Program","Department of Agriculture and Farmers Welfare, Government of Punjab, India","Aug &ndash; Oct 2018","")])}</div>
 <div class="cvsec"><h2>Selected honors</h2>{rows([
  ("2nd Place, NxS Hackathon (Team Georgia)","Nitrogen Use Efficiency Workshop, Starkville, MS","2026",""),
  ("3rd Place, Poster Contest","Nitrogen Use Efficiency Workshop, Starkville, MS","2026",""),
  ("1st Place, Bayer Graduate Hackathon Challenge","CANVAS 2025, Salt Lake City, UT","2025","24-hour competition with 30 graduate students from 15 universities. Our team built a genomic prediction model combining linear mixed models and random forests to pick maize genotypes for field testing."),
  ("Outstanding Graduate Student Award","International Society of Precision Agriculture, 16th ICPA","2024",""),
  ("1st Place, Graduate Poster Competition","Precision Nutrient Management, 16th ICPA","2024",""),
  ("1st Place, Sensor-Based Nutrient Management Poster","ASA-CSSA-SSSA Annual Meeting","2023",""),
  ("2nd Place, Ag Hackathon (soil carbon modeling)","ASA-CSSA-SSSA Annual Meeting","2023",""),
  ("1st Place, Environmental Quality Poster","ASA-CSSA-SSSA Annual Meeting","2021","")])}</div>
 <div class="cvsec"><h2>Invited and workshop talks</h2>{rows([
  ("Variable-rate nitrogen in corn: agronomic, economic, and remote-sensing perspectives","Brazil-Global Digital Agriculture Workshop, UNESP, Brazil","Jul 2026","One of six invited speakers; 100+ attendees."),
  ("Let the Plants Talk: Using Sensors for Crop Nutrient Management","Precision Agriculture Workshop, UGA Griffin","Mar 2025","Workshop for growers, crop consultants, USDA personnel and extension staff."),
  ("Proximal and Aerial Sensors for In-Season Variable Nitrogen Rate Application in Corn","1st Minas Precision Agriculture Symposium, UFLA, Brazil","Mar 2024","")])}</div>
 <div class="cvsec"><h2>Service &amp; leadership</h2>{rows([
  ("Co-President and Founding Member","Integrative Precision Agriculture Club, UGA","2024 &ndash; 2026","Organized the 2026 IPAC Innovation Showcase for 45 graduate students and 35 faculty, and a speaker series carried live to the Athens, Tifton and Griffin campuses."),
  ("Peer reviewer (11 manuscripts)","Precision Agriculture; Agronomy Journal; Agrosystems, Geosciences &amp; Environment; Agricultural &amp; Environmental Letters","2025 &ndash;",""),
  ("Chair, Webinar Subcommittee","ASA-CSSA-SSSA Graduate Student Committee","2023 &ndash;",""),
  ("Co-organizer, Graduate Student Networking Session","ASA-CSSA-SSSA International Annual Meeting, San Antonio, TX","2024",""),
  ("Member","ASA, CSSA and SSSA (2021 &ndash; present); International Society of Precision Agriculture (2024 &ndash; present)","","")])}</div>
 <div class="cvsec"><h2>Skills</h2><div class="chips"><span>R (tidymodels, lme4, Shiny)</span><span>Python (working knowledge)</span><span>SAS</span><span>Git / GitHub</span><span>XGBoost &amp; random forests</span><span>Explainable AI</span><span>Mixed-effects models</span><span>Meta-analysis</span><span>QGIS / ArcMap / ERDAS</span><span>Pix4D</span><span>UAV multispectral &amp; LiDAR</span><span>Ion chromatography</span><span>ICP-OES</span><span>FAA Part 107</span><span>English, Punjabi, Hindi</span></div></div>
</div></section>""")

def bare(u):
    return re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
contact = "".join(f'<li><div><b>{k}</b><br><a href="{u}" aria-label="{k}: {bare(u)}">{bare(u)}</a></div></li>' for k, u in LINKS.items())
page("contact.html", "Contact", "Contact Amrinder Jakhar, Ph.D. candidate in precision agriculture and data science at the University of Georgia.",
 phead("Contact", "I am looking for postdoctoral, industry and faculty positions in precision agriculture starting in 2027. Email is the best way to reach me.")
 + f"""<section><div class="wrap">
 <h2 class="sr-only">Contact details</h2>
 <ul class="contact-list">
  <li><div><b>Email</b><br><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
  <li><div><b>Office</b><br>Department of Crop and Soil Sciences<br>University of Georgia, Athens, GA 30602</div></li>
  {contact}
 </ul>
</div></section>""")

page("404.html", "Page not found", "Page not found.",
 phead("Page not found", 'I could not find that page. Use the menu above or go back to the <a href="/">home page</a>.'))

# GitHub Pages extras
write("CNAME", "amrinderjakhar.com\n")
write(".nojekyll", "")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}/{'' if h == 'index.html' else h}</loc></url>\n" for h, _ in NAV) + "</urlset>\n")
print("built", sorted(p.name for p in OUT.glob("*")))
