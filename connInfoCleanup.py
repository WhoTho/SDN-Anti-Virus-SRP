connFile = open("/home/gopal/Desktop/srpantivirus/IoT-23-Dataset-IndividualScenarios-CTU-IoT-Malware-Capture-9-1/conn.log")
outputData = open("/home/gopal/Desktop/srpantivirus/IoT-23-Dataset-IndividualScenarios-CTU-IoT-Malware-Capture-9-1/connPacketInfo", "w+")

for i in range(8):
    connFile.readline()

while True:
    line = connFile.readline()
    if not line: break
    lineList = line.split()
    #print(lineList)
    if len(lineList)!=21: break
    if lineList[10]=="-" or lineList[9]=="-":
        ratio = "-"
    else:
        div = int(lineList[9]) + int(lineList[10])
        if div != 0:
            ratio = str(round(int(lineList[10]) / (int(lineList[9]) + int(lineList[10])),5))
        else:
            ratio = "0"

    dataList = [lineList[8],lineList[9],lineList[10],ratio,lineList[16],lineList[18]]
    outputData.write("\t".join(dataList)+"\n")

connFile.close()
outputData.close()