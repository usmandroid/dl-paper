#!/usr/bin/env python3

import json
import sys
import requests
from pathlib import Path

import unicodedata

def clean_filename(name):

    name = unicodedata.normalize(
        "NFKD",
        name
    )

    name = name.replace(
        "\\012",
        " "
    )

    return "".join(
        c for c in name
        if c.isalnum()
        or c in " .-_"
    )



INPUT = sys.argv[1]
OUTDIR = Path(sys.argv[2])


OUTDIR.mkdir(
    parents=True,
    exist_ok=True
)


with open(INPUT) as f:
    papers = json.load(f)


session = requests.Session()


for idx, paper in enumerate(papers):

    title = paper["title"]

    print("\n", title)

    safe = clean_filename(title).replace(" ", "_")

    pdfs = paper.get(
        "pdf_urls",
        []
    )


    for pdf in pdfs:

        print("Downloading:", pdf)

        try:
            r = session.get(
                pdf,
                timeout=30
            )

            if (
                r.status_code == 200
                and (
                    r.content.startswith(b"%PDF")
                    or "pdf" in r.headers.get("content-type", "").lower()
                )
            ):

                outfile = (
                    OUTDIR /
                    f"{safe}.pdf"
                )

                outfile.write_bytes(
                    r.content
                )

                print(
                    "Saved:",
                    outfile
                )

        except Exception as e:
            print(
                "FAILED",
                e
            )


