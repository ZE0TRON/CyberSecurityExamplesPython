import paramiko
import getpass
ServerIP = input("Enter Server IP: ")
username = input("Username: ")
password = getpass.getpass("Password")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ServerIP,username=username,password=password)
while True:
    session = client.get_transport().open_session()
    command = input("Command : ")
    if(command == "exit"):
        break
    session.exec_command(command)
    print("Server : ",session.recv(1024))
