import nmap

portScan = nmap.PortScanner()
targetIP= input("Enter Target IP Range : ")
targetPort= input("Enter Target Port : ")
portScan.scan(targetIP,targetPORT)
for host in portScan.all_hosts():
    print("Host : ",hosts)
    print("Port : ",portScan[hosts].all_tcp())
