import math
from collections import Counter

diccionarioxd={'j': 0.09090909090909091, 'u': 0.09090909090909091, 'a': 0.18181818181818182, 'n': 0.18181818181818182, 'e': 0.18181818181818182, 's': 0.09090909090909091, 't': 0.09090909090909091, 'b': 0.09090909090909091}
longitudes = ['1001', '1000', '111', '110', '011', '101', '010', '001', '000']

def entropia(diccionario):
    probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        print(probabilidad)
        print(diccionario[probabilidad])

        probabilidades.append(diccionario[probabilidad])

        print (probabilidades[cont])
        cont = cont + 1
    print (probabilidades)
    entropia = 0
    cont = 0
    while  cont < len(probabilidades):
        operacion = (-probabilidades[cont]) * (math.log(probabilidades[cont],2))
        entropia = entropia + operacion
        print (entropia)
        cont = cont + 1    
    return entropia

entropias = entropia(diccionarioxd)

print("esta es la entropia: ", entropias)

def LongitudMinima(diccionario,longitudes):
    probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        print(probabilidad)
        print(diccionario[probabilidad])

        probabilidades.append(diccionario[probabilidad])

        print (probabilidades[cont])
        cont = cont + 1
    print (probabilidades)
    longitud = 0
    cont = 0

    print('len del diccionario: ', len(diccionarioxd))

    while  cont < len(probabilidades):


        operacion = probabilidades[cont]*(len(longitudes[cont]))
        longitud = longitud + operacion
        print (longitud)
        cont = cont + 1

    return longitud


longitud = LongitudMinima(diccionarioxd, longitudes)
print("esta es la longitud promedio: ", longitud)

def eficiencia(entropias, longitud):
    eficiencias = entropias / longitud
    return eficiencias

eficiencias = eficiencia(entropias, longitud)
print("esta es la eficiencia: ", eficiencias)

def tasadecompresion(diccionarioxd, longitudes):
    tasa = (math.log(len(diccionarioxd),2)) / longitudes
    return tasa

tasa = tasadecompresion(diccionarioxd, longitud)
print("esta es la tasa de compresion: ", tasa)
