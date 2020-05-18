from calendar_class import *
import os
import sys
from add_event import *
from remove_event import *


sched = Schedule()

if len(sys.argv) == 2 and sys.argv[1] == 'head':
    # prints head (5) of calendar
    os.system('clear')
    sched.head()

elif len(sys.argv) == 2 and sys.argv[1] == 'tail':
    # prints tail (5) of calendar
    os.system('clear')
    sched.tail()

elif len(sys.argv) == 2 and sys.argv[1] == 'len':
    # prints length of Schedule
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
    # add event to calendar x_num days away
    remove_event(sys.argv[2])
    print(f'Event removed: {sys.argv[2]}')

else:
    # prints calendar in chronological order
    os.system('clear') # will show up as JHJ in atom, no fuss
    os.system('clear')
    sched.display()
    # print(f'total: {sched.len()}')

''' REMOVE FUNCTION BUGS

elif len(sys.argv) == 3 and sys.argv[1] == '-r':
    # add event to calendar x_num days away
    remove_event(sys.argv[2])
    print(f'Event removed: {sys.argv[2]}')

'''
