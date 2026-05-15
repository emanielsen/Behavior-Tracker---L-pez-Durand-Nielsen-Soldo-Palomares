# Behavior Tracker - López Durand, Nielsen, Soldo Palomares
Repositorio colaborativo del proyecto Behavior Tracker

Este proyecto permite la lectura, recolección y utilización de datos sobre un archivo que contiene información acerca de la duración y la frequencia del uso de aplicaciones en el teléfono.

Cómo incluir la librería Pandas:

- Primero se abrirá el archivo csv provisionado con la función de Pandas para poder utilizar los otros métodos para poder manejar los datos del archivo.
- Después se le adjuntará un nombre a todas las columnas para poder ordenarlas y buscarlas mejor. El index será el que yá está provisionado por el excel.
- Se van a tener que cambiar el código de algunas funciones ya existentes para que puedan ser compatibles con las Series y DataFrames.