connLabeledFile = open("/home/gopal/Desktop/srpantivirus/IoT-23-Dataset-IndividualScenarios-CTU-IoT-Malware-Capture-9-1/conn.log.labeled")
outputData = open("/home/gopal/Desktop/srpantivirus/IoT-23-Dataset-IndividualScenarios-CTU-IoT-Malware-Capture-9-1/packetType", "w+")

for i in range(8):
    connLabeledFile.readline()

while True:
    line = connLabeledFile.readline()
    #print(f'Line {line}')
    if not line: break
    lineList = line.split()
    #print(lineList,len(lineList))
    if len(lineList)!=23: break
    outputData.write(lineList[21]+"\n")

connLabeledFile.close()
outputData.close()