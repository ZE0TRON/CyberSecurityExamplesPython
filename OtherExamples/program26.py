import requests
import subprocess
while 1:
    subprocess.check_output("""sudo tcpdump -c 1 -i en0 >>deneme.txt""",shell = True)
    IP=subprocess.check_output("sudo cat deneme.txt|grep IP|cut -d -f3|cut -d -f1,2,3,4")
    sonuc = requests.get('wget https://www.usom.gov.tr/url-list.txt',verify=False)
    if(str(IP1) in str(sonuc)):
        print("Zararli bir yere gidip geliyorsun")
