import subprocess
#subprocess.Popen(["ls","-l"])
#subprocess.Popen(["ls -a"],shell=True)
firefox_Proc = subprocess.Popen(["ps -A | grep firefox | cut -c -6"],stdout=subprocess.PIPE,shell=True)
(out,err) = firefox_Proc.communicate()
if out.decode() != "":
    print("Firefox PID : ",out.decode())
else:
    print("No Firefox Running")
