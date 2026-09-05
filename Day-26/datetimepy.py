'''
from datetime import date,time,datetime,timedelta
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())
'''

'''
from datetime import date,time,datetime,timedelta

t =time(23,6,5)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
'''
'''
from datetime import date,time,datetime,timedelta
n = datetime.now()
print(n)
print(n.strftime('%d-%m-%y'))
print(n.strftime('%d-%m-%Y %H:%M:%S'))
print(n.strftime('%d-%m-%Y %H:%M:%S %p'))
print(n.strftime('%d %b %Y %H:%M:%S %p'))
print(n.strfftime('%d %B %Y %H:%M:%S %p'))
print(n.strfftime('%a %d %B %Y %H:%M:%S %p'))
print(n.strfftime('%A %d %B %Y %H:%M:%S %p'))
'''

from datetime import date,time,datetime,timedelta

t = date.today()
n = datetime.now()
t7 = t + timedelta(days=7)
t5 = t - timedelta(days=7)
n15 = n + timedelta(minutes=15)
print(t,t7,t5)
print(n,n15)snipp




