# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:07:15 2026

@author: Tomas Lopez Durand
"""

import src.cargar_datos
import stc.metricas
import stc.procesamiento_datos
from cargar_datos import cargar_datos_a_dicc
from metricas import calcular_promedio_uso
from metricas import calcular_uso_por_app
from procesamiento_datos import filtrar_por_participante

archivo = "data/BehaviorTracker_mock_data"

dicc_participantes = cargar_datos_a_dicc(archivo)

while True:
    try:
        id_part = int(input("Ingrese el ID del participante al que se quiere buscar: "))
        break
    except ValueError as e:
        print("ID ingresado es inválido. ", e)

participante = filtrar_por_participante(dicc_participantes, id_part)
promedio_uso = calcular_promedio_uso(participante)
uso_por_app = calcular_uso_por_app(participante)
print(f"El promedio de uso del participante seleccionado es: {promedio_uso}")
print(f"El uso total {uso_por_app}")

