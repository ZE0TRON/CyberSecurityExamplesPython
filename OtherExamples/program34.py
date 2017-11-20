import re #regexp101.com gir alıştırma yap
text="simgeozger.com.tr"

if re.match("simge",text):
    print("FOUND !")
else:
    print("HOT FOUND!")
