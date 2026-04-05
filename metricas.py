#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:19:42 2026

@author: emanielsen
"""

def calcular_tiempo_total(datos):
    '''
    calcula el total del tiempo de uso de un participante.

    Parameters
    ----------
    datos : lista
        lista con los registros del participante.

    Returns
    -------
    suma : float
        suma de todo tiempo total (intensidad de uso).

    '''
    suma = 0
    for registro in datos:
        tiempo = registro[4]
        suma += tiempo
    return suma




def calcular_promedio_uso(datos):
    '''
    Calcula el promedio del tiempo de uso de un participante.    

    Parameters
    ----------
    datos : lista
        lista con los registros del participante.

    Returns
    -------
    promedio : float
        promedio del tiempo de uso.

    '''
    try:
        total = calcular_tiempo_total(datos)
        promedio = total / len(datos)
        return promedio
    except:
        print("no hay datos para calcular el promedio.") 
        return 0
    
    
    
def calcular_uso_por_app(datos):
    '''
    Calcula el tiempo total de uso por cada aplicación.

    Parameters
    ----------
    datos : lista
        lista con los registros del participante.

    Returns
    -------
    uso_apps : dicc
        diccionario con las apps como claves y el tiempo total como valor.

    '''
    uso_apps = {}

    for registro in datos:
        app = registro[2]
        tiempo = registro[4]

        if app not in uso_apps:
            uso_apps[app] = 0

        uso_apps[app] += tiempo

    return uso_apps