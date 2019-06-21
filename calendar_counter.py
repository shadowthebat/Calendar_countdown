from datetime import datetime as d
from count_key import *
import os

class D:
    ''' the date count class '''
    def __init__(self, label, d1):
        self.label = label
        self.d1 = d1
        self.dist = None
    

    def display_distance(self):
        ''' Calculates distance between two dates and prints results '''
        if self.d1 > d.now():
            self.dist = self.d1 - d.now()
        else:
            self.dist = d.now() - self.d1
    
        print(f'{self.label.upper():} {t_format(self.d1.day)}-{t_format(self.d1.month)}-{self.d1.year}')
        print(f'- {round(self.dist.days/30, 1)} months')
        print(f'- {self.dist.days} days')
        print()

def year_finder(key_value):
    ''' Returns date with appropriate year '''
    if d.now().month >= key_value.month and d.now().day >= key_value.day:
        return d(d.now().year + 1, key_value.month, key_value.day)
    else:
        return d(d.now().year, key_value.month, key_value.day )

def t_format(x):
    ''' returns double didgit format for minute and hour values if needed '''
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

# defning date variables
ny = d((d.now().year + 1), 1, 1)
bday = year_finder(born)
canada = year_finder(can)


os.system('clear')
master = []
# creating the countdowns and displaying the results
bday = D('birthday', bday)
bday = bday.display_distance
master.append(bday)

ny = D('new years', ny)
ny = ny.display_distance
master.append(ny)

canada = D('canada day', can)
canada = canada.display_distance
master.append(canada)



for i in master:
    i()