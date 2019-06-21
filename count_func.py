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
