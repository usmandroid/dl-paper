#!/usr/bin/env python3

import json
import sys
import requests
from bs4 import BeautifulSoup


INPUT = sys.argv[1]
OUTPUT = sys.argv[2]


with open(INPUT) as f:
    papers = json.load(f)


session = requests.Session()

headers = {
    "User-Agent":
    "Mozilla/5.0"
}


for paper in papers:

    print("Processing:", paper["title"])

    try:
        html = session.get(
            paper["url"],
            headers=headers,
            timeout=10
        ).text

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        links = []

        for a in soup.find_all("a"):
            href = a.get("href", "")

            if href.startswith("http"):
                links.append(href)


        pdfs = [
            x for x in links
            if ".pdf" in x.lower()
        ]

        paper["pdf_urls"] = pdfs


        bib_links = [
            x for x in links
            if "scholar.bib" in x
        ]

        paper["bibtex_urls"] = bib_links


    except Exception as e:

        paper["error"] = str(e)


with open(
    OUTPUT,
    "w"
) as f:
    json.dump(
        papers,
        f,
        indent=2
    )


