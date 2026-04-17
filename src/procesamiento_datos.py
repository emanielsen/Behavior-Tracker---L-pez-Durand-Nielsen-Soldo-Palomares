#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:06:02 2026

@author: emanielsen
"""

def filtrar_por_participante(datos, id_participante):
    '''
    Filtra los registros de un participante específico a partir de una lista de datos.

    Parameters
    ----------
    datos : lista
        lista de diccionarios con información de participantes.
    
    
    id_participante : int
        id del participante en cuestión del que serán buscados sus datos.

    Returns 
    -------
    dato : diccionario
    diccionario con los datos del participante.    

    '''
    
    for dato in datos: 
        for participante in dato:
            if participante == id_participante:
                return dato[participante]
   
    return "No existe ese participante."

#IMPORTAR LAS FUNCIONES DE METRICAS