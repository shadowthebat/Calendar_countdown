from count_func import *
from count_key import *
import os


# defning date variables
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

kbd = D('kaya', kbd)
master[kbd.dist.days] = kbd

mbd = D('mommy', mbd)
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

stpat = D('st patricks day', stpat)
master[stpat.dist.days] = stpat

# prints countdowns in chronological order
for i in sorted(master.keys(), reverse=True):
    master[i].display()
