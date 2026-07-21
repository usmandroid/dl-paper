#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage:"
    echo "$0 <username>"
    exit 1
fi


USER="$1"

BASE="$HOME/dl-paper/users/$USER"

LATEST=$(find "$BASE/incoming" \
    -type f \
    -name "*.pdf" \
    -printf "%T@ %p\n" \
    | sort -n \
    | tail -1 \
    | cut -d' ' -f2-)


if [ -z "$LATEST" ]; then
    echo "No PDFs found"
    exit 1
fi


TITLE=$(basename "$LATEST" .pdf)

TARGET="$BASE/papers/$TITLE"

mkdir -p "$TARGET"

mv "$LATEST" "$TARGET/paper.pdf"


echo "Moved:"
echo "$LATEST"
echo "to:"
echo "$TARGET"


echo "BibTeX placeholder:"
echo "$TARGET/paper.bib"

