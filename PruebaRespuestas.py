#Ejercicio 1
#Obtener la información de la siguiente Api y enlistar los datos en una tabla

#https://pokeapi.co/api/v2/pokemon/

import requests
import pandas as pd

def pokeApiAll():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    resp = requests.get(url)
    jsonResp = resp.json()
    print(jsonResp['results'])
    df = pd.json_normalize(jsonResp['results'])
    return df

pokeApiAll()

#Ejercicio 1.1
#Obtener la información de la siguiente Api y agregar la opción para buscar un pokemon

url = 'https://pokeapi.co/api/v2/pokemon/{pokemon}'

def pokeApiFindPokemon(criterio='pikachu'):
    url = 'https://pokeapi.co/api/v2/pokemon/'+criterio
    resp = requests.get(url)
    jsonResp = resp.json()
    print(jsonResp)
    return jsonResp

# pokeApiFindPokemon()

#Ejercicio 2
"""A través de la lectura del set de datos Data.csv es necesario limpiar y estandarizar  
la información en un nuevo archivo llamado Salida.csv
aplicando las siguientes reglas de limpieza de datos"""

#Reglas de Limpieza
"""Conversión de minusculas a Mayusculas, quitar caracteres especiales, quitar espacios a los costados,
quitar espacios entre renglones,
cambiar el separador de cada columna de un tabulador (\t) por un pipe (|)
"""


def cleanData(Path = 'C:\\Users\\GRMENDOZA\\Documents\\Python\\PruebaTecnica\\',nfile = 'Data.txt'):
    print('Trabajando en %s'%Path)    

    print('Transformando archivos...')
    print('Archivo... '+nfile)
    countrow=0
    fileTemp=open(Path + nfile, 'r')
    fileEnd=open(Path + nfile[:-4] + '.csv', 'w')
    for rowtemp in fileTemp:
        
        countrow+=1
        cleanrow=[]
        tempsplit=rowtemp.split('\t')
        for element in tempsplit[1:]:
            cleanrow.append(element.replace("\t","").replace("\n","").strip(" ").strip('"').upper())
        StrRow="|".join(cleanrow)
        
        if len(StrRow)>1:
            if StrRow[0]=='':
                pass
            else:
                fileEnd.write(StrRow+'\n')
    fileTemp.close()
    fileEnd.close()


#Ejercicio 3
"""Usando la siguiente cadena y patron de token, filtra solo los tokens y texto con el simbolo de +"""

text="GUSTAVO 12324 MENDOZA $#%&$%&$%"
token="|+|^|+|!|"
newText="GUSTAVO MENDOZA"


def parsearToken(text="GUSTAVO 12324 MENDOZA $#%&$%&$%",token="|+|^|+|!|"):
    
    textSplit = text.split(' ')
    tokenSplit = token.strip('|').split('|')
    print(textSplit)
    print(tokenSplit)
    
    if len(textSplit) == len(tokenSplit):
        newList=[]
        for index, token in enumerate(tokenSplit):
            if token == '+':
                # print(index)
                newList.append(textSplit[index])
        
        print(newList)
    
# parsearToken()