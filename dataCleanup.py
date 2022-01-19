folders = [*map(str,range(1,19))]

for folder in folders:
    filePath = lambda name: f"/home/gopal/Desktop/srpantivirus/CTU-13-Dataset-Normal/{folder}/" + name
    clean = lambda value: value if value!="-" else "0"

    connFile = open(filePath("conn.log"))

    certFilesExist = True
    try:
        sslFile = open(filePath("ssl.log"))
        x509File = open(filePath("x509.log"))
    except:
        certFilesExist = False

    outputData = open(filePath("benignInfo"), "w+")

    x509InfoDict = {"-":["0","0"]}
    certificateDict = {}

    if certFilesExist:
        for line in x509File.readlines()[8:-1]:
            lineList = line.split("\t")

            fingerprint = lineList[1]
            dns = lineList[14]
            key_length = clean(lineList[11])

            if dns != "-":
                domainCount = str(dns.count(",") + 1)
            else:
                domainCount = "0"

            x509InfoDict[fingerprint] = [domainCount, key_length]
        #print(x509InfoDict)
        
        for line in sslFile.readlines()[8:-1]:
            lineList = line.split("\t")

            uid = lineList[1]
            ssl_history = lineList[15].split(",")

            domainCount, key_length = x509InfoDict[ssl_history[0]]

            if ssl_history[0] != "-":
                certPathLength = str(len(ssl_history))
            else:
                certPathLength = "0"

            certificateDict[lineList[1]] = [certPathLength, domainCount, key_length]
        #print(certificateDict)


    states = ["S0","S1","SF","REJ","S2","S3","RSTO","RSTR","RSTOS0","RSTRH","SH","SHR","OTH"]
    protocols = ["udp", "tcp", "icmp"]

    for i in range(8):
        connFile.readline()

    while True:
        line = connFile.readline()
        if not line: break

        lineList = line.split("\t")

        if len(lineList)!=21: break

        uid = lineList[1]
        protocol = str(protocols.index(lineList[6])+1) if lineList[6] in protocols else "0"
        conn_state = str(states.index(lineList[11])+1) if lineList[11] in states else "0"
        duration = clean(lineList[8])
        orig_bytes = clean(lineList[9])
        resp_bytes = clean(lineList[10])
        orig_pkts = clean(lineList[16])
        orig_ip_bytes = clean(lineList[17])
        resp_pkts = clean(lineList[18])
        resp_ip_bytes = clean(lineList[19])

        total_bytes = int(orig_bytes) + int(resp_bytes)
        ratio = str(round(int(resp_bytes) / total_bytes,5)) if total_bytes != 0 else "0"

        if uid in certificateDict:
            certPathLength, domainCount, key_length = certificateDict[uid]
        else:
            certPathLength = domainCount = key_length = "0"
        
        dataList = [protocol, conn_state, duration, orig_bytes, resp_bytes, orig_pkts, orig_ip_bytes, resp_pkts, resp_ip_bytes, ratio, certPathLength, domainCount, key_length]
        outputData.write("\t".join(dataList)+"\n")
    print("Finished folder",folder)
