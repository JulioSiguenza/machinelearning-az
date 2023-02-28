#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:47:18 2023

@author: juliosiguenza
"""
#plantilla datos categoricos

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



from sklearn.impute import SimpleImputer




dataset = pd.read_csv('data.csv')
x= dataset.iloc[:, :-1].values
y= dataset.iloc[: , 3].values

#Codificar datos categoricos(paises, etc)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
LabelEncoderX = LabelEncoder()
x[:,0] = LabelEncoderX.fit_transform(x[:,0]) #remplazamos la columna de paises
#por una columna ya codificada en numeros

encoder = OneHotEncoder(categories='auto', sparse=False)

# Obtener la primera columna de X
columna_0 = x[:, 0].reshape(-1, 1)

# Aplicar OneHotEncoder a la primera columna
columna_0_dummy = encoder.fit_transform(columna_0)

# Eliminar la primera columna original de X
x = x[:, 1:]

# Unir las nuevas columnas dummy a X
x = np.hstack((columna_0_dummy, x))


#hacemos lo mismo con la variable Y pero aca solo es necesario el labelencoder
labelEncoder_y = LabelEncoder()
y = labelEncoder_y.fit_transform(y)