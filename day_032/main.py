import datetime as dt
import smtplib
import random

# Open the quotes file and select a random quote
def select_quote():
    with open("quotes.txt", mode="r") as f:
        quotes =f.readlines()
        
    return random.choice(quotes)

# Read current date time and check if it's Monday
current_dt = dt.datetime.now()
if current_dt.weekday() == 0:
    my_email = ""
    password = ""
    qotd = select_quote()

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject: Your Monday Inspiration\n\n{qotd}"
        )
