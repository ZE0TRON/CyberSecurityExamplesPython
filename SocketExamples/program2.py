#program2
import socket
mySocket = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)
mySocket.connect(("www.google.com",80))
mySocket.send("GET / HTTP/1.1")
data=mySocket.recv(2048) #recieve data with given buffer size
mySocket.close()
print(data.decode())
