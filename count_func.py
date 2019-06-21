from datetime import datetime as d

class D:
    ''' the date count class '''
    def __init__(self, label, d_input):
        self.label = label.upper()
        self.d_input = d_input
        self.dist = cal_dist(d_input)
        self.dist_months = cal_months(self.dist.days)
        self.date_formated = d_format(self.d_input)
        self.day_of_week = day_of_week(self.d_input)
    
    
    def display(self):
        ''' Displays the distance between two dates '''
        print(f'{self.label:} {self.date_formated} {self.day_of_week}')
        print(f'- {self.dist_months} months')
        print(f'- {self.dist.days} days')
        print()

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
    if d.now().month >= key_value.month and d.now().day >= key_value.day:
        return d(d.now().year + 1, key_value.month, key_value.day)
    else:
        return d(d.now().year, key_value.month, key_value.day )

def t_format(x):
    ''' returns double digit format for minute and hour values if needed '''
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

def day_of_week(x):
    ''' converts weekday() digit to human readable weekday '''
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday' ,3: 'Thursday' ,4: 'Friday',5: 'Saturday' ,6: 'Sunday'}
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
        mondays = []
        for i in range(1, 15):
            if d(x+1, 10, i).weekday() == 0:
                mondays.append(i)
        if d(x+1, 10, mondays[1]) >= d.now():
            return d(x+1, 10, mondays[1])

def labour_day(x=d.now().year):
    ''' first monday of september '''
    mondays = []
    for i in range(1, 8):
        if d(x, 9, i).weekday() == 0:
            mondays.append(i)
    if d(x, 9, mondays[0]) >= d.now():
        return d(x, 9, mondays[0])
    else:
        mondays = []
        for i in range(1, 8):
            if d(x+1, 9, i).weekday() == 0:
                mondays.append(i)
        if d(x+1, 9, mondays[0]) >= d.now():
            return d(x+1, 9, mondays[0])

def victoria_day(x=d.now().year):
    ''' monday between the 18th and 24th of may inclusive '''
    mondays = []
    for i in range(18, 25):
        if d(x, 5, i).weekday() == 0:
            mondays.append(i)
    if d(x, 5, mondays[0]) >= d.now():
        return d(x, 5, mondays[0])
    else:
        mondays = []
        for i in range(18, 25):
            if d(x+1, 5, i).weekday() == 0:
                mondays.append(i)
        if d(x+1, 5, mondays[0]) >= d.now():
            return d(x+1, 5, mondays[0])

def mothers_day(x=d.now().year):
    ''' second sunday of may '''
    sundays = []
    for i in range(1, 15):
        if d(x, 5, i).weekday() == 6:
            sundays.append(i)
    if d(x, 5, sundays[1]) >= d.now():
        return d(x, 5, sundays[1])
    else:
        sundays = []
        for i in range(1, 15):
            if d(x+1, 5, i).weekday() == 6:
                sundays.append(i)
        if d(x+1, 5, sundays[1]) >= d.now():
            return d(x+1, 5, sundays[1])

def fathers_day(x=d.now().year):
    ''' third sunday in june '''
    sundays = []
    for i in range(1, 22):
        if d(x, 6, i).weekday() == 6:
            sundays.append(i)
    if d(x, 6, sundays[2]) >= d.now():
        return d(x, 6, sundays[2])
    else:
        sundays = []
        for i in range(1, 22):
            if d(x+1, 6, i).weekday() == 6:
                sundays.append(i)
        if d(x+1, 6, sundays[2]) >= d.now():
            return d(x+1, 6, sundays[2])
