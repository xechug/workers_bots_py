#lectura de datos de intercambio imerr y rcerr comprobando la etiqueta error para identificar problema en los envios de información a diferentes servidores

import os
import smtplib
import shutil
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from xml.etree import ElementTree

list_file = []
list_error = []
for file in os.listdir(r"Output"):
    #time.sleep(30)
    if file.endswith(".imerr") or file.endswith(".rcerr") or file.endswith(".sherr"):
        list_file.append(file)

# with open("file.txt", "w") as output:
# output.write(str(list_file))

for file in list_file:
    with open ('Output/'+file, 'rt', encoding='utf-8') as f:
        tree = ElementTree.parse(f)

    for node in tree.iter('Error'):
        print(node.text)


list_file = []
exit()


