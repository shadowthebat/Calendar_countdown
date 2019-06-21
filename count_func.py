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
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday' ,3: 'Thursday' ,4: 'Friday',5: 'Saturday' ,6: 'Sunday'}
    return days[x.weekday()]

def thanks_giving():
    mondays = []
    for i in range(1,15):
        if d(d.now().year, 10, i).weekday() == 0:
            mondays.append(i)
    if d(d.now().year, 10, mondays[1]) >= d.now():
        return d(d.now().year, 10, mondays[1])
    else:
        return d(d.now().year + 1, 10, mondays[1])

def labour_day():
    mondays = []
    for i in range(1,8):
        if d(d.now().year, 9, i).weekday() == 0:
            mondays.append(i)
    if d(d.now().year, 9, mondays[0]) >= d.now():
        return d(d.now().year, 9, mondays[0])
    else:
        return d(d.now().year + 1, 9, mondays[0])

def victoria_day(x=d.now().year):
    mondays = []
    for i in range(18,25):
        if d(x, 5, i).weekday() == 0:
            mondays.append(i)
    if d(x, 5, mondays[0]) >= d.now():
        return d(x, 5, mondays[0])
    else:
        mondays = []
        for i in range(18,25):
            if d(x+1, 5, i).weekday() == 0:
                mondays.append(i)
        if d(x+1, 5, mondays[0]) >= d.now():
            return d(x+1, 5, mondays[0])
