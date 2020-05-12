from datetime import datetime as d


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

def upcomming(key_value):
    ''' Returns date with appropriate year '''
    if key_value <= d.now():
        return d(d.now().year + 1, key_value.month, key_value.day)
    else:
        return key_value

m = mothers_day()
print(m)

print(upcomming(m))
