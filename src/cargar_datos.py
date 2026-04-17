#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:41:48 2026

@author: emanielsen
"""


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
    
    try:
        int1 = int(separar[0])
        str1 = str(separar[1])
        str2 = str(separar[2])
        int2 = int(separar[3])
        int3 = int(separar[4])
    except:
        raise ValueError(f"Error al parsear línea: {linea}")
        
    else:
        lista_parseada = [int1, str1, str2, int2, int3]
        return lista_parseada
    



    
    
def cargar_datos_a_dicc(ruta):
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
    
    datos = []
    registro_participante = {}
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                registro = parsear_linea(linea)
                
    except:
        raise FileNotFoundError("el archivo no existe o no se puede encontrar.")
            
            
    else:
        id_participante = registro[0]
        if id_participante not in registro_participante:
            registro_participante[id_participante] = {
                "id": id_participante,
                "fecha": [],
                "app": [],
                "cantidad_uso": [],
                "tiempo_uso": []
                   }
            registro_participante[id_participante]["fecha"].append(registro[1])
            registro_participante[id_participante]["app"].append(registro[2])
            registro_participante[id_participante]["cantidad_uso"].append(registro[3])
            registro_participante[id_participante]["tiempo_uso"].append(registro[4])
        else:
            registro_participante[id_participante]["fecha"].append(registro[1])
            registro_participante[id_participante]["app"].append(registro[2])
            registro_participante[id_participante]["cantidad_uso"].append(registro[3])
            registro_participante[id_participante]["tiempo_uso"].append(registro[4])
           
        datos.append(registro_participante)
            
    return datos
       