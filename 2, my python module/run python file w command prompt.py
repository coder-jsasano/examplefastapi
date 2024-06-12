#send email
import smtplib

sender = "junpei.sasano0416@gmail.com"
receiver = "junexsamurai@gmail.com"
password = "Jsasano0416"
subject = "Python email test"
body = "This is a test. If it works I'm in bliss:)"

#header
message = f"""From: Jquan Sasano{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in")
    server.sendmail(sender,receiver,message)
    print("Email has been sent properly!")

except:
    print("Unable to sign in :(")