# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:27:36 2020

@author: USUARIO
"""
import numpy as np
import pandas as pd
from mylib import mylib

data_dir='../Data/weatherAUS.csv'
lluvia_AUS=pd.read_csv(data_dir)

# Utilizar mi función para el reporte del csv
mi_reporte=mylib.dqr(lluvia_AUS)