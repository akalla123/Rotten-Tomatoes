#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:17:10 2018

@author: jaynanda
"""

import pandas as pd
import numpy as np

train = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/scifi_numeric.csv")

feature = pd.DataFrame(train['Genre'])
train = train.drop('Genre',axis=1)

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(train, feature, test_size= 0.30)

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial')
clf.fit(X_train, y_train)

res = clf.predict(X_test)

from sklearn.metrics import accuracy_score

print (accuracy_score(res,y_test))