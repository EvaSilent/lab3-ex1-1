import smtplib

fromname = 'Simantha Hong'
fromaddr = 'simorah@gmail.com'
toname = 'Hong Simantha'
toaddr = 'daughta_girl14@hotmail.com'
subject = 'Hi'
msg = 'Hey, how are youuu?'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'simorah@gmail.com'
password = 'tymzdnhqzdmcuatz'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()