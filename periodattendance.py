import datetime as dt
import pandas as pd
day = dt.datetime.today().strftime("%A")
time = dt.datetime.now().strftime("%H:%M")
#print(day, time)
day = "Sunday"
clock = dt.time(dt.datetime.now().hour, dt.datetime.now().minute)
#clock = dt.time(9,22)
def period_finder():
    #print(clock)
    if clock >= dt.time(8,40) and clock < dt.time(9,30):
        return 1
    elif clock >= dt.time(9,30) and clock < dt.time(10,25):
        return 2
    elif clock >= dt.time(10,25) and clock < dt.time(10,40):
        return "break"
    elif clock >= dt.time(10,40) and clock < dt.time(11,30):
        return 3
    elif clock >= dt.time(11,30) and clock < dt.time(12,20):
        return 4
    elif clock >= dt.time(12,20) and clock < dt.time(13,10):
        return "break"
    elif clock >= dt.time(13,10) and clock < dt.time(14,0):
        return 5
    elif clock >= dt.time(14,0) and clock < dt.time(14,50):
        return 6
    elif clock >= dt.time(14,50) and clock < dt.time(15,0):
        return "break"
    elif clock >= dt.time(15,0) and clock < dt.time(15,50):
        return 7
    elif clock >= dt.time(15,50) and clock <= dt.time(16,20):
        return 8
    else:
        return "break"
#print(period_finder())
timetable = pd.read_csv('C:\\Users\\vignesh\\Desktop\\timetable.csv', index_col='Day')
period_num = period_finder()
if day == "Saturday" or day == "Sunday":
    day = timetable.at[day,str(1)]
if period_num == "break":
    period = "break"
else:
    period = timetable.at[day,str(period_num)]
#print(period)
