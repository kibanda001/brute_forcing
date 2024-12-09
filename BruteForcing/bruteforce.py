import paramiko
import sys
cmd1 = "ipconfig"
cmd2 = "netstat -an"
list = open(sys.argv[1], "r")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for line in list.readlines():
    username_password = line.strip().split(":")
    try:
        ssh.connect("localhost", username = username_password[0], password = username_password[1])
    except paramiko.AuthenticationException:
        print("[0] username and password")
    else:
        print("[1] The username : %s AND Password : %s" % (username_password[0], username_password[1]))
        stdin, stdout, stderr = ssh.exec_command(cmd2)
        for line in stdout.readlines():
            print(line.strip())
        break
ssh.close()