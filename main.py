# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:07:15 2026

@author: Tomas Lopez Durand
"""

import cargar_datos
import metricas
import procesamiento_datos
from cargar_datos import cargar_datos_a_dicc
from metricas import calcular_promedio_uso
from metricas import calcular_uso_por_app
from procesamiento_datos import filtrar_por_participante

archivo = "data/BehaviorTracker_mock_data"

dicc_participantes = cargar_datos_a_dicc(archivo)
promedio_uso = calcular_promedio_uso(dicc_participantes)
uso_por_app = calcular_uso_por_app(dicc_participantes)

