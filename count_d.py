from datetime import datetime as d
from count_key import born
import os

def bday_finder():
    ''' Returns birthdate with appropriate year '''
    if d.now().month >= born.month and d.now().day >= born.day:
        return d(d.now().year + 1, born.month, born.day)
    else:
        return d(d.now().year, born.month, born.day )

def distance(x, y):
    ''' Calculates distance between to dates '''
    if x > y:
        return x - y
    else:
        return y - x

bday = bday_finder()
ny = d((d.now().year + 1), 1, 1)


os.system('clear')
print('BIRTHDAY:')
print(f'- {distance(bday, d.now()).days/30} months')
print(f'- {distance(bday, d.now())}')
print()
print()
print()
print()
print()
print()
print(f'NEW YEARS:\n{distance(ny, d.now())} ({distance(ny, d.now()).days/30} months)')
