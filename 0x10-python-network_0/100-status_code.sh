#!/bin/bash
# Script that sends a request to a URL and displays only the status code of the response

# Send a GET request to the URL provided as the first argument and save the HTTP status code
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "$response"

