#!/usr/bin/env python3

import json
import requests
import sys
from pathlib import Path


INPUT = sys.argv[1]
OUTDIR = Path(sys.argv[2])


OUTDIR.mkdir(
    parents=True,
    exist_ok=True
)


papers = json.loads(
    Path(INPUT).read_text()
)


for paper in papers:

    url = paper.get(
        "bibtex_url"
    )

    if not url:
        continue


    title = (
        paper["title"]
        .replace("/", "_")
        .replace(" ", "_")
    )


    print(
        "Bib:",
        title
    )


    r = requests.get(
        url,
        timeout=20
    )


    if "@article" in r.text or "@inproceedings" in r.text:

        outfile = (
            OUTDIR /
            f"{title}.bib"
        )

        outfile.write_text(
            r.text
        )

        print(
            "saved",
            outfile
        )


