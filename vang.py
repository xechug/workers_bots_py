#SCRIPT DE DETECCION DE PROCESOS OCULTOS EN LOS SERVIDORES PARA DETECTAR ROOTKIT Y OTROS PROBLEMAS DE CIBERSEGURIDAD, CON AVISO AL USUARIO

import wmi #modulo que detecta procesos ocultos y muestra la informacion de subprocessos
from time import asctime
import smtplib
import string
import socket
import time



hostname = str(socket.gethostname())
time_now = str(asctime())

#alert_firewall = subprocess.check_call('netsh advfirewall show allprofiles')

f = wmi.WMI()
alert_process = []
remitente = ""
HOST = ""
destinatario = [""]
passwd = ""


for process in f.Win32_Process():
    alert_process.append(process.Name)

def send_alert_python():
    subject = 'Alerta de procesos monitorizados en el servidor ' + hostname + ' ' + time_now
    message = 'Proceso python.exe detectado, revisar posible incidencia de ciberseguridad en el servidor ' + hostname + ' ' + time_now
    email = 'Subject: {}\n\n{}'.format(subject, message)
    server = smtplib.SMTP(HOST)
    server.starttls()
    server.login(remitente, passwd)
    server.sendmail(remitente, destinatario, email)
    server.quit()

def send_alert_winget():
    subject = 'Alerta de procesos monitorizados en el servidor ' + hostname + ' ' + time_now
    message = 'Proceso python3.exe detectado, revisar posible incidencia de ciberseguridad en el servidor ' + hostname + ' ' + time_now
    email = 'Subject: {}\n\n{}'.format(subject, message)
    server = smtplib.SMTP(HOST)
    server.starttls()
    server.login(remitente, passwd)
    server.sendmail(remitente, destinatario, email)
    server.quit()


#print(alert_process)

if 'python.exe' in alert_process:
    send_alert_python()

if 'winget.exe' in alert_process:
    send_alert_winget()

