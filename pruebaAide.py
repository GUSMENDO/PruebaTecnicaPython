
import requests
import pandas as pd
import json

#EJERCICIO 1
URL ='https://pokeapi.co/api/v2/pokemon/'
r = requests.get(URL).text

# objeto = json.loads(r)
# print ("Results: " + objeto['results'])


result = r.json()
df = pd.DataFrame(result['results'])
print(df)

# print(dh["results"].head())

# if results:
#      for i in results:
#         name= i['name']
#         url= i['url']
#         print(name + ' ' + url)

df = pd.DataFrame(x)
print(df)

payload = x.json()

results = payload.get('results', [])

if results:
    for i in results:
        name= i['name']
        url= i['url']
        print(name + ' ' + url)

#EJERCICIO 2 

pokemon = input('Ingresa pokemon')
pok = df[df['name']== pokemon]

#EJERCICIO 3 

import pandas as pd

df = pd.read_csv('info.csv')

print(df.shape)
print(df.columns)
print(df.columns.str.lower())


#EJERCICIO 4 

lista = [1,3,5,6,7,8,4,6,7,4]
if lista:
    for i in lista:
        for j in lista:
            if((lista[i] + lista[j]) == 12):
                if(lista[i] != lista[j]):
                    print(str(lista[i]) + ' ' + str(lista[j]) + str(i) +' '+ str(j) )



