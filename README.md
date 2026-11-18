# amrinderjakhar.com

Personal academic website of Amrinder Jakhar, served by GitHub Pages at https://amrinderjakhar.com.

Plain static HTML/CSS/JS, no framework. Page text lives in `build.py`. Do not edit the `.html` files by hand: they are regenerated from `build.py` and `publications.csv`.

## Adding a paper

1. Open `publications.csv` on GitHub and click the pencil icon (Edit).
2. Add a new line at the bottom. The DOI alone is enough, followed by commas for the empty columns, for example:
   `10.1016/j.fcr.2027.109000,journal,,,,,nitrogen; remote sensing,`
3. Click **Commit changes**. In about a minute the "Rebuild site" action fills in the title, authors, journal and year from Crossref and updates the Publications page. If the action shows a red X under the **Actions** tab, the DOI was not found: check it, or fill in the details yourself.

Columns: `doi, type, year, title, authors, journal, topics, note`.
`type` is `journal`, `review` (submitted or under review), `proc` (proceedings) or `ext` (extension); blank means journal.
`topics` drives the filter buttons: `nitrogen; remote sensing; machine learning; soil and water; decision tools`.
For a paper without a DOI, fill in the title, authors, journal and year yourself. When a submitted paper is published, add its DOI and change `type` to `journal`.

## Editing text on a page

1. On GitHub open `build.py` and click the pencil icon. Use Ctrl+F to find the sentence you want to change.
2. Change only the words. Leave the quote marks and the `<p>`, `</p>`, `<a ...>` pieces as they are.
3. Click **Commit changes**. In about a minute the "Rebuild site" action regenerates the pages. A green check under the **Actions** tab means it is live (hard refresh if you still see the old text). A red X means something is wrong: open the run and read the red line.

## Previewing on your own computer

1. Download or clone the repository. Python 3.10 or newer is needed.
2. In a terminal, go into the folder and run `python3 build.py .` (this rewrites the `.html` files).
3. Run `python3 -m http.server 8000` and open http://localhost:8000. Press Ctrl+C to stop.

## Adding or replacing the CV PDF

Upload the public CV as `assets/Amrinder_Jakhar_CV.pdf`. The "Download full CV (PDF)" button on the CV page appears after the rebuild. Do not upload a version with a phone number or references.

## Photos

Field photos live in `assets/img/` as small WebP files (the homepage background is `field-plots-900.webp` and `field-plots-1600.webp`). Keep new photos under about 150 KB each so the site stays fast.

## When you graduate

Search `build.py` for `UPDATE AT GRADUATION`: the comment lists the places that say "Ph.D. candidate".
