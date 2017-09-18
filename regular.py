import re
allfinds = []
str = "we need to inform him with the latest information"
if re.search("inform","we need to inform him with the latest information"):
    allfinds = re.findall("inform","we need to inform him with the latest information")

for i in allfinds:
    print(i)

for i in re.finditer("inform", str):
    print(i)
    loctup = i.span()
    print(loctup)

str = "Sat,hat,mat,pat"
allStr = re.findall("[h-m]at",str)

for i in allStr:
    print(i)

