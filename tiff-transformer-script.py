#SCRIPT QUE DIVIDE EN DIFERENTES PAGINAS ARCHIVOS DE IMAGÉN TIFF y los sube a un servvidor

import os
import datetime
import copy
import shutil
import paramiko
from PIL import Image

today_upload =datetime.date.today()
format_today = today_upload.strftime('%Y%m%d')

path= ''

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files (path):
    print(file)

file_tiff_processed = copy.copy(file)

img = Image.open(path+file)

x = 1
for i in range(100):
     try:
         img.seek(i)
         img.save(path+'ESC01_01_'+format_today+'_'+str(x+i).zfill(5)+'.tif')
     except EOFError:
         break

img.close()
shutil.move(path + file_tiff_processed, path + 'PROCESADO')

host = ""
port = 22
username = ""
password = ""

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
sftp = ssh.open_sftp()

pathremote = "/"

for file in os.listdir(path):
    if file.endswith(".tif"):
        print(file)
        localpath = path+file
        print(localpath)
        sftp.put(localpath, os.path.join(pathremote, file))

sftp.close()
ssh.close()

for file in os.listdir(path):
    if file.endswith(".tif"):
        os.remove(path+file)









