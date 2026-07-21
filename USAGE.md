
```bash
cd ~/dl-paper

source .venv/bin/activate

```

Let's test with Ilya Sutskever's Profile `https://scholar.google.com/citations?user=x04W_mMAAAAJ&hl=en&oi=ao`
 

Ilya Sutskever
Co-Founder and Chief Scientist at Safe Superintelligence Inc
Verified email at ssi.inc - Homepage

 
```bash
./dlpaper-fetch.sh \
"https://scholar.google.com/citations?user=x04W_mMAAAAJ&hl=en&oi=ao"

# manually download missing PDFs

cp ~/Downloads/*.pdf \
users/x04W_mMAAAAJ/incoming/

./dlpaper-process.sh x04W_mMAAAAJ

```


use offline .html file of google scholar page
```
python lib/import_scholar_html.py \
import/x04W_mMAAAAJ.html \
> users/x04W_mMAAAAJ/logs/publications.json

```
Downloads a formatted json file containing title year and scholar link to articles
```
python lib/enrich_publications.py \
users/x04W_mMAAAAJ/logs/publications.json \
users/x04W_mMAAAAJ/logs/enriched.json

```

Download pdf's from the PDF file URL's
```
python lib/download_bib.py \
users/x04W_mMAAAAJ/logs/enriched.json \
users/x04W_mMAAAAJ/bib
```

organize incoming PDF's

```
python lib/organize_papers.py \
users/x04W_mMAAAAJ
```
Process Papers
```
python lib/process_papers.py \
users/x04W_mMAAAAJ
```
