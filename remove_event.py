import os
from datetime import datetime as d
import re
import sys


def remove_string(cur_str, x, y):
    """ Removes substring from index x to index y """
    return cur_str[:x] + cur_str[y:]

def remove_event(label):
    """ Removes datetime key and label from key.py """
    with open('key.py', 'r') as f:
        key_file = f.read()

    # remove datetime object from key.py>## EXTRA
    to_rm_dt = re.search(label, key_file)
    key_file = remove_string(key_file, to_rm_dt.span()[0]-1, to_rm_dt.span()[1]+17)

    # remove key from key.py>key_plus
    to_rm_key = re.search(label, key_file)
    key_file = remove_string(key_file, to_rm_key.span()[0], to_rm_key.span()[1]+2)

    # remove label from key.py>label_plus
    to_remove_label = re.search(label, key_file)
    key_file = remove_string(key_file, to_remove_label.span()[0]-1, to_remove_label.span()[1]+3)

    with open('key.py', 'w') as f:
        # Overwrites key.py with update
        f.write(key_file)
    return
