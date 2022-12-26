#Ejercicio 1
#Obtener la información de la siguiente Api y enlistar los datos en una tabla

#https://pokeapi.co/api/v2/pokemon/

import requests
import pandas as pd

#Ejercicio 1.1
#Obtener la información de la siguiente Api y agregar la opción para buscar un pokemon

#https://pokeapi.co/api/v2/pokemon/pikachu

#Ejercicio 2
"""A través de la lectura del set de datos Data.csv es necesario limpiar y estandarizar  
la información en un nuevo archivo llamado Salida.csv
aplicando las siguientes reglas de limpieza de datos"""

#Reglas de Limpieza
"""Conversión de minusculas a Mayusculas, quitar caracteres especiales, quitar espacios a los costados,
quitar espacios entre renglones,
cambiar el separador de cada columna de un tabulador (\t) por un pipe (|)
"""

#Ejercicio 3
"""Usando la siguiente cadena y patron de token, filtra solo los tokens y texto con el simbolo de +"""

text="GUSTAVO 12324 MENDOZA $#%&$%&$%"
token="|+|^|+|!|"
newText="GUSTAVO MENDOZA"
