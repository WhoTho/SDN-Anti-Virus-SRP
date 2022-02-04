import matplotlib.pyplot as MPL
import numpy as NP
import sklearn.metrics as SKL
import xgboost as XGB
from xgboost import XGBClassifier

filePath = lambda name:"/home/gopal/Desktop/srpantivirus/master/"+name


fullInput = NP.loadtxt(filePath("testMixedPacketInfo"), delimiter="\t")
fullOutput = NP.loadtxt(filePath("testMixedPacketType"), delimiter="\t")

assert(len(fullInput)==len(fullOutput))

model = XGBClassifier()
model.load_model(filePath("model.txt"))

labels = ["protocol", "conn_state", "duration", "orig_bytes", "resp_bytes", "orig_pkts", "orig_ip_bytes", "resp_pkts", "resp_ip_bytes", "ratio", "certPathLength", "domainCount", "key_length"]

CMLabels = ["Benign", "Malicious"]

model.feature_names = labels

font = {'weight' : 'bold',
        'size'   : 22}

MPL.rc('font', **font)

XGB.plot_importance(model).set_yticklabels(labels[::-1])

predictions = model.predict(X=fullInput)
cm = SKL.confusion_matrix(fullOutput, predictions)
disp = SKL.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=CMLabels)
disp.plot()
MPL.show()

assert(len(fullOutput)==len(predictions))


truePositive = 0
falsePositive = 0
trueNegative = 0
falseNegative = 0
for real,pred in zip(fullOutput, predictions):
    if real == 0:
        if pred == 0: trueNegative += 1
        else: falsePositive += 1
    else:
        if pred == 1: truePositive += 1
        else: falseNegative += 1

print(f'Accuracy: {(truePositive + trueNegative) / len(predictions)}')
print(f'Precision: {truePositive / (truePositive + falsePositive)}')
print(f'Recall: {truePositive / (truePositive + falseNegative)}')
print(f'Selectivity: {trueNegative / (trueNegative + falsePositive)}')
