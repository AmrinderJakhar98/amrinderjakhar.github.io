#!/usr/bin/env python3
"""Generates the static pages of amrinderjakhar.com into OUT. Edit content here, re-run."""
import pathlib, sys
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

SITE = "https://amrinderjakhar.com"
EMAIL = "aj01359@uga.edu"
LINKS = {
    "ORCID": "https://orcid.org/0009-0001-9110-8118",
    "Google Scholar": "https://scholar.google.com/citations?user=-YphPCoAAAAJ",
    "GitHub": "https://github.com/AmrinderJakhar98",
    "LinkedIn": "https://www.linkedin.com/in/amrinder-jakhar-272b331a4/",
}
LOGO = ('<svg viewBox="0 0 100 100" aria-hidden="true"><mask id="aj-cut"><rect width="100" height="100" fill="#fff"/>'
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

NAV = [("index.html", "Home"), ("research.html", "Research"), ("publications.html", "Publications"),
       ("teaching.html", "Teaching"), ("cv.html", "CV"), ("contact.html", "Contact")]

import json
JSONLD = '<script type="application/ld+json">' + json.dumps({
  "@context": "https://schema.org", "@type": "Person",
  "name": "Amrinder Jakhar",
  "url": SITE + "/", "image": SITE + "/assets/img/amrinder-jakhar.jpg",
  "email": "mailto:" + EMAIL,
  "jobTitle": "Ph.D. Candidate, Crop and Soil Sciences",
  "description": "Agronomist and applied data scientist working on precision agriculture, remote sensing, machine learning and water quality.",
  "affiliation": {"@type": "CollegeOrUniversity", "name": "University of Georgia", "url": "https://www.uga.edu"},
  "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Mississippi State University"},
               {"@type": "CollegeOrUniversity", "name": "Punjab Agricultural University"}],
  "knowsAbout": ["Precision agriculture", "Remote sensing", "Machine learning", "Nitrogen management", "Water quality", "Agricultural data science"],
  "sameAs": [u for k, u in LINKS.items() if u.startswith("http")],
  "address": {"@type": "PostalAddress", "addressLocality": "Athens", "addressRegion": "GA", "addressCountry": "US"},
}, separators=(",", ":")) + '</script>'

def page(fn, title, desc, body):
    menu = "".join(f'<li><a href="{h}"{" aria-current=page" if h == fn else ""}>{t}</a></li>' for h, t in NAV)
    social = " ".join(f'<a href="{u}">{k}</a>' for k, u in LINKS.items())
    full = "Amrinder Jakhar | Precision Agriculture & Data Science" if fn == "index.html" else f"{title} | Amrinder Jakhar"
    canon = SITE + ("/" if fn == "index.html" else "/" + fn)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/icons/social-preview.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/icons/favicon.ico" sizes="32x32"><link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">
<meta name="theme-color" content="#0f1913">
<script>document.documentElement.className="js"</script>
<link rel="stylesheet" href="assets/css/style.css">
{JSONLD if fn == "index.html" else ""}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
<a class="brand" href="index.html">{LOGO}<span>Amrinder Jakhar<small>Precision Ag &amp; Data Science</small></span></a>
<button class="burger" aria-label="Menu" aria-expanded="false">&#9776;</button>
<ul class="menu">{menu}</ul>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
<span>&copy; 2026 Amrinder Jakhar &middot; Athens, Georgia &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
<span class="social">{social}</span>
</div></footer>
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""
    (OUT / fn).write_text(html)

def phead(h, p):
    return f'<div class="phead"><div class="wrap"><div class="eyebrow">Amrinder Jakhar</div><h1>{h}</h1><p>{p}</p></div></div>'

# ---------------------------------------------------------------- data
THEMES = [
 ("sensor", "Sensor-based nitrogen management",
  "Using canopy sensors to set side-dress nitrogen rates in irrigated corn.",
  ["Six site-years of irrigated corn trials across Georgia (Tifton, Midville, Watkinsville)",
   "Side-dress timing, at-planting rate and sensor prescriptions against uniform-rate controls",
   "Agronomic and economic optimum N rates, nitrogen use efficiency and partial profit",
   "Global meta-analysis: 235 paired comparisons from 25 studies in nine countries"],
  ["Corn", "Nitrogen", "On-farm trials", "Meta-analysis"]),
 ("drone", "Remote sensing",
  "Comparing proximal canopy sensors, UAV multispectral and satellite imagery over the same plots.",
  ["Proximal active sensors (Crop Circle, GreenSeeker), MicaSense UAV multispectral, PlanetScope",
   "Canopy cover and soil background explain why platforms disagree",
   "Vegetation-index and normalization choices for in-season N prescriptions",
   "UAV LiDAR in cotton: flight settings, plant height and yield prediction"],
  ["UAV", "Satellite", "LiDAR", "Vegetation indices"]),
 ("ml", "Machine learning",
  "Yield prediction and image models built from field, weather and sensor data.",
  ["Gradient boosting (XGBoost) and random forests with tidymodels resampling and tuning",
   "Explainable AI for peanut yield and grade prediction (Computers and Electronics in Agriculture, 2026)",
   "Within-field cotton yield prediction and model generalizability",
   "Random forest / XGBoost soil-pixel removal from UAV imagery; YOLO kernel counting"],
  ["XGBoost", "Random forest", "XAI", "R & Python"]),
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
import csv, re, html as _html, urllib.request, urllib.parse
PUB_CSV = pathlib.Path(__file__).with_name("publications.csv")
FIELDS = ["doi", "type", "year", "title", "authors", "journal", "topics", "note"]
TOPIC_KEYS = {"nitrogen": "nitrogen", "remote sensing": "sensing", "machine learning": "ml",
              "soil and water": "water", "decision tools": "tools"}
ME = "Jakhar"

def clean_doi(d):
    d = (d or "").strip()
    for p in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "doi:"):
        if d.lower().startswith(p):
            d = d[len(p):]
    return d.strip()

def crossref(doi):
    """Metadata for a DOI from Crossref, or {} when offline or unknown."""
    try:
        req = urllib.request.Request("https://api.crossref.org/works/" + urllib.parse.quote(doi),
                                     headers={"User-Agent": "academic-website-builder/1.0"})
        m = json.load(urllib.request.urlopen(req, timeout=20))["message"]
    except Exception as e:
        print("  Crossref lookup failed for", doi, "-", e)
        return {}
    def initials(g):
        return " ".join(p[0] + "." for p in g.replace("-", " ").split() if p)
    auth = [f"{a.get('family', '')}, {initials(a.get('given', ''))}".strip(", ") for a in m.get("author", [])]
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
    rows = list(csv.DictReader(PUB_CSV.open(newline="", encoding="utf-8-sig")))
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
    if changed:
        with PUB_CSV.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            w.writeheader()
            w.writerows({f: r[f] for f in FIELDS} for r in rows)
        print("publications.csv updated")
    rows = [r for r in rows if r["title"]]
    rows.sort(key=lambda r: r["year"] or "9999", reverse=True)
    return rows

PUBS = load_pubs()

def kind(r):
    return (r["type"] or "journal").lower()

def pub_html(r):
    esc = _html.escape
    tags = " ".join(TOPIC_KEYS.get(t.strip().lower(), "") for t in r["topics"].split(";"))
    note = r["note"] or ("First author" if r["authors"].startswith(ME) else "")
    b = f'<span class="badge">{esc(note)}</span>' if note else ""
    authors = re.sub(r"(" + ME + r", [A-Z]\.(?: ?[A-Z]\.)*)", r"<b>\1</b>", esc(r["authors"]))
    l = f'<div class="links"><a href="https://doi.org/{esc(r["doi"])}">DOI</a></div>' if r["doi"] else ""
    return (f'<div class="pub" data-tags="{tags}"><div class="yr">{esc(r["year"])}</div><div>'
            f'<div class="t">{esc(r["title"])}{b}</div><div class="a">{authors}</div>'
            f'<div class="v">{esc(r["journal"])}</div>{l}</div></div>')

NEWS = [
 ("Nov 2026", "Presented an oral talk and a poster at CANVAS 2026 in Portland, OR."),
 ("Oct 2026", "Defended my Ph.D. dissertation at the University of Georgia."),
 ("Aug 2026", "2nd place, NxS Hackathon, and 3rd place poster at the Nitrogen Use Efficiency Workshop."),
 ("Jul 2026", "Invited speaker, Brazil-Global Digital Agriculture Workshop, UNESP Jaboticabal."),
 ("2026", "Meta-analysis on sensor-based variable-rate nitrogen published in <i>Precision Agriculture</i>."),
 ("Nov 2025", "1st place, Bayer Graduate Hackathon Challenge (Team DataGenix), CANVAS 2025."),
]

# ---------------------------------------------------------------- pages
cards = "".join(f'<div class="card reveal"><div class="icon">{ICON[i]}</div><h3>{h}</h3><p>{d}</p></div>' for i, h, d, _, _ in THEMES)
news = "".join(f'<li><time>{d}</time><span>{t}</span></li>' for d, t in NEWS)
sel = "".join(pub_html(p) for p in PUBS if kind(p) == "journal")

page("index.html", "Home",
 "Amrinder Jakhar is an agronomist and applied data scientist working on precision agriculture, remote sensing, machine learning and water quality.",
 f"""
<section class="hero"><div class="wrap">
 <div>
  <div class="eyebrow">Crop and Soil Sciences &middot; University of Georgia</div>
  <h1>Amrinder Jakhar</h1>
  <p class="lead">I am a Ph.D. candidate at the University of Georgia. I study in-season nitrogen management in corn using canopy sensors, drone and satellite imagery, and machine learning.</p>
  <ul class="tags"><li>Ph.D. Crop &amp; Soil Sciences, UGA</li><li>Remote sensing</li><li>Machine learning</li><li>Water quality</li><li>FAA Part 107 pilot</li></ul>
  <div class="btns"><a class="btn btn-primary" href="cv.html">View CV</a><a class="btn btn-ghost" href="publications.html">Publications</a><a class="btn btn-ghost" href="contact.html">Get in touch</a></div>
  <p style="margin:18px 0 0;color:#c8d6cc">&#9993; <a style="color:#8fc06b" href="mailto:{EMAIL}">{EMAIL}</a></p>
 </div>
 <div class="portrait"><picture><source srcset="assets/img/amrinder-jakhar.webp" type="image/webp"><img src="assets/img/amrinder-jakhar.jpg" alt="Portrait of Amrinder Jakhar" width="320" height="320" fetchpriority="high"></picture></div>
</div></section>

<div class="wrap"><div class="stats">
 <div class="stat reveal"><b>{sum(kind(p) == "journal" for p in PUBS)}</b><span>peer-reviewed articles</span></div>
 <div class="stat reveal"><b>6</b><span>site-years of corn N trials</span></div>
 <div class="stat reveal"><b>3</b><span>sensing platforms compared</span></div>
 <div class="stat reveal"><b>12+</b><span>research &amp; hackathon awards</span></div>
</div></div>

<section><div class="wrap two">
 <div>
    <h2>About me</h2>
  <p>I work in Dr. Leonardo M. Bastos's lab in the Department of Crop and Soil Sciences. I defended my dissertation in October 2026 and will graduate in May 2027.</p>
  <p>Most of my Ph.D. has been in corn fields in south and central Georgia. I compare handheld canopy sensors, drone imagery and satellite imagery for deciding how much nitrogen to side-dress, and I led a meta-analysis on sensor-based variable-rate nitrogen in maize that came out in <i>Precision Agriculture</i> this year.</p>
  <p>I also fit machine learning models, mostly gradient boosting and random forests in R, and have worked with lab mates on yield prediction for peanut and cotton. For my M.S. at Mississippi State University I studied biochar and gypsum in Delta cotton and soybean, including how they change nutrient losses in soil water.</p>
  <p>I am looking for positions in precision agriculture and agricultural data science starting in 2027.</p>
 </div>
 <div>
    <h2>News</h2>
  <ul class="news">{news}</ul>
 </div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head"><div><h2>Research</h2></div><a href="research.html">All research &rarr;</a></div>
 <div class="grid g4">{cards}</div>
</div></section>

<section><div class="wrap">
 <div class="sec-head"><div><h2>Peer-reviewed articles</h2></div><a href="publications.html">Full list &rarr;</a></div>
 <div class="pubs">{sel}</div>
</div></section>
""")

themes = "".join(
 f'<div class="theme reveal"><div class="num">0{n}</div><div><div class="icon">{ICON[i]}</div><h2>{h}</h2><p>{d}</p>'
 + "".join(f'<span class="pill">{t}</span>' for t in tags)
 + "<ul>" + "".join(f"<li>{x}</li>" for x in pts) + "</ul></div></div>"
 for n, (i, h, d, pts, tags) in enumerate(THEMES, 1))
page("research.html", "Research", "Research by Amrinder Jakhar on sensor-based nitrogen, remote sensing, machine learning and water quality.",
 phead("Research", "My Ph.D. is on nitrogen management and crop sensing in Georgia corn. My M.S. was on soil amendments and water quality.")
 + f'<section><div class="wrap">{themes}</div></section>'
 + """<section class="alt"><div class="wrap two">
 <div><div class="kicker">Field sites</div><h2>Field sites</h2>
 <p>Replicated corn nitrogen trials at UGA research farms in Tifton (Ponder and Rigdon Farms), Midville and Watkinsville (Iron Horse Farm), plus on-farm trials with Georgia growers. M.S. field work in the Mississippi Delta.</p></div>
 <div><div class="kicker">Toolkit</div><h2>Equipment and methods</h2>
 <div class="chips"><span>Crop Circle ACS-435</span><span>GreenSeeker</span><span>MicaSense Altum-PT</span><span>DJI M300 RTK</span><span>Zenmuse L1 LiDAR</span><span>PlanetScope</span><span>Veris MSP3</span><span>Mixed-effects models</span><span>Meta-analysis</span><span>EONR / AONR</span><span>XGBoost</span><span>tidymodels</span><span>QGIS</span><span>Pix4D</span><span>Sapelo2 HPC</span></div></div>
</div></section>""")

groups = [("journal","Peer-reviewed journal articles"),("review","Submitted and under review"),("proc","Conference proceedings"),("ext","Extension and outreach")]
pubs = "".join(f'<h2>{g}</h2>' + "".join(pub_html(p) for p in PUBS if kind(p) == k) for k, g in groups)
page("publications.html", "Publications", "Publications by Amrinder Jakhar in precision agriculture, remote sensing, machine learning and water quality.",
 phead("Publications", 'Journal articles, manuscripts under review and conference papers. Also on <a style="color:#8fc06b" href="'+LINKS["Google Scholar"]+'">Google Scholar</a> and <a style="color:#8fc06b" href="'+LINKS["ORCID"]+'">ORCID</a>.')
 + f"""<section><div class="wrap">
 <div class="filters"><button class="on" data-f="all">All</button><button data-f="nitrogen">Nitrogen</button><button data-f="sensing">Remote sensing</button><button data-f="ml">Machine learning</button><button data-f="water">Soil &amp; water</button><button data-f="tools">Decision tools</button></div>
 <div class="pubs">{pubs}</div></div></section>""")

page("teaching.html", "Teaching & Mentoring", "Teaching, mentoring, open-source code and outreach by Amrinder Jakhar.",
 phead("Teaching &amp; Mentoring", "Teaching and mentoring at the University of Georgia.")
 + f"""<section><div class="wrap two">
 <div><div class="kicker">Teaching</div><h2>CRSS 8030: Data Science &amp; Statistical Programming Applied to Agriculture</h2>
 <p class="when" style="color:var(--muted)">Teaching Assistant &middot; University of Georgia &middot; Spring 2025</p>
 <p>I held weekly office hours and helped graduate students with R and statistical modeling. I had taken the course myself in 2024.</p>
 <p>I also taught one lecture and lab on gradient boosting with XGBoost and tidymodels. The code and recording are public.</p>
 <div class="btns"><a class="btn btn-dark" href="https://github.com/AmrinderJakhar98/XgBoost_2025_dsa">Lesson code</a><a class="btn btn-dark" href="https://www.youtube.com/watch?v=64FaToOxLLo">Watch the recording</a></div></div>
 <div><div class="kicker">Mentoring</div><h2>Students I have mentored</h2>
 <ul class="tl">
  <li><div class="when">2024 &middot; 8 months</div><h3>Visiting graduate researcher, USP / ESALQ</h3><p>Co-supervised a project on nitrogen rate effects on corn grain quality for dairy nutrition.</p></li>
  <li><div class="when">2024 &middot; Young Scholars Program</div><h3>Rahul Mohanty</h3><p>Using drone and satellite imagery to prescribe nitrogen fertilizer in corn.</p></li>
  <li><div class="when">2023 &middot; Young Scholars Program</div><h3>Clayton Bivins</h3><p>Drone imagery processing and analysis; featured in a UGA CAES article.</p></li>
 </ul></div>
</div></section>
<section class="alt"><div class="wrap">
 <div class="kicker">Open code &amp; decision tools</div><h2>Code and tools</h2>
 <div class="grid g3">
  <div class="card reveal"><div class="icon">{ICON['code']}</div><h3>XGBoost teaching module</h3><p>Annotated, reproducible R lesson on gradient boosting with tidymodels (2025).</p></div>
  <div class="card reveal"><div class="icon">{ICON['ml']}</div><h3>PGRx dashboard</h3><p>Co-developer of a cotton plant growth regulator recommender; manuscript under review.</p></div>
  <div class="card reveal"><div class="icon">{ICON['sensor']}</div><h3>Cotton variety selector</h3><p>Co-developer of a dashboard turning Georgia variety trials into variety choices (2025).</p></div>
  <div class="card reveal"><div class="icon">{ICON['water']}</div><h3>NxS Advisor</h3><p>Nitrogen-by-sulfur decision tool, 2nd place at the 2026 NUE Workshop hackathon.</p></div>
  <div class="card reveal"><div class="icon">{ICON['drone']}</div><h3>Optical-sensor N algorithm library</h3><p>Reproducible R implementations of published in-season N algorithms (in progress).</p></div>
  <div class="card reveal"><div class="icon">{ICON['people']}</div><h3>Outreach</h3><p>Field-day sensor demos for ~100 growers, and drone and data science sessions for school students.</p></div>
 </div>
</div></section>""")

CVBTN = '<p><a class="btn btn-dark" href="assets/Amrinder_Jakhar_CV.pdf">Download full CV (PDF)</a></p>' if (OUT / "assets/Amrinder_Jakhar_CV.pdf").exists() else ""

def rows(items):
    return "".join(f'<div class="row"><div><b>{a}</b>{"<br>"+b if b else ""}</div><div class="d">{d}</div>{f"<div class=s>{s}</div>" if s else ""}</div>' for a, b, d, s in items)

page("cv.html", "CV", "Curriculum vitae of Amrinder Jakhar, agronomist and agricultural data scientist: education, research, honors, talks and skills.",
 phead("Curriculum Vitae", "Education, research experience, honors and skills.")
 + f"""<section><div class="wrap">
 {CVBTN}
 <div class="cvsec"><h2>Education</h2>{rows([
  ("Ph.D., Crop and Soil Sciences","University of Georgia, Athens, GA","2023 &ndash; May 2027","Dissertation on in-season sensor-based corn nitrogen management in Georgia. Advisor: Dr. Leonardo M. Bastos. Defended October 30, 2026."),
  ("Graduate Certificate in Agricultural Data Science","University of Georgia","Award May 2027",""),
  ("M.S., Agronomy","Mississippi State University, MS","2021 &ndash; 2022","Thesis: Biochar and gypsum effects on soil properties and water quality in cotton and soybean systems in the Mississippi Delta. Advisor: Dr. Jagmandeep Dhillon."),
  ("B.Sc. (Hons.), Agriculture","Punjab Agricultural University, Ludhiana, India","2013 &ndash; 2019","")])}</div>
 <div class="cvsec"><h2>Research experience</h2>{rows([
  ("Graduate Research Assistant","Crop and Soil Sciences, University of Georgia","2023 &ndash; present","Multi-site-year corn N trials; proximal, UAV and satellite sensing; optimum N rate models; global meta-analysis; collaborative ML and UAV LiDAR studies."),
  ("Graduate Research Assistant","Mississippi State University","2021 &ndash; 2022","Biochar and gypsum effects on soil physical properties and water quality, with lysimeter soil-solution monitoring and IC, Lachat and ICP-OES analysis."),
  ("Intern, Cotton Development Program","Government of Punjab, India","2018","")])}</div>
 <div class="cvsec"><h2>Selected honors</h2>{rows([
  ("1st Place, Bayer Graduate Hackathon Challenge","CANVAS 2025, Salt Lake City","2025",""),
  ("Outstanding Graduate Student Award","International Society of Precision Agriculture, 16th ICPA","2024",""),
  ("1st Place, Graduate Poster Competition","Precision Nutrient Management, 16th ICPA","2024",""),
  ("1st Place, Sensor-Based Nutrient Management Poster","ASA-CSSA-SSSA Annual Meeting","2023",""),
  ("2nd Place, Ag Hackathon (soil carbon modeling)","ASA-CSSA-SSSA Annual Meeting","2023",""),
  ("1st Place, Environmental Quality Poster","ASA-CSSA-SSSA Annual Meeting","2021","")])}</div>
 <div class="cvsec"><h2>Invited talks</h2>{rows([
  ("Variable-rate nitrogen in corn: agronomic, economic, and remote-sensing perspectives","Brazil-Global Digital Agriculture Workshop, UNESP, Brazil","Jul 2026",""),
  ("Let the Plants Talk: Using Sensors for Crop Nutrient Management","Precision Agriculture Workshop, UGA Griffin","Mar 2025",""),
  ("Proximal and Aerial Sensors for In-Season Variable Nitrogen Rate Application in Corn","1st Minas Precision Agriculture Symposium, UFLA, Brazil","Mar 2024","")])}</div>
 <div class="cvsec"><h2>Service &amp; leadership</h2>{rows([
  ("Co-President and Founding Member","Integrative Precision Agriculture Club, UGA","2024 &ndash; 2026",""),
  ("Peer reviewer (11 manuscripts)","Precision Agriculture; Agronomy Journal; AGE; Agricultural &amp; Environmental Letters","2025 &ndash;",""),
  ("Chair, Webinar Subcommittee","ASA-CSSA-SSSA Graduate Student Committee","2023 &ndash;","")])}</div>
 <div class="cvsec"><h2>Skills</h2><div class="chips"><span>R (tidymodels, lme4, Shiny)</span><span>Python</span><span>SAS</span><span>Git / GitHub</span><span>XGBoost &amp; random forests</span><span>Explainable AI</span><span>Mixed-effects models</span><span>Meta-analysis</span><span>QGIS / ArcMap / ERDAS</span><span>Pix4D</span><span>UAV multispectral &amp; LiDAR</span><span>Ion chromatography</span><span>ICP-OES</span><span>FAA Part 107</span><span>English, Punjabi, Hindi</span></div></div>
</div></section>""")

contact = "".join(f'<li><div class="icon">{ICON["link"]}</div><div><b>{k}</b><br><a href="{u}">{u if u != "#" else "add link"}</a></div></li>' for k, u in LINKS.items())
page("contact.html", "Contact", "Contact Amrinder Jakhar, Ph.D. candidate in precision agriculture and data science at the University of Georgia.",
 phead("Contact", "I am looking for postdoctoral, industry and faculty positions in precision agriculture starting in 2027. Email is the best way to reach me.")
 + f"""<section><div class="wrap two">
 <div><ul class="contact-list">
  <li><div class="icon">{ICON['mail']}</div><div><b>Email</b><br><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
  <li><div class="icon">{ICON['pin']}</div><div><b>Office</b><br>Department of Crop and Soil Sciences<br>University of Georgia, Athens, GA 30602</div></li>
  {contact}
 </ul></div>
</div></section>""")

# GitHub Pages extras
(OUT / "CNAME").write_text("amrinderjakhar.com\n")
(OUT / ".nojekyll").write_text("")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}/{'' if h == 'index.html' else h}</loc></url>\n" for h, _ in NAV) + "</urlset>\n")
(OUT / "404.html").write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Not found | Amrinder Jakhar</title><link rel="stylesheet" href="/assets/css/style.css"><div class="phead" style="min-height:100vh"><div class="wrap"><h1>Page not found</h1><p><a style="color:#8fc06b" href="/">Back to home</a></p></div></div>')
print("built", sorted(p.name for p in OUT.glob("*")))
