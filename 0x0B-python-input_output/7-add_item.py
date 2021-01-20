#!/usr/bin/python3
"""Adds all arguments to a Python list, then saves them to a file"""


import json
from sys import argv
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
new_list = []
i = 1

if (len(argv) > 1):
    while i < len(argv):
        new_list.append(argv[i])

save_to_json_file(new_list, file_name)
