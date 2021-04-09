#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


import requests
from sys import argv

if __name__ == "__main__":
    # https://docs.python-requests.org/en/master/user/quickstart/#json-response-content
    if len(argv) == 1:
        q = ""  # if no argument is given
    else:
        q = argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        data = r.json()
        if data:
            # if the response body is properly JSON formatted and not empty
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")  # if the JSON is empty
    except:
        print("Not a valid JSON")  # if the JSON is invalid
