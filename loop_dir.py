

import paramiko
from stat import S_ISDIR, S_ISREG


def listdir_r(sftp, remotedir):
    for entry in sftp.listdir_attr(remotedir):
        remotepath = remotedir + "/" + entry.filename
        mode = entry.st_mode
        if S_ISDIR(mode):
            listdir_r(sftp, remotepath)
        elif S_ISREG(mode):
            print(remotepath)


router_ip = "192.168.1.177"
router_username = "yossiambalo"
router_password = "1123"

ssh = paramiko.SSHClient()

# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
ssh.connect(router_ip,
            username=router_username,
            password=router_password,
            look_for_keys=False )

sftp_client = ssh.open_sftp()

listdir_r(sftp_client,"Documents")