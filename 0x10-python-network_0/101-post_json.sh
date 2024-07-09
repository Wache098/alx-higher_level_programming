#!/bin/bash
# Script that sends a JSON POST request to a URL and displays the body of the response

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

url=$1
json_file=$2

# Validate if the JSON file is valid
if ! jq '.' "$json_file" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with JSON content
response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$url")

# Display the body of the response
echo "$response"
