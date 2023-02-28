#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 00:03:08 2023

@author: juliosiguenza
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.impute import SimpleImputer


dataset = pd.read_csv('data.csv')
x= dataset.iloc[:, :-1].values
y= dataset.iloc[: , 3].values

#tratamiento de los NA



#dividir la data set en un conjunto de entrenamiento y otro de testing
from sklearn.model_selection import train_test_split
x_train, x_test , y_train , y_test = train_test_split(x, y, test_size=0.2, random_state=(0))

#escalado de variables(cuando la variables difieren de mucha cantidad)
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""









