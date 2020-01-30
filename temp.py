'''import pandas as pd
final = pd.read_csv("C:\\Users\\vignesh\\Desktop\\try.csv", index_col="Roll")
final['hi'] = "Ab"
final.set_value(3115,'newc','Present')
#final.to_csv("C:\\Users\\vignesh\\Desktop\\try.csv", index=False)
#final["Id"] = pd.to_numeric(final["Id"])
#final['Id'] = final['Id'].astype(int)
print(final.columns)
final.to_csv("C:\\Users\\vignesh\\Desktop\\try.csv")
print(final.head())
print(final.loc[3115])'''

import pandas as pd
from periodattendance import period
'''import datetime as dt
print(dt.datetime.now().hour)
print(type(dt.time(21,36)))
clock = dt.time(dt.datetime.now().hour, dt.datetime.now().minute)
if clock > dt.time(21,55) and clock <= dt.time(22,20):
    print("yes")
else:
    print("No")'''

'''mail = pd.read_csv("C:\\Users\\vignesh\\Desktop\\mail.csv", index_col="Sub")

receiver = "{}".format(mail.loc[period])
print(period)
print(receiver)
print(type(mail.at[period,"MailId"]))
#print(timetable.head())'''
import datetime as dt
from periodattendance import period
import periodattendance
print("{}_{}".format(period,dt.datetime.now().strftime("%H:%M")))
print(str(periodattendance.clock))