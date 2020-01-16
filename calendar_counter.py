from fresh_calendar import *
from count_key import *
import os
import sys


sched = Schedule()

if len(sys.argv) == 2 and sys.argv[1] == 'head':
    # prints head (5) of calendar
    head = sorted(master.keys(), reverse=True)
    for i in head[-5:]:
        master[i].display()

elif len(sys.argv) == 2 and sys.argv[1] == 'tail':
    # prints tail (5) of calendar
    tail = sorted(master.keys(), reverse=True)
    for i in tail[:5]:
        master[i].display()

else:
    # prints calendar in chronological order
    for i in sorted(master.keys(), reverse=True):
        master[i].display()

sched = Schedule()
sched.display()
