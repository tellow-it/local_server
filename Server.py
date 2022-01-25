import socket
from random import randint
import os
from dotenv import load_dotenv, find_dotenv
from Mail_Smtp import send_mail_admin, send_mail_client

load_dotenv(find_dotenv())
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
IMAP_HOST = os.getenv('IMAP_HOST')
IMAP_PORT = os.getenv('IMAP_PORT')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
PERIOD_CHECK = os.getenv('PERIOD_CHECK')


s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(2)
c, adr = s.accept()
print("Socket Up and running with a connection from", adr)
while True:
    mail = c.recv(1024).decode()
    print("C:", mail)
    sendData = "Incorrect input:"
    ok = 'OK'
    if "@gmail.com" in mail:
        c.send(ok.encode())
        print("S:" + ok)
        break
    else:
        c.send(sendData.encode())
        print("S:" + sendData)
message = c.recv(1024).decode()
print("C:", message)
ID = randint(1, 10000)
print(ID)

# setup the parameters of the message


send_mail_admin(EMAIL_PASSWORD, EMAIL_LOGIN, EMAIL_LOGIN, ID, message)
send_mail_client(EMAIL_PASSWORD, mail, mail, ID)
c.close()

d = socket.socket()
port1 = 20000
d.bind(('', port1))
d.listen(2)
k, addr = d.accept()
print("Socket Up and running with a connection from", addr)
k.send(str(ID).encode())
print(str(ID))
k.close()
