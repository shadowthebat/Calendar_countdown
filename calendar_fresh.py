from calendar_class import *
import os
import sys


sched = Schedule()

if len(sys.argv) == 2 and sys.argv[1] == 'head':
    # prints head (5) of calendar
    os.system('clear')
    sched.head()

elif len(sys.argv) == 2 and sys.argv[1] == 'tail':
    # prints tail (5) of calendar
    os.system('clear')
    sched.tail()

else:
    # prints calendar in chronological order
    os.system('clear') # will show up as JHJ in atom, no fuss
    os.system('clear')
    sched.display()
