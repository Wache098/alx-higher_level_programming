#!/bin/bash
# Script that makes a request to cause the server to respond with "You got me!"

# Send a POST request to the server with specific headers
curl -sX PUT -d "user_id=98" 0.0.0.0:5000/catch_me -L

