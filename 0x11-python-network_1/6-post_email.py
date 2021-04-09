#!/usr/bin/python3
"""Script that takes in a URL and an email address,
   - sends a POST request to the passed URL with the email as a parameter,
   - and finally displays the body of the response"""

import requests
from sys import argv


if __name__ == "__main__":
    # https://docs.python-requests.org/en/master/user/quickstart/#more-complicated-post-requests
    r = requests.post(argv[1], {'email': argv[2]})
    print(r.text)
