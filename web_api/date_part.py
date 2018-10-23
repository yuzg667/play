#coding:utf8

import datetime

def date_part(date='2017-03-01'):
    global year,month,day
    year=date[0:4]
    month_first=int(date[5:6])
    month = date[6:7]
    if month_first ==0:
        month = date[6:7]
    else :
        month = date[5:7]

    day=date[8:10]
    
    year = int(year)
    month = int(month)
    day = int(day)
    
    d = datetime.date(year,month,day)
    return d

# ִ�з���    
# d1 = date_part(date='2015-08-14')
# d2 = date_part(date='2014-09-05')
# (d2-d1).days