import re

fh= open("test.txt")
for line in fh:
    if re.search(r"com", line):
        print("\n\n FOUND !!\n")
        print(line.rstrip())

fh.close()
