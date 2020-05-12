# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:55:21 2020

@author: USUARIO
"""
# Se importa la librería pandas con el alías pd
import pandas as pd

# Se carga el data set elegido de Kaggle de dos formas distintas:
##########################################################################
# 1. Se carga el data set con toda la dirección del archivo
data_dir="C:/Users/USUARIO/Desktop/Ingeniería Financiera/4to Semestre/Ciencia de datos/Data/weatherAUS.csv"
rain_australia=pd.read_csv(data_dir)

# 2. Se carga el data set ingresando a la carpeta que lo contiene
direccion='../Data/weatherAUS.csv'
# El atributo index_col pone a la columna elegida como índice,
## en este caso se escoge la fecha para índice 
lluvia=pd.read_csv(direccion,index_col="Date")