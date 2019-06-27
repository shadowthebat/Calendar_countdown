from count_func import *
from count_key import *
import os
import sys

# define date variables with correct year if needed
ny = upcomming(ny)
bday = upcomming(born)
canada = upcomming(can)
kbd = upcomming(kbd)
mbd = upcomming(mbd)
stj = upcomming(stj)
hallow = upcomming(hallow)
remember = upcomming(remember)
xmas = upcomming(xmas)
valen = upcomming(valen)
stpat = upcomming(stpat)
nana = upcomming(nana)
andy = upcomming(andy)

#jewish holidays
hanu = holidays.hanukkah(d.now().year)
hanu = d(hanu[0], hanu[1], hanu[2])
hanu = upcomming(hanu)

purim = holidays.purim(d.now().year)
purim = d(purim[0], purim[1], purim[2])
purim = upcomming(purim)

rosh_hashanah = holidays.rosh_hashanah(d.now().year)
rosh_hashanah = d(rosh_hashanah[0], rosh_hashanah[1], rosh_hashanah[2])
rosh_hashanah = upcomming(rosh_hashanah)

yom_kippur = holidays.yom_kippur(d.now().year)
yom_kippur = d(yom_kippur[0], yom_kippur[1], yom_kippur[2])
yom_kippur = upcomming(yom_kippur)

passover = holidays.passover(d.now().year)
passover = d(passover[0], passover[1], passover[2])
passover = upcomming(passover)

shavuot = holidays.shavuot(d.now().year)
shavuot = d(shavuot[0], shavuot[1], shavuot[2])
shavuot = upcomming(shavuot)

sukkot = holidays.sukkot(d.now().year)
sukkot = d(sukkot[0], sukkot[1], sukkot[2])
sukkot = upcomming(sukkot)

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

labour = D('labour day', labour_day())
master[labour.dist.days] = labour

thanks = D('thanks giving', thanks_giving())
master[thanks.dist.days] = thanks
''' sukkot and thanks fall on same day, must solve '''
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

victoria = D('vitoria day', victoria_day())
master[victoria.dist.days] = victoria

nana = D('nanas bday', nana)
master[nana.dist.days] = nana

andy = D('andys bday', andy)
master[andy.dist.days] = andy

mothers = D('mothers day', mothers_day())
master[mothers.dist.days] = mothers

fathers = D('fathers day', fathers_day())
master[fathers.dist.days] = fathers

#jewish holidays
hanu = D('hanukkah', hanu)
master[hanu.dist.days] = hanu

purim = D('purim', purim)
master[purim.dist.days] = purim

rosh_hashanah = D('rosh hashanah', rosh_hashanah)
master[rosh_hashanah.dist.days] = rosh_hashanah

yom_kippur = D('yom kippur', yom_kippur)
master[yom_kippur.dist.days] = yom_kippur

passover = D('passover', passover)
master[passover.dist.days] = passover

shavuot = D('shavuot', shavuot)
master[shavuot.dist.days] = shavuot

sukkot = D('sukkot', sukkot)
master[sukkot.dist.days] = sukkot



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

