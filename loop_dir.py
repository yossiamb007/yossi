

import paramiko
import os
from stat import S_ISDIR, S_ISREG
import sys
from pathlib import Path

def listdir_rec(sftp, remotedir):
    if OS_type == "mac":
       file_sep="/"
    elif OS_type == "win":
        file_sep="\\"
    for entry in sftp.listdir_attr(remotedir):
        remotepath = remotedir + file_sep + entry.filename
        mode = entry.st_mode
        if S_ISDIR(mode):
            listdir_rec(sftp, remotepath)
        elif S_ISREG(mode):
            print(remotepath)
file_sep=""
OS_type = sys.argv[1]
host_ip = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
dir_path = sys.argv[5]

ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
ssh.connect(host_ip,
            username=username,
            password=password,
            look_for_keys=False)

sftp_client = ssh.open_sftp()

listdir_rec(sftp_client,dir_path)
ssh.close();