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
    datos_participante : lista
    lista con los datos del participante (id_participante).    

    '''
    
    if id_participante in datos:
       datos_participante = datos[id_participante]
       return datos_participante
   
    
    else:
       return "no existe ese participante."