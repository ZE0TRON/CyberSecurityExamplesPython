import socket
targetIP = input("Target IP: ")
portSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
start = int(input("Baslangic Portunu Giriniz : "))
end = int(input("Bitis Portunu Giriniz : "))
for i in range(start,end+1):
    try:
        print("Trying "+str(i)+"now")
        conn = portSocket.connect((targetIP,i))
        print("Port "+str(i)+" is OPEN!")
    except:
        pass
socket.close()
