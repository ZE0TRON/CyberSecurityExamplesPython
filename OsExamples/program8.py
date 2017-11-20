import os
import time
print("getpid(): ",os.getpid())
print("getlogin(): ",os.getlogin())
print("uname(): ",os.uname())
print("getcwd(): ",os.getcwd())
print("MyFolder exists : ",os.path.exists("MyFolder"))
print("program6.py exists : ",os.path.isfile("program6.py"))
print("Os Sep : ",os.sep)
print("Name : ",os.name)
print("Directory : ",os.listdir())

userHome = os.path.expanduser("~")
desktop = userHome + os.sep +"Desktop"
print("Desktop Path : ",desktop)

for files in enumerate(os.listdir(desktop)):
    if files[1].endswith("png"):
        print(files)

for files in os.listdir(desktop):
    if files.endswith("png"):
        print(files)

os.mkdir("hacktrickconf2017")
time.sleep(5)
os.rename("hacktrickconf2017", "pythonforhackers")
time.sleep(5)
os.rmdir("pythonforhackers")
