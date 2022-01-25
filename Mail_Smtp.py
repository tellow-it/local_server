# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

EMAIL_LOGIN = 'python.test.myserver@gmail.com'
EMAIL_PASSWORD = 'Van2345Tikhonov'
IMAP_HOST = 'imap.gmail.com'
IMAP_PORT = 993
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
PERIOD_CHECK = 60


def send_mail_admin(ps, fr, to, sb, ms):
    # create message object instance
    msg = MIMEMultipart()
    message = ms
    # setup the parameters of the message
    password = ps
    msg['From'] = fr
    msg['To'] = to
    msg['Subject'] = str(sb)
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP(SMTP_HOST)
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg['To']))


def send_mail_client(ps, fr, to, sb):
    # create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = ps
    msg['From'] = fr
    msg['To'] = to
    msg['Subject'] = str(sb)
    # create server
    server = smtplib.SMTP(SMTP_HOST)
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg['To']))
