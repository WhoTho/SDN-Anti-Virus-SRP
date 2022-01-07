filePath = lambda name:"/home/gopal/Desktop/srpantivirus/CTU-1-log-output/"+name

connFile = open(filePath("conn.log"))
sslFile = open(filePath("ssl.log"))
x509File = open(filePath("x509.log"))
outputData = open(filePath("allPacketInfo"), "w+")


x509InfoDict = {"-":[0,0]}
for line in x509File.readlines()[8:-1]:
    lineList = line.split("\t")
    if lineList[14]!="-":
        domainCount = lineList[14].count(",")+1
    else:
        domainCount = 0
    x509InfoDict[lineList[1]]=[domainCount,int(lineList[11])]
#print(x509InfoDict)


certificateDict = {}
#certLengthsList = []
for line in sslFile.readlines()[8:-1]:
    lineList = line.split("\t")
    certList = lineList[15].split(",")
    if certList[0]!="-":
        certPathLength = len(certList)
    else:
        certPathLength = 0
    certificateDict[lineList[1]]=[certPathLength,*x509InfoDict[certList[0]]]
#print(certificateDict)


for i in range(8):
    connFile.readline()

while True:
    line = connFile.readline()
    if not line: break
    lineList = line.split()
    #print(lineList)
    if len(lineList)!=21: break
    if lineList[10]=="-" or lineList[9]=="-":
        ratio = "0"
    else:
        div = int(lineList[9]) + int(lineList[10])
        if div != 0:
            ratio = str(round(int(lineList[10]) / (int(lineList[9]) + int(lineList[10])),5))
        else:
            ratio = "0"
    
    if lineList[1] in certificateDict:
        certData = certificateDict[lineList[1]]
    else:
        certData = [0,0,0]

    if lineList[9]=="-": lineList[9]="0"
    if lineList[10]=="-": lineList[10]="0"
    
    dataList = [lineList[8],lineList[9],lineList[10],ratio,lineList[16],lineList[18],*map(str,certData)]
    outputData.write("\t".join(dataList)+"\n")

# Setup:
# 0             1                       2                               3                   4                       5                   6                               7                       8
# Duration      Size of flows orig      total size of flows resp        ratio of sizes      outbound packets        inbound packets     length of certificate path      certificate length      number of domains in certificate