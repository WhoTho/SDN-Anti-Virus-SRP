folderPath = lambda folder: f"/home/gopal/Desktop/srpantivirus/CTU-13-Dataset/{folder}/maliciousInfo"

outputFile = open("/home/gopal/Desktop/srpantivirus/masterMalicousInfo", "w+")

folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "13"]

for folder in folders:
    infoFile = open(folderPath(folder))
    while True:
        line = infoFile.readline()
        if not line: break

        outputFile.write(line)

print("done")
