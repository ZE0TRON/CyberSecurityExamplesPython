from scapy.all import *
import random
arpPacket = ARP()
for i in range(0,255):
    for j in range(0,255):
        sourceIP = "192.168."+str(i)+"."+str(j)
        arpPacket.pdst = sourceIP
        arpPacket.op="who-has"
        p=sr1(arpPacket)
        #arpPacket.show()
    #ARP REPLAY la arp tablosunu doldurup cihazıları internetten düşürebiliri
