import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

user_name = 'liamlin5609@gmail.com'
password = 'jqahnfmkkdadkmrk'

receiver = 'liamlin5609@gmail.com'
context = ssl.create_default_context()
message = """\
Subject: I am bad Ryan!!
Hi
My name is Ryan!!!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, receiver, message)
