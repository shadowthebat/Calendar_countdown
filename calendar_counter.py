from count_func import *
from count_key import *
import os
import sys

# defining date variables from datetime objects
ny = upcomming(ny)
bday = upcomming(born)
canada = upcomming(can)
kbd = upcomming(kbd)
mbd = upcomming(mbd)
stj = upcomming(stj)
labour = upcomming(labour)
thanks = upcomming(thanks)
hallow = upcomming(hallow)
remember = upcomming(remember)
xmas = upcomming(xmas)
valen = upcomming(valen)
stpat = upcomming(stpat)


os.system('clear')
os.system('clear')
master = {}

# create and add countdowns to master dictionary
bday = D('birthday', bday)
master[bday.dist.days] = bday

ny = D('new years', ny)
master[ny.dist.days] = ny

canada = D('canada day', can)
master[canada.dist.days] = canada

kbd = D('kaya\'s bday', kbd)
master[kbd.dist.days] = kbd

mbd = D('mom\'s bday', mbd)
master[mbd.dist.days] = mbd

stj = D('st. jean', stj)
master[stj.dist.days] = stj
'''
labour = D('labour day', labour)
master[labour.dist.days] = labour

thanks = D('thanks giving', thanks)
master[thanks.dist.days] = thanks
'''
hallow = D('halloween', hallow)
master[hallow.dist.days] = hallow

remember = D('rememberance day', remember)
master[remember.dist.days] = remember

xmas = D('christmas', xmas)
master[xmas.dist.days] = xmas

valen = D('valentines day', valen)
master[valen.dist.days] = valen

stpat = D('st patricks day', stpat)
master[stpat.dist.days] = stpat

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
    # prints countdowns in chronological order
    for i in sorted(master.keys(), reverse=True):
        master[i].display()
