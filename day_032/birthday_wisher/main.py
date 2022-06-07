import datetime as dt
import pandas
import random
import smtplib

# Read in birthdays CSV file
birthdays_df = pandas.read_csv("birthdays.csv")

# Iterate through each row in the CSV file
for index, row in birthdays_df.iterrows():

    #Take the current time and the birthday. If the day and month match, pick a random letter template and read it in.
    current_dt = dt.datetime.now()
    birthday = dt.datetime(year=row.year, month=row.month, day=row.day)
    if current_dt.month == birthday.month:
        if current_dt.day == birthday.day:
            with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as f:
                letter_template = f.read()
            # Replace the [Name] placeholder with the person's name from the CSV 
            final_letter = letter_template.replace("[NAME]", row["name"])
            
            # Send the email
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.ehlo()
                connection.starttls()
                connection.login(user="", password="")
                connection.sendmail(
                    from_addr="",
                    to_addrs=row.email,
                    msg=f"Subject: Happy Birthday!\n\n{final_letter}"
                )

                





