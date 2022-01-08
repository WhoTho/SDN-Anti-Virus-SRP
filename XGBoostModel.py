import matplotlib.pyplot as MPL
import numpy as NP
import sklearn.metrics as SKL
import xgboost as XGB
from xgboost import DMatrix, XGBClassifier

filePath = lambda name:"/home/gopal/Desktop/srpantivirus/packetDatasets/"+name


maliciousInput = NP.loadtxt(filePath("malicious"), delimiter="\t")
maliciousOutput = [1]*len(maliciousInput)
benignInput = NP.loadtxt(filePath("benign"), delimiter="\t")
benignOutput = [0]*len(benignInput)

fullInput = NP.concatenate((maliciousInput,benignInput))
fullOutput = NP.concatenate((maliciousOutput,benignOutput))
assert(len(fullInput)==len(fullOutput))

labels = ["Duration","Size of flows orig","total size of flows resp","ratio of sizes","outbound packets","inbound packets","length of certificate path","certificate length","number of domains in certificate"]

dataTrain = DMatrix(fullInput,label=fullOutput, feature_names=labels)


param = {"verbosity":1,"max_depth":6, "objective":"binary:logistic"}
numberOfRounds = 50


model = XGB.train(param, dataTrain, numberOfRounds)
print(XGB.get_config())
print(fullInput[6])
pre = model.predict(DMatrix([fullInput[6]], feature_names=labels))
print(fullOutput[6])
print(pre)
XGB.plot_importance(model)
MPL.show()

model = XGBClassifier(max_depth=6,n_estimators=50)
print(model)

model.fit(fullInput,fullOutput)
print(fullInput[6])
print(model.predict(fullInput[6]))
print(fullOutput[6])

#SKL.recall_score()



#fullInput = maliciousInput + benignInput
#print(fullInput)

# Setup:
# 0             1                       2                               3                   4                       5                   6                               7                       8
# Duration      Size of flows orig      total size of flows resp        ratio of sizes      outbound packets        inbound packets     length of certificate path      certificate length      number of domains in certificate
