import itertools as IT

import numpy as NP
import tensorflow as TF
from tensorflow import keras as KR

# Simple code to generate sample test data
perms = set(list(IT.permutations([0]*4+[1]*4,4)))
inputTemp = []
outputTemp = []
print(perms)
for p in perms:
    inputTemp.append(p)
    a = (p[0]^p[1])^p[2]^p[3]
    outputTemp.append([a])

print(inputTemp)
print(outputTemp)
inputDataTrain = NP.array(inputTemp)
outputDataTrain = NP.array(outputTemp)

model = KR.Sequential([
    KR.layers.Dense(8, input_dim=4, activation='relu'),
    KR.layers.Dense(1, activation='sigmoid')
])


model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics='accuracy')


history = model.fit(
    inputDataTrain,
    outputDataTrain,
    epochs=1000,
    verbose=2
)

predictions = model.predict(inputDataTrain).round()
print(predictions)
evaluation = model.evaluate(inputDataTrain,outputDataTrain)
print(evaluation)
print(inputDataTrain)
print(outputDataTrain)
