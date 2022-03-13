import numpy as np
# import scipy as scp
import matplotlib.pyplot as plt
import pandas as pd
# import sympy as sym
import sklearn as sk
import seaborn as sns

from sklearn import datasets

df = datasets.load_diabetes()
x = df.data
y = df.target
from sklearn.model_selection import train_test_split
xtrn,xtst,ytrn,ytst=train_test_split(x,y,test_size=0.2)


import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense


model = keras.Sequential()
model.add(Dense(12, input_dim=10, activation="relu"))
model.add(Dense(10, activation="relu"))
model.add(Dense(1, activation="sigmoid"))


model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(xtrn,ytrn, epochs=5)

_, accuracy = model.evaluate(xtst, ytst)
print("Model accuracy: %.2f"% (accuracy*100))

predictions = model.predict(x)
print([round(x[0]) for x in predictions])