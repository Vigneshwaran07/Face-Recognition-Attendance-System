import yagmail
import os
from periodattendance import period
from periodattendance import period_num
import pandas as pd

mail = pd.read_csv("C:\\Users\\vignesh\\Desktop\\mail.csv", index_col="Sub")

receiver = mail.at[period,"MailId"]  # receiver email address
body = "Attendence File"  # email body
filename = "C:\\Users\\vignesh\\Desktop\\Result.csv"  # attach the file

# mail information
yag = yagmail.SMTP("vikyclan1@gmail.com", "vignesh473")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
print("Mail Sent to "+ mail.at[period,"MailId"] )
