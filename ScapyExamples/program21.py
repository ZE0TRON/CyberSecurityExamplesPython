from scapy.all import *
from scapy.layers.dns import DNS
def capturedPacket(packet):
    if packet.haslayer(DNS) and packet.getLayer(DNS).qr == 0: #qr = 0 -> Request qr = 1 ->Reply
        print("Packet : ",packet.summary().split("/")[3])
while True:
    sniff(iface="eth0",filter="udp port 53",prn=capturedPacket)
