from convertdate import holidays
from odd_dates import *

# Define Datetime objects
bday = d(d.now().year, 8, 7)
kbd = d(d.now().year, 5, 9)
mbd = d(d.now().year, 11, 26)
canada = d(d.now().year, 7, 1)
ny = d(d.now().year, 1, 1)
stj = d(d.now().year, 6, 24)
hallow = d(d.now().year, 10, 31)
remember = d(d.now().year, 11, 11)
xmas = d(d.now().year, 12, 25)
valen = d(d.now().year, 2, 14)
stpat = d(d.now().year, 3, 17)
nana = d(d.now().year, 9, 17)
andy = d(d.now().year, 6, 1)

fathers_day = fathers_day()
mothers_day = mothers_day()
victoria_day = victoria_day()
labour_day = labour_day()
thanks_giving = thanks_giving()


# Jewish holidays
hanu = holidays.hanukkah(d.now().year) # extract from convertdate
hanu = d(hanu[0], hanu[1], hanu[2]) # convert to datetime object

purim = holidays.purim(d.now().year)
purim = d(purim[0], purim[1], purim[2])

rosh_hashanah = holidays.rosh_hashanah(d.now().year)
rosh_hashanah = d(rosh_hashanah[0], rosh_hashanah[1], rosh_hashanah[2])

yom_kippur = holidays.yom_kippur(d.now().year)
yom_kippur = d(yom_kippur[0], yom_kippur[1], yom_kippur[2])

passover = holidays.passover(d.now().year)
passover = d(passover[0], passover[1], passover[2])

shavuot = holidays.shavuot(d.now().year)
shavuot = d(shavuot[0], shavuot[1], shavuot[2])

sukkot = holidays.sukkot(d.now().year)
sukkot = d(sukkot[0], sukkot[1], sukkot[2])

key = [bday, kbd, mbd, canada, ny, stj, hallow, remember, xmas, valen, stpat, nana, andy, fathers_day, mothers_day, victoria_day, labour_day, thanks_giving, hanu, purim, rosh_hashanah, yom_kippur, passover, shavuot, sukkot]

labels = ['birthday', 'kaya\'s bday',
'mom\'s bday','canada day','new years',
'st. jean', 'halloween','rememberance day','christmas',
'valentines','st patricks day','nana\'s bday',
'andy\'s bday', 'father\'s day', 'mother\'s day', 'victoria day', 'labour day', 'thanks giving', 'hannuka','purim','rosh hashana','yom kipur','passover', 'shavuot', 'sukkot']
