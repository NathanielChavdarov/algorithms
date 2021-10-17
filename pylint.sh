#!/usr/bin/env bash

# Run pylint, collect output as json
pylint --exit-zero --persistent=no --format json algorithms/ >.pylint.json

jqcmd='[.[]|select(.type==$x)]|length'
fatals="$(jq --arg x fatal "$jqcmd" .pylint.json)"
errors="$(jq --arg x error "$jqcmd" .pylint.json)"
warnings="$(jq --arg x warning "$jqcmd" .pylint.json)"
refactors="$(jq --arg x refactor "$jqcmd" .pylint.json)"
conventions="$(jq --arg x convention "$jqcmd" .pylint.json)"
usages="$(jq --arg x usage "$jqcmd" .pylint.json)"

max_fatal=0
max_error=0
max_warning=0
max_refactor=0
max_convention=20
max_usage=0

if [[ "$fatals" -gt "$max_fatal" -o "$fatals" -gt "$max_fatal" -o "$errors" -gt "$max_error" -o "$warnings" -gt "$max_warning" -o "$refactor" -gt "$max_refactor" -o "$conventions" -gt "$max_convention" ]] then
    pylint --exit-zero --persistent=no algorithms/
    echo
    echo "Fatal: $fatals (max $max_fatal)"
    echo "Error: $errors (max $max_error)"
    echo "Warning: $warnings (max $max_warning)"
    echo "Refactor: $refactors (max $max_refactor)"
    echo "Convention: $conventions (max $max_convention)"
    echo "Usage: $usages (max $max_usage)"
    exit 1
fi