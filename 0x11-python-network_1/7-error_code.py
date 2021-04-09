#!/usr/bin/python3
"""Script that takes in a URL :
   - sends a request to the URL
   - displays the body of the response"""


import requests
from sys import argv
from requests.exceptions import HTTPError

try:
    r = requests.get(argv[1])
    # https://docs.python-requests.org/en/master/user/quickstart/#response-status-codes
    r.raise_for_status()
    print(r.text)
except HTTPError as http_error:
    print('Error code: {}'.format(r.status_code))
