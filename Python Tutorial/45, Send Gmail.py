#Send gmail with smtplib

import smtplib

sender = "ender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email with Python"

#header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587) #default port number = 587
server.starttls()

try:
    server.login(sender,password)
    print("Logged in!")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print('Unable to sign in')



