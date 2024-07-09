#!/bin/bash
# Script that makes a request to cause the server to respond with "You got me!"

# Send a POST request to the server with specific headers and data
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

