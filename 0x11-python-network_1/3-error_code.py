#!/usr/bin/python3
"""Script that takes in a URL :
    - sends a request to the URL,
    - and displays the body of the response, decoded in utf-8"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    # https://docs.python.org/3/howto/urllib2.html#httperror
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
