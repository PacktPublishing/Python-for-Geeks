import paramiko

ip='172.16.2.50'
port=22
username='root'
password='rootroot'


cmd= 'show ip interface brief \n'

def main():

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password)

        stdin, stdout, stderr = ssh.exec_command(cmd)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        print(resp)

    finally:
        ssh.close()

if __name__ == '__main__':
    main()
