#!/usr/bin/env bash
set -euo pipefail

BASE="$HOME/dl-paper"

if [ $# -lt 1 ]; then
    echo "Usage: $0 <google-scholar-profile-url>"
    exit 1
fi

PROFILE="$1"

mkdir -p "$BASE"

source "$BASE/lib/scholar.sh"
source "$BASE/lib/download.sh"

USERNAME=$(extract_username "$PROFILE")

USERDIR="$BASE/users/$USERNAME"

mkdir -p \
    "$USERDIR/incoming" \
    "$USERDIR/papers" \
    "$USERDIR/bib" \
    "$USERDIR/manual" \
    "$USERDIR/logs"

echo "Scholar user: $USERNAME"

fetch_papers "$PROFILE" "$USERDIR"

echo
echo "Done."
echo "Manual downloads, if any, are in:"
echo "$USERDIR/manual"

