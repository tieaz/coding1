#!/bin/bash

find . -maxdepth 1 -name "*.py" | while read -r file; do
    echo ""
    echo "------------------------------------------"
    echo "Running: $file"
    echo "------------------------------------------"
    python3 "$file"
done
