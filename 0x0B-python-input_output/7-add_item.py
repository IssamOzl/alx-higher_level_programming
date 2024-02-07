#!/usr/bin/python3
""" 7-add_item module """
from sys import argv
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = load_from_json_file(filename)

for index in argv[1:]:
    json_list.append(index)
save_to_json_file(json_list, filename)
