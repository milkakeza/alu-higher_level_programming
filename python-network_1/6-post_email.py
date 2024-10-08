#!/usr/bin/python3
"""A script that:
takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header ofthe response."""

import sys
import requests

if __name__ == "__main__":

    new_value = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], new_value)
    print(req.text)
