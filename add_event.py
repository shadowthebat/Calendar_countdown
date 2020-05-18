import os
from datetime import datetime as d
import re
import sys
from datetime import timedelta as td

def insert_string(cur_str, add_str, pos):
    """ Insert substring into string at index"""
    beginning = cur_str[:pos]
    added = add_str
    end = cur_str[pos:]
    return f'{beginning}{added}{end}'

def add_event_by_date(title, day, month):
    """ Updates key.py with added date info """
    with open('key.py', 'r') as f:
        key_file = f.read()

    add_date_object = f"{title} = d({d.now().year}, {month}, {day})\n"
    key_title = f'{title}, '
    label_title = f'\'{title}\', '

    # update additional datetimes
    a = re.search(r'EXTRA', key_file)
    key_file = insert_string(key_file, add_date_object, a.span()[1]+1)

    # update list: key
    k = re.search(r'key_plus', key_file)
    key_file = insert_string(key_file, key_title, k.span()[1]+4)

    # update list: labels
    l = re.search(r'labels_plus', key_file)
    key_file = insert_string(key_file, label_title, l.span()[1]+4)

    with open('key.py', 'w') as f:
        # Overwrites key.py with update
        f.write(key_file)
    return


def add_event_by_dist_days(title, dist_days):
    """ Updates key.py with added date info """
    with open('key.py', 'r') as f:
        key_file = f.read()

    dt_object = d.now() + td(days = int(dist_days))
    add_date_object = f"{title} = d({dt_object.year}, {dt_object.month}, {dt_object.day})\n"
    key_title = f'{title}, '
    label_title = f'\'{title}\', '

    # update additional datetimes
    a = re.search(r'EXTRA', key_file)
    key_file = insert_string(key_file, add_date_object, a.span()[1]+1)

    # update list: key
    k = re.search(r'key_plus', key_file)
    key_file = insert_string(key_file, key_title, k.span()[1]+4)

    # update list: labels
    l = re.search(r'labels_plus', key_file)
    key_file = insert_string(key_file, label_title, l.span()[1]+4)

    with open('key.py', 'w') as f:
        # Overwrites key.py with update
        f.write(key_file)
    return
