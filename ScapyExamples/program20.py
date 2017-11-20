def Int2Bin(integer):
    binary = "{0:b}".format(integer)
    return binary

def seperation(IPs,count):
    sep =".".join(Int2Bin(int(IPs.split(".")[x]))for x in range(count))
    return sep

IP = input("Enter an IP adress : ")
Subnet = input("Enter subnet mask : ")

sepip=seperation(IP,4)
sepsub=seperation(Subnet,4)
print(IP,"->",sepip)
print(Subnet, "->",sepsub) #subnetin tersi wildcardi verir network tararken sonunda /subnetteki 1 sayısı kadar
print("Scan operator : ",sepsub.count("1"))
