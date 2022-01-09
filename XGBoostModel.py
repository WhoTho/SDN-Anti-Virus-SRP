import matplotlib.pyplot as MPL
import numpy as NP
import sklearn.metrics as SKL
import xgboost as XGB
from sklearn import model_selection as SKLMS
from xgboost import DMatrix, XGBClassifier

filePath = lambda name:"/home/gopal/Desktop/srpantivirus/packetDatasets/"+name



# maliciousInput = NP.loadtxt(filePath("malicious"), delimiter="\t")
# maliciousOutput = NP.ones(len(maliciousInput))
# benignInput = NP.loadtxt(filePath("benign"), delimiter="\t")
# benignOutput = NP.zeros(len(benignInput))

fullInput = NP.loadtxt(filePath("mixedPacketInfo"), delimiter="\t")
fullOutput = NP.loadtxt(filePath("mixedPacketType"), delimiter="\t")
Xtrain,Xtest,Ytrain,Ytest = SKLMS.train_test_split(fullInput,fullOutput)
assert(len(fullInput)==len(fullOutput))

labels = ["Duration","Size of flows orig","total size of flows resp","ratio of sizes","outbound packets","inbound packets","length of certificate path","certificate length","number of domains in certificate"]

dataTrain = DMatrix(Xtrain,label=Ytrain,feature_names=labels)
dataTest = DMatrix(Xtest,label=Ytest,feature_names=labels)


param = {"verbosity":0,"max_depth":9, "eta":0.01,"objective":"binary:hinge", "eval_metric":"error", "n_estimators":1000}
numberOfRounds = 100000

watchlist = [(dataTrain,'train'),(dataTest,'eval')]
evals_result = {}
model = XGB.train(param, dataTrain, numberOfRounds, watchlist, evals_result=evals_result,early_stopping_rounds=7500)
model.save_model(filePath("model.txt"))

evalOutput = open(filePath("evalOutput"),"w+")


i=0
while i < len(evals_result['eval']['error']):
    evalOutput.write(str(evals_result['train']['error'][i])+"\t"+str(evals_result['eval']['error'][i])+"\n")
    i+=1
print("done")

#model = XGB.cv(dtrain=dataTrain, params=param,nfold=10,metrics="auc",seed=1)
#print(XGB.get_config())
# print(f'fullnput: {fullInput[6]}')
# pre = model.predict(DMatrix([fullInput[6]], feature_names=labels))
# print(fullOutput[6])
# print(pre)
XGB.plot_importance(model)
MPL.show()



#SKL.recall_score()



#fullInput = maliciousInput + benignInput
#print(fullInput)

# Setup:
# 0             1                       2                               3                   4                       5                   6                               7                       8
# Duration      Size of flows orig      total size of flows resp        ratio of sizes      outbound packets        inbound packets     length of certificate path      certificate length      number of domains in certificate
