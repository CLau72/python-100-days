from cmath import e
import email
import smtplib

my_email = "carselau72@yahoo.com"
password = ""

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:

        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="calau@ra.rockwell.com", msg="Sup, nerd?")


