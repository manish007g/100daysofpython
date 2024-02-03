##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "markandey3213@gmail.com"
password = "ckam oxgi tmjz iwoz"
now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
bdict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in bdict:
    bday_person = bdict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path)as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=bday_person["email"],
                            msg=f"Subject: Happy birthday !!\n\n{contents}")
# 4. Send the letter generated in step 3 to that person's email address.





