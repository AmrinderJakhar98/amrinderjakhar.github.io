# amrinderjakhar.com

Personal academic website of Amrinder Jakhar, served by GitHub Pages at https://amrinderjakhar.com.

Plain static HTML/CSS/JS, no framework. Page text lives in `build.py`; edit it and run `python3 build.py .` to regenerate the HTML pages.

## Adding a paper

1. Open `publications.csv` on GitHub and click the pencil icon (Edit).
2. Add a new line at the bottom. The DOI alone is enough, followed by commas for the empty columns, for example:
   `10.1016/j.fcr.2027.109000,journal,,,,,nitrogen; remote sensing,`
3. Click **Commit changes**. In about a minute the "Rebuild site" action fills in the title, authors, journal and year from Crossref and updates the Publications page.

Columns: `doi, type, year, title, authors, journal, topics, note`.
`type` is `journal`, `review` (submitted or under review), `proc` (proceedings) or `ext` (extension); blank means journal.
`topics` drives the filter buttons: `nitrogen; remote sensing; machine learning; soil and water; decision tools`.
For a paper without a DOI, fill in the title, authors, journal and year yourself. When a submitted paper is published, add its DOI and change `type` to `journal`.
