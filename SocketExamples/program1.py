#first program
#can i see that
import socket
mySocket = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)
mySocket.bind(("192.169.1.30",8088)) #server socketini ip ye bindla
mySocket.listen(1) # kac tane bağlantı aynı anda kabul edilebilir

while True:
    client, addr = mySocket.accept()
    print(addr[0]," is connected to the server")
    client.send("Server loves you bro")
    client.close()
    
