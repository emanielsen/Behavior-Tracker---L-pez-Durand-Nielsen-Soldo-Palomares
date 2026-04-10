#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:41:48 2026

@author: emanielsen
"""
archivo = open("datos.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    print(linea)
    
archivo.close()

def parsear_linea(linea):
    '''
    función que modifica la linea de un archivo, separando los valores por comas y
    asigna a sus valores (una vez separados) como int o str.

    Parameters
    ----------
    linea : str
        linea del archivo, sin ninguna modificación.

    Returns
    -------
    lista_parseada : lista
        lista con los elementos de la linea separados por coma y convertidos a su tipo correspondiente (int o str).

    '''
    lista_parseada = []
    separar = linea.split(",")
    int1 = int(separar[0])
    str1 = str(separar[1])
    str2 = str(separar[2])
    int2 = int(separar[3])
    int3 = int(separar[4])
    
    lista_parseada = [int1, str1, str2, int2, int3]
    
    return lista_parseada
    
    
    
    
    
    

    
    
def cargar_datos(ruta):
    '''
    Lee un archivo .CSV, parsea cada línea y organiza los datos en un diccionario 
    donde cada clave es un id de participante y su valor es una lista de registros del participante.

    Parameters
    ----------
    ruta : str
        ruta del archivo a leer.

    Returns
    -------
    datos : dicc
        diccionario con los datos agrupados por participante.

    '''
    
    datos = {}
    
    with open(ruta, "r") as archivo:
        for linea in archivo:
            registro = parsear_linea(linea)
            id_participante = registro[0]
            if id_participante not in datos:
                datos[id_participante] = []

            datos[id_participante].append(registro)
            
    return datos
       