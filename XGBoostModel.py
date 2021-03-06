import matplotlib.pyplot as MPL
import numpy as NP
import sklearn.metrics as SKL
from sklearn import model_selection as SKLMS
from xgboost import XGBClassifier

filePath = lambda name : "/home/gopal/Desktop/srpantivirus/test2/" + name

# Getting the inputs and correct outputs
fullInput = NP.loadtxt(filePath("mixedPacketInfo"), delimiter="\t")
fullOutput = NP.loadtxt(filePath("mixedPacketType"), delimiter="\t")

# Splitting data to have a training set and a testing set
Xtrain, Xtest, Ytrain, Ytest = SKLMS.train_test_split(fullInput, fullOutput, stratify=fullOutput, random_state=10)
assert(len(fullInput)==len(fullOutput))

# Setting the parameters
numberOfRounds = 1000
watchlist = [(Xtrain, Ytrain), (Xtest, Ytest)]
param = {"use_label_encoder" : False, "verbosity" : 0, "max_depth" : 9, "eta" : 0.01, "objective" : "binary:hinge",
"n_estimators" : numberOfRounds, "eval_set" : watchlist, "early_stopping_rounds" : 50, "subsample" : 0.75}

# Training the model
model = XGBClassifier(**param)
model.fit(X=Xtrain, y=Ytrain, eval_set=[(Xtrain, Ytrain), (Xtest, Ytest)], eval_metric='error')

# Evaluating the training session
evals_result = model.evals_result()
model.save_model(filePath("model.txt"))

evalOutput = open(filePath("evalOutput"), "w+")

# Writing training session results to an output file
i=0
while i < len(evals_result['validation_0']['error']):
    evalOutput.write(str(evals_result['validation_0']['error'][i])+"\t"+str(evals_result['validation_1']['error'][i])+"\n")
    i+=1
print("done")

# Shows full results of all the data in a confusion matrix
predictions = model.predict(X=fullInput)
cm = SKL.confusion_matrix(fullOutput, predictions)
disp = SKL.ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
MPL.show()