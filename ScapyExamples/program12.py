from scapy.all import *
import random
random.seed()
numberOfPackets= int(input("Paket sayısını giriniz"))
targetIP= input("Target Ip yi giriniz : ")
for i in range(numberOfPackets):
    ipPacket = IP()
    icmpPacket = ICMP() #pinge benzer acik veya kapalı olduğunu belirler sistemin
    ipPacket.dst = targetIP
    srcIP=str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))
    print("SrcIP : ",srcIP)
    ipPacket.src =srcIP
    ipPacket.show()
    icmpPacket.show()
    send(ipPacket/icmpPacket)  #ICMP paketleri gitmek için bir IP headera ihtiyac duyar
    time.sleep(2)
    print(P)
