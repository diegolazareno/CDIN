# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:12:02 2020

@author: USUARIO
"""

import pandas as pd
import string

#%% Importar los datos
# El dataset está sucio, por lo que debe ser limpiado
dirty=pd.read_csv("../Data/dirty_data.csv")

#%% Remover signos de puntuación
# !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
def remove_punctuation(x):
    try:
        x="".join(ch for ch in x if ch not in string.punctuation)
    except:
        pass
    return x

#%% Remover dígitos
# 0123456789
def remove_digits(x):
    try:
        x="".join(ch for ch in x if ch not in string.digits)
    except:
        pass 
    return x

#%% Remover espacios en blanco
def remove_whitespace(x):
    try:
        x="".join(x.split)
    except:
        pass
    return x

#%% Reemplazar texto
def replace_text(x,to_replace,replacement):
    try:
        x=x.replace(to_replace,replacement)
    except:
        pass
    return x

#%% Convertir a mayúsculas
def uppercase_text(x):
    try:
        x=x.upper()
    except:
        pass
    return x

#%% Convertir a minúsculas
def lowercase_text(x):
    try:
        x=x.lower()
    except:
        pass
    return x

#%% Dejar sólo dígitos
def digits(x):
    try:
        x="".join(ch for ch in x if ch in string.digits)
    except:
        pass
    return x

#%% Aplicar las funciones
dirty.people=dirty["people"].apply(remove_punctuation).apply(lowercase_text).apply(remove_digits)
dirty.people=dirty.people.apply(replace_text,args=("d","")).apply(replace_text,args=("aa","a"))

#%% Limpiar columna matricial
idx=dirty.marital.isnull()
dirty.marital[idx]="missing"
dirty.marital=dirty.marital.apply(uppercase_text)

dirty.ssn=dirty.ssn.apply(digits)

#%% Función para agregar ceros a la columna del número de celular
def ceros_ssn(x):
    try:
        x=str(x)
        while (len(x)<10):
            x="0"+x
    except:
        pass
    return x
dirty.ssn=dirty.ssn.apply(ceros_ssn)
dirty.ssn=dirty.ssn.apply(replace_text,args=("nan","000"))