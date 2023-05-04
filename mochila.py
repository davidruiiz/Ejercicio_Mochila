def es_solucion(solucion, capacidad):
    """Determina si la el conjunto de objetos en solucion es una solución válida"""
    total=0
    for elemento in solucion:
        total = round(total)+(elemento[1],2)
    if total == capacidad:
        return True
    else:
        return False
    
def mochila(conjunto_candidatos, capacidad):
    """Algoritmo voraz para resolver el problema de la mochila"""
    solucion= []
    restante = capacidad
    while conjunto_candidatos and not es_solucion(solucion, capacidad):
        dato = conjunto_candidatos.pop(0)
        if dato[1] <= restante:
            solucion.append(dato)
            restante = round(restante - dato[1],2)
    return solucion
 
import pandas as pd

# Crear un dataframe con los datos del CSV
df = pd.read_csv('pokemon.csv', sep=';')
df1 = pd.read_csv('Pokemon_Go.csv', sep=';')

# fusionar dos datasets
df2 = pd.merge(df, df1, on='name', how='inner')