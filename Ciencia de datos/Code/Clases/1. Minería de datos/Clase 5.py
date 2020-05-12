# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:07:28 2020

@author: USUARIO
"""
# Test de películas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as skm # metricas de similitud
import scipy.spatial.distance as sc #métricas de distancias

#%% 
# Se importa el data set con el test de películas
file='../Data/Test.xlsx'
#test_peliculas=pd.read_excel(file)

test_peliculas=pd.read_excel("C:/Users/USUARIO/Desktop/Ingeniería Financiera/4to Semestre/Ciencia de datos/Data/Test.xlsx")

# El DataFrame tiene columnas innecesarias, se eliminan
# .iloc permite recortar DataFrames. Puede escribirse en forma de rango con saltos
# El límite final de la función .iloc no incluye tal término, por eso se le añade +1
# En este caso se desean recortar dos columnas y dejar intacta la tercera, por eso se pone 3 en los saltos
# Los valores vacíos se llenan con ceros
data=test_peliculas.iloc[:,4:(len(test_peliculas.iloc[0])+1):3].fillna(0)

#%%
# Ciclo anidado para llenar con 1 las calificaciones mayores o iguales a 3, 0 de lo contrario
for i in range(len(data)):
    for j in range(len(data.iloc[0])):
        if j>0:
            if data.iloc[i,j]>=3:
                data.iloc[i,j]=1
            else:
                data.iloc[i,j]=0

#%% Calcular índices de similitud en usuarios: Lazareno y Christian
# Lazareno (1er argumento de la función) se encuentra en .index (parte lateral)
# Christian (2do argumento de la función) se encuentra en .columns (parte superior)
# La función sólo acepta argumentos en formato lista
cf_m=skm.confusion_matrix(list(data.iloc[0,1:]),list(data.iloc[1,1:]))

#%% Índice de similitud simple calculado de dos formas distintas
sim_simple=skm.accuracy_score(list(data.iloc[0,1:]),list(data.iloc[1,1:]))

#The default, axis=None, will sum all of the elements of the input array.
# Se suman los elementos que se comparten y se dividen entre los elementos totales
sim_simple_new=(cf_m[0,0]+cf_m[1,1])/np.sum(cf_m)

#%% Cálculo del índice de similitud simple con los compañeros
# Se busca al compañero con el que se tiene mayor similitud
indices_sim=pd.DataFrame(np.zeros((len(data),1)))
for i in range(len(data)):
    indices_sim.iloc[i,0]=skm.accuracy_score(list(data.iloc[0,1:]),list(data.iloc[i,1:]))

# Se remueve la fila con el mayor índice de similitud, pues me compara conmigo mismo
indice=indices_sim.idxmax()[0] # idxmax devuelve un vector con índice 0, por ello se accede a la única posición
indices_sim.drop([indice],inplace=True)

# Ahora se busca el índice del compañero con mayor similitud a mis datos
indice_sim_max=indices_sim.idxmax()[0]
# Con el índice del compañero se accede a su nombre con ayuda del DataFrame original
print("El compañero con el que tengo mayor índice de similitud simple es:",data.iloc[indice_sim_max,0])

#%% Índice de similitud de Jackard
# Jackard sólo toma en cuenta los 1&1, la función de skm no funciona
sim_jac=skm.jaccard_similarity_score(list(data.iloc[0,1:]),list(data.iloc[1,1:]))
sim_jac_new=(cf_m[1,1])/(np.sum(cf_m)-cf_m[0,0]) #Proporción de elementos concordantes

#%% Cálculo de las distancias, con distintos métodos

d1=sc.matching(data.iloc[0,1:],data.iloc[1,1:])

# Y = pdist(X, 'jaccard')
# Computes the Jaccard distance between the points. Given two vectors, u and v, the Jaccard distance is the proportion of those elements u[i] and v[i] that disagree
d2=sc.jaccard(data.iloc[0,1:],data.iloc[1,1:]) # Proporción de elementos no concordantes  

#%% Calcular todas las combinaciones posibles

# Y = pdist(X, 'hamming')
# Computes the normalized Hamming distance, or the proportion of those vector elements between two n-vectors u and v which disagree. To save memory, the matrix X can be of type boolean.
D1=sc.pdist(data.iloc[:,1:],"matching")
D1=sc.squareform(D1)
D1=pd.DataFrame(D1)

# Distancia de Jaccard: complemento del Índice de Jaccard
D2=sc.pdist(data.iloc[:,1:],"jaccard")
D2=sc.squareform(D2)
D2=pd.DataFrame(D2)

#%% Seleccionar un usuario y determinar los usuarios más parecidos

# En este caso yo soy el usuario 0
user=0
# Comparación mía con los demás usuarios por el método "matching" o "hamming" para calcular distancias
D_user=D1.iloc[user]
# Ordenar de menor a mayor índice de similitud
D_user_sort=np.sort(D_user)
# Ordenar de menor a mayor índice de similitud poniendo el índice del usuario en lugar del valor numérico
indx_user=np.argsort(D_user)

#%% Recomendación versión 1. El usuario más parecido 

# Localizarme en el DataFrame donde califiqué las películas
User=data.loc[user]
# Localizar las calificaciones que dió el usuario más parecido conmigo: Juan Enrique Aguirre López
User_sim=data.loc[indx_user[1]]
# Vector con valores booleanos para las películas que le gustaron a Juan Enrique pero a mí no
indx_recomen=(User_sim==1)&(User==0)
# Vector de recomendación con las películas que le gustaron a Juan Enrique
## Se devuelven los nombres de las películas donde se encuentra un valor True
recomend1=list(User.index[indx_recomen])

#%% Recomendación versión 2. Los n usuarios más parecidos
# Se genera una media con las calificaciones que dieron los 5 usuarios más parecidos a mí
# Con la media se escoge un umbral de 0.5 y con base a esto se me recomiendan películas
User=data.loc[user]
User_sim=np.mean(data.loc[indx_user[1:6]],axis=0)
User_sim[User_sim<=0.5]=0
User_sim[User_sim>0.5]=1
indx_recomen=(User_sim==1)&(User==0)
recomend2=list(User.index[indx_recomen])