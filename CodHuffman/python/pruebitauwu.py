# Código de Huffman en Python José Rodrigo Ávila - Valentina Hernández Pascagaza- Valeria Tavera Gomáz

import math
from collections import Counter

PalabraUsuario=input(" Por favor ingrese un texto de entre 10 y 15 caracteres: ")

if len(PalabraUsuario)>15:
    print("Su palabra tiene más de 15 caracteres")
    PalabraUsuario=input(" Por favor ingrese un texto de entre 10 y 15 caracteres: ")
if len(PalabraUsuario)<10:
    print("Su palabra tiene menos de 10 caracteres")
    PalabraUsuario=input(" Por favor ingrese un texto de entre 10 y 15 caracteres: ")

# Funcion para sacar Probabilidades

def get_probabilities(content):
    content = content.replace(" ","")
    total = len(content)
    c = Counter(content)
    res = {}
    for char,count in c.items():
        res[char] = float(count)/total
    print(res)
    return res

# Funcion para calcular la entropia
def entropia(diccionario):
    Probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        print(probabilidad)
        print(diccionario[probabilidad])
        Probabilidades.append(diccionario[probabilidad])
        print (Probabilidades[cont])
        cont = cont + 1
    print (Probabilidades)
    entropia = 0
    cont = 0
    while  cont < len(Probabilidades):
        operacion = (-Probabilidades[cont]) * (math.log(Probabilidades[cont],2))
        entropia = entropia + operacion
        print (entropia)
        cont = cont + 1    
    return entropia

# Creación de árboles 
class ÁrbolNodos(object):
    def __init__(self, izquierda=None, derecha=None):
        self.izquierda = izquierda
        self.derecha = derecha

    def ramificación(self):
        return (self.izquierda, self.derecha)

    def nodos(self):
        return (self.izquierda, self.derecha)

    def palabra(self):
        return '%s_%s' % (self.izquierda, self.derecha)

# Implementación código de Huffman 
def ÁrbolHuffman(nodo, izquierda=True, binString=''):
    if type(nodo) is str:
        return {nodo: binString}
    (l, r) = nodo.ramificación()
    d = dict()
    d.update(ÁrbolHuffman(l, True, binString + '1'))
    d.update(ÁrbolHuffman(r, False, binString + '0'))
    return d

# Cálculo longitud promedio
def LongitudMinima(diccionario,longitudes):
    Probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        Probabilidades.append(diccionario[probabilidad])
        cont = cont + 1
    longitud = 0
    cont = 0

    while  cont < len(Probabilidades):
        operacion = Probabilidades[cont]*(len(longitudes[cont]))
        longitud = longitud + operacion
        cont = cont + 1
    return longitud

# Cálculo de Frecuencia palabras
freq = {}
for c in PalabraUsuario:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodos = freq

while len(nodos) > 1:
    (key1, c1) = nodos[-1]
    (key2, c2) = nodos[-2]
    nodos = nodos[:-2]
    nodo = ÁrbolNodos(key1, key2)
    nodos.append((nodo, c1 + c2))

    nodos = sorted(nodos, key=lambda x: x[1], reverse=True)

# Se Calcula la eficiencia
def eficiencia(entropias, longitud):
    eficiencias = entropias / longitud
    return eficiencias

# Se Calcula la tasa de compresión
def tasadecompresion(diccionario, longitudes):
    tasa = (math.log(len(diccionario),2)) / longitudes
    return tasa

CódigoHuffman = ÁrbolHuffman(nodos[0][0])
Probabilidades = get_probabilities(PalabraUsuario)
Entropía = entropia(Probabilidades)

print(' Caracter | Código Huffman ')
print('--------------------------')
Longitudes=[]
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, CódigoHuffman[char]))
    Longitudes.append(CódigoHuffman[char])
print('♥')
print('La trama total es:' , (CódigoHuffman))
print('La entropía es :' , Entropía)

Longitud = LongitudMinima(Probabilidades,Longitudes)
Eficiencia = eficiencia(Entropía,Longitud)
Tasa = tasadecompresion(Probabilidades, Longitud)

print('La longitud promedio es: ',Longitud)
print('La Eficiencia es :', Eficiencia)
print("La tasa de compresion es : ", Longitud)