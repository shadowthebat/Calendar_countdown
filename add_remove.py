import os
from datetime import datetime as d
import re
import sys
from datetime import timedelta as td

def insert_string(cur_str, add_str, pos):
    beginning = cur_str[:pos]
    added = add_str
    end = cur_str[pos:]
    return f'{beginning}{added}{end}'

def remove_string(cur_str, x, y):
    return cur_str[:x] + cur_str[y:]

def rm_dt(cur_str, x, y):
    new_string = remove_string(cur_str, x-1, y+25)
    return new_string

def rm_key(cur_str, x, y):
    new_string = remove_string(cur_str, x, y+2)
    return new_string

def rm_label(cur_str, x, y):
    new_string = remove_string(cur_str, x-1 , y+3)
    return new_string


def add_event_by_date(title, day, month):
    """ temp_description """

    with open('key.py', 'r') as f:
        key_file = f.read()

    add_date_object = f"{title} = d(d.now().year, {month}, {day})\n"
    key_title = f'{title}, '
    label_title = f'\'{title}\', '

    # update additional datetimes
    a = re.search(r'EXTRA', key_file)
    key_file = insert_string(key_file, add_date_object, a.span()[1]+1)

    # update list: key
    k = re.search(r'key', key_file)
    key_file = insert_string(key_file, key_title, k.span()[1]+4)

    # update list: labels
    l = re.search(r'labels', key_file)
    key_file = insert_string(key_file, label_title, l.span()[1]+4)

    with open('key.py', 'w') as f:
        f.write(key_file)
    return


def add_event_by_dist_days(title, dist_days):
    """ tmp desc """
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
    k = re.search(r'key', key_file)
    key_file = insert_string(key_file, key_title, k.span()[1]+4)

    # update list: labels
    l = re.search(r'labels', key_file)
    key_file = insert_string(key_file, label_title, l.span()[1]+4)

    with open('key.py', 'w') as f:
        f.write(key_file)
    return


def remove_event(label):
    """ tmp desc """
    with open('key.py', 'r') as f:
        key_file = f.read()
    r = key_file

    # remove datetime object
    to_remove_dt = re.search(label, key_file)
    key_file = rm_dt(key_file, to_remove_dt.span()[0], to_remove_dt.span()[1])

    to_rm_key = re.search(label, key_file)
    key_file = rm_key(key_file, to_rm_key.span()[0], to_rm_key.span()[1])

    to_remove_label = re.search(label, key_file)
    key_file = rm_label(key_file, to_remove_label.span()[0], to_remove_label.span()[1])

    with open('key.py', 'w') as f:
        f.write(key_file)
    return


'''

goal: add dates from terminal.
ex:
    call -a {label} {d} {m}
    call -t {label} {num_days}


goal: remove dates from terminal
ex:
    call -r {label}

'''
