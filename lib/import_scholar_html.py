#!/usr/bin/env python3

import sys
import json
from bs4 import BeautifulSoup
from pathlib import Path


html_file = sys.argv[1]

html = Path(html_file).read_text(
    encoding="utf-8"
)

soup = BeautifulSoup(
    html,
    "lxml"
)


papers = []

for row in soup.select(".gsc_a_tr"):

    title = row.select_one(".gsc_a_at")

    if not title:
        continue

    paper = {
        "title": title.text.strip(),
        "url": title.get("href")
    }


    year = row.select_one(".gsc_a_y")

    if year:
        paper["year"] = year.text.strip()


    papers.append(paper)


print(
    json.dumps(
        papers,
        indent=2
    )
)

