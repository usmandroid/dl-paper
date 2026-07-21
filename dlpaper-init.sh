#!/usr/bin/env bash
set -euo pipefail

sudo apt install curl wget poppler-utils python3 python3-pip -y

PROJECT="$HOME/dl-paper"

mkdir -p "$PROJECT"
cd "$PROJECT"

echo "Creating Python virtual environment..."

python3 -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip

cat > requirements.txt <<EOF
scholarly
bibtexparser
pypdf
requests
beautifulsoup4
lxml
crossrefapi
EOF

pip install -r requirements.txt


mkdir -p \
    lib \
    users


touch README.md


chmod +x \
    dlpaper-*.sh \
    lib/*.sh


echo
echo "Initialized:"
echo "$PROJECT"
echo
echo "Activate environment:"
echo "source $PROJECT/.venv/bin/activate"
