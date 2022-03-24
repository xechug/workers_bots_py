#script que se encarga de mover archivos pdf y clasificarlos en diferentes entornos de red

import shutil
import paramiko, os
from stat import S_ISDIR

host = ""
port = 22
transport = paramiko.Transport((host, port))
username = ""
password = ""

transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)


def sftp_walk(remotepath):
    path = remotepath
    files = []
    folders = []
    for f in sftp.listdir_attr(remotepath):
        if S_ISDIR(f.st_mode):
            pass
        else:
            files.append(f.filename)
    if files:
        yield path, files
    for folder in folders:
        new_path = os.path.join(remotepath, folder)
        for x in sftp_walk(new_path):
            yield x


for path, files in sftp_walk('/path/'):
    for file in files:
        sftp.get(path + '/' + file,
                 os.path.join(r'\\path', file))

for path, files in sftp_walk('/path/'):
    for file in files:
        sftp.rename(path + '/' + file, path + '//' + file)

for file in os.listdir(r''):
    if file.endswith(".pdf"):
        shutil.move(r'' + file, r'')


