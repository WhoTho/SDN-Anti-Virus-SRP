import random

filePath = lambda name:"/home/gopal/Desktop/srpantivirus/packetDatasets/"+name

maliciousInput = open(filePath("malicious"))
benignInput = open(filePath("benign"))

packetInput = open(filePath("mixedPacketInfo"),"w+")
packetOutput = open(filePath("mixedPacketType"),"w+")

# 60705
mal = True
beg = True
while True:
    if not mal and not beg:
        break
    goFor = random.randint(0,1)
    if not beg or (mal and goFor==0):
        line = maliciousInput.readline()
        if not line:
            mal = False
            continue
        t="1"
    else:
        line = benignInput.readline()
        if not line:
            beg = False
            continue
        t="0"
    line=line.rstrip("\n")
    packetInput.write(line+"\n")
    packetOutput.write(t+"\n")
print("done")
