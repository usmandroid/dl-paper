#!/usr/bin/env python3

import json
import shutil
import sys
import re
from pathlib import Path


BASE = Path(sys.argv[1])

INCOMING = BASE / "incoming"
PAPERS = BASE / "papers"
BIB = BASE / "bib"
LOGS = BASE / "logs"


PAPERS.mkdir(
    exist_ok=True
)


def slugify(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9]+",
        "-",
        text
    )

    return text.strip("-")


with open(
    LOGS / "enriched.json"
) as f:

    publications = json.load(f)



for pdf in INCOMING.glob("*.pdf"):

    print("\nProcessing:")
    print(pdf.name)


    matched = None
    best_score = 0

    filename = pdf.stem.lower()


    for paper in publications:

        title = paper["title"].lower()

        words = [
            w for w in re.findall(r"[a-z0-9]+", title)
            if len(w) > 4
        ]

        matches = sum(
            w in filename
            for w in words
        )

        score = matches / max(len(words), 1)


        if score > best_score:
            best_score = score
            matched = paper


    # reject weak matches
    if best_score < 0.4:
        matched = None
        


    if matched:

        folder_name = slugify(
            matched["title"]
        )

    else:

        folder_name = slugify(
            pdf.stem
        )


    target = PAPERS / folder_name


    target.mkdir(
        exist_ok=True
    )


    shutil.move(
        pdf,
        target / pdf.name
    )


    metadata = {
        "title": matched["title"]
        if matched else pdf.stem,

        "year": matched.get("year")
        if matched else None,

        "pdf_file":
        pdf.name
    }


    with open(
        target / "metadata.json",
        "w"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=2,
            ensure_ascii=False
        )


    print(
        "Created:",
        target
    )


