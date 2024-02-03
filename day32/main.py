import smtplib

def send_mail():
    global quote
    my_email = "markandey3213@gmail.com"
    password = "ckam oxgi tmjz iwoz"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        message = f"Subject: Monday Motivation!! \n\n{quote}!!"
        connection.sendmail(
            from_addr=my_email,
            to_addrs="markandey321523@yahoo.com",
            msg=message
        )

import datetime as dt
import random
quote=""
now = dt.datetime.now()
day = now.weekday()
if day == 4:
    with open("quotes_all.txt") as data_file:
        data = data_file.readlines()
        quote = random.choice(data)
        send_mail()

