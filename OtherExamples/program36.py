import smtplib
from bluetooth import *
import bluetooth
devList = bluetooth.discover_devices()

def findDevs():
    foundDevs = bluetooth.discover_devices(lookup_names=True)
    for (addr,name) in foundDevs:
