# Código de Huffman en Python José Rodrigo Ávila - Valentina Hernández Pascagaza- Valeria Tavera Goméz
from tkinter import *
from collections import Counter
import math
      
# Funcion para calcular la entropia
def HallarEntropia():
    palabra=PalabraUsuario.get()
    palabra = palabra.replace(" ","")
    total = len(palabra)
    c = Counter(palabra)
    res = {}
    for char,count in c.items():
        res[char] = float(count)/total
    diccionario=res
    Probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        Probabilidades.append(diccionario[probabilidad])
        cont = cont + 1
    entropia = 0
    cont = 0
    while  cont < len(Probabilidades):
        operacion = (-Probabilidades[cont]) * (math.log(Probabilidades[cont],2))
        entropia = entropia + operacion
        cont = cont + 1 
    if len(PalabraUsuario.get())>15:
        LabelPalabraUsuario.configure(text="Su palabra tiene más de 15 caracteres")
        LabelEntropia.configure(text="Se ingreso un texto inválido")
    else:
        if len(PalabraUsuario.get())<10:
            LabelPalabraUsuario.configure(text="Su palabra tiene menos de 10 caracteres")
            LabelEntropia.configure(text="Se ingreso un texto inválido")
        else:
            LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
            TextoEntropia=('La entropía para', palabra ,'es de :', entropia)      
            LabelEntropia.configure(text=TextoEntropia)

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

#Funcion mostrar huffman
def FuncionHuffman():
    freq = {}
    for c in PalabraUsuario.get():
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
    CódigoHuffman = ÁrbolHuffman(nodos[0][0])
    Longitudes=[]
    print('caracter | codigo')
    for (char, frequency) in freq:
        print(' %-4r |%12s' % (char, CódigoHuffman[char]))
        Longitudes.append(CódigoHuffman[char])
    if len(PalabraUsuario.get())>15:
        LabelPalabraUsuario.configure(text="Su palabra tiene más de 15 caracteres")
        LabelTramaTotal.configure(text="Se ingreso un texto inválido")
    else:
        if len(PalabraUsuario.get())<10:
            LabelPalabraUsuario.configure(text="Su palabra tiene menos de 10 caracteres")
            LabelTramaTotal.configure(text="Se ingreso un texto inválido")
        else:
            LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
            TextoTramaTotal=('La trama total de', PalabraUsuario.get(),'es:' , (CódigoHuffman))
            LabelTramaTotal.configure(text=TextoTramaTotal) 

#Funcion Para Hallar Longitud Promedio    
def Longitud():
    freq = {}
    for c in PalabraUsuario.get():
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
    CódigoHuffman = ÁrbolHuffman(nodos[0][0])
    Longitudes=[]
    for (char, frequency) in freq:
        Longitudes.append(CódigoHuffman[char])

    palabra=PalabraUsuario.get()
    palabra = palabra.replace(" ","")
    total = len(palabra)
    c = Counter(palabra)
    res = {}
    for char,count in c.items():
        res[char] = float(count)/total
    diccionario=res
    Probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        Probabilidades.append(diccionario[probabilidad])
        cont = cont + 1
    longitud = 0
    cont = 0
    while  cont < len(Probabilidades):
        operacion = Probabilidades[cont]*(len(Longitudes[cont]))
        longitud = longitud + operacion
        cont = cont + 1
    if len(PalabraUsuario.get())>15:
        LabelPalabraUsuario.configure(text="Su palabra tiene más de 15 caracteres")
        LabelLongitudPromedio.configure(text="Se ingreso un texto inválido")
    else:
        if len(PalabraUsuario.get())<10:
            LabelPalabraUsuario.configure(text="Su palabra tiene menos de 10 caracteres")
            LabelLongitudPromedio.configure(text="Se ingreso un texto inválido")
        else:
            LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
            TextoLongitudPromedio=('La lonigtud promedio para', palabra ,'es de :', longitud)    
            LabelLongitudPromedio.configure(text=TextoLongitudPromedio)
    

#Funcion Hallar Eficiencia   
def eficiencia():
    palabra=PalabraUsuario.get()
    palabra = palabra.replace(" ","")
    total = len(palabra)
    c = Counter(palabra)
    res = {}
    for char,count in c.items():
        res[char] = float(count)/total
    diccionario=res
    Probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        Probabilidades.append(diccionario[probabilidad])
        cont = cont + 1
    entropia = 0
    cont = 0
    while  cont < len(Probabilidades):
        operacion = (-Probabilidades[cont]) * (math.log(Probabilidades[cont],2))
        entropia = entropia + operacion
        cont = cont + 1 

    freq = {}
    for cc in PalabraUsuario.get():
        if cc in freq:
            freq[cc] += 1
        else:
            freq[cc] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodos = freq
    while len(nodos) > 1:
        (key1, c1) = nodos[-1]
        (key2, c2) = nodos[-2]
        nodos = nodos[:-2]
        nodo = ÁrbolNodos(key1, key2)
        nodos.append((nodo, c1 + c2))
        nodos = sorted(nodos, key=lambda x: x[1], reverse=True)
    CódigoHuffman = ÁrbolHuffman(nodos[0][0])
    Longitudes=[]
    for (char, frequency) in freq:
        Longitudes.append(CódigoHuffman[char])

    palabra=PalabraUsuario.get()
    palabra = palabra.replace(" ","")
    total = len(palabra)
    c = Counter(palabra)
    res = {}
    for char,count in c.items():
        res[char] = float(count)/total
    diccionario=res
    Probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        Probabilidades.append(diccionario[probabilidad])
        cont = cont + 1
    longitud = 0
    cont = 0
    while  cont < len(Probabilidades):
        operacion2 = Probabilidades[cont]*(len(Longitudes[cont]))
        longitud = longitud + operacion2
        cont = cont + 1

    eficiencia = entropia / longitud

    if len(PalabraUsuario.get())>15:
        LabelPalabraUsuario.configure(text="Su palabra tiene más de 15 caracteres")
        LabelEficiencia.configure(text="Se ingreso un texto inválido")
    else:
        if len(PalabraUsuario.get())<10:
            LabelPalabraUsuario.configure(text="Su palabra tiene menos de 10 caracteres")
            LabelEficiencia.configure(text="Se ingreso un texto inválido")
        else:
            LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
            TextoMostrarEficiencia = ('La eficiencia de ', PalabraUsuario.get() ,'es de :',eficiencia)
            LabelEficiencia.configure(text=TextoMostrarEficiencia)

#Función Tasa de Compresión

def compresion():
    freq = {}
    for c in PalabraUsuario.get():
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
    CódigoHuffman = ÁrbolHuffman(nodos[0][0])
    Longitudes=[]
    for (char, frequency) in freq:
        Longitudes.append(CódigoHuffman[char])

    palabra=PalabraUsuario.get()
    palabra = palabra.replace(" ","")
    total = len(palabra)
    c = Counter(palabra)
    res = {}
    for char,count in c.items():
        res[char] = float(count)/total
    diccionario=res
    Probabilidades = []
    cont = 0
    for probabilidad in diccionario.keys():
        Probabilidades.append(diccionario[probabilidad])
        cont = cont + 1
    longitud = 0
    cont = 0
    while  cont < len(Probabilidades):
        operacion = Probabilidades[cont]*(len(Longitudes[cont]))
        longitud = longitud + operacion
        cont = cont + 1
        probabilidades = PalabraUsuario.get()
        tasa = (math.log(len(probabilidades),2)) / longitud
        
    if len(PalabraUsuario.get())>15:
        LabelPalabraUsuario.configure(text="Su palabra tiene más de 15 caracteres")
        LabelTasaDeCompresion.configure(text="Se ingreso un texto inválido")
    if len(PalabraUsuario.get())<10:
        LabelPalabraUsuario.configure(text="Su palabra tiene menos de 10 caracteres")
        LabelTasaDeCompresion.configure(text="Se ingreso un texto inválido")
    if len(PalabraUsuario.get())<=14 and len(PalabraUsuario.get()) >= 11:
        LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
        TextoTasaDeCompresion=('La tasa de compresion para ',PalabraUsuario.get() , 'es de :',tasa)
        LabelTasaDeCompresion.configure(text=TextoTasaDeCompresion)

#Creación ventana
ventana=Tk()
ventana.title("Código Huffman")
ventana.geometry('900x800')
TituloInterfaz=Label(ventana, text="Código Huffman", bd=10, fg='black', font=("Helvetica", 16))
TituloInterfaz.grid(row=1, column=2)

PalabraUsuario=StringVar()
LabelPalabraUsuario=Label(ventana, text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
LabelPalabraUsuario.grid(row=2, column=2)
EntradaUsuario=Entry(ventana, textvariable=PalabraUsuario, width=50)
EntradaUsuario.grid(row=3, column=2)

Espacio=Label(ventana)
Espacio.grid(row=5, column=2) 

BotonEntropia=Button(ventana, text="Calcular Entropía", width=25, command=HallarEntropia)
BotonEntropia.grid(row=6, column=0)
LabelEntropia=Label(ventana, text=" ")
LabelEntropia.grid(row=6, column=2)

BotonLongitudPromedio=Button(ventana, text="Calcular Longitud Promedio", width=25,command=Longitud)
BotonLongitudPromedio.grid(row=7, column=0)
LabelLongitudPromedio=Label(ventana, text=" ")
LabelLongitudPromedio.grid(row=7, column=2)

BotonEficiencia=Button(ventana, text="Calcular Eficiencia", width=25, command=eficiencia)
BotonEficiencia.grid(row=8, column=0)
LabelEficiencia=Label(ventana, text=" ")
LabelEficiencia.grid(row=8, column=2)

BotonTasaDeCompresion=Button(ventana, text="Calcular Tasa De Compresion", width=25, command=compresion)
BotonTasaDeCompresion.grid(row=9, column=0)
LabelTasaDeCompresion=Label(ventana, text=" ")
LabelTasaDeCompresion.grid(row=9, column=2)

BotonTablaCodigoHuffman=Button(ventana, text="Mostrar Codigo Huffman", width=25, command=FuncionHuffman)
BotonTablaCodigoHuffman.grid(row=10, column=0)
LabelTramaTotal=Label(ventana, text=" ")
LabelTramaTotal.grid(row=10,column=2)

ventana.mainloop()