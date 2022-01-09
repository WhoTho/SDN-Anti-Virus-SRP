import matplotlib.pyplot as MPL
import numpy as NP
import sklearn.metrics as SKL
from sklearn import model_selection as SKLMS
from xgboost import XGBClassifier

filePath = lambda name:"/home/gopal/Desktop/srpantivirus/packetDatasets/"+name

fullInput = NP.loadtxt(filePath("mixedPacketInfo"), delimiter="\t")
fullOutput = NP.loadtxt(filePath("mixedPacketType"), delimiter="\t")
Xtrain,Xtest,Ytrain,Ytest = SKLMS.train_test_split(fullInput,fullOutput,stratify=fullOutput,random_state=10)
assert(len(fullInput)==len(fullOutput))

labels = ["Duration","Size of flows orig","total size of flows resp","ratio of sizes","outbound packets","inbound packets","length of certificate path","number of domains in certificate","certificate length"]

numberOfRounds = 1000
watchlist = [(Xtrain,Ytrain),(Xtest,Ytest)]
param = {"use_label_encoder":False,"verbosity":0,"max_depth":9,"eta":0.01,"objective":"binary:hinge","n_estimators":numberOfRounds,"eval_set":watchlist,"early_stopping_rounds":100}

model = XGBClassifier(**param)
model.fit(X=Xtrain,y=Ytrain,eval_set=[(Xtrain,Ytrain),(Xtest,Ytest)],eval_metric='error')
evals_result = model.evals_result()
model.save_model(filePath("model.txt"))

evalOutput = open(filePath("evalOutput"),"w+")


i=0
while i < len(evals_result['validation_0']['error']):
    evalOutput.write(str(evals_result['validation_0']['error'][i])+"\t"+str(evals_result['validation_1']['error'][i])+"\n")
    i+=1
print("done")

cmLabels = ["Malicious","Benign"]
predictions = model.predict(X=fullInput)
cm = SKL.confusion_matrix(fullOutput, predictions)
disp = SKL.ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=cmLabels)
disp.plot()
MPL.show()

# Setup:
# 0             1                       2                               3                   4                       5                   6                               7                                     8
# Duration      Size of flows orig      total size of flows resp        ratio of sizes      outbound packets        inbound packets     length of certificate path      number of domains in certificate      certificate length
