#script asociado a un daemon en linux que puede comprobar cada x tiempo conexiones a FTP, y en caso de errores, enviar un correo notificando el error y el problema

#! /usr/bin/env python
import ftplib
from time import asctime
import time
import smtplib
import string


FROM = ""
HOST = ""
emails = ["", ""]
passwd = ""


def ftp_test():
    try:
        server = ftplib.FTP()
        server.connect('', 21)
        server.login('', '')
        # You don't have to print this, because this command itself prints dir contents

        print(server.dir())
        time.sleep(30)
        print(server.getwelcome())
    except Exception as e:
        print(e)
        send_error(e)


def send_error(e):
    test_type = 'FTP'
    service_name = 'CONNECT'
    server_url = ''

    subject = 'Error Connect SFTP: %s: %s %s ( %s ) ' % (
        service_name, asctime(), test_type.upper(), server_url)
    message = 'Not Connect SFTP %s \r\n Service: %s  \r\n Type Error: %s \r\n Server : %s ' % (
        service_name, test_type.upper(), e, server_url)

    TO = ', '.join(emails)
    BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % subject,
        "",
        message
    ), "\r\n")
    server = smtplib.SMTP(HOST)
    server.starttls()
    server.login(FROM, passwd)
    server.sendmail(FROM, emails, BODY)
    server.quit()


ftp_test()