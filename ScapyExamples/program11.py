from scapy.all import *
ipPacket = IP()
icmpPacket = ICMP() #pinge benzer acik veya kapalı olduğunu belirler sistemin
targetIP= input("Target IP: ")
ipPacket.dst = targetIP
sourceIP = input("Source IP: ")
ipPacket.src = sourceIP

ipPacket.show()
icmpPacket.show()
send(ipPacket/icmpPacket)  #ICMP paketleri gitmek için bir IP headera ihtiyac duyar
