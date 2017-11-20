# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open("deneme.txt","r") as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of '
msg['From'] = "cmpbilge@gmail.com"
msg['To'] = "cmpbilge@gmail.com"
# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user,pwd)
s.send_message(user,to,msg.as_string())
s.close()
