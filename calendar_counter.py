from count_func import *
from count_key import *
import os


# defning date variables
ny = upcomming(ny)
bday = upcomming(born)
canada = upcomming(can)


os.system('clear')
master = {}
# create and add countdowns to master dictionary
bday = D('birthday', bday)
master[bday.dist.days] = bday

ny = D('new years', ny)
master[ny.dist.days] = ny

canada = D('canada day', can)
master[canada.dist.days] = canada

# prints countdowns from soonest to latest
for i in sorted(master.keys()):
    master[i].display()
