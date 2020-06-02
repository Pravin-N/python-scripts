from datetime import timedelta, date
import os, glob
from pathlib import Path

def daterange(startdate, enddate):
    for n in range(int((enddate - startdate).days)):
        yield startdate + timedelta(n)

startdate = date(2018, 1, 1)
enddate = date(2018, 4, 1)

p = Path(r'C:\Users\ACE\Desktop\Python\datesfiles')

for singledate in daterange(startdate, enddate):
    file1 = open(f'{p}\{singledate.strftime("%m-%d-%Y")}.txt', 'w')
    file1.close()
    print(f'{p}\{singledate.strftime("%m-%d-%Y")}.txt', 'w')