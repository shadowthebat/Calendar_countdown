from datetime import datetime as d
from count_key import *
import os

class D:
    ''' the date count class '''
    def __init__(self, label, d_input):
        self.label = label.upper()
        self.d_input = d_input
        self.dist = cal_dist(d_input)
        self.dist_months = cal_months(self.dist.days)
        self.date_formated = d_format(self.d_input)
    

    def display_distance(self):
        ''' Calculates distance between two dates and prints results '''
        print(f'{self.label:} {self.date_formated}')
        print(f'- {self.dist_months} months')
        print(f'- {self.dist.days} days')
        print()

def d_format(x):
    return f'{t_format(x.day)}-{t_format(x.month)}-{x.year}'

def cal_months(x):
    return round(x/30, 1)

def cal_dist(x):
    ''' Calculates distance between two dates '''
    if x > d.now():
        return x - d.now()
    else:
        return d.now() - x

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

# creating the countdowns and displaying the results
bday = D('birthday', bday)
bday.display_distance()

ny = D('new years', ny)
ny.display_distance()

canada = D('canada day', can)
canada.display_distance()

