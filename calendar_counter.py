from fresh_calendar import *
from count_key import *
import os
import sys


sched = Schedule()

if len(sys.argv) == 2 and sys.argv[1] == 'head':
    # prints head (5) of calendar
    sched.head()

elif len(sys.argv) == 2 and sys.argv[1] == 'tail':
    # prints tail (5) of calendar
    sched.tail()

else:
    # prints calendar in chronological order
    sched.display()
