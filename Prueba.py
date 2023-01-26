#Ejercicio 1
#Obtener la información de la siguiente Api y enlistar los datos en una tabla

#https://pokeapi.co/api/v2/pokemon/

import requests
import pandas as pd
import openpyxl
import re
class Filtro2:
    def __init__(self):
        self.nombre_archivo = "Data.txt"

    def problema1(self):
        url = "https://pokeapi.co/api/v2/pokemon/"

        respuesta = requests.get(url)

        respuesta =respuesta.json()


        df = pd.DataFrame([[key["name"], key["url"]] for key in respuesta["results"]], columns=['Name', 'Url'])

        print(df)
    def ejercicio11(self,buscar=None):
        self.buscar=buscar
        print('Ejercicio 1.1',"\n")
        #Obtener la información de la siguiente Api y agregar la opción para buscar un pokemon
        #buscar = str(input("dime que pokemon quieres buscar :"))
        url2=f'https://pokeapi.co/api/v2/pokemon/{buscar}'

        respuesta1=requests.get(url2)

        respuesta1=respuesta1.json()

        print(f'la altura de {respuesta1["name"]} es {respuesta1["height"]} y sus movimientos son los siguientes :')

        for x in respuesta1['moves']:
            print("\t","\t","\t","\t",x["move"]["name"])
#ejercicio 2
    def ejercicio2(self):
        wb = openpyxl.Workbook()
        hoja = wb.active
        count = 0
        limpiar = open(self.nombre_archivo)
        datos = []
        for h in limpiar:
            if count>0:
                if len(h)>5:
                    h= h.upper()
                    h = h.replace("\n", "")
                    h = h.replace('"', "")
                    h = h.replace('FEMENINO', "F")
                    datos.append(h.split('\t'))
                    count+=1
            elif count==0:  
                h = h.replace("\n", "")
                h = h.replace('"', "")
                hoja.append(tuple(h.split('\t')))
                count+=1
                try:
                    h = re.sub(r"[^a-zA-Z0-9]","",h)
                except:
                    pass
            else:
                break
        for dato in datos:
            hoja.append(dato)
        wb.save('datos.xlsx')
        #Problema 3

    def ejercicio3(self,text=None):
        self.text = text
        token="|+|^|+|!|"
        
        # try:
        #     text_nuevo = re.sub(token,"", texto)
        #     print(text_nuevo)
        # except:
        #     print(texto)
        #para remplazar los valores y que quede como muestras en el ejemplo seria asi
        try:
            text_nuevo = re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ]+'," ", self.text)
            print(text_nuevo)
        except:
            print(texto)

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

f = Filtro2()

f.problema1()
f.ejercicio11(buscar='raticate')
f.ejercicio2()
f.ejercicio3(text="GUSTAVO 12324 MENDOZA $#%&$%&$%")
