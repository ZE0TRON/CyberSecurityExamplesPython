import zipfile
passfile=open("pass.txt","r")
password=0
myzip = zipfile.ZipFile("Zipli.zip")

for pasw in passfile.readlines():
    try:
        zipfile.ZipFile.open(myzip,mode="r",pwd=pasw)
        print(pasw)
    except:
        pass

print(password)
