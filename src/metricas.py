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
    if "tiempo_uso" not in datos:
        raise KeyError("no existe tiempo_uso")
    suma = sum(datos["tiempo_uso"])
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
    if "tiempo_uso" not in datos:
        raise KeyError("tiempo_uso no existe")
    try:
        total = calcular_tiempo_total(datos)
        promedio = total / len(datos["tiempo_uso"])
        return promedio
    except ZeroDivisionError:
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
    cont = 0
    if "app" not in datos:
        raise KeyError("no existe la clave app")
        
    if "tiempo_uso" not in datos:
        raise KeyError("no existe la clave tiempo_uso")
    
    if len(datos["app"]) != len(datos["tiempo_uso"]):
        raise ValueError("Error, las listas no tienen el mismo tamaño") 
   
    for app in datos["app"]:
        tiempo = datos["tiempo_uso"][cont]

        if app not in uso_apps:
            uso_apps[app] = 0

        uso_apps[app] += tiempo
        cont += 1

    return uso_apps