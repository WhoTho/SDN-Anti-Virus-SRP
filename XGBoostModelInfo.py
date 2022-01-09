import matplotlib.pyplot as MPL
import numpy as NP
import sklearn.metrics as SKL
import xgboost as XGB
from xgboost import XGBClassifier

filePath = lambda name:"/home/gopal/Desktop/srpantivirus/packetDatasets/"+name


fullInput = NP.loadtxt(filePath("mixedPacketInfo"), delimiter="\t")
fullOutput = NP.loadtxt(filePath("mixedPacketType"), delimiter="\t")

assert(len(fullInput)==len(fullOutput))


model = XGBClassifier()
model.load_model(filePath("model.txt"))

labels = ["Duration","Size of flows orig","total size of flows resp","ratio of sizes","outbound packets","inbound packets","length of certificate path","number of domains in certificate","certificate length"]

model.feature_names = labels

XGB.plot_importance(model).set_yticklabels(labels[::-1])

cmLabels = ["Malicious","Benign"]
predictions = model.predict(X=fullInput)
cm = SKL.confusion_matrix(fullOutput, predictions)
disp = SKL.ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=cmLabels)
disp.plot()
MPL.show()

print(f'Accuracy: {SKL.accuracy_score(fullOutput, predictions)}')
print(f'Precision: {SKL.precision_score(fullOutput, predictions)}')
print(f'Recall: {SKL.recall_score(fullOutput, predictions)}')