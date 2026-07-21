#!/usr/bin/env bash

fetch_papers()
{
    local PROFILE="$1"
    local USERDIR="$2"

    echo "Fetching scholar page..."

    HTML=$(curl -Ls "$PROFILE")

    echo "$HTML" \
    | grep -oE 'https?://[^"]+\.pdf' \
    | sort -u \
    > "$USERDIR/logs/pdf-links.txt"


    while read -r URL
    do
        NAME=$(basename "$URL" | tr '?' '_')

        echo "Trying $URL"

        if curl \
            -L \
            --fail \
            -o "$USERDIR/incoming/$NAME" \
            "$URL"
        then
            echo "Downloaded $NAME"

        else
            echo "$URL" \
            >> "$USERDIR/manual/needs-download.url"

            echo "Manual download required:"
            echo "$URL"
        fi

    done < "$USERDIR/logs/pdf-links.txt"
}
