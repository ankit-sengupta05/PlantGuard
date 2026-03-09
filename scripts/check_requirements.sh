#!/usr/bin/env bash
# scripts/check_requirements.sh
FILE=requirements.txt
if [[ -f """" ]]; then
    # Basic check: no empty lines
    if grep -q '^[[:space:]]*$' """"; then
        echo 'Error: requirements.txt has empty lines'
        exit 1
    fi
fi
