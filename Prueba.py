#Ejercicio 1
#Obtener la información de la siguiente Api y enlistar los datos en una tabla

#https://pokeapi.co/api/v2/pokemon/

import requests
import pandas as pd
import json
from tabulate import tabulate
import csv
import re
# -*- coding: utf-8 -*-

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

url = "https://pokeapi.co/api/v2/pokemon/"

#Ejercicio 1
def GetAllInfoPokemonFromURL(url):
    """Obtiene la informacion de la api de pokemon y la tubula
    Parametros: 
    url: url a consultar
    
    Retorna 
    tabla con la informacion encontrada en la url"""
    try:
        # name_pokemon= input("Introduce el nombre de un pokemon: ")
        nombres=[]
        urls=[]
        _info_api = json.loads(requests.get(url).text)
        for item in _info_api["results"]:
            item["name"]=nombres.append(item["name"].upper())
            item["url"]=urls.append(item["url"])
        return(pd.Series(index=nombres, data=urls))
    except Exception as e:
        print(e)

#Ejercicio 1.1
def GetPokemonInfo():
    """Obtiene informacion del pokemon
    Parametros:
    No requiere parametros
    retorna:
        Datos como nombre, experiencia, altura y peso del pokemon
    """
    try:
        url = "https://pokeapi.co/api/v2/pokemon/"
        pokemon=str(raw_input("Introduce el nombre del pokemon que quieres buscar: "))
        _info_api = json.loads(requests.get(url+pokemon).text)
        if _info_api:
            _info_pokemon = "El pokemon: "+str(pokemon)+", tiene la siguiente experiencia: "+str(_info_api["base_experience"])+", mide: "+str(_info_api["height"])+ " y pesa: "+str(_info_api["weight"])+"kg"
            return(_info_pokemon)
        else:
            return("No hay informacion del pokemon llamado: "+pokemon)
        # _array_pokemon = url['']
    except Exception as e:
        return("No hay informacion del pokemon solicitado")


# print(GetAllInfoPokemonFromURL(url))
# print(GetPokemonInfo())

def LimpiarArchivoCVS():
    """estandarizar  
    la información en un nuevo archivo llamado Salida.csv"""
    try:
        array_filas=[]
        with open("Data.txt", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row!=[]:
                    row[0]= row[0]
                    # row[0]=(re.sub(r"[^a-zA-Z0-9]","",(row[0].replace("\t","|").replace(" ","")))).upper()
                    row[0]=((row[0].replace("\t","|").replace(" ","").replace('"',"").replace("_","").replace('\xe1','a').replace('\xf1',"n").replace('\xf3','o').replace('\xfa','u').replace("\xed","i").replace('\xe9',"e"))).upper().split("|")
                    _nueva_cadena=""
                    for item in row[0]:
                        item= (re.sub(r"[^a-zA-Z0-9]","",item)).encode('utf-8')
                    # _nueva_cadena = "|".join(row[0])
                    _nueva_cadena=row[0]
                    array_filas.append(_nueva_cadena)
            print(array_filas)
        
        with open('Salida.csv', 'w') as file:
            writer = csv.writer(file, delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(array_filas)
    except Exception as e:
        return("Opps algo ocurrio intentalo nuevamente")

def limpiarAcentos(cadena):
    try:
        acentos = {'á':'a',"é":'e','í':'i','ó':'o','ú':'u','ñ':'n'}
        for a,b in acentos:
            s=cadena.replace(a,b).replace(a.upper(),b.upper())
        return s
    except Exception as e:
        return('error')

print(LimpiarArchivoCVS())

def FiltrarTokens():
    """Usando la siguiente cadena y patron de token, filtra solo los tokens y texto con el simbolo de +"""
    try:
        text= str(raw_input("Introduce el texto que quieres filtrar: "))
        token= str(raw_input("Introduce el patron de token que quieres filtrar: "))
        character= str(raw_input("Introduce el caracter que quieres filtrar: "))
        _array_text = text.split(" ")
        _array_token = token.split("|")
        _array_text_filtrado=[]
        _array_token_filtrado=[]
        texto_a_retornar = ""
        if "" in _array_token:
            _array_token.remove("")
        for i,item in enumerate(_array_token):
            if item==character:
                _array_token_filtrado.append(_array_text[i])
                texto_a_retornar = texto_a_retornar + _array_text[i]+" "
        return("Tu nuevo texto es: "+texto_a_retornar)
    except Exception as e:
        return("Opps algo ocurrio intentalo nuevamente")

# print(FiltrarTokens())
