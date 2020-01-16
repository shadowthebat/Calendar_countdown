from key import *
from convertdate import holidays
import os
import sys

# -- Classes --
class Event:
    def __init__(self, label, datee):
        ''' Individual Event information '''
        self.label = label.upper()
        self.datee = upcomming(datee)
        self.dist = cal_dist(self.datee)
        self.dist_months = cal_months(self.dist.days)
        self.date_formated = d_format(self.datee)
        self.day_of_week = day_of_week(self.datee)

    def display(self):
        ''' Displays the distance between Event dates and current date '''
        print(f'{self.label:} {self.date_formated} {self.day_of_week}')
        print(f'- {self.dist_months} months')
        print(f'- {self.dist.days+1} days')
        print()


class Schedule:
    def __init__(self):
        ''' Full Schedule arranged chronologically '''
        self.master = {}
        for j, k in zip(labels, key):
            e = Event(j, k)
            increment = 0
            while e.dist.days + increment in self.master.keys():
                increment += 0.01
            self.master[e.dist.days + increment] = e

    def display(self):
        ''' prints calendar in chronological order '''
        for i in sorted(self.master.keys(), reverse = True):
            self.master[i].display()

    def head(self):
        ''' prints head (5) of calendar '''
        head = sorted(self.master.keys(), reverse=True)
        for i in head[-5:]:
            self.master[i].display()

    def tail(self):
        ''' prints tail (5) of calendar '''
        tail = sorted(self.master.keys(), reverse=True)
        for i in tail[:5]:
            self.master[i].display()
            
    def len(self):
        return len(self.master)


# -- Functions --
def d_format(x):
    ''' returns date formated dd-mm-yyyy '''
    return f'{t_format(x.day)}-{t_format(x.month)}-{x.year}'

def cal_months(x):
    ''' converts days remaining to months remaining'''
    return round(x/30, 1)

def cal_dist(x):
    ''' Calculates distance between two dates '''
    if x > d.now():
        return x - d.now()
    else:
        return d.now() - x

def upcomming(key_value):
    ''' Returns date with appropriate year '''
    if key_value <= d.now():
        return d(d.now().year + 1, key_value.month, key_value.day)
    else:
        return d(d.now().year, key_value.month, key_value.day)

def t_format(x):
    ''' returns double digit format for minute and hour values if needed '''
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

def day_of_week(x):
    ''' converts weekday() digit to human readable weekday '''
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    return days[x.weekday()]

def thanks_giving(x=d.now().year):
    ''' second monday of october '''
    mondays = []
    for i in range(1, 15):
        if d(x, 10, i).weekday() == 0:
            mondays.append(i)
    if d(x, 10, mondays[1]) >= d.now():
        return d(x, 10, mondays[1])
    else:
        return thanks_giving(x+1)

def labour_day(x=d.now().year):
    ''' first monday of september '''
    mondays = []
    for i in range(1, 8):
        if d(x, 9, i).weekday() == 0:
            mondays.append(i)
    if d(x, 9, mondays[0]) >= d.now():
        return d(x, 9, mondays[0])
    else:
        return labour_day(x+1)

def victoria_day(x=d.now().year):
    ''' monday between the 18th and 24th of may inclusive '''
    mondays = []
    for i in range(18, 25):
        if d(x, 5, i).weekday() == 0:
            mondays.append(i)
    if d(x, 5, mondays[0]) >= d.now():
        return d(x, 5, mondays[0])
    else:
        return victoria_day(x+1)

def mothers_day(x=d.now().year):
    ''' second sunday of may '''
    sundays = []
    for i in range(1, 15):
        if d(x, 5, i).weekday() == 6:
            sundays.append(i)
    if d(x, 5, sundays[1]) >= d.now():
        return d(x, 5, sundays[1])
    else:
        return mothers_day(x+1)

def fathers_day(x=d.now().year):
    ''' third sunday in june '''
    sundays = []
    for i in range(1, 22):
        if d(x, 6, i).weekday() == 6:
            sundays.append(i)
    if d(x, 6, sundays[2]) >= d.now():
        return d(x, 6, sundays[2])
    else:
        return fathers_day(x+1)
