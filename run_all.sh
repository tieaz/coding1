#!/bin/bash

shopt -s nullglob

for file in *.py; do
    echo ""
    echo "------------------------------------------"
    echo "Running: $file"
    echo "------------------------------------------"
    python3 "$file"
done
