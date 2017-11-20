from scapy.all import *
import random
arpPacket = ARP()
sourceIP = "192.168.43.205"
arpPacket.pdst = sourceIP
arpPacket.op="who-has"
uns,ans =sr(arpPacket)
print(uns)
print(ans)
#arpPacket.show()
#ARP REPLAY la arp tablosunu doldurup cihazıları internetten düşürebiliri
