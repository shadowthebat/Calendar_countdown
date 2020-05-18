from calendar_class import *
import os
import sys
from add_event import *
from remove_event import *
from key import labels_plus


if len(sys.argv) == 2 and sys.argv[1] == 'head':
    # prints head (5) of calendar
    sched = Schedule()
    os.system('clear')
    sched.head()

elif len(sys.argv) == 2 and sys.argv[1] == 'tail':
    # prints tail (5) of calendar
    sched = Schedule()
    os.system('clear')
    sched.tail()

elif len(sys.argv) == 2 and sys.argv[1] == 'len':
    # prints length of Schedule
    sched = Schedule()
    print(sched.len())

elif len(sys.argv) == 5 and sys.argv[1] == '-a':
    # add event to calendar with given date
    add_event_by_date(sys.argv[2], sys.argv[3], sys.argv[4])
    print(f'Event added: {sys.argv[2]}')

elif len(sys.argv) == 4 and sys.argv[1] == '-t':
    # add event to calendar x_num days away
    add_event_by_dist_days(sys.argv[2], sys.argv[3])
    print(f'Event added: {sys.argv[2]}')

elif len(sys.argv) == 3 and sys.argv[1] == '-r':
    # removes event from calendar
    if sys.argv[2] in labels_plus:
        remove_event(sys.argv[2])
        print(f'Event removed: {sys.argv[2]}')
    else:
        print(f'Event cannot be removed: {sys.argv[2]}')

else:
    # prints full calendar in chronological order
    sched = Schedule()
    os.system('clear')
    os.system('clear')
    sched.display()
    # print(f'total: {sched.len()}')
