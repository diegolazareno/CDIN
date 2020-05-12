# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc
import sklearn.metrics as skm

#%% Generar datos
# Cada lista es un punto con dirección <i,j>. En otras palabras, cada fila es un punto en R^2
X=np.array([[2,3],[20,30],[-2,-3],[2,-3]])

# Visualización de los datos generados
plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.grid()
plt.show()

#%% Distancia Euclideana
# Para calcular las distancias se compara cada fila contra cada fila, es decir, punto contra punto
# Ejemplo: ((30-3)^2-(20-2)^2) 
D1=sc.pdist(X,"euclidean")
D1=sc.squareform(D1)

#%% Índice coseno
D2=sc.pdist(X,"cosine")
D2=sc.squareform(D2)
D2=D2/2 #El Índice coseno va de 0 a 2, si lo dividimos entre 2 podemos estandarizarlo
# Valores cercanos a 1 indican poca similitud, de lo contrario, valores cercanos a 0 indican mayor similitud

#%% Índice correlación
D3=sc.pdist(X,"correlation")
D3=sc.squareform(D3)