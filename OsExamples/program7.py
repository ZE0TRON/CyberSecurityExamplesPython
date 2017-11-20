import _thread
import time

def oddNumber(number):
    while True:
        time.sleep(2)
        print(number)
        number+=2

def evenNumber(number):
    while True:
        time.sleep(1)
        print(number)
        number+=2

_thread.start_new_thread(oddNumber, (1,))
_thread.start_new_thread(evenNumber, (0,))

while 1:
    time.sleep(1)
    print("Python for Hackers")
