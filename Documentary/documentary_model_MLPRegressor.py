#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:17:10 2018

@author: jaynanda
"""

import pandas as pd
import numpy as np

train = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/documentary_numeric.csv")

feature = pd.DataFrame(train['Genre'])
train = train.drop('Genre',axis=1)

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(train, feature, test_size= 0.30)

from sklearn.neural_network import MLPRegressor
clf = MLPRegressor(hidden_layer_sizes=(5,), activation='relu', solver='adam', learning_rate='adaptive', max_iter=1000, learning_rate_init=0.01, alpha=0.01)

clf.fit(X_train, y_train)

res = clf.predict(X_test)
lsd=[]

for item in res:
    if item>=0.5:
        lsd.append(1)
    else:
        lsd.append(0)

from sklearn.metrics import accuracy_score

print (accuracy_score(lsd,y_test))