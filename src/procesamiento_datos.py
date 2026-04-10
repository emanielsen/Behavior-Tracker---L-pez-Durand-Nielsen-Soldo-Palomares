#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:06:02 2026

@author: emanielsen
"""

def filtrar_por_participante(datos, id_participante):
    '''
    

    Parameters
    ----------
    datos : lista
    
    id_participante : int
        id del participante en cuestión del que serán buscados sus datos.

    Returns 
    -------
    dato : diccionario
    diccionario con los datos del participante.    

    '''
    
    for dato in datos: 
        if dato["id"] == id_participante:
            return dato
   
    
    else:
       return "no existe ese participante."

#IMPORTAR LAS FUNCIONES DE METRICAS