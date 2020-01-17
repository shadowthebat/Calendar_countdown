from datetime import datetime as d


# -- Odd Date Functions --
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
