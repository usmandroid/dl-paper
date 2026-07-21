#!/usr/bin/env bash

extract_username()
{
    local url="$1"

    echo "$url" \
    | sed -n 's/.*user=\([^&]*\).*/\1/p'
}

