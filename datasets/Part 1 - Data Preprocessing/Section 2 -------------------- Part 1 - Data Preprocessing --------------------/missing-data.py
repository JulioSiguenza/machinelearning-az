#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:48:09 2023

@author: juliosiguenza
"""

#plantilla datos faltantes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



from sklearn.impute import SimpleImputer




dataset = pd.read_csv('data.csv')
x= dataset.iloc[:, :-1].values
y= dataset.iloc[: , 3].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(fill_value= "NaN", strategy = "mean")
imputer = imputer.fit(x[: , 1:3])#del 1 al 3 porque en python no coge la ultima
x[:,1:3] = imputer.transform(x[:, 1:3])#aqui se remplaza la columna que esta en todas 
#las filas pero solo en las columnas 1 y 2 que tienen datos vacios