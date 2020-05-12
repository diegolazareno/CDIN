# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:12:16 2020

@author: USUARIO
"""
#%% 
import pandas as pd
# Se leen los csv's y se procede a realizar el DQR con la librería
df_1=pd.read_csv('../Data/Accidents_2015.csv')
df_2=pd.read_csv('../Data/Casualties_2015.csv')
df_3=pd.read_csv('../Data/Vehicles_2015.csv')

#%%
from mylib import mylib
# Se llama a la librería para realizar el DQR
reporte_1=mylib.dqr(df_1)
reporte_2=mylib.dqr(df_2)
reporte_3=mylib.dqr(df_3)
#%% Guardar los DQR en un archivo csv
reporte_1.to_csv('../Data/Accidents_DQR.csv')
reporte_2.to_csv('../Data/Casualties_DQR.csv')
reporte_3.to_csv('../Data/Vehicles_DQR.csv')
#%% Consultas sencillas de información

# value_counts: Return a Series containing counts of unique values
# value_counts cuenta los valores que comparten un mismo índice, en este caso el índice es Date
num_by_date=pd.DataFrame(pd.value_counts(df_1["Date"]))

# groupby split the data into groups based on some criteria
# Una vez se realiza el método groupby se accede a una columna en específico y se opera en ella
vehicles_day=pd.DataFrame(df_1.groupby(["Date"])["Number_of_Vehicles"].sum())
casualties_day=pd.DataFrame(df_1.groupby(["Date"])["Number_of_Casualties"].sum())

#Se crea un nuevo DataFrame con el número de accidentes, accidentados y vehículos por fecha
vehicles_casualties=num_by_date.join(vehicles_day).join(casualties_day)
#%% Consultas sencillas de información
vehicles_by_day=df_1.groupby(["Day_of_Week"])["Number_of_Vehicles"].sum()
vehicle_by_time=df_1.groupby(["Time"])["Number_of_Vehicles"].sum()
vehicle_by_day_time=df_1.groupby(["Day_of_Week","Time"])["Number_of_Vehicles"].sum()
vehicle_by_position=df_1.groupby(["Latitude","Longitude"])["Number_of_Vehicles"].sum()
#%% Histogramas
import matplotlib.pyplot as plt

plt.hist(df_1["Latitude"][df_1["Latitude"].isnull()==False],bins=30)
plt.xlabel("Latitude")
plt.ylabel("Num_Accidents")
plt.title("Histogram_Accidents")
plt.grid()
plt.show()

plt.hist(df_1["Longitude"][df_1["Longitude"].isnull()==False],bins=30)
plt.xlabel("Longitude")
plt.ylabel("Num_Accidents")
plt.title("Histogram_Accidents")
plt.grid()
plt.show()