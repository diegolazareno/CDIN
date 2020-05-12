# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:34:24 2020

@author: USUARIO
"""

class mylib:
    # Se crea una función llamada Data Quality Report para explorar la base de datos
    def dqr(data):
        import pandas as pd
    # Lista de variables de la base de datos
        columns=pd.DataFrame(list(data.columns.values),columns=["Nombres"],index=list(data.columns.values))
    
        # Lista de tipos de datos
        data_types=pd.DataFrame(data.dtypes,columns=["Data_Types"])
    
        # Lista de datos perdidos
        missing_values=pd.DataFrame(data.isnull().sum(),columns=["Missing_Values"])
    
        # Lista de los datos presentes
        present_values=pd.DataFrame(data.count(),columns=["Present_Values"])
    
        # Lista de valores únicos, que no se repitan
        unique_values=pd.DataFrame(columns=["Unique_Values"])
        for col in list(data.columns.values):
            unique_values.loc[col]=[data[col].nunique()]

        # Lista de valores mínimos
        min_values=pd.DataFrame(columns=["Min"])
        for col in list(data.columns.values):
            try:
                min_values.loc[col]=[data[col].min()]
            except:
                pass
    
        # Lista de valores máximos
        max_values=pd.DataFrame(columns=["Max"])
        for col in list(data.columns.values):
            try:
                max_values.loc[col]=[data[col].max()]
            except:
                pass
    
        return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values)