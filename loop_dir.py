

import paramiko
import os
from stat import S_ISDIR, S_ISREG
import sys


def listdir_rec(sftp, remotedir):
    for entry in sftp.listdir_attr(remotedir):
        remotepath = remotedir + "/" + entry.filename
        mode = entry.st_mode
        if S_ISDIR(mode):
            listdir_rec(sftp, remotepath)
        elif S_ISREG(mode):
            print(remotepath)

host_ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
dir_path = sys.argv[4]

ssh = paramiko.SSHClient()
# Load SSH host keys.
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