from count_func import *
from count_key import *
import os


# defning date variables
ny = upcomming(ny)
bday = upcomming(born)
canada = upcomming(can)


os.system('clear')

# creating the countdowns and displaying the results
bday = D('birthday', bday)
bday.display()

ny = D('new years', ny)
ny.display()

canada = D('canada day', can)
canada.display()
