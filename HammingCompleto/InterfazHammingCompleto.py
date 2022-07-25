#Codificación Hamming Completa (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)

from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import numpy as np
import random
from typing import TextIO
from tkinter import scrolledtext
from collections import Counter
import pyperclip as clipboard
import operator
import math
import re
import sys

#Funcion Codificacion Huffman
def CodificacionHuffman(): 
    ventana.withdraw()
    # Funcion para calcular la entropia
    def HallarEntropia():
        palabra=PalabraUsuario1.get()
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
        if len(PalabraUsuario1.get())>15:
            LabelPalabraUsuario1.configure(text="Su palabra tiene más de 15 caracteres")
            LabelEntropia1.configure(text="Se ingreso un texto inválido")
        else:
            if len(PalabraUsuario1.get())<10:
                LabelPalabraUsuario1.configure(text="Su palabra tiene menos de 10 caracteres")
                LabelEntropia1.configure(text="Se ingreso un texto inválido")
            else:
                LabelPalabraUsuario1.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
                TextoEntropia=('La entropía para', palabra ,'es de :', entropia)      
                LabelEntropia1.configure(text=TextoEntropia)

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
        for c in PalabraUsuario1.get():
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
        TramaFinal=""
        TramaFinal=TramaFinal.join(Longitudes)
        TramaFinal=TramaFinal.replace(" ", "")

        if len(PalabraUsuario1.get())>15:
            LabelPalabraUsuario1.configure(text="Su palabra tiene más de 15 caracteres")
            LabelTramaTotal1.configure(text="Se ingreso un texto inválido")
        else:
            if len(PalabraUsuario1.get())<10:
                LabelPalabraUsuario1.configure(text="Su palabra tiene menos de 10 caracteres")
                LabelTramaTotal1.configure(text="Se ingreso un texto inválido")
            else:
                LabelPalabraUsuario1.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
                TextoTramaTotal=('La trama total de', PalabraUsuario1.get(),'es:' , (CódigoHuffman))
                TextoGuardarTramaTotal=(Longitudes)
                LabelGuardarTramaTotal1.configure(text=TextoGuardarTramaTotal)
                LabelTramaTotal1.configure(text=TextoTramaTotal) 

    #Funcion Para Hallar Longitud Promedio    
    def Longitud():
        freq = {}
        for c in PalabraUsuario1.get():
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

        palabra=PalabraUsuario1.get()
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
        if len(PalabraUsuario1.get())>15:
            LabelPalabraUsuario1.configure(text="Su palabra tiene más de 15 caracteres")
            LabelLongitudPromedio1.configure(text="Se ingreso un texto inválido")
        else:
            if len(PalabraUsuario1.get())<10:
                LabelPalabraUsuario1.configure(text="Su palabra tiene menos de 10 caracteres")
                LabelLongitudPromedio1.configure(text="Se ingreso un texto inválido")
            else:
                LabelPalabraUsuario1.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
                TextoLongitudPromedio=('La lonigtud promedio para', palabra ,'es de :', longitud)    
                LabelLongitudPromedio1.configure(text=TextoLongitudPromedio)  

    #Funcion Hallar Eficiencia   
    def eficiencia():
        palabra=PalabraUsuario1.get()
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
        for cc in PalabraUsuario1.get():
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

        palabra=PalabraUsuario1.get()
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

        if len(PalabraUsuario1.get())>15:
            LabelPalabraUsuario1.configure(text="Su palabra tiene más de 15 caracteres")
            LabelEficiencia1.configure(text="Se ingreso un texto inválido")
        else:
            if len(PalabraUsuario1.get())<10:
                LabelPalabraUsuario1.configure(text="Su palabra tiene menos de 10 caracteres")
                LabelEficiencia1.configure(text="Se ingreso un texto inválido")
            else:
                LabelPalabraUsuario1.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
                TextoMostrarEficiencia = ('La eficiencia de ', PalabraUsuario1.get() ,'es de :',eficiencia)
                LabelEficiencia1.configure(text=TextoMostrarEficiencia)

    #Función Tasa de Compresión
    def compresion():
        freq = {}
        for c in PalabraUsuario1.get():
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

        palabra=PalabraUsuario1.get()
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
            probabilidades = PalabraUsuario1.get()
            tasa = (math.log(len(probabilidades),2)) / longitud
            
        if len(PalabraUsuario1.get())>15:
            LabelPalabraUsuario1.configure(text="Su palabra tiene más de 15 caracteres")
            LabelTasaDeCompresion1.configure(text="Se ingreso un texto inválido")
        if len(PalabraUsuario1.get())<10:
            LabelPalabraUsuario1.configure(text="Su palabra tiene menos de 10 caracteres")
            LabelTasaDeCompresion1.configure(text="Se ingreso un texto inválido")
        if len(PalabraUsuario1.get())<=14 and len(PalabraUsuario1.get()) >= 11:
            LabelPalabraUsuario1.configure(text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
            TextoTasaDeCompresion=('La tasa de compresion para ',PalabraUsuario1.get() , 'es de :',tasa)
            LabelTasaDeCompresion1.configure(text=TextoTasaDeCompresion)   
    
    #Funcion Guardar Trama
    def Guardar():
        TextoTrama=LabelGuardarTramaTotal1.cget("text")
        TextoTrama=TextoTrama.replace(" ", "")
        clipboard.copy(TextoTrama)

    #Funcion Volver    
    def Volver():
        VentanaCodificacionHuffman.destroy()
        ventana.deiconify()

    #Creación ventana
    VentanaCodificacionHuffman=Toplevel()
    VentanaCodificacionHuffman.title("Código Huffman")
    VentanaCodificacionHuffman.geometry('900x400')
    TituloInterfaz1=Label(VentanaCodificacionHuffman, text="Código Huffman", bd=10, fg='black', font=("Helvetica", 16))
    TituloInterfaz1.grid(row=1, column=2)

    PalabraUsuario1=StringVar()
    LabelPalabraUsuario1=Label(VentanaCodificacionHuffman, text="Por favor ingrese un texto de entre 10 y 15 caracteres :")
    LabelPalabraUsuario1.grid(row=2, column=2)
    EntradaUsuario1=Entry(VentanaCodificacionHuffman, textvariable=PalabraUsuario1, width=50)
    EntradaUsuario1.grid(row=3, column=2)

    Espacio1=Label(VentanaCodificacionHuffman)
    Espacio1.grid(row=5, column=2) 

    BotonEntropia1=Button(VentanaCodificacionHuffman, text="Calcular Entropía", width=25, command=HallarEntropia)
    BotonEntropia1.grid(row=6, column=0)
    LabelEntropia1=Label(VentanaCodificacionHuffman, text=" ")
    LabelEntropia1.grid(row=6, column=2)

    BotonLongitudPromedio1=Button(VentanaCodificacionHuffman, text="Calcular Longitud Promedio", width=25,command=Longitud)
    BotonLongitudPromedio1.grid(row=7, column=0)
    LabelLongitudPromedio1=Label(VentanaCodificacionHuffman, text=" ")
    LabelLongitudPromedio1.grid(row=7, column=2)

    BotonEficiencia1=Button(VentanaCodificacionHuffman, text="Calcular Eficiencia", width=25, command=eficiencia)
    BotonEficiencia1.grid(row=8, column=0)
    LabelEficiencia1=Label(VentanaCodificacionHuffman, text=" ")
    LabelEficiencia1.grid(row=8, column=2)

    BotonTasaDeCompresion1=Button(VentanaCodificacionHuffman, text="Calcular Tasa De Compresion", width=25, command=compresion)
    BotonTasaDeCompresion1.grid(row=9, column=0)
    LabelTasaDeCompresion1=Label(VentanaCodificacionHuffman, text=" ")
    LabelTasaDeCompresion1.grid(row=9, column=2)

    BotonTablaCodigoHuffman1=Button(VentanaCodificacionHuffman, text="Mostrar Codigo Huffman", width=25, command=FuncionHuffman)
    BotonTablaCodigoHuffman1.grid(row=10, column=0)
    LabelTramaTotal1=Label(VentanaCodificacionHuffman, text=" ")
    LabelTramaTotal1.grid(row=10,column=2)

    BotonGuardar1=Button(VentanaCodificacionHuffman, text="Guardar Trama Final", width=25, command=Guardar)
    BotonGuardar1.grid(row=11, column=0)
    LabelGuardarTramaTotal1=Label(VentanaCodificacionHuffman, text=" ") 
    LabelGuardarTramaTotal1.grid(row=12, column=2)

    BotonVolver1=Button(VentanaCodificacionHuffman, text="Regresar", width=25, command=Volver)
    BotonVolver1.grid(row=13, column=0)

    VentanaCodificacionHuffman.mainloop()

#Funcion CodificacionShannonFano
def CodificacionShannonFano():
    ventana.withdraw()
    def DiccionarioPalabra(palabra):
        caracteres=list(palabra)
        diccionario={}
        for caracter in range(len(caracteres)):
            diccionario[palabra[caracter]]=0
        return diccionario

    #Sacar frecuencias
    def Frecuencias(mensaje):
        palabra=mensaje
        palabra = palabra.replace(" ","")
        total = len(palabra)
        c = Counter(palabra)
        res = {}
        for char,count in c.items():
            res[char] = float(count)/total
        return res

    #Ordenamiento por orden de aparición (mayor a menor)
    def OrdenarFrecuenciasAparicion(diccionario):
        frecuencias=list(diccionario) 
        OrdenAparicion={}
        for posicion in range(len(frecuencias)):
            repeticiones=0
            for caracter in range(len(frecuencias)):
                if frecuencias[posicion] == frecuencias[caracter]:
                    repeticiones=repeticiones+1
                else:
                    repeticiones=repeticiones
            OrdenAparicion[frecuencias[posicion]]=repeticiones 
        OrdenAparicion = sorted(OrdenAparicion.items() , key=operator.itemgetter(1), reverse=True)  
        return OrdenAparicion

    #Ordenamiento por orden de aparicion inverso (menor a mayor)
    def OrdenarFrecuenciasAparicionInverso(diccionario):
        frecuencias=diccionario 
        OrdenAparicionInverso={}
        for posicion in range(len(frecuencias)):
            repeticiones=0
            for caracter in range(len(frecuencias)):
                if frecuencias[posicion] == frecuencias[caracter]:
                    repeticiones=repeticiones+1
                else:
                    repeticiones=repeticiones
            OrdenAparicionInverso[frecuencias[posicion]]=repeticiones
        OrdenAparicionInverso = sorted(OrdenAparicionInverso.items() , key=operator.itemgetter(1)) 
        return OrdenAparicionInverso

    #Ordenamiento por orden alfabético (a-z)
    def OrdenarFrecuenciasAlfabetico(diccionario):
        frecuencias=diccionario
        OrdenAlfabetico={}
        for posicion in range(len(frecuencias)):
            repeticiones=0
            for caracter in range(len(frecuencias)):
                if frecuencias[posicion] == frecuencias[caracter]:
                    repeticiones=repeticiones+1
                else:
                    repeticiones=repeticiones
            OrdenAlfabetico[frecuencias[posicion]]=repeticiones
        OrdenAlfabetico = sorted(OrdenAlfabetico.items() , key=operator.itemgetter(0))
        return OrdenAlfabetico

    #Ordenamiento por orden alfabético inverso (z-a)
    def OrdenarFrecuenciasAlfabeticoInverso(diccionario):
        frecuencias=diccionario
        OrdenAlfabeticoInverso={}
        for posicion in range(len(frecuencias)):
            repeticiones=0
            for caracter in range(len(frecuencias)):
                if frecuencias[posicion] == frecuencias[caracter]:
                    repeticiones=repeticiones+1
                else:
                    repeticiones=repeticiones
            OrdenAlfabeticoInverso[frecuencias[posicion]]=repeticiones
        OrdenAlfabeticoInverso = sorted(OrdenAlfabeticoInverso.items() , key=operator.itemgetter(0), reverse=True)
        return OrdenAlfabeticoInverso

    #Funcion Para Hallar Entropia
    def entropia(diccionario):
        probabilidades = []
        cont = 0
        for probabilidad in diccionario.keys():    
            probabilidades.append(diccionario[probabilidad])
            cont = cont + 1
        entropia = 0
        cont = 0
        while  cont < len(probabilidades):
            operacion = (-probabilidades[cont]) * (math.log(probabilidades[cont],2))
            entropia = entropia + operacion
            cont = cont + 1    
        return entropia

    #Funcion Para Hallar Longitud Promedio    
    def LongitudPromedio(diccionario,frecuencias):
        i=0
        h=list(frecuencias)
        r=list(diccionario)
        sumatoria=0
        while i<len(frecuencias):        
            bits=(len(frecuencias[h[i]]))
            longitud=diccionario[r[i]]*(bits)
            sumatoria=sumatoria+longitud
            i=i+1
        TextoLabelLongitudPromedio=('La longitud promedio de', sumatoria)
        LabelLongitudPromedio2.configure(text=TextoLabelLongitudPromedio)
        return(sumatoria)

    #Funcion Longitud Minima
    def longitu_minima(prob):
        i=0
        h=list(prob)
        long = []
        dictlong={}
        while i<len(prob):
            long.append(math.log(prob[h[i]],2)*-1)
            i=i+1
        i=0
        while i<len(prob):
            dictlong[h[i]] = long[i]
            i=i+1
        return dictlong

    #Funcion Eficiencia
    def Eficiencia(entropias, longitudMinima):
        eficiencias = entropias / longitudMinima
        return eficiencias
        
    #Funcion Tasa Compresion
    def TasaDeCompresion(longitudpromedio,palabra):
        content = palabra.replace(" ","")
        c = Counter(content)
        unicos=0
        for char,count in c.items():
            if count==1:
                unicos=unicos+1   
        if unicos==0:
            unicos=0
        elif unicos>0:
            unicos=(math.log(unicos,2))/longitudpromedio
        return unicos

    #Funcion para hallar punto medio
    def ObtenerMitadFrecuencia(a_dict):
        diccionario=dict(a_dict)
        Mitad=(sum(diccionario.values())/2)
        suma=0
        suma_anterior=0
        last_key=0
        i=1
        for key in diccionario:
            suma_anterior=suma
            suma=suma+diccionario[key]
            if(suma >= Mitad):
                if abs(suma_anterior-Mitad) < abs(suma-Mitad):
                    return last_key
                else:
                    return key
            last_key=key
            i=i+1

    #FuncionCodificarDiccionario
    def Codificador(key_mitad,contenedor,diccionario):
        digito=0
        if len(diccionario)>1:
            for key in dict(diccionario):
                contenedor[key]=(str(contenedor[key])+str(digito))
                if key == key_mitad:
                    digito=1    
        return contenedor

    #Funcion dividir arreglo por mitades
    def PartirDiccionnario(diccionario,key_mitad):
        n1={}
        n2={}
        dictionary=dict(diccionario)
        selector=0
        for i in range(len(dictionary)):
            if str(list(dictionary.items())[i][0])==str(key_mitad):
                selector=i        
        n1=dict(list(dictionary.items())[0:selector+1])
        n2=dict(list(dictionary.items())[selector+1:len(dictionary)])        
        return [n1,n2]

    #Funcion ajustar contenidos
    def AjustarPalabra(content):
        for key in content:
            content[key]=str(list(content[key])[1:len(list(content))])
        return content

    #Verificador
    def VerificarPalabra(palabra):
        lista=list(palabra)
        lista_inversa=lista[::-1]
        if lista==lista_inversa:
            return True
        else:
            return False

    #"Funcion generar valores"
    def ShannonFano():
        palabra=PalabraUsuario2.get()
        Shan={}
        print(palabra)
        while VerificarPalabra(palabra) == False:
            LabelPalabraUsuario2.configure(text="Su palabra no es palindroma")     
        Ordenado=OrdenarFrecuenciasAparicion(palabra)
        Directorio=[dict(Ordenado)] 
        FrecuenciasPalabra=DiccionarioPalabra(palabra)  
        
        i=0
        while len(Directorio) < (len(palabra)*3):
            Directorio[i]=sorted(Directorio[i].items(),key=operator.itemgetter(1), reverse=True)
            Mitad=ObtenerMitadFrecuencia(Directorio[i])
            FrecuenciasPalabra=Codificador(Mitad,FrecuenciasPalabra,Directorio[i])
            DirectorioDividido=PartirDiccionnario(Directorio[i],Mitad)
            Directorio.append(dict(DirectorioDividido[0]))
            Directorio.append(dict(DirectorioDividido[1]))
            i=i+1
        Shan=AjustarPalabra(FrecuenciasPalabra)
        TramaTotal2=Shan.values()
        ListaTramaTotal2=list(TramaTotal2)
        TramaTotal2men=""
        TramaTotal2men=TramaTotal2men.join(ListaTramaTotal2)
        print(TramaTotal2men)
        Entro=entropia(Frecuencias(PalabraUsuario2.get()))
        TextoLabelEntropia=('La Entropia de', PalabraUsuario2.get(), 'es:', Entro)
        LabelEntropia2.configure(text=TextoLabelEntropia)
        LPromedio=LongitudPromedio(Frecuencias(PalabraUsuario2.get()),FrecuenciasPalabra)
        TasaComp=TasaDeCompresion(LPromedio,palabra)
        TextoLabelTasaCompresion=('La tasa de compresion de ', PalabraUsuario2.get() , 'es', TasaComp)
        LabelTasaDeCompresion2.configure(text=TextoLabelTasaCompresion)
        TextoLabelLongitudPromedio=('La longitud promedio de',PalabraUsuario2.get() ,'es', LPromedio)
        LabelLongitudPromedio2.configure(text=TextoLabelLongitudPromedio)
        TextoLabelTramaTotal=("La trama total de", PalabraUsuario2.get() ," es : " , Shan)
        TextoLabelTramaTotal2=(TramaTotal2men)
        LabelGuardarTramaTotal2.configure(text=TramaTotal2men)
        LabelTramaTotal2.configure(text=TextoLabelTramaTotal)

    #Funcion Guardar Trama
    def Guardar():
        TextoTrama=LabelGuardarTramaTotal2.cget("text")
        TextoTrama=TextoTrama.replace(" ", "")
        characters = "][',"
        for x in range(len(characters)):
            TextoTrama = TextoTrama.replace(characters[x],"")
        clipboard.copy(TextoTrama)

    #Funcion Volver    
    def Volver():
        VentanaShannonFano.destroy()
        ventana.deiconify()

    #Creación ventana
    VentanaShannonFano=Toplevel()
    VentanaShannonFano.title("Código Shannon Fano")
    VentanaShannonFano.geometry('900x400')
    TituloInterfaz2=Label(VentanaShannonFano, text="Código Shannon Fano", bd=10, fg='black', font=("Helvetica", 16))
    TituloInterfaz2.grid(row=1, column=2)

    PalabraUsuario2=StringVar()
    LabelPalabraUsuario2=Label(VentanaShannonFano, text="Por favor ingrese un texto de entre palindromo de hasta 25 caracteres :")
    LabelPalabraUsuario2.grid(row=2, column=2)
    EntradaUsuario2=Entry(VentanaShannonFano, textvariable=PalabraUsuario2, width=50)
    EntradaUsuario2.grid(row=3, column=2)

    Espacio2=Label(VentanaShannonFano)
    Espacio2.grid(row=5, column=2) 

    LabelEntropia2=Label(VentanaShannonFano, text=" ")
    LabelEntropia2.grid(row=6, column=2)

    LabelLongitudPromedio2=Label(VentanaShannonFano, text=" ")
    LabelLongitudPromedio2.grid(row=7, column=2)

    LabelTasaDeCompresion2=Label(VentanaShannonFano, text=" ")
    LabelTasaDeCompresion2.grid(row=9, column=2)

    BotonTablaCodigoHuffman2=Button(VentanaShannonFano, text="Mostrar Shannon Fano", width=25, command=ShannonFano)
    BotonTablaCodigoHuffman2.grid(row=11, column=2)
    LabelTramaTotal2=Label(VentanaShannonFano, text=" ")
    LabelTramaTotal2.grid(row=10,column=2)

    BotonGuardar2=Button(VentanaShannonFano, text="Guardar Trama Final", width=25, command=Guardar)
    BotonGuardar2.grid(row=12, column=2)
    LabelGuardarTramaTotal2=Label(VentanaShannonFano, text=" ") 
    LabelGuardarTramaTotal2.grid(row=13, column=2)

    BotonVolver2=Button(VentanaShannonFano, text="Regresar", width=25, command=Volver)
    BotonVolver2.grid(row=14, column=2)

    VentanaShannonFano.mainloop()

#Funcion CodificacionAritmetica
def CodificacionAritmetica():
    ventana.withdraw()
    #Funcion verificación palabra
    def VerificarPalabra():
        a=1
        palabra=PalabraUsuario3.get()
        len1=len(palabra)
        if(len1<5):
            LabelPalabraUsuario3.configure(text="Su palabra es de menos de 5 caracteres")
            a=1
        elif(len1>10):
            LabelPalabraUsuario3.configure(text="Su palabra es de más de 10 caracteres")
            a=1
        else:
            for i in range(len(palabra)):
                if(palabra[i]=="a" or palabra[i]=="s" or palabra[i]=="m" or palabra[i]=="e" or palabra[i]=="l"):            
                    LabelPalabraUsuario3.configure(text="Por favor ingrese un texto de entre 5 y 10 caracteres usando solo a, s, m, e y l:")
                    a=0
                else:
                    LabelPalabraUsuario3.configure(text="Su palabra tiene caracteres no permitidos")
                    a=1
        return a

    #Mensaje en diccionario
    def DiccionarioPalabra(palabra):
        caracteres=list(palabra)
        diccionario={}
        for caracter in range(len(caracteres)):
            diccionario[palabra[caracter]]=0
        return diccionario

    #Ordenamiento por orden de aparición (mayor a menor)
    def OrdenarFrecuenciasAparicion(diccionario):
        frecuencias=list(diccionario) 
        OrdenAparicion={}
        for posicion in range(len(frecuencias)):
            repeticiones=0
            for caracter in range(len(frecuencias)):
                if frecuencias[posicion] == frecuencias[caracter]:
                    repeticiones=repeticiones+1
                else:
                    repeticiones=repeticiones
            OrdenAparicion[frecuencias[posicion]]=repeticiones 
        return OrdenAparicion

    #Probabilidades por letra
    def Aritmetica():
        a=VerificarPalabra()
        if(a==1):
            LabelTramaTotal3.configure(text="La palabra ingresada no es valida")
        elif(a==0):
            mensaje=PalabraUsuario3.get()
            palabra=mensaje
            patron = r'(\w)'
            mensaje = re.sub(patron, r'\1 ', mensaje)
            mensaje = mensaje.lower() 
            listaPalabras = mensaje.split()
            frecuenciaPalabra = []
            for w in listaPalabras:
                frecuenciaPalabra.append(listaPalabras.count(w))   

            TextoLabelA=("Probabilidad a : ",ProbabilidadA3.get())
            TextoLabelS=("Probabilidad s : ",ProbabilidadS3.get())
            TextoLabelM=("Probabilidad m : ",ProbabilidadM3.get())
            TextoLabelE=("Probabilidad e : ",ProbabilidadE3.get())
            TextoLabelL=("Probabilidad l : ",ProbabilidadL3.get())
            LabelA3.configure(text=TextoLabelA)
            LabelS3.configure(text=TextoLabelS)
            LabelM3.configure(text=TextoLabelM)
            LabelE3.configure(text=TextoLabelE)
            LabelL3.configure(text=TextoLabelL)        
        
            Pri=mensaje[0]
            Seg=mensaje[1]
            Ter=mensaje[2]
            Cuar=mensaje[3]
            Quin=mensaje[4]
            Sex=mensaje[5]
            Sep=mensaje[6]
            Oct=mensaje[7]
            Nov=mensaje[8]
            Dec=mensaje[9]
            
            P1=float(ProbabilidadA3.get())
            P2=float(ProbabilidadS3.get())
            P3=float(ProbabilidadM3.get())
            P4=float(ProbabilidadE3.get())
            P5=float(ProbabilidadL3.get())

            PT=P1+P2+P3+P4+P5
            b=1
            if(PT!=1):
                Espacio13.configure(text="la suma de las probabilidades no es de 1")
                b=1
            else:
                Espacio13.configure(text="La suma de las probabilidades es de 1")
                b=0
            if(b==0):
                Minimos=[0,P1,P1+P2,P1+P2+P3,P1+P2+P3+P4]
                Maximos=[P1,P1+P2,P1+P2+P3,P1+P2+P3+P4,P1+P2+P3+P4+P5]
                AMinimo=0
                AMaximo=1
                NuevoMinimo=0
                NuevoMaximo=0
                CodificacionMin=list()
                CodificacionMax=list()
                ValoresMinimos=list()
                ValoresMaximos=list()
                lim=1

                for i in range(len(listaPalabras)):               
                    if(listaPalabras[i]=="a"):
                        NuevoMaximo=NuevoMaximo+P1
                        NuevoMinimo=NuevoMaximo-P1
                    if(listaPalabras[i]=="s"):
                        NuevoMaximo=NuevoMaximo+P2
                        NuevoMinimo=NuevoMaximo-P2
                    if(listaPalabras[i]=="m"): 
                        NuevoMaximo=NuevoMaximo+P3
                        NuevoMinimo=NuevoMaximo-P3
                    if(listaPalabras[i]=="e"):
                        NuevoMaximo=NuevoMaximo+P4
                        NuevoMinimo=NuevoMaximo-P4
                    if(listaPalabras[i]=="l"):   
                        NuevoMaximo=NuevoMaximo+P5 
                        NuevoMinimo=NuevoMaximo-P5        
                    
                    CodificacionMin.append("Min"+str(lim))
                    CodificacionMax.append("Max"+str(lim))
                    lim=lim+1
                    Inferior=AMinimo+((AMaximo-AMinimo)*NuevoMinimo)
                    Superior=AMinimo+((AMaximo-AMinimo)*NuevoMaximo)
                    AMinimo=Inferior
                    AMaximo=Superior
                    if(Superior==1):
                        i=10
                    ValoresMinimos.append(Inferior)
                    ValoresMaximos.append(Superior)
                    CodificacionMin.append(Inferior)
                    CodificacionMax.append(Superior)
                    
                ValorDecoMin=ValoresMinimos[-1]
                ValorDecimal=ValorDecoMin
                ValorDecoMax=ValoresMaximos[-1]
                num=0
                ValoresDeco=list()
                ValoresDeco2=list()
                ValoresDeco.append("A"+str(num))
                ValoresDeco2.append("A"+str(num))        
                ValoresDeco.append(ValorDecoMin)        
                ValoresDeco2.append(ValorDecoMin)
                num=1     

                M1=0
                M2=P1
                M3=P1+P2
                M4=P1+P2+P3
                M5=P1+P2+P3+P4
                M6=P1+P2+P3+P4+P5  

                for i in range(len(palabra)):
                    count=0
                    count2=0            
                    for n in range(len(Maximos)):
                        if (M2 >= ValorDecoMin) and (count==0):
                            Limite = M2
                            count=count+1
                        if (M3 >= ValorDecoMin) and (count==0):
                            Limite = M3
                            count=count+1
                        if (M4 >= ValorDecoMin) and (count==0):
                            Limite = M4
                            count=count+1 
                        if (M5 >= ValorDecoMin) and (count==0):
                            Limite = M5
                            count=count+1
                        if (M6 >= ValorDecoMin) and (count==0):
                            Limite = M6
                            count=count+1

                    for n in range(len(Minimos)):
                        if (M1 >= ValorDecoMin) and (count2==0):
                            Limite2=M1
                            count2=count2+1
                        if (M2 >= ValorDecoMin) and (count2==0):
                            Limite2 = M1
                            count2=count2+1
                        if (M3 >= ValorDecoMin) and (count2==0):
                            Limite2 = M2
                            count2=count2+1
                        if (M4 >= ValorDecoMin) and (count2==0):
                            Limite2 = M3
                            count2=count2+1
                        if (M5 >= ValorDecoMin) and (count2==0):
                            Limite2 = M4
                            count2=count2+1
                        if (M6 >= ValorDecoMin) and (count2==0):
                            Limite2 = M5
                            count2=count2+1

                    ValoresDeco.append("A"+str(num))
                    ValoresDeco2.append("A"+str(num))
                    An=(ValorDecoMax-Limite2)/(Limite-Limite2)
                    ValorDecoMax=An      
                    ValorDecoMin=ValorDecoMax
                    num=num+1
                    ValoresDeco.append(An)
                    ValoresDeco2.append(An)    
                ValoresDeco2.pop(-1) 
                ValoresDeco2.pop(-1)
                TextoLabelCodificacion=("Los minimos en la codificacion de su palabra son : ", CodificacionMin)
                LabelTramaTotalCodificacion3.configure(text=TextoLabelCodificacion)    
                TextoLabelCodificacion2=("Los maximos en la codificacion de su palabra son : ", CodificacionMax)
                LabelTramaTotalCodificacion23.configure(text=TextoLabelCodificacion2)  
                TextoLabelTramaTotal=("La decodificacion de su palabra es : ", ValoresDeco2)
                LabelTramaTotal3.configure(text=TextoLabelTramaTotal)

                Decimal=ValorDecimal
                potencia=0
                Multiplicacion=0
                Entero=0
                Suma=0
                TramaBinaria=list()
                n=abs(ValorDecimal) - abs(int(ValorDecimal))
                rn=len(str(n))
                contadorcito=0
                while contadorcito != rn:                
                    Multiplicacion=(Decimal*2) 
                    Entero=int(Multiplicacion)
                    Decimal=(Multiplicacion-Entero)
                    TramaBinaria.append(Entero)                             
                    potencia=(potencia-1)
                    Validacion=pow(2,potencia)
                    Numform=Entero*Validacion
                    Suma=Numform+Suma
                    contadorcito=contadorcito+1
                TextoLabelTramaBinaria=("El codigo Binario De Su Palabra es : ", TramaBinaria)
                LabelGuardarTramaTotal3.configure(text=TramaBinaria)
                LabelMostrarBinario3.configure(text=TextoLabelTramaBinaria)
            else:
                LabelTramaTotal3.configure(text=" error ")
                LabelTramaTotalCodificacion3.configure(text=" error ")
                LabelTramaTotalCodificacion23.configure(text=" error ")
                LabelMostrarBinario3.configure(text=" error ")

    #Funcion Guardar Trama
    def Guardar():
        TextoTrama=LabelGuardarTramaTotal3.cget("text")
        TextoTrama=TextoTrama.replace(" ", "")
        characters = "][',"
        for x in range(len(characters)):
            TextoTrama = TextoTrama.replace(characters[x],"")
        clipboard.copy(TextoTrama)

    #Funcion Volver    
    def Volver():
        VentanaCodificacionAritmetica.destroy()
        ventana.deiconify()

    #Creación ventana
    VentanaCodificacionAritmetica=Toplevel()
    VentanaCodificacionAritmetica.title("Codificación Aritmetica")
    VentanaCodificacionAritmetica.geometry('1250x560')
    TituloInterfaz3=Label(VentanaCodificacionAritmetica, text="Codificación Aritmetica", bd=10, fg='black', font=("Helvetica", 16))
    TituloInterfaz3.grid(row=1, column=2)

    PalabraUsuario3=StringVar()
    LabelPalabraUsuario3=Label(VentanaCodificacionAritmetica, text="Por favor ingrese un texto de entre 5 y 10 caracteres usando solo a, s, m, e y l:")
    LabelPalabraUsuario3.grid(row=2, column=2)
    EntradaUsuario3=Entry(VentanaCodificacionAritmetica, textvariable=PalabraUsuario3, width=50)
    EntradaUsuario3.grid(row=3, column=2)

    Espacio3=Label(VentanaCodificacionAritmetica, text=" Ingrese las probabilidades en decimales para cada letra ")
    Espacio3.grid(row=4, column=2) 

    Espacio13=Label(VentanaCodificacionAritmetica, text=" la suma de las 5 probabilidades debe ser de 1 ")
    Espacio13.grid(row=5, column=2)

    ProbabilidadA3=StringVar()
    LabelA3=Label(VentanaCodificacionAritmetica, text=" Probabilidad a : ")
    LabelA3.grid(row=6, column=1)
    EntradaUsuarioPA3=Entry(VentanaCodificacionAritmetica, textvariable=ProbabilidadA3, width=10)
    EntradaUsuarioPA3.grid(row=6, column=2)

    ProbabilidadS3=StringVar()
    LabelS3=Label(VentanaCodificacionAritmetica, text=" Probabilidad s : ")
    LabelS3.grid(row=7, column=1)
    EntradaUsuarioPS3=Entry(VentanaCodificacionAritmetica, textvariable=ProbabilidadS3, width=10)
    EntradaUsuarioPS3.grid(row=7, column=2)

    ProbabilidadM3=StringVar()
    LabelM3=Label(VentanaCodificacionAritmetica, text=" Probabilidad m : ")
    LabelM3.grid(row=8, column=1)
    EntradaUsuarioPM3=Entry(VentanaCodificacionAritmetica, textvariable=ProbabilidadM3, width=10)
    EntradaUsuarioPM3.grid(row=8, column=2)

    ProbabilidadE3=StringVar()
    LabelE3=Label(VentanaCodificacionAritmetica, text=" Probabilidad e : ")
    LabelE3.grid(row=9, column=1)
    EntradaUsuarioPE3=Entry(VentanaCodificacionAritmetica, textvariable=ProbabilidadE3, width=10)
    EntradaUsuarioPE3.grid(row=9, column=2)

    ProbabilidadL3=StringVar()
    LabelL3=Label(VentanaCodificacionAritmetica, text=" Probabilidad l : ")
    LabelL3.grid(row=10, column=1)
    EntradaUsuarioPL3=Entry(VentanaCodificacionAritmetica, textvariable=ProbabilidadL3, width=10)
    EntradaUsuarioPL3.grid(row=10, column=2)

    Espacio23=Label(VentanaCodificacionAritmetica)
    Espacio23.grid(row=11, column=2) 

    LabelCodificacion3=Label(VentanaCodificacionAritmetica, text=" Codificacion Limites Minimos ")
    LabelCodificacion3.grid(row=13,column=1)
    LabelTramaTotalCodificacion3=Label(VentanaCodificacionAritmetica, text=" ")
    LabelTramaTotalCodificacion3.grid(row=13,column=2)

    LabelCodificacion23=Label(VentanaCodificacionAritmetica, text=" Codificacion Limites Maximos ")
    LabelCodificacion23.grid(row=14,column=1)
    LabelTramaTotalCodificacion23=Label(VentanaCodificacionAritmetica, text=" ")
    LabelTramaTotalCodificacion23.grid(row=14,column=2)

    LabelDecodificacion3=Label(VentanaCodificacionAritmetica, text=" Decodificacion ")
    LabelDecodificacion3.grid(row=15,column=1)
    LabelTramaTotal3=Label(VentanaCodificacionAritmetica, text=" ")
    LabelTramaTotal3.grid(row=15,column=2)


    LabelBinario3=Label(VentanaCodificacionAritmetica, text=" Codigo Binario ")
    LabelBinario3.grid(row=16,column=1)
    LabelMostrarBinario3=Label(VentanaCodificacionAritmetica, text=" ")
    LabelMostrarBinario3.grid(row=16,column=2)

    BotonTablaCodificacionAritmetica3=Button(VentanaCodificacionAritmetica, text="Mostrar Codificacion Aritmetica", width=25, command=lambda : Aritmetica())
    BotonTablaCodificacionAritmetica3.grid(row=12, column=2)

    BotonGuardar3=Button(VentanaCodificacionAritmetica, text="Guardar Trama Final", width=25, command=Guardar)
    BotonGuardar3.grid(row=17, column=2)
    LabelGuardarTramaTotal3=Label(VentanaCodificacionAritmetica, text=" ") 
    LabelGuardarTramaTotal3.grid(row=18, column=2)

    BotonVolver3=Button(VentanaCodificacionAritmetica, text="Regresar", width=25, command=Volver)
    BotonVolver3.grid(row=19, column=2)

    VentanaCodificacionAritmetica.mainloop()

#Funcion CodificacionAritmeticaModificada
def CodificacionAritmeticaModificada():
    ventana.withdraw()    
    def Base3():
        val=0    
        palabra=PalabraUsuario.get()
        len1=len(palabra)
        if(len1<7):
            LabelPalabraUsuario.configure(text="Su palabra es de menos de 7 caracteres")
            val=0
        elif(len1>12):
            LabelPalabraUsuario.configure(text="Su palabra es de más de 12 caracteres")
            val=0
        else:
            for i in range(len(palabra)):
                if(palabra[i]=="z" or palabra[i]=="a" or palabra[i]=="p"):            
                    LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 7 y 12 caracteres usando solo z,a,p :")
                    val=1
                    LabelError.configure(text=" ")
                elif(palabra[i]=="f" or palabra[i]=="e" or palabra[i]=="t" or palabra[i]=="g" or palabra[i]=="u" or palabra[i]=="d"):
                    LabelPalabraUsuario.configure(text="Su palabra tiene caracteres no permitidos") 
                    val=0
                else:
                    LabelPalabraUsuario.configure(text="Su palabra tiene caracteres no permitidos")
                    val=0
        return val

    def Base6():
        val=0
        palabra=PalabraUsuario.get()
        len1=len(palabra)
        if(len1<7):
            LabelPalabraUsuario.configure(text="Su palabra es de menos de 7 caracteres")
            val=0
        elif(len1>12):
            LabelPalabraUsuario.configure(text="Su palabra es de más de 12 caracteres")
            val=0
        else:
            for i in range(len(palabra)):
                if(palabra[i]=="z" or palabra[i]=="a" or palabra[i]=="p" or palabra[i]=="f" or palabra[i]=="e" or palabra[i]=="t"):            
                    LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 7 y 12 caracteres usando solo z,a,p,f,e,t :")
                    val=2
                    LabelError.configure(text=" ")
                elif(palabra[i]=="g" or palabra[i]=="u" or palabra[i]=="d"):
                    LabelPalabraUsuario.configure(text="Su palabra tiene caracteres no permitidos")
                    val=0
                else:
                    LabelPalabraUsuario.configure(text="Su palabra tiene caracteres no permitidos")
                    val=0
        return val

    def Base9():
        val=0
        palabra=PalabraUsuario.get()
        len1=len(palabra)
        if(len1<7):
            LabelPalabraUsuario.configure(text="Su palabra es de menos de 7 caracteres")
            val=0
        elif(len1>12):
            LabelPalabraUsuario.configure(text="Su palabra es de más de 12 caracteres")
            val=0
        else:
            for i in range(len(palabra)):
                if(palabra[i]=="z" or palabra[i]=="a" or palabra[i]=="p" or palabra[i]=="f" or palabra[i]=="e" or palabra[i]=="t" or palabra[i]=="g" or palabra[i]=="u" or palabra[i]=="d"):            
                    LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 7 y 12 caracteres usando solo z,a,p,f,e,t,g,u,d :")
                    val=3
                    LabelError.configure(text=" ")
                else:
                    LabelPalabraUsuario.configure(text="Su palabra tiene caracteres no permitidos")
                    val=0    
        return val

    def AritmeticaModificada(val):

        validacion=val
        Letras1="zap"
        Letras2="zapfet"
        Letras3="zapfetgud"

        Posiciones=[1,2,3,4,5,6,7,8,9,10,11,12] 
        Exponentes=[0,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10] 

        if validacion==0:
            LabelError.configure(text=" Su palabra no es valida para la base pedida ")

        #Proceso Base3
        elif validacion==1:
            mensaje1=PalabraUsuario.get()
            Mensaje1=mensaje1.maketrans(Letras1,"012")
            men1=mensaje1.translate(Mensaje1)
            print(men1)
            Entmen1=int(men1)
            len1=len(men1)
            Num1=float(Entmen1/(math.pow(10,(len1))))
            DigitosDComa1=len(str(Num1))
            L1=int(DigitosDComa1-2)
            ValoresPos=list()
            
            #ExponentesBase3
            i=2
            while i in range(len(Posiciones)):
                ValoresPos.append(math.pow(Posiciones[2],Exponentes[i]))  
                i=i+1

            #Base3 
            LetrasNum1 = str(men1)
            ListaNum1 = []
            for n in LetrasNum1:    
                n = int(n)    
                ListaNum1.append(n)      
            VectorSuma = [x*y for x,y in zip(ValoresPos,ListaNum1)]   
            DecimalNum1=sum(VectorSuma)
            TextoLabelMostrarValorBase3=("El valor de su palabra en base 3 es :",DecimalNum1)
            LabelMostrarValorBase.configure(text=TextoLabelMostrarValorBase3)

            Multiplicacion=0
            Entero=0
            Validacion=0
            Numform=0
            Potencia=0
            BinarioFinal="0."
            ResBin=""
            cont=0
            Resp=0
            B=0
            int_base_6=0
            resp_base_6=0
            longitud=len(str(Num1))-1
            while cont <= len(str(DecimalNum1)):
                Potencia=Potencia-1
                Multiplicacion=DecimalNum1*2
                Entero=int(Multiplicacion)
                DecimalNum1=Multiplicacion-Entero
                Validacion=pow(2,Potencia)
                Numform=Entero*Validacion
                Resp= Resp + Numform
                resp_base_6=Resp
                if Entero==1:
                    prueba=""
                    for i in range(longitud):
                        A=resp_base_6*6
                        int_base_6=int(A)
                        resp_base_6= A-int_base_6
                        prueba = prueba + str(int_base_6)
                ResBin= ResBin + str(Entero)
                cont= cont+1
            BinarioFinal= BinarioFinal + ResBin 
            
            TextoLabelMostrarValorMinimoCodificar1=("El valor en que se aproxima su palabra es :", A)    
            LabelMostrarValorMinimoCodificar.configure(text=TextoLabelMostrarValorMinimoCodificar1)
            LabelGuardarTramaTotal3.configure(text=BinarioFinal)
            TextoLabelMostrarTramaBinariaReducida1=("El numero binario de su palabra es :", BinarioFinal)
            LabelMostrarTramaBinariaReducida.configure(text=TextoLabelMostrarTramaBinariaReducida1)

        #Proceso Base 6
        elif validacion==2:
            mensaje2=PalabraUsuario.get()
            Mensaje2=mensaje2.maketrans(Letras2,"012345")
            men2=mensaje2.translate(Mensaje2)
            Entmen2=int(men2)
            len2=len(men2)
            Num2=float(Entmen2/(math.pow(10,(len2))))
            DigitosDComa2=len(str(Num2))
            L2=int(DigitosDComa2-2)
            ValoresPos2=list()

            #ExponentesBase6
            i=2
            while i in range(len(Posiciones)):
                ValoresPos2.append(math.pow(Posiciones[5],Exponentes[i]))  
                i=i+1

            #Base6 
            LetrasNum2 = str(men2)
            ListaNum2 = []
            for n in LetrasNum2:    
                n = int(n)    
                ListaNum2.append(n)      
            VectorSuma2 = [x*y for x,y in zip(ValoresPos2,ListaNum2)]           
            DecimalNum2=sum(VectorSuma2)
            TextoLabelMostrarValorBase6=("El valor de su palabra en base 10 es :",DecimalNum2,"y en base 6:",Num2)
            LabelMostrarValorBase.configure(text=TextoLabelMostrarValorBase6)
            Multiplicacion=0
            Entero=0
            Validacion=0
            Numform=0
            Potencia=0
            BinarioFinal2="0."
            ResBin=""
            cont=0
            Resp=0
            B=0
            int_base_6=0
            resp_base_6=0
            longitud=len(str(Num2))-1
            while cont <= len(str(DecimalNum2)):
                Potencia=Potencia-1
                Multiplicacion=DecimalNum2*2
                Entero=int(Multiplicacion)
                DecimalNum2=Multiplicacion-Entero
                Validacion=pow(2,Potencia)
                Numform=Entero*Validacion
                Resp= Resp + Numform
                resp_base_6=Resp
                if Entero==1:
                    prueba=""
                    for i in range(longitud):
                        B=resp_base_6*6
                        int_base_6=int(B)
                        resp_base_6= B-int_base_6
                        prueba = prueba + str(int_base_6)
                ResBin= ResBin + str(Entero)
                cont= cont+1
            BinarioFinal2= BinarioFinal2 + ResBin          

            TextoLabelMostrarValorMinimoCodificar2=("El valor en que se aproxima su palabra es :", B)    
            LabelMostrarValorMinimoCodificar.configure(text=TextoLabelMostrarValorMinimoCodificar2)
            LabelGuardarTramaTotal3.configure(text=BinarioFinal2)
            TextoLabelMostrarTramaBinariaReducida2=("El numero binario de su palabra es :", BinarioFinal2)
            LabelMostrarTramaBinariaReducida.configure(text=TextoLabelMostrarTramaBinariaReducida2)
                            
        #Proceso Base 9
        elif validacion==3:
            mensaje3=PalabraUsuario.get()
            Mensaje3=mensaje3.maketrans(Letras3,"012345678")
            men3=mensaje3.translate(Mensaje3)
            Entmen3=int(men3)
            len3=len(men3)
            Num3=float(Entmen3/(math.pow(10,(len3))))
            DigitosDComa3=len(str(Num3))  
            L3=int(DigitosDComa3-2)
            ValoresPos3=list()
        
            #ExponentesBase9
            i=2
            while i in range(len(Posiciones)):
                ValoresPos3.append(math.pow(Posiciones[8],Exponentes[i]))  
                i=i+1

            #Base9 
            LetrasNum3 = str(men3)
            ListaNum3 = []
            for n in LetrasNum3:    
                n = int(n)    
                ListaNum3.append(n)      
            VectorSuma3 = [x*y for x,y in zip(ValoresPos3,ListaNum3)]  
            DecimalNum3=sum(VectorSuma3)
            TextoLabelMostrarValorBase9=("El valor de su palabra en base 9 es :",DecimalNum3)
            LabelMostrarValorBase.configure(text=TextoLabelMostrarValorBase9)
            Multiplicacion=0
            Entero=0
            Validacion=0
            Numform=0
            Potencia=0
            BinarioFinal3="0."
            ResBin=""
            cont=0
            Resp=0
            B=0
            int_base_6=0
            resp_base_6=0
            longitud=len(str(Num3))-1
            while cont <= len(str(DecimalNum3)):
                Potencia=Potencia-1
                Multiplicacion=DecimalNum3*2
                Entero=int(Multiplicacion)
                DecimalNum3=Multiplicacion-Entero
                Validacion=pow(2,Potencia)
                Numform=Entero*Validacion
                Resp= Resp + Numform
                resp_base_6=Resp
                if Entero==1:
                    prueba=""
                    for i in range(longitud):
                        C=resp_base_6*6
                        int_base_6=int(C)
                        resp_base_6= C-int_base_6
                        prueba = prueba + str(int_base_6)
                ResBin= ResBin + str(Entero)
                cont= cont+1
            BinarioFinal3= BinarioFinal3 + ResBin        
            TextoLabelMostrarValorMinimoCodificar3=("El valor en que se aproxima su palabra es :", C)    
            LabelMostrarValorMinimoCodificar.configure(text=TextoLabelMostrarValorMinimoCodificar3)
            LabelGuardarTramaTotal3.configure(text=BinarioFinal3)
            TextoLabelMostrarTramaBinariaReducida3=("El numero binario de su palabra es :", BinarioFinal3)
            LabelMostrarTramaBinariaReducida.configure(text=TextoLabelMostrarTramaBinariaReducida3)
    
    #Funcion Guardar Trama
    def Guardar():
        TextoTrama=LabelGuardarTramaTotal3.cget("text")
        TextoTrama=TextoTrama.replace(" ", "")
        characters = "][',"
        for x in range(len(characters)):
            TextoTrama = TextoTrama.replace(characters[x],"")
        clipboard.copy(TextoTrama)

    #Funcion Volver    
    def Volver():
        VentanaCodificacionAritmeticaModificada.destroy()
        ventana.deiconify()

    #Creación ventana
    VentanaCodificacionAritmeticaModificada=Toplevel()
    VentanaCodificacionAritmeticaModificada.title("Codificación Aritmetica Modificada")
    VentanaCodificacionAritmeticaModificada.geometry('1250x550')
    TituloInterfaz=Label(VentanaCodificacionAritmeticaModificada, text="Codificación Aritmetica Modificada", bd=10, fg='black', font=("Helvetica", 16))
    TituloInterfaz.grid(row=1, column=2)

    PalabraUsuario=StringVar()
    LabelPalabraUsuario=Label(VentanaCodificacionAritmeticaModificada, text="Por favor ingrese un texto de entre 7 y 12 caracteres usando el alfabeto mostrado para la base que desee:")
    LabelPalabraUsuario.grid(row=2, column=2)
    EntradaUsuario=Entry(VentanaCodificacionAritmeticaModificada, textvariable=PalabraUsuario, width=50)
    EntradaUsuario.grid(row=7, column=2)

    AlfabetoBase3=Label(VentanaCodificacionAritmeticaModificada, text=" Alfabeto para Base 3 : ")
    AlfabetoBase3.grid(row=4, column=1)
    LabelAlfabetoBase3=Label(VentanaCodificacionAritmeticaModificada, text=" z,a,p ") 
    LabelAlfabetoBase3.grid(row=4, column=2)

    AlfabetoBase6=Label(VentanaCodificacionAritmeticaModificada, text=" Alfabeto para Base 6 : ")
    AlfabetoBase6.grid(row=5, column=1)
    LabelAlfabetoBase6=Label(VentanaCodificacionAritmeticaModificada, text=" z,a,p,f,e,t ") 
    LabelAlfabetoBase6.grid(row=5, column=2)

    AlfabetoBase9=Label(VentanaCodificacionAritmeticaModificada, text=" Alfabeto para Base 9 : ")
    AlfabetoBase9.grid(row=6, column=1)
    LabelAlfabetoBase9=Label(VentanaCodificacionAritmeticaModificada, text=" z,a,p,f,e,t,g,u,d ") 
    LabelAlfabetoBase9.grid(row=6, column=2)

    Espacio2=Label(VentanaCodificacionAritmeticaModificada)
    Espacio2.grid(row=11, column=2) 

    LabelTramaBinariaReducida=Label(VentanaCodificacionAritmeticaModificada, text=" La trama binaria de su palabra es : ")
    LabelTramaBinariaReducida.grid(row=14,column=1)
    LabelMostrarTramaBinariaReducida=Label(VentanaCodificacionAritmeticaModificada, text=" ")
    LabelMostrarTramaBinariaReducida.grid(row=14,column=2)

    LabelValorBase=Label(VentanaCodificacionAritmeticaModificada, text=" El valor de su palabra en la base escogida es : ")
    LabelValorBase.grid(row=15,column=1)
    LabelMostrarValorBase=Label(VentanaCodificacionAritmeticaModificada, text=" ")
    LabelMostrarValorBase.grid(row=15,column=2)

    LabelValorMinimoCodificar=Label(VentanaCodificacionAritmeticaModificada, text=" El valor usado para mostrar su palabra es : ")
    LabelValorMinimoCodificar.grid(row=16,column=1)
    LabelMostrarValorMinimoCodificar=Label(VentanaCodificacionAritmeticaModificada, text=" ")
    LabelMostrarValorMinimoCodificar.grid(row=16,column=2)

    BotonTablaCodificacionAritmetica=Button(VentanaCodificacionAritmeticaModificada, text="Mostrar Codificacion Aritmetica Modificada Base 3", width=40, command=lambda : AritmeticaModificada(Base3()))
    BotonTablaCodificacionAritmetica.grid(row=20, column=2)
    BotonTablaCodificacionAritmetica=Button(VentanaCodificacionAritmeticaModificada, text="Mostrar Codificacion Aritmetica Modificada Base 6", width=40, command=lambda : AritmeticaModificada(Base6()))
    BotonTablaCodificacionAritmetica.grid(row=21, column=2)
    BotonTablaCodificacionAritmetica=Button(VentanaCodificacionAritmeticaModificada, text="Mostrar Codificacion Aritmetica Modificada Base 9", width=40, command=lambda : AritmeticaModificada(Base9()))
    BotonTablaCodificacionAritmetica.grid(row=22, column=2)

    LabelError=Label(VentanaCodificacionAritmeticaModificada, text=" ")
    LabelError.grid(row=23, column=2)
    BotonGuardar3=Button(VentanaCodificacionAritmeticaModificada, text="Guardar Trama Final", width=25, command=Guardar)
    BotonGuardar3.grid(row=24, column=2)
    LabelGuardarTramaTotal3=Label(VentanaCodificacionAritmeticaModificada, text=" ") 
    LabelGuardarTramaTotal3.grid(row=25, column=2)
    BotonVolver3=Button(VentanaCodificacionAritmeticaModificada, text="Regresar", width=25, command=Volver)
    BotonVolver3.grid(row=26, column=2)

    VentanaCodificacionAritmeticaModificada.mainloop()

#Funcion Codificaion RLE
def CodificacionRLE():
    ventana.withdraw()
    #FuncionCrearMatriz
    def CrearMatriz():
        matriz=np.array([
        [Posicion1.get(), Posicion2.get(), Posicion3.get(), Posicion4.get(), Posicion5.get(), Posicion6.get(), Posicion7.get(), Posicion8.get(), Posicion9.get(), Posicion10.get()],
        [Posicion11.get(), Posicion12.get(), Posicion13.get(), Posicion14.get(), Posicion15.get(), Posicion16.get(), Posicion17.get(), Posicion18.get(), Posicion19.get(), Posicion20.get()],
        [Posicion21.get(), Posicion22.get(), Posicion23.get(), Posicion24.get(), Posicion25.get(), Posicion26.get(), Posicion27.get(), Posicion28.get(), Posicion29.get(), Posicion30.get()],
        [Posicion31.get(), Posicion32.get(), Posicion33.get(), Posicion34.get(), Posicion35.get(), Posicion36.get(), Posicion37.get(), Posicion38.get(), Posicion39.get(), Posicion40.get()],
        [Posicion41.get(), Posicion42.get(), Posicion43.get(), Posicion44.get(), Posicion45.get(), Posicion46.get(), Posicion47.get(), Posicion48.get(), Posicion49.get(), Posicion50.get()],
        [Posicion51.get(), Posicion52.get(), Posicion53.get(), Posicion54.get(), Posicion55.get(), Posicion56.get(), Posicion57.get(), Posicion58.get(), Posicion59.get(), Posicion60.get()],
        [Posicion61.get(), Posicion62.get(), Posicion63.get(), Posicion64.get(), Posicion65.get(), Posicion66.get(), Posicion67.get(), Posicion68.get(), Posicion69.get(), Posicion70.get()],
        [Posicion71.get(), Posicion72.get(), Posicion73.get(), Posicion74.get(), Posicion75.get(), Posicion76.get(), Posicion77.get(), Posicion78.get(), Posicion79.get(), Posicion80.get()],
        [Posicion81.get(), Posicion82.get(), Posicion83.get(), Posicion84.get(), Posicion85.get(), Posicion86.get(), Posicion87.get(), Posicion88.get(), Posicion89.get(), Posicion90.get()],
        [Posicion91.get(), Posicion92.get(), Posicion93.get(), Posicion94.get(), Posicion95.get(), Posicion96.get(), Posicion97.get(), Posicion98.get(), Posicion99.get(), Posicion100.get()]])
        
        ercont=0
        i=0
        while i < 10:
            j=0
            while j < 10:
                try:
                    ValorMatriz=matriz[i,j]
                    Prueval=int(ValorMatriz)*1
                    if(Prueval==1 or Prueval==0):
                        LabelError.configure(text="los valores en su matriz estan permitidos ")
                except ValueError:
                    ercont=ercont+1
                    LabelError.configure(text="los valores en su matriz no estan permitidos ")                       
                j=j+1
            i=i+1
        if(ercont!=0):
            LabelError.configure(text="los valores en su matriz no estan permitidos ")
        return matriz

    #Funcion Primeros Valores Matriz Filas
    def RandomArregloFilas():
        Matriz=np.array([
        [Posicion1.get(), Posicion2.get(), Posicion3.get(), Posicion4.get(), Posicion5.get(), Posicion6.get(), Posicion7.get(), Posicion8.get(), Posicion9.get(), Posicion10.get()],
        [Posicion11.get(), Posicion12.get(), Posicion13.get(), Posicion14.get(), Posicion15.get(), Posicion16.get(), Posicion17.get(), Posicion18.get(), Posicion19.get(), Posicion20.get()],
        [Posicion21.get(), Posicion22.get(), Posicion23.get(), Posicion24.get(), Posicion25.get(), Posicion26.get(), Posicion27.get(), Posicion28.get(), Posicion29.get(), Posicion30.get()],
        [Posicion31.get(), Posicion32.get(), Posicion33.get(), Posicion34.get(), Posicion35.get(), Posicion36.get(), Posicion37.get(), Posicion38.get(), Posicion39.get(), Posicion40.get()],
        [Posicion41.get(), Posicion42.get(), Posicion43.get(), Posicion44.get(), Posicion45.get(), Posicion46.get(), Posicion47.get(), Posicion48.get(), Posicion49.get(), Posicion50.get()],
        [Posicion51.get(), Posicion52.get(), Posicion53.get(), Posicion54.get(), Posicion55.get(), Posicion56.get(), Posicion57.get(), Posicion58.get(), Posicion59.get(), Posicion60.get()],
        [Posicion61.get(), Posicion62.get(), Posicion63.get(), Posicion64.get(), Posicion65.get(), Posicion66.get(), Posicion67.get(), Posicion68.get(), Posicion69.get(), Posicion70.get()],
        [Posicion71.get(), Posicion72.get(), Posicion73.get(), Posicion74.get(), Posicion75.get(), Posicion76.get(), Posicion77.get(), Posicion78.get(), Posicion79.get(), Posicion80.get()],
        [Posicion81.get(), Posicion82.get(), Posicion83.get(), Posicion84.get(), Posicion85.get(), Posicion86.get(), Posicion87.get(), Posicion88.get(), Posicion89.get(), Posicion90.get()],
        [Posicion91.get(), Posicion92.get(), Posicion93.get(), Posicion94.get(), Posicion95.get(), Posicion96.get(), Posicion97.get(), Posicion98.get(), Posicion99.get(), Posicion100.get()]])
        
        intervalo=Intervalo.get()
        if(intervalo=="1"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(0,1)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1
        elif(intervalo=="2"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(1,7)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1
        elif(intervalo=="3"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(8,15)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1
        else:
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(0,1)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1
        

        Matriz[0,0]=Matriz[0,1]
        Matriz[9,9]=Matriz[9,8]
        
        i=0
        while i<=9:
            j=0
            while j<=9:
                PosFin=Matriz[i,9]
                if(i!=9):
                    PosAnt=Matriz[i,8]
                    PosIn=Matriz[i+1,0]
                    PosSig=Matriz[i+1,1]
                    PosSig2=Matriz[i+1,2]
                else:
                    PosIn=PosFin
                    PosSig=PosFin
                if(PosFin!=PosIn and PosFin!=PosSig and PosFin!=PosSig2):
                    Matriz[i+1,0]=PosFin
                elif(PosFin!=PosIn and PosFin==PosSig):
                    Matriz[i+1,0]=PosFin
                elif(PosFin!=PosAnt and PosFin!=PosIn and PosFin!=PosSig):
                    Matriz[i+1,0]=PosFin
                j=j+1
            i=i+1
        
        lista1=[Matriz[0,0],Matriz[0,1],Matriz[0,2],Matriz[0,3],Matriz[0,4],Matriz[0,5],Matriz[0,6],Matriz[0,7],Matriz[0,8],Matriz[0,9]]        
        lista2=[Matriz[1,0],Matriz[1,1],Matriz[1,2],Matriz[1,3],Matriz[1,4],Matriz[1,5],Matriz[1,6],Matriz[1,7],Matriz[1,8],Matriz[1,9]]
        lista3=[Matriz[2,0],Matriz[2,1],Matriz[2,2],Matriz[2,3],Matriz[2,4],Matriz[2,5],Matriz[2,6],Matriz[2,7],Matriz[2,8],Matriz[2,9]]
        lista4=[Matriz[3,0],Matriz[3,1],Matriz[3,2],Matriz[3,3],Matriz[3,4],Matriz[3,5],Matriz[3,6],Matriz[3,7],Matriz[3,8],Matriz[3,9]]
        lista5=[Matriz[4,0],Matriz[4,1],Matriz[4,2],Matriz[4,3],Matriz[4,4],Matriz[4,5],Matriz[4,6],Matriz[4,7],Matriz[4,8],Matriz[4,9]]
        lista6=[Matriz[5,0],Matriz[5,1],Matriz[5,2],Matriz[5,3],Matriz[5,4],Matriz[5,5],Matriz[5,6],Matriz[5,7],Matriz[5,8],Matriz[5,9]]
        lista7=[Matriz[6,0],Matriz[6,1],Matriz[6,2],Matriz[6,3],Matriz[6,4],Matriz[6,5],Matriz[6,6],Matriz[6,7],Matriz[6,8],Matriz[6,9]]
        lista8=[Matriz[7,0],Matriz[7,1],Matriz[7,2],Matriz[7,3],Matriz[7,4],Matriz[7,5],Matriz[7,6],Matriz[7,7],Matriz[7,8],Matriz[7,9]]
        lista9=[Matriz[8,0],Matriz[8,1],Matriz[8,2],Matriz[8,3],Matriz[8,4],Matriz[8,5],Matriz[8,6],Matriz[8,7],Matriz[8,8],Matriz[8,9]]
        lista10=[Matriz[9,0],Matriz[9,1],Matriz[9,2],Matriz[9,3],Matriz[9,4],Matriz[9,5],Matriz[9,6],Matriz[9,7],Matriz[9,8],Matriz[9,9]]

        texto1=str(lista1[0])
        ArregloPos1.delete(0,END)
        ArregloPos1.insert(0,texto1)
        texto2=str(lista1[1])
        ArregloPos2.delete(0,END)
        ArregloPos2.insert(0,texto2)
        texto3=str(lista1[2])
        ArregloPos3.delete(0,END)
        ArregloPos3.insert(0,texto3)
        texto4=str(lista1[3])
        ArregloPos4.delete(0,END)
        ArregloPos4.insert(0,texto4)
        texto5=str(lista1[4])
        ArregloPos5.delete(0,END)
        ArregloPos5.insert(0,texto5)
        texto6=str(lista1[5])
        ArregloPos6.delete(0,END)
        ArregloPos6.insert(0,texto6)
        texto7=str(lista1[6])
        ArregloPos7.delete(0,END)
        ArregloPos7.insert(0,texto7)
        texto8=str(lista1[7])
        ArregloPos8.delete(0,END)
        ArregloPos8.insert(0,texto8)
        texto9=str(lista1[8])
        ArregloPos9.delete(0,END)
        ArregloPos9.insert(0,texto9)
        texto10=str(lista1[9])
        ArregloPos10.delete(0,END)
        ArregloPos10.insert(0,texto10)

        texto11=str(lista2[0])
        ArregloPos11.delete(0,END)
        ArregloPos11.insert(0,texto11)
        texto12=str(lista2[1])
        ArregloPos12.delete(0,END)
        ArregloPos12.insert(0,texto12)
        texto13=str(lista2[2])
        ArregloPos13.delete(0,END)
        ArregloPos13.insert(0,texto13)
        texto14=str(lista2[3])
        ArregloPos14.delete(0,END)
        ArregloPos14.insert(0,texto14)
        texto15=str(lista2[4])
        ArregloPos15.delete(0,END)
        ArregloPos15.insert(0,texto15)
        texto16=str(lista2[5])
        ArregloPos16.delete(0,END)
        ArregloPos16.insert(0,texto16)
        texto17=str(lista2[6])
        ArregloPos17.delete(0,END)
        ArregloPos17.insert(0,texto17)
        texto18=str(lista2[7])
        ArregloPos18.delete(0,END)
        ArregloPos18.insert(0,texto18)
        texto19=str(lista2[8])
        ArregloPos19.delete(0,END)
        ArregloPos19.insert(0,texto19)
        texto20=str(lista2[9])
        ArregloPos20.delete(0,END)
        ArregloPos20.insert(0,texto20)

        texto21=str(lista3[0])
        ArregloPos21.delete(0,END)
        ArregloPos21.insert(0,texto21)
        texto22=str(lista3[1])
        ArregloPos22.delete(0,END)
        ArregloPos22.insert(0,texto22)
        texto23=str(lista3[2])
        ArregloPos23.delete(0,END)
        ArregloPos23.insert(0,texto23)
        texto24=str(lista3[3])
        ArregloPos24.delete(0,END)
        ArregloPos24.insert(0,texto24)
        texto25=str(lista3[4])
        ArregloPos25.delete(0,END)
        ArregloPos25.insert(0,texto25)
        texto26=str(lista3[5])
        ArregloPos26.delete(0,END)
        ArregloPos26.insert(0,texto26)
        texto27=str(lista3[6])
        ArregloPos27.delete(0,END)
        ArregloPos27.insert(0,texto27)
        texto28=str(lista3[7])
        ArregloPos28.delete(0,END)
        ArregloPos28.insert(0,texto28)
        texto29=str(lista3[8])
        ArregloPos29.delete(0,END)
        ArregloPos29.insert(0,texto29)
        texto30=str(lista3[9])
        ArregloPos30.delete(0,END)
        ArregloPos30.insert(0,texto30)

        texto31=str(lista4[0])
        ArregloPos31.delete(0,END)
        ArregloPos31.insert(0,texto31)
        texto32=str(lista4[1])
        ArregloPos32.delete(0,END)
        ArregloPos32.insert(0,texto32)
        texto33=str(lista4[2])
        ArregloPos33.delete(0,END)
        ArregloPos33.insert(0,texto33)
        texto34=str(lista4[3])
        ArregloPos34.delete(0,END)
        ArregloPos34.insert(0,texto34)
        texto35=str(lista4[4])
        ArregloPos35.delete(0,END)
        ArregloPos35.insert(0,texto35)
        texto36=str(lista4[5])
        ArregloPos36.delete(0,END)
        ArregloPos36.insert(0,texto36)
        texto37=str(lista4[6])
        ArregloPos37.delete(0,END)
        ArregloPos37.insert(0,texto37)
        texto38=str(lista4[7])
        ArregloPos38.delete(0,END)
        ArregloPos38.insert(0,texto38)
        texto39=str(lista4[8])
        ArregloPos39.delete(0,END)
        ArregloPos39.insert(0,texto39)
        texto40=str(lista4[9])
        ArregloPos40.delete(0,END)
        ArregloPos40.insert(0,texto40)

        texto41=str(lista5[0])
        ArregloPos41.delete(0,END)
        ArregloPos41.insert(0,texto41)
        texto42=str(lista5[1])
        ArregloPos42.delete(0,END)
        ArregloPos42.insert(0,texto42)
        texto43=str(lista5[2])
        ArregloPos43.delete(0,END)
        ArregloPos43.insert(0,texto43)
        texto44=str(lista5[3])
        ArregloPos44.delete(0,END)
        ArregloPos44.insert(0,texto44)
        texto45=str(lista5[4])
        ArregloPos45.delete(0,END)
        ArregloPos45.insert(0,texto45)
        texto46=str(lista5[5])
        ArregloPos46.delete(0,END)
        ArregloPos46.insert(0,texto46)
        texto47=str(lista5[6])
        ArregloPos47.delete(0,END)
        ArregloPos47.insert(0,texto47)
        texto48=str(lista5[7])
        ArregloPos48.delete(0,END)
        ArregloPos48.insert(0,texto48)
        texto49=str(lista5[8])
        ArregloPos49.delete(0,END)
        ArregloPos49.insert(0,texto49)
        texto50=str(lista5[9])
        ArregloPos50.delete(0,END)
        ArregloPos50.insert(0,texto50)

        texto51=str(lista6[0])
        ArregloPos51.delete(0,END)
        ArregloPos51.insert(0,texto51)
        texto52=str(lista6[1])
        ArregloPos52.delete(0,END)
        ArregloPos52.insert(0,texto52)
        texto53=str(lista6[2])
        ArregloPos53.delete(0,END)
        ArregloPos53.insert(0,texto53)
        texto54=str(lista6[3])
        ArregloPos54.delete(0,END)
        ArregloPos54.insert(0,texto54)
        texto55=str(lista6[4])
        ArregloPos55.delete(0,END)
        ArregloPos55.insert(0,texto55)
        texto56=str(lista6[5])
        ArregloPos56.delete(0,END)
        ArregloPos56.insert(0,texto56)
        texto57=str(lista6[6])
        ArregloPos57.delete(0,END)
        ArregloPos57.insert(0,texto57)
        texto58=str(lista6[7])
        ArregloPos58.delete(0,END)
        ArregloPos58.insert(0,texto58)
        texto59=str(lista6[8])
        ArregloPos59.delete(0,END)
        ArregloPos59.insert(0,texto59)
        texto60=str(lista6[9])
        ArregloPos60.delete(0,END)
        ArregloPos60.insert(0,texto60)

        texto61=str(lista7[0])
        ArregloPos61.delete(0,END)
        ArregloPos61.insert(0,texto61)
        texto62=str(lista7[1])
        ArregloPos62.delete(0,END)
        ArregloPos62.insert(0,texto62)
        texto63=str(lista7[2])
        ArregloPos63.delete(0,END)
        ArregloPos63.insert(0,texto63)
        texto64=str(lista7[3])
        ArregloPos64.delete(0,END)
        ArregloPos64.insert(0,texto64)
        texto65=str(lista7[4])
        ArregloPos65.delete(0,END)
        ArregloPos65.insert(0,texto65)
        texto66=str(lista7[5])
        ArregloPos66.delete(0,END)
        ArregloPos66.insert(0,texto66)
        texto67=str(lista7[6])
        ArregloPos67.delete(0,END)
        ArregloPos67.insert(0,texto67)
        texto68=str(lista7[7])
        ArregloPos68.delete(0,END)
        ArregloPos68.insert(0,texto68)
        texto69=str(lista7[8])
        ArregloPos69.delete(0,END)
        ArregloPos69.insert(0,texto69)
        texto70=str(lista7[9])
        ArregloPos70.delete(0,END)
        ArregloPos70.insert(0,texto70)

        texto71=str(lista8[0])
        ArregloPos71.delete(0,END)
        ArregloPos71.insert(0,texto71)
        texto72=str(lista8[1])
        ArregloPos72.delete(0,END)
        ArregloPos72.insert(0,texto72)
        texto73=str(lista8[2])
        ArregloPos73.delete(0,END)
        ArregloPos73.insert(0,texto73)
        texto74=str(lista8[3])
        ArregloPos74.delete(0,END)
        ArregloPos74.insert(0,texto74)
        texto75=str(lista8[4])
        ArregloPos75.delete(0,END)
        ArregloPos75.insert(0,texto75)
        texto76=str(lista8[5])
        ArregloPos76.delete(0,END)
        ArregloPos76.insert(0,texto76)
        texto77=str(lista8[6])
        ArregloPos77.delete(0,END)
        ArregloPos77.insert(0,texto77)
        texto78=str(lista8[7])
        ArregloPos78.delete(0,END)
        ArregloPos78.insert(0,texto78)
        texto79=str(lista8[8])
        ArregloPos79.delete(0,END)
        ArregloPos79.insert(0,texto79)
        texto80=str(lista8[9])
        ArregloPos80.delete(0,END)
        ArregloPos80.insert(0,texto80)

        texto81=str(lista9[0])
        ArregloPos81.delete(0,END)
        ArregloPos81.insert(0,texto81)
        texto82=str(lista9[1])
        ArregloPos82.delete(0,END)
        ArregloPos82.insert(0,texto82)
        texto83=str(lista9[2])
        ArregloPos83.delete(0,END)
        ArregloPos83.insert(0,texto83)
        texto84=str(lista9[3])
        ArregloPos84.delete(0,END)
        ArregloPos84.insert(0,texto84)
        texto85=str(lista9[4])
        ArregloPos85.delete(0,END)
        ArregloPos85.insert(0,texto85)
        texto86=str(lista9[5])
        ArregloPos86.delete(0,END)
        ArregloPos86.insert(0,texto86)
        texto87=str(lista9[6])
        ArregloPos87.delete(0,END)
        ArregloPos87.insert(0,texto87)
        texto88=str(lista9[7])
        ArregloPos88.delete(0,END)
        ArregloPos88.insert(0,texto88)
        texto89=str(lista9[8])
        ArregloPos89.delete(0,END)
        ArregloPos89.insert(0,texto89)
        texto90=str(lista9[9])
        ArregloPos90.delete(0,END)
        ArregloPos90.insert(0,texto90)

        texto91=str(lista10[0])
        ArregloPos91.delete(0,END)
        ArregloPos91.insert(0,texto91)
        texto92=str(lista10[1])
        ArregloPos92.delete(0,END)
        ArregloPos92.insert(0,texto92)
        texto93=str(lista10[2])
        ArregloPos93.delete(0,END)
        ArregloPos93.insert(0,texto93)
        texto94=str(lista10[3])
        ArregloPos94.delete(0,END)
        ArregloPos94.insert(0,texto94)
        texto95=str(lista10[4])
        ArregloPos95.delete(0,END)
        ArregloPos95.insert(0,texto95)
        texto96=str(lista10[5])
        ArregloPos96.delete(0,END)
        ArregloPos96.insert(0,texto96)
        texto97=str(lista10[6])
        ArregloPos97.delete(0,END)
        ArregloPos97.insert(0,texto97)
        texto98=str(lista10[7])
        ArregloPos98.delete(0,END)
        ArregloPos98.insert(0,texto98)
        texto99=str(lista10[8])
        ArregloPos99.delete(0,END)
        ArregloPos99.insert(0,texto99)
        texto100=str(lista10[9])
        ArregloPos100.delete(0,END)
        ArregloPos100.insert(0,texto100)

    #Funcion Primeros Valores Matriz Columnas
    def RandomArregloColumnas():
        Matriz=np.array([
        [Posicion1.get(), Posicion2.get(), Posicion3.get(), Posicion4.get(), Posicion5.get(), Posicion6.get(), Posicion7.get(), Posicion8.get(), Posicion9.get(), Posicion10.get()],
        [Posicion11.get(), Posicion12.get(), Posicion13.get(), Posicion14.get(), Posicion15.get(), Posicion16.get(), Posicion17.get(), Posicion18.get(), Posicion19.get(), Posicion20.get()],
        [Posicion21.get(), Posicion22.get(), Posicion23.get(), Posicion24.get(), Posicion25.get(), Posicion26.get(), Posicion27.get(), Posicion28.get(), Posicion29.get(), Posicion30.get()],
        [Posicion31.get(), Posicion32.get(), Posicion33.get(), Posicion34.get(), Posicion35.get(), Posicion36.get(), Posicion37.get(), Posicion38.get(), Posicion39.get(), Posicion40.get()],
        [Posicion41.get(), Posicion42.get(), Posicion43.get(), Posicion44.get(), Posicion45.get(), Posicion46.get(), Posicion47.get(), Posicion48.get(), Posicion49.get(), Posicion50.get()],
        [Posicion51.get(), Posicion52.get(), Posicion53.get(), Posicion54.get(), Posicion55.get(), Posicion56.get(), Posicion57.get(), Posicion58.get(), Posicion59.get(), Posicion60.get()],
        [Posicion61.get(), Posicion62.get(), Posicion63.get(), Posicion64.get(), Posicion65.get(), Posicion66.get(), Posicion67.get(), Posicion68.get(), Posicion69.get(), Posicion70.get()],
        [Posicion71.get(), Posicion72.get(), Posicion73.get(), Posicion74.get(), Posicion75.get(), Posicion76.get(), Posicion77.get(), Posicion78.get(), Posicion79.get(), Posicion80.get()],
        [Posicion81.get(), Posicion82.get(), Posicion83.get(), Posicion84.get(), Posicion85.get(), Posicion86.get(), Posicion87.get(), Posicion88.get(), Posicion89.get(), Posicion90.get()],
        [Posicion91.get(), Posicion92.get(), Posicion93.get(), Posicion94.get(), Posicion95.get(), Posicion96.get(), Posicion97.get(), Posicion98.get(), Posicion99.get(), Posicion100.get()]])
        
        intervalo=Intervalo.get()
        if(intervalo=="1"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(0,1)
                    if j>1:
                        UltPos=Matriz[j-1,i]
                        AntPos=Matriz[j-2,i]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[j,i]=Val
                    j=j+1
                i=i+1
        elif(intervalo=="2"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(1,7)
                    if j>1:
                        UltPos=Matriz[j-1,i]
                        AntPos=Matriz[j-2,i]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[j,i]=Val
                    j=j+1
                i=i+1
        elif(intervalo=="3"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(8,15)
                    if j>1:
                        UltPos=Matriz[j-1,i]
                        AntPos=Matriz[j-2,i]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[j,i]=Val
                    j=j+1
                i=i+1
        else:
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(0,1)
                    if j>1:
                        UltPos=Matriz[j-1,i]
                        AntPos=Matriz[j-2,i]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[j,i]=Val
                    j=j+1
                i=i+1

        Matriz[0,0]=Matriz[1,0]
        Matriz[9,9]=Matriz[8,9]
        
        i=0
        while i<=9:
            j=0
            while j<=9:
                PosFin=Matriz[9,j]
                if(j!=9):
                    PosAnt=Matriz[8,j]
                    PosIn=Matriz[0,j+1]
                    PosSig=Matriz[1,j+1]
                    PosSig2=Matriz[2,j+1]
                else:
                    PosIn=PosFin
                    PosSig=PosFin
                if(PosFin!=PosIn and PosFin!=PosSig and PosFin!=PosSig2):
                    Matriz[0,j+1]=PosFin
                elif(PosFin!=PosIn and PosFin==PosSig):
                    Matriz[0,j+1]=PosFin
                elif(PosFin!=PosAnt and PosFin!=PosIn and PosFin!=PosSig):
                    Matriz[0,j+1]=PosFin
                j=j+1
            i=i+1
        
        lista1=[Matriz[0,0],Matriz[0,1],Matriz[0,2],Matriz[0,3],Matriz[0,4],Matriz[0,5],Matriz[0,6],Matriz[0,7],Matriz[0,8],Matriz[0,9]]        
        lista2=[Matriz[1,0],Matriz[1,1],Matriz[1,2],Matriz[1,3],Matriz[1,4],Matriz[1,5],Matriz[1,6],Matriz[1,7],Matriz[1,8],Matriz[1,9]]
        lista3=[Matriz[2,0],Matriz[2,1],Matriz[2,2],Matriz[2,3],Matriz[2,4],Matriz[2,5],Matriz[2,6],Matriz[2,7],Matriz[2,8],Matriz[2,9]]
        lista4=[Matriz[3,0],Matriz[3,1],Matriz[3,2],Matriz[3,3],Matriz[3,4],Matriz[3,5],Matriz[3,6],Matriz[3,7],Matriz[3,8],Matriz[3,9]]
        lista5=[Matriz[4,0],Matriz[4,1],Matriz[4,2],Matriz[4,3],Matriz[4,4],Matriz[4,5],Matriz[4,6],Matriz[4,7],Matriz[4,8],Matriz[4,9]]
        lista6=[Matriz[5,0],Matriz[5,1],Matriz[5,2],Matriz[5,3],Matriz[5,4],Matriz[5,5],Matriz[5,6],Matriz[5,7],Matriz[5,8],Matriz[5,9]]
        lista7=[Matriz[6,0],Matriz[6,1],Matriz[6,2],Matriz[6,3],Matriz[6,4],Matriz[6,5],Matriz[6,6],Matriz[6,7],Matriz[6,8],Matriz[6,9]]
        lista8=[Matriz[7,0],Matriz[7,1],Matriz[7,2],Matriz[7,3],Matriz[7,4],Matriz[7,5],Matriz[7,6],Matriz[7,7],Matriz[7,8],Matriz[7,9]]
        lista9=[Matriz[8,0],Matriz[8,1],Matriz[8,2],Matriz[8,3],Matriz[8,4],Matriz[8,5],Matriz[8,6],Matriz[8,7],Matriz[8,8],Matriz[8,9]]
        lista10=[Matriz[9,0],Matriz[9,1],Matriz[9,2],Matriz[9,3],Matriz[9,4],Matriz[9,5],Matriz[9,6],Matriz[9,7],Matriz[9,8],Matriz[9,9]]

        texto1=str(lista1[0])
        ArregloPos1.delete(0,END)
        ArregloPos1.insert(0,texto1)
        texto2=str(lista1[1])
        ArregloPos2.delete(0,END)
        ArregloPos2.insert(0,texto2)
        texto3=str(lista1[2])
        ArregloPos3.delete(0,END)
        ArregloPos3.insert(0,texto3)
        texto4=str(lista1[3])
        ArregloPos4.delete(0,END)
        ArregloPos4.insert(0,texto4)
        texto5=str(lista1[4])
        ArregloPos5.delete(0,END)
        ArregloPos5.insert(0,texto5)
        texto6=str(lista1[5])
        ArregloPos6.delete(0,END)
        ArregloPos6.insert(0,texto6)
        texto7=str(lista1[6])
        ArregloPos7.delete(0,END)
        ArregloPos7.insert(0,texto7)
        texto8=str(lista1[7])
        ArregloPos8.delete(0,END)
        ArregloPos8.insert(0,texto8)
        texto9=str(lista1[8])
        ArregloPos9.delete(0,END)
        ArregloPos9.insert(0,texto9)
        texto10=str(lista1[9])
        ArregloPos10.delete(0,END)
        ArregloPos10.insert(0,texto10)

        texto11=str(lista2[0])
        ArregloPos11.delete(0,END)
        ArregloPos11.insert(0,texto11)
        texto12=str(lista2[1])
        ArregloPos12.delete(0,END)
        ArregloPos12.insert(0,texto12)
        texto13=str(lista2[2])
        ArregloPos13.delete(0,END)
        ArregloPos13.insert(0,texto13)
        texto14=str(lista2[3])
        ArregloPos14.delete(0,END)
        ArregloPos14.insert(0,texto14)
        texto15=str(lista2[4])
        ArregloPos15.delete(0,END)
        ArregloPos15.insert(0,texto15)
        texto16=str(lista2[5])
        ArregloPos16.delete(0,END)
        ArregloPos16.insert(0,texto16)
        texto17=str(lista2[6])
        ArregloPos17.delete(0,END)
        ArregloPos17.insert(0,texto17)
        texto18=str(lista2[7])
        ArregloPos18.delete(0,END)
        ArregloPos18.insert(0,texto18)
        texto19=str(lista2[8])
        ArregloPos19.delete(0,END)
        ArregloPos19.insert(0,texto19)
        texto20=str(lista2[9])
        ArregloPos20.delete(0,END)
        ArregloPos20.insert(0,texto20)

        texto21=str(lista3[0])
        ArregloPos21.delete(0,END)
        ArregloPos21.insert(0,texto21)
        texto22=str(lista3[1])
        ArregloPos22.delete(0,END)
        ArregloPos22.insert(0,texto22)
        texto23=str(lista3[2])
        ArregloPos23.delete(0,END)
        ArregloPos23.insert(0,texto23)
        texto24=str(lista3[3])
        ArregloPos24.delete(0,END)
        ArregloPos24.insert(0,texto24)
        texto25=str(lista3[4])
        ArregloPos25.delete(0,END)
        ArregloPos25.insert(0,texto25)
        texto26=str(lista3[5])
        ArregloPos26.delete(0,END)
        ArregloPos26.insert(0,texto26)
        texto27=str(lista3[6])
        ArregloPos27.delete(0,END)
        ArregloPos27.insert(0,texto27)
        texto28=str(lista3[7])
        ArregloPos28.delete(0,END)
        ArregloPos28.insert(0,texto28)
        texto29=str(lista3[8])
        ArregloPos29.delete(0,END)
        ArregloPos29.insert(0,texto29)
        texto30=str(lista3[9])
        ArregloPos30.delete(0,END)
        ArregloPos30.insert(0,texto30)

        texto31=str(lista4[0])
        ArregloPos31.delete(0,END)
        ArregloPos31.insert(0,texto31)
        texto32=str(lista4[1])
        ArregloPos32.delete(0,END)
        ArregloPos32.insert(0,texto32)
        texto33=str(lista4[2])
        ArregloPos33.delete(0,END)
        ArregloPos33.insert(0,texto33)
        texto34=str(lista4[3])
        ArregloPos34.delete(0,END)
        ArregloPos34.insert(0,texto34)
        texto35=str(lista4[4])
        ArregloPos35.delete(0,END)
        ArregloPos35.insert(0,texto35)
        texto36=str(lista4[5])
        ArregloPos36.delete(0,END)
        ArregloPos36.insert(0,texto36)
        texto37=str(lista4[6])
        ArregloPos37.delete(0,END)
        ArregloPos37.insert(0,texto37)
        texto38=str(lista4[7])
        ArregloPos38.delete(0,END)
        ArregloPos38.insert(0,texto38)
        texto39=str(lista4[8])
        ArregloPos39.delete(0,END)
        ArregloPos39.insert(0,texto39)
        texto40=str(lista4[9])
        ArregloPos40.delete(0,END)
        ArregloPos40.insert(0,texto40)

        texto41=str(lista5[0])
        ArregloPos41.delete(0,END)
        ArregloPos41.insert(0,texto41)
        texto42=str(lista5[1])
        ArregloPos42.delete(0,END)
        ArregloPos42.insert(0,texto42)
        texto43=str(lista5[2])
        ArregloPos43.delete(0,END)
        ArregloPos43.insert(0,texto43)
        texto44=str(lista5[3])
        ArregloPos44.delete(0,END)
        ArregloPos44.insert(0,texto44)
        texto45=str(lista5[4])
        ArregloPos45.delete(0,END)
        ArregloPos45.insert(0,texto45)
        texto46=str(lista5[5])
        ArregloPos46.delete(0,END)
        ArregloPos46.insert(0,texto46)
        texto47=str(lista5[6])
        ArregloPos47.delete(0,END)
        ArregloPos47.insert(0,texto47)
        texto48=str(lista5[7])
        ArregloPos48.delete(0,END)
        ArregloPos48.insert(0,texto48)
        texto49=str(lista5[8])
        ArregloPos49.delete(0,END)
        ArregloPos49.insert(0,texto49)
        texto50=str(lista5[9])
        ArregloPos50.delete(0,END)
        ArregloPos50.insert(0,texto50)

        texto51=str(lista6[0])
        ArregloPos51.delete(0,END)
        ArregloPos51.insert(0,texto51)
        texto52=str(lista6[1])
        ArregloPos52.delete(0,END)
        ArregloPos52.insert(0,texto52)
        texto53=str(lista6[2])
        ArregloPos53.delete(0,END)
        ArregloPos53.insert(0,texto53)
        texto54=str(lista6[3])
        ArregloPos54.delete(0,END)
        ArregloPos54.insert(0,texto54)
        texto55=str(lista6[4])
        ArregloPos55.delete(0,END)
        ArregloPos55.insert(0,texto55)
        texto56=str(lista6[5])
        ArregloPos56.delete(0,END)
        ArregloPos56.insert(0,texto56)
        texto57=str(lista6[6])
        ArregloPos57.delete(0,END)
        ArregloPos57.insert(0,texto57)
        texto58=str(lista6[7])
        ArregloPos58.delete(0,END)
        ArregloPos58.insert(0,texto58)
        texto59=str(lista6[8])
        ArregloPos59.delete(0,END)
        ArregloPos59.insert(0,texto59)
        texto60=str(lista6[9])
        ArregloPos60.delete(0,END)
        ArregloPos60.insert(0,texto60)

        texto61=str(lista7[0])
        ArregloPos61.delete(0,END)
        ArregloPos61.insert(0,texto61)
        texto62=str(lista7[1])
        ArregloPos62.delete(0,END)
        ArregloPos62.insert(0,texto62)
        texto63=str(lista7[2])
        ArregloPos63.delete(0,END)
        ArregloPos63.insert(0,texto63)
        texto64=str(lista7[3])
        ArregloPos64.delete(0,END)
        ArregloPos64.insert(0,texto64)
        texto65=str(lista7[4])
        ArregloPos65.delete(0,END)
        ArregloPos65.insert(0,texto65)
        texto66=str(lista7[5])
        ArregloPos66.delete(0,END)
        ArregloPos66.insert(0,texto66)
        texto67=str(lista7[6])
        ArregloPos67.delete(0,END)
        ArregloPos67.insert(0,texto67)
        texto68=str(lista7[7])
        ArregloPos68.delete(0,END)
        ArregloPos68.insert(0,texto68)
        texto69=str(lista7[8])
        ArregloPos69.delete(0,END)
        ArregloPos69.insert(0,texto69)
        texto70=str(lista7[9])
        ArregloPos70.delete(0,END)
        ArregloPos70.insert(0,texto70)

        texto71=str(lista8[0])
        ArregloPos71.delete(0,END)
        ArregloPos71.insert(0,texto71)
        texto72=str(lista8[1])
        ArregloPos72.delete(0,END)
        ArregloPos72.insert(0,texto72)
        texto73=str(lista8[2])
        ArregloPos73.delete(0,END)
        ArregloPos73.insert(0,texto73)
        texto74=str(lista8[3])
        ArregloPos74.delete(0,END)
        ArregloPos74.insert(0,texto74)
        texto75=str(lista8[4])
        ArregloPos75.delete(0,END)
        ArregloPos75.insert(0,texto75)
        texto76=str(lista8[5])
        ArregloPos76.delete(0,END)
        ArregloPos76.insert(0,texto76)
        texto77=str(lista8[6])
        ArregloPos77.delete(0,END)
        ArregloPos77.insert(0,texto77)
        texto78=str(lista8[7])
        ArregloPos78.delete(0,END)
        ArregloPos78.insert(0,texto78)
        texto79=str(lista8[8])
        ArregloPos79.delete(0,END)
        ArregloPos79.insert(0,texto79)
        texto80=str(lista8[9])
        ArregloPos80.delete(0,END)
        ArregloPos80.insert(0,texto80)

        texto81=str(lista9[0])
        ArregloPos81.delete(0,END)
        ArregloPos81.insert(0,texto81)
        texto82=str(lista9[1])
        ArregloPos82.delete(0,END)
        ArregloPos82.insert(0,texto82)
        texto83=str(lista9[2])
        ArregloPos83.delete(0,END)
        ArregloPos83.insert(0,texto83)
        texto84=str(lista9[3])
        ArregloPos84.delete(0,END)
        ArregloPos84.insert(0,texto84)
        texto85=str(lista9[4])
        ArregloPos85.delete(0,END)
        ArregloPos85.insert(0,texto85)
        texto86=str(lista9[5])
        ArregloPos86.delete(0,END)
        ArregloPos86.insert(0,texto86)
        texto87=str(lista9[6])
        ArregloPos87.delete(0,END)
        ArregloPos87.insert(0,texto87)
        texto88=str(lista9[7])
        ArregloPos88.delete(0,END)
        ArregloPos88.insert(0,texto88)
        texto89=str(lista9[8])
        ArregloPos89.delete(0,END)
        ArregloPos89.insert(0,texto89)
        texto90=str(lista9[9])
        ArregloPos90.delete(0,END)
        ArregloPos90.insert(0,texto90)

        texto91=str(lista10[0])
        ArregloPos91.delete(0,END)
        ArregloPos91.insert(0,texto91)
        texto92=str(lista10[1])
        ArregloPos92.delete(0,END)
        ArregloPos92.insert(0,texto92)
        texto93=str(lista10[2])
        ArregloPos93.delete(0,END)
        ArregloPos93.insert(0,texto93)
        texto94=str(lista10[3])
        ArregloPos94.delete(0,END)
        ArregloPos94.insert(0,texto94)
        texto95=str(lista10[4])
        ArregloPos95.delete(0,END)
        ArregloPos95.insert(0,texto95)
        texto96=str(lista10[5])
        ArregloPos96.delete(0,END)
        ArregloPos96.insert(0,texto96)
        texto97=str(lista10[6])
        ArregloPos97.delete(0,END)
        ArregloPos97.insert(0,texto97)
        texto98=str(lista10[7])
        ArregloPos98.delete(0,END)
        ArregloPos98.insert(0,texto98)
        texto99=str(lista10[8])
        ArregloPos99.delete(0,END)
        ArregloPos99.insert(0,texto99)
        texto100=str(lista10[9])
        ArregloPos100.delete(0,END)
        ArregloPos100.insert(0,texto100)

    #Funcion Primeros Valores Matriz Zig Zag
    def RandomArregloZigZag():
        Matriz=np.array([
        [Posicion1.get(), Posicion2.get(), Posicion3.get(), Posicion4.get(), Posicion5.get(), Posicion6.get(), Posicion7.get(), Posicion8.get(), Posicion9.get(), Posicion10.get()],
        [Posicion11.get(), Posicion12.get(), Posicion13.get(), Posicion14.get(), Posicion15.get(), Posicion16.get(), Posicion17.get(), Posicion18.get(), Posicion19.get(), Posicion20.get()],
        [Posicion21.get(), Posicion22.get(), Posicion23.get(), Posicion24.get(), Posicion25.get(), Posicion26.get(), Posicion27.get(), Posicion28.get(), Posicion29.get(), Posicion30.get()],
        [Posicion31.get(), Posicion32.get(), Posicion33.get(), Posicion34.get(), Posicion35.get(), Posicion36.get(), Posicion37.get(), Posicion38.get(), Posicion39.get(), Posicion40.get()],
        [Posicion41.get(), Posicion42.get(), Posicion43.get(), Posicion44.get(), Posicion45.get(), Posicion46.get(), Posicion47.get(), Posicion48.get(), Posicion49.get(), Posicion50.get()],
        [Posicion51.get(), Posicion52.get(), Posicion53.get(), Posicion54.get(), Posicion55.get(), Posicion56.get(), Posicion57.get(), Posicion58.get(), Posicion59.get(), Posicion60.get()],
        [Posicion61.get(), Posicion62.get(), Posicion63.get(), Posicion64.get(), Posicion65.get(), Posicion66.get(), Posicion67.get(), Posicion68.get(), Posicion69.get(), Posicion70.get()],
        [Posicion71.get(), Posicion72.get(), Posicion73.get(), Posicion74.get(), Posicion75.get(), Posicion76.get(), Posicion77.get(), Posicion78.get(), Posicion79.get(), Posicion80.get()],
        [Posicion81.get(), Posicion82.get(), Posicion83.get(), Posicion84.get(), Posicion85.get(), Posicion86.get(), Posicion87.get(), Posicion88.get(), Posicion89.get(), Posicion90.get()],
        [Posicion91.get(), Posicion92.get(), Posicion93.get(), Posicion94.get(), Posicion95.get(), Posicion96.get(), Posicion97.get(), Posicion98.get(), Posicion99.get(), Posicion100.get()]])
        
        intervalo=Intervalo.get()
        if(intervalo=="1"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(0,1)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1
        elif(intervalo=="2"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(1,7)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1
        elif(intervalo=="3"):
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(8,15)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1
        else:
            i=0
            while i<=9:
                j=0
                while j<=9:       
                    Val=random.randint(0,1)
                    if j>1:
                        UltPos=Matriz[i,j-1]
                        AntPos=Matriz[i,j-2]
                        if(UltPos!=Val):
                            if(UltPos!=AntPos):
                                Val=UltPos                        
                    Matriz[i,j]=Val
                    j=j+1
                i=i+1

        Matriz[0,0]=Matriz[0,1]
        Matriz[9,9]=Matriz[9,8]

        lista1=[Matriz[0,0],Matriz[0,1],Matriz[0,2],Matriz[0,3],Matriz[0,4],Matriz[0,5],Matriz[0,6],Matriz[0,7],Matriz[0,8],Matriz[0,9]]        
        lista2=[Matriz[1,0],Matriz[1,1],Matriz[1,2],Matriz[1,3],Matriz[1,4],Matriz[1,5],Matriz[1,6],Matriz[1,7],Matriz[1,8],Matriz[1,9]]
        lista3=[Matriz[2,0],Matriz[2,1],Matriz[2,2],Matriz[2,3],Matriz[2,4],Matriz[2,5],Matriz[2,6],Matriz[2,7],Matriz[2,8],Matriz[2,9]]
        lista4=[Matriz[3,0],Matriz[3,1],Matriz[3,2],Matriz[3,3],Matriz[3,4],Matriz[3,5],Matriz[3,6],Matriz[3,7],Matriz[3,8],Matriz[3,9]]
        lista5=[Matriz[4,0],Matriz[4,1],Matriz[4,2],Matriz[4,3],Matriz[4,4],Matriz[4,5],Matriz[4,6],Matriz[4,7],Matriz[4,8],Matriz[4,9]]
        lista6=[Matriz[5,0],Matriz[5,1],Matriz[5,2],Matriz[5,3],Matriz[5,4],Matriz[5,5],Matriz[5,6],Matriz[5,7],Matriz[5,8],Matriz[5,9]]
        lista7=[Matriz[6,0],Matriz[6,1],Matriz[6,2],Matriz[6,3],Matriz[6,4],Matriz[6,5],Matriz[6,6],Matriz[6,7],Matriz[6,8],Matriz[6,9]]
        lista8=[Matriz[7,0],Matriz[7,1],Matriz[7,2],Matriz[7,3],Matriz[7,4],Matriz[7,5],Matriz[7,6],Matriz[7,7],Matriz[7,8],Matriz[7,9]]
        lista9=[Matriz[8,0],Matriz[8,1],Matriz[8,2],Matriz[8,3],Matriz[8,4],Matriz[8,5],Matriz[8,6],Matriz[8,7],Matriz[8,8],Matriz[8,9]]
        lista10=[Matriz[9,0],Matriz[9,1],Matriz[9,2],Matriz[9,3],Matriz[9,4],Matriz[9,5],Matriz[9,6],Matriz[9,7],Matriz[9,8],Matriz[9,9]]

        texto1=str(lista1[0])
        ArregloPos1.delete(0,END)
        ArregloPos1.insert(0,texto1)
        texto2=str(lista1[1])
        ArregloPos2.delete(0,END)
        ArregloPos2.insert(0,texto2)
        texto3=str(lista1[2])
        ArregloPos3.delete(0,END)
        ArregloPos3.insert(0,texto3)
        texto4=str(lista1[3])
        ArregloPos4.delete(0,END)
        ArregloPos4.insert(0,texto4)
        texto5=str(lista1[4])
        ArregloPos5.delete(0,END)
        ArregloPos5.insert(0,texto5)
        texto6=str(lista1[5])
        ArregloPos6.delete(0,END)
        ArregloPos6.insert(0,texto6)
        texto7=str(lista1[6])
        ArregloPos7.delete(0,END)
        ArregloPos7.insert(0,texto7)
        texto8=str(lista1[7])
        ArregloPos8.delete(0,END)
        ArregloPos8.insert(0,texto8)
        texto9=str(lista1[8])
        ArregloPos9.delete(0,END)
        ArregloPos9.insert(0,texto9)
        texto10=str(lista1[9])
        ArregloPos10.delete(0,END)
        ArregloPos10.insert(0,texto10)

        texto11=str(lista2[0])
        ArregloPos11.delete(0,END)
        ArregloPos11.insert(0,texto11)
        texto12=str(lista2[1])
        ArregloPos12.delete(0,END)
        ArregloPos12.insert(0,texto12)
        texto13=str(lista2[2])
        ArregloPos13.delete(0,END)
        ArregloPos13.insert(0,texto13)
        texto14=str(lista2[3])
        ArregloPos14.delete(0,END)
        ArregloPos14.insert(0,texto14)
        texto15=str(lista2[4])
        ArregloPos15.delete(0,END)
        ArregloPos15.insert(0,texto15)
        texto16=str(lista2[5])
        ArregloPos16.delete(0,END)
        ArregloPos16.insert(0,texto16)
        texto17=str(lista2[6])
        ArregloPos17.delete(0,END)
        ArregloPos17.insert(0,texto17)
        texto18=str(lista2[7])
        ArregloPos18.delete(0,END)
        ArregloPos18.insert(0,texto18)
        texto19=str(lista2[8])
        ArregloPos19.delete(0,END)
        ArregloPos19.insert(0,texto19)
        texto20=str(lista2[9])
        ArregloPos20.delete(0,END)
        ArregloPos20.insert(0,texto20)

        texto21=str(lista3[0])
        ArregloPos21.delete(0,END)
        ArregloPos21.insert(0,texto21)
        texto22=str(lista3[1])
        ArregloPos22.delete(0,END)
        ArregloPos22.insert(0,texto22)
        texto23=str(lista3[2])
        ArregloPos23.delete(0,END)
        ArregloPos23.insert(0,texto23)
        texto24=str(lista3[3])
        ArregloPos24.delete(0,END)
        ArregloPos24.insert(0,texto24)
        texto25=str(lista3[4])
        ArregloPos25.delete(0,END)
        ArregloPos25.insert(0,texto25)
        texto26=str(lista3[5])
        ArregloPos26.delete(0,END)
        ArregloPos26.insert(0,texto26)
        texto27=str(lista3[6])
        ArregloPos27.delete(0,END)
        ArregloPos27.insert(0,texto27)
        texto28=str(lista3[7])
        ArregloPos28.delete(0,END)
        ArregloPos28.insert(0,texto28)
        texto29=str(lista3[8])
        ArregloPos29.delete(0,END)
        ArregloPos29.insert(0,texto29)
        texto30=str(lista3[9])
        ArregloPos30.delete(0,END)
        ArregloPos30.insert(0,texto30)

        texto31=str(lista4[0])
        ArregloPos31.delete(0,END)
        ArregloPos31.insert(0,texto31)
        texto32=str(lista4[1])
        ArregloPos32.delete(0,END)
        ArregloPos32.insert(0,texto32)
        texto33=str(lista4[2])
        ArregloPos33.delete(0,END)
        ArregloPos33.insert(0,texto33)
        texto34=str(lista4[3])
        ArregloPos34.delete(0,END)
        ArregloPos34.insert(0,texto34)
        texto35=str(lista4[4])
        ArregloPos35.delete(0,END)
        ArregloPos35.insert(0,texto35)
        texto36=str(lista4[5])
        ArregloPos36.delete(0,END)
        ArregloPos36.insert(0,texto36)
        texto37=str(lista4[6])
        ArregloPos37.delete(0,END)
        ArregloPos37.insert(0,texto37)
        texto38=str(lista4[7])
        ArregloPos38.delete(0,END)
        ArregloPos38.insert(0,texto38)
        texto39=str(lista4[8])
        ArregloPos39.delete(0,END)
        ArregloPos39.insert(0,texto39)
        texto40=str(lista4[9])
        ArregloPos40.delete(0,END)
        ArregloPos40.insert(0,texto40)

        texto41=str(lista5[0])
        ArregloPos41.delete(0,END)
        ArregloPos41.insert(0,texto41)
        texto42=str(lista5[1])
        ArregloPos42.delete(0,END)
        ArregloPos42.insert(0,texto42)
        texto43=str(lista5[2])
        ArregloPos43.delete(0,END)
        ArregloPos43.insert(0,texto43)
        texto44=str(lista5[3])
        ArregloPos44.delete(0,END)
        ArregloPos44.insert(0,texto44)
        texto45=str(lista5[4])
        ArregloPos45.delete(0,END)
        ArregloPos45.insert(0,texto45)
        texto46=str(lista5[5])
        ArregloPos46.delete(0,END)
        ArregloPos46.insert(0,texto46)
        texto47=str(lista5[6])
        ArregloPos47.delete(0,END)
        ArregloPos47.insert(0,texto47)
        texto48=str(lista5[7])
        ArregloPos48.delete(0,END)
        ArregloPos48.insert(0,texto48)
        texto49=str(lista5[8])
        ArregloPos49.delete(0,END)
        ArregloPos49.insert(0,texto49)
        texto50=str(lista5[9])
        ArregloPos50.delete(0,END)
        ArregloPos50.insert(0,texto50)

        texto51=str(lista6[0])
        ArregloPos51.delete(0,END)
        ArregloPos51.insert(0,texto51)
        texto52=str(lista6[1])
        ArregloPos52.delete(0,END)
        ArregloPos52.insert(0,texto52)
        texto53=str(lista6[2])
        ArregloPos53.delete(0,END)
        ArregloPos53.insert(0,texto53)
        texto54=str(lista6[3])
        ArregloPos54.delete(0,END)
        ArregloPos54.insert(0,texto54)
        texto55=str(lista6[4])
        ArregloPos55.delete(0,END)
        ArregloPos55.insert(0,texto55)
        texto56=str(lista6[5])
        ArregloPos56.delete(0,END)
        ArregloPos56.insert(0,texto56)
        texto57=str(lista6[6])
        ArregloPos57.delete(0,END)
        ArregloPos57.insert(0,texto57)
        texto58=str(lista6[7])
        ArregloPos58.delete(0,END)
        ArregloPos58.insert(0,texto58)
        texto59=str(lista6[8])
        ArregloPos59.delete(0,END)
        ArregloPos59.insert(0,texto59)
        texto60=str(lista6[9])
        ArregloPos60.delete(0,END)
        ArregloPos60.insert(0,texto60)

        texto61=str(lista7[0])
        ArregloPos61.delete(0,END)
        ArregloPos61.insert(0,texto61)
        texto62=str(lista7[1])
        ArregloPos62.delete(0,END)
        ArregloPos62.insert(0,texto62)
        texto63=str(lista7[2])
        ArregloPos63.delete(0,END)
        ArregloPos63.insert(0,texto63)
        texto64=str(lista7[3])
        ArregloPos64.delete(0,END)
        ArregloPos64.insert(0,texto64)
        texto65=str(lista7[4])
        ArregloPos65.delete(0,END)
        ArregloPos65.insert(0,texto65)
        texto66=str(lista7[5])
        ArregloPos66.delete(0,END)
        ArregloPos66.insert(0,texto66)
        texto67=str(lista7[6])
        ArregloPos67.delete(0,END)
        ArregloPos67.insert(0,texto67)
        texto68=str(lista7[7])
        ArregloPos68.delete(0,END)
        ArregloPos68.insert(0,texto68)
        texto69=str(lista7[8])
        ArregloPos69.delete(0,END)
        ArregloPos69.insert(0,texto69)
        texto70=str(lista7[9])
        ArregloPos70.delete(0,END)
        ArregloPos70.insert(0,texto70)

        texto71=str(lista8[0])
        ArregloPos71.delete(0,END)
        ArregloPos71.insert(0,texto71)
        texto72=str(lista8[1])
        ArregloPos72.delete(0,END)
        ArregloPos72.insert(0,texto72)
        texto73=str(lista8[2])
        ArregloPos73.delete(0,END)
        ArregloPos73.insert(0,texto73)
        texto74=str(lista8[3])
        ArregloPos74.delete(0,END)
        ArregloPos74.insert(0,texto74)
        texto75=str(lista8[4])
        ArregloPos75.delete(0,END)
        ArregloPos75.insert(0,texto75)
        texto76=str(lista8[5])
        ArregloPos76.delete(0,END)
        ArregloPos76.insert(0,texto76)
        texto77=str(lista8[6])
        ArregloPos77.delete(0,END)
        ArregloPos77.insert(0,texto77)
        texto78=str(lista8[7])
        ArregloPos78.delete(0,END)
        ArregloPos78.insert(0,texto78)
        texto79=str(lista8[8])
        ArregloPos79.delete(0,END)
        ArregloPos79.insert(0,texto79)
        texto80=str(lista8[9])
        ArregloPos80.delete(0,END)
        ArregloPos80.insert(0,texto80)

        texto81=str(lista9[0])
        ArregloPos81.delete(0,END)
        ArregloPos81.insert(0,texto81)
        texto82=str(lista9[1])
        ArregloPos82.delete(0,END)
        ArregloPos82.insert(0,texto82)
        texto83=str(lista9[2])
        ArregloPos83.delete(0,END)
        ArregloPos83.insert(0,texto83)
        texto84=str(lista9[3])
        ArregloPos84.delete(0,END)
        ArregloPos84.insert(0,texto84)
        texto85=str(lista9[4])
        ArregloPos85.delete(0,END)
        ArregloPos85.insert(0,texto85)
        texto86=str(lista9[5])
        ArregloPos86.delete(0,END)
        ArregloPos86.insert(0,texto86)
        texto87=str(lista9[6])
        ArregloPos87.delete(0,END)
        ArregloPos87.insert(0,texto87)
        texto88=str(lista9[7])
        ArregloPos88.delete(0,END)
        ArregloPos88.insert(0,texto88)
        texto89=str(lista9[8])
        ArregloPos89.delete(0,END)
        ArregloPos89.insert(0,texto89)
        texto90=str(lista9[9])
        ArregloPos90.delete(0,END)
        ArregloPos90.insert(0,texto90)

        texto91=str(lista10[0])
        ArregloPos91.delete(0,END)
        ArregloPos91.insert(0,texto91)
        texto92=str(lista10[1])
        ArregloPos92.delete(0,END)
        ArregloPos92.insert(0,texto92)
        texto93=str(lista10[2])
        ArregloPos93.delete(0,END)
        ArregloPos93.insert(0,texto93)
        texto94=str(lista10[3])
        ArregloPos94.delete(0,END)
        ArregloPos94.insert(0,texto94)
        texto95=str(lista10[4])
        ArregloPos95.delete(0,END)
        ArregloPos95.insert(0,texto95)
        texto96=str(lista10[5])
        ArregloPos96.delete(0,END)
        ArregloPos96.insert(0,texto96)
        texto97=str(lista10[6])
        ArregloPos97.delete(0,END)
        ArregloPos97.insert(0,texto97)
        texto98=str(lista10[7])
        ArregloPos98.delete(0,END)
        ArregloPos98.insert(0,texto98)
        texto99=str(lista10[8])
        ArregloPos99.delete(0,END)
        ArregloPos99.insert(0,texto99)
        texto100=str(lista10[9])
        ArregloPos100.delete(0,END)
        ArregloPos100.insert(0,texto100)

    #Proceso Por Filas
    def AgruparLecturaFilas(matriz):
        Grupos=list()
        Valores=list()
        cont=0
        i=0
        while i < 10:
            j=0
            PosFin=0
            PosSig=0
            while j < 10:
                Pos1=matriz[i,j]
                if(j!=9):            
                    Pos2=matriz[i,j+1]
                else:
                    Pos2=None
                if(Pos1==Pos2):
                    cont=cont+1
                    PosFin=matriz[i,9]
                    if(i!=9):
                        PosSig=matriz[i+1,0]
                    else:
                        PosSig=2
                elif PosFin==PosSig and j==9:
                    cont=cont+1
                else:
                    cont=cont+1
                    valor=matriz[i,j]
                    Valores.append(valor)
                    Grupos.append(cont)
                    cont=0                               
                j=j+1
            i=i+1

        TextoGrupos=("Los grupos de la matriz son: ", Grupos)
        TextoValores=("Los valores de los grupos son: ", Valores)
        LabelMostrarGrupos.configure(text=TextoGrupos)
        LabelMostrarValores.configure(text=TextoValores)

        MaximoVal = None
        for pos, num in enumerate(Valores):
            if(MaximoVal is None or num > MaximoVal):
                MaximoVal=num
                IndiceVal=pos
        BinarioVal=bin(int(MaximoVal))[2:]
        NumeroBinarioVal=Grupos[IndiceVal]

        Maximo = None
        for pos, num in enumerate(Grupos):
            if(Maximo is None or num > Maximo):
                Maximo=num
                Indice=pos
        NumeroBinario=Valores[Indice]
        TextoMayorGrupo=("El mayor grupo es de", Maximo, " de ", NumeroBinario, "El mayor valor es de ",MaximoVal,"apareciendo",NumeroBinarioVal,"veces")
        LabelMostrarMayorGrupo.configure(text=TextoMayorGrupo)

        Binario = 0
        multiplicador = 1
        while Maximo != 0: 
            Binario = Binario + Maximo % 2 * multiplicador
            Maximo //= 2 
            multiplicador *= 10 

        NumBits=(len(str(Binario)))
        NumbitsCompre=NumBits+1
        NumBits2=(len(str(BinarioVal)))
        NumBitsTotal=0
        NumBitsTotalVal=0
        ResultadoBits=list()
        contadorant=0
        Anticipado="1"
        i=0
        if(NumBits<NumBits2):
            NumbitsAnti=NumBits2
        else:
            NumbitsAnti=NumBits
        while i<NumbitsAnti-1:
            if Anticipado[-1]=="1":
                Anticipado=Anticipado+"0"
            elif Anticipado[-1]=="0":
                Anticipado=Anticipado+"1"
            i=i+1
        i=0
        while i< len(Grupos):
            valorcito=Valores[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumbitsAnti):
                valorcito=str(valorcito).zfill(NumbitsAnti)
            NumBitsTotalVal=NumBitsTotalVal+len(str(valorcito))
            ResultadoBits.append(valorcito)  
            contadorant=contadorant+1
            if(contadorant==NumbitsAnti):
                ResultadoBits.append(Anticipado)
                contadorant=0 
            Decimal=Grupos[i]
            Binario2 = 0
            multiplicador2 = 1
            while Decimal != 0:             
                Binario2 = Binario2+ Decimal % 2 * multiplicador2
                Decimal //= 2 
                multiplicador2 *= 10 
            if(len(str(Binario2))<NumbitsAnti):
                Binario2=str(Binario2).zfill(NumbitsAnti)
            NumBitsTotal=NumBitsTotal+len(str(Binario2))
            ResultadoBits.append(Binario2)
            contadorant=contadorant+1
            if(contadorant==NumbitsAnti):
                ResultadoBits.append(Anticipado)
                contadorant=0 
            i=i+1
        LongitudMatriz=len(ResultadoBits)
        NumBitsTotal=NumBitsTotal+NumBitsTotalVal
        NumbitsCompre=LongitudMatriz
        TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
        TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits)
        LabelGuardarTramaTotal3.configure(text=ResultadoBits)
        LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
        LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
        Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100   
        TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
        LabelMostrarTasaCompresion.configure(text=TextoCompresion)  

    #Proceso Por Columnas
    def AgruparLecturaColumnas(matriz):
        Grupos=list()
        Valores=list()
        cont=0
        j=0
        while j < 10:
            i=0
            PosFin=0
            PosSig=0
            while i < 10:
                Pos1=matriz[i,j]
                if(i!=9):            
                    Pos2=matriz[i+1,j]
                else:
                    Pos2=None
                PosFin=matriz[9,j]
                if(j!=9):
                    PosSig=matriz[0,j+1]
                else:
                    PosSig=2
                if(Pos1==Pos2):
                    cont=cont+1
                elif PosFin==PosSig and i==9:
                    cont=cont+1
                else:
                    cont=cont+1
                    valor=matriz[i,j]
                    Valores.append(valor)
                    Grupos.append(cont)
                    cont=0                               
                i=i+1
            j=j+1

        TextoGrupos=("Los grupos de la matriz son: ", Grupos)
        TextoValores=("Los valores de los grupos son: ", Valores)
        LabelMostrarGrupos.configure(text=TextoGrupos)
        LabelMostrarValores.configure(text=TextoValores)
        
        MaximoVal = None
        for pos, num in enumerate(Valores):
            if(MaximoVal is None or num > MaximoVal):
                MaximoVal=num
                IndiceVal=pos
        BinarioVal=bin(int(MaximoVal))[2:]
        NumeroBinarioVal=Grupos[IndiceVal]

        Maximo = None
        for pos, num in enumerate(Grupos):
            if(Maximo is None or num > Maximo):
                Maximo=num
                Indice=pos
        NumeroBinario=Valores[Indice]
        TextoMayorGrupo=("El mayor grupo es de", Maximo, " de ", NumeroBinario, "El mayor valor es de ",MaximoVal,"apareciendo",NumeroBinarioVal,"veces")
        LabelMostrarMayorGrupo.configure(text=TextoMayorGrupo)

        Binario = 0
        multiplicador = 1
        while Maximo != 0: 
            Binario = Binario + Maximo % 2 * multiplicador
            Maximo //= 2 
            multiplicador *= 10 

        NumBits=(len(str(Binario)))
        NumbitsCompre=NumBits+1
        NumBits2=(len(str(BinarioVal)))
        NumBitsTotal=0
        NumBitsTotalVal=0
        ResultadoBits=list()
        Anticipado="1"
        i=0
        if(NumBits<NumBits2):
            NumbitsAnti=NumBits2
        else:
            NumbitsAnti=NumBits
        while i<NumbitsAnti-1:
            if Anticipado[-1]=="1":
                Anticipado=Anticipado+"0"
            elif Anticipado[-1]=="0":
                Anticipado=Anticipado+"1"
            i=i+1
        i=0
        contadorant=0
        while i< len(Grupos):
            valorcito=Valores[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumbitsAnti):
                valorcito=str(valorcito).zfill(NumbitsAnti)
            NumBitsTotalVal=NumBitsTotalVal+len(str(valorcito))
            ResultadoBits.append(valorcito)
            contadorant=contadorant+1
            if(contadorant==NumbitsAnti):
                ResultadoBits.append(Anticipado)
                contadorant=0
            Decimal=Grupos[i]
            Binario2 = 0
            multiplicador2 = 1
            while Decimal != 0: 
                Binario2 = Binario2+ Decimal % 2 * multiplicador2
                Decimal //= 2 
                multiplicador2 *= 10 
            if(len(str(Binario2))<NumbitsAnti):
                Binario2=str(Binario2).zfill(NumbitsAnti)
            NumBitsTotal=NumBitsTotal+len(str(Binario2))
            ResultadoBits.append(Binario2)
            contadorant=contadorant+1
            if(contadorant==NumbitsAnti):
                ResultadoBits.append(Anticipado)
                contadorant=0 
            i=i+1
        LongitudMatriz=len(ResultadoBits)
        NumBitsTotal=NumBitsTotal+NumBitsTotalVal
        NumbitsCompre=LongitudMatriz
        TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
        TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits)
        LabelGuardarTramaTotal3.configure(text=ResultadoBits)
        LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
        LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
        Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100 
        TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
        LabelMostrarTasaCompresion.configure(text=TextoCompresion)  

    #Proceso Por Zig Zag
    def AgruparLecturaZigZag(matriz):
        alto=10
        ancho=10
        MatrizSolucion=[[] for i in range(ancho+alto-1)]

        for i in range(ancho):
            for j in range(alto):
                sum=i+j
                if(sum%2 ==0):
                    MatrizSolucion[sum].insert(0,matriz[i][j])
                else:
                    MatrizSolucion[sum].append(matriz[i][j])		
        lista=list()
        for i in MatrizSolucion:
            for j in i:
                    lista.append(j)
    
        lista2=list()
        lista3=list()
        cont=0
        i=0
        a=len(lista)-1
        while i < len(lista):
            Pos1=lista[i]
            if(i!=a):
                Pos2=lista[i+1]
            else:
                Pos2=None
            if(Pos1==Pos2):
                cont=cont+1
            else:
                cont=cont+1
                valor=lista[i]
                lista2.append(cont)
                lista3.append(valor)
                cont=0
            i=i+1

        TextoGrupos=("Los grupos de la matriz son: ", lista2)
        TextoValores=("Los valores de los grupos son: ", lista3)
        LabelMostrarGrupos.configure(text=TextoGrupos)
        LabelMostrarValores.configure(text=TextoValores)

        MaximoVal = None
        for pos, num in enumerate(lista3):
            if(MaximoVal is None or num > MaximoVal):
                MaximoVal=num
                IndiceVal=pos
        BinarioVal=bin(int(MaximoVal))[2:]
        NumeroBinarioVal=lista2[IndiceVal]

        Maximo = None
        for pos, num in enumerate(lista2):
            if(Maximo is None or num > Maximo):
                Maximo=num
                Indice=pos
        NumeroBinario=lista3[Indice]

        TextoMayorGrupo=("El mayor grupo es de", Maximo, " de ", NumeroBinario, "El mayor valor es de ",MaximoVal,"apareciendo",NumeroBinarioVal,"veces")
        LabelMostrarMayorGrupo.configure(text=TextoMayorGrupo)

        Binario = 0
        multiplicador = 1

        while Maximo != 0: 
            Binario = Binario + Maximo % 2 * multiplicador
            Maximo //= 2 
            multiplicador *= 10 

        NumBits=(len(str(Binario)))
        NumbitsCompre=NumBits+1
        NumBits2=(len(str(BinarioVal)))
        NumbitsCompreVal=NumBits2+1
        NumBitsTotal=0
        NumBitsTotalVal=0
        ResultadoBits=list()
        Anticipado="1"
        contadorant=0
        i=0
        if(NumBits<NumBits2):
            NumbitsAnti=NumBits2
        else:
            NumbitsAnti=NumBits
        while i<NumbitsAnti-1:
            if Anticipado[-1]=="1":
                Anticipado=Anticipado+"0"
            elif Anticipado[-1]=="0":
                Anticipado=Anticipado+"1"
            i=i+1
        ResultadoBits.append(Anticipado)
        i=0
        while i< len(lista2):
            valorcito=lista3[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumbitsAnti):
                valorcito=str(valorcito).zfill(NumbitsCompreVal)
            NumBitsTotalVal=NumBitsTotalVal+len(str(valorcito))
            ResultadoBits.append(valorcito)
            contadorant=contadorant+1 
            if(contadorant==NumbitsAnti):
                ResultadoBits.append(Anticipado)
                contadorant=0 
            Decimal=lista2[i]
            Binario2 = 0
            multiplicador2 = 1
            while Decimal != 0: 
                Binario2 = Binario2+ Decimal % 2 * multiplicador2
                Decimal //= 2 
                multiplicador2 *= 10 
            if(len(str(Binario2))<NumbitsAnti):
                Binario2=str(Binario2).zfill(NumbitsAnti)
            NumBitsTotal=NumBitsTotal+len(str(Binario2))
            ResultadoBits.append(Binario2)
            contadorant=contadorant+1 
            if(contadorant==NumbitsAnti):
                ResultadoBits.append(Anticipado)
                contadorant=0 
            i=i+1
        LongitudMatriz=len(ResultadoBits)
        NumBitsTotal=NumBitsTotal+NumBitsTotalVal
        NumbitsCompre=LongitudMatriz
        TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
        TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits)
        LabelGuardarTramaTotal3.configure(text=ResultadoBits)
        LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
        LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
        Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100 
        TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
        LabelMostrarTasaCompresion.configure(text=TextoCompresion) 
    
    #Funcion Guardar Trama
    def Guardar():
        TextoTrama=LabelGuardarTramaTotal3.cget("text")
        TextoTrama=TextoTrama.replace(" ", "")
        characters = "][',"
        for x in range(len(characters)):
            TextoTrama = TextoTrama.replace(characters[x],"")
        clipboard.copy(TextoTrama)

    #Funcion Volver    
    def Volver():
        VentanaCodificacionREL.destroy()
        ventana.deiconify()

    #Creación ventana
    VentanaCodificacionREL=Toplevel()
    VentanaCodificacionREL.title("Codificación RLE")
    VentanaCodificacionREL.geometry('1500x650')
    TituloInterfaz=Label(VentanaCodificacionREL, text="Codificación RLE", bd=10, fg='black', font=("Helvetica", 16))
    TituloInterfaz.grid(row=0, column=0)
    framecito = Frame(VentanaCodificacionREL)
    framecito.grid(row=16, column=0)

    #Instrucciones
    LabelInstrucciones=Label(VentanaCodificacionREL, text="Por favor ingrese sus valores en la matriz garantizando que siempre haya al menos 2 de cada uno juntos")
    LabelInstrucciones.grid(row=1, column=0)
    Espacio=Label(VentanaCodificacionREL,text="ingrese 1 para valores entre 1 y 0, 2 para valores entre 1 y 7 y 3 para valores entre 8 y 15 ",)
    Espacio.grid(row=2,column=0)
    Intervalo=StringVar()
    EntradaIntervalo=Entry(VentanaCodificacionREL,textvariable=Intervalo,width=20)
    EntradaIntervalo.grid(row=3,column=0)

    #ValoresMatrizfila1
    Posicion1=StringVar()
    ArregloPos1=Entry(VentanaCodificacionREL,textvariable=Posicion1,width=5)
    ArregloPos1.grid(row=3,column=2,sticky=NSEW)
    Posicion2=StringVar()
    ArregloPos2=Entry(VentanaCodificacionREL,textvariable=Posicion2,width=5)
    ArregloPos2.grid(row=3,column=3,sticky=NSEW)
    Posicion3=StringVar()
    ArregloPos3=Entry(VentanaCodificacionREL,textvariable=Posicion3,width=5)
    ArregloPos3.grid(row=3,column=4,sticky=NSEW)
    Posicion4=StringVar()
    ArregloPos4=Entry(VentanaCodificacionREL,textvariable=Posicion4,width=5)
    ArregloPos4.grid(row=3,column=5,sticky=NSEW)
    Posicion5=StringVar()
    ArregloPos5=Entry(VentanaCodificacionREL,textvariable=Posicion5,width=5)
    ArregloPos5.grid(row=3,column=6,sticky=NSEW)
    Posicion6=StringVar()
    ArregloPos6=Entry(VentanaCodificacionREL,textvariable=Posicion6,width=5)
    ArregloPos6.grid(row=3,column=7,sticky=NSEW)
    Posicion7=StringVar()
    ArregloPos7=Entry(VentanaCodificacionREL,textvariable=Posicion7,width=5)
    ArregloPos7.grid(row=3,column=8,sticky=NSEW)
    Posicion8=StringVar()
    ArregloPos8=Entry(VentanaCodificacionREL,textvariable=Posicion8,width=5)
    ArregloPos8.grid(row=3,column=9,sticky=NSEW)
    Posicion9=StringVar()
    ArregloPos9=Entry(VentanaCodificacionREL,textvariable=Posicion9,width=5)
    ArregloPos9.grid(row=3,column=10,sticky=NSEW)
    Posicion10=StringVar()
    ArregloPos10=Entry(VentanaCodificacionREL,textvariable=Posicion10,width=5)
    ArregloPos10.grid(row=3,column=11,sticky=NSEW)

    #ValoresMatrizFila2
    Posicion11=StringVar()
    ArregloPos11=Entry(VentanaCodificacionREL,textvariable=Posicion11,width=5)
    ArregloPos11.grid(row=4,column=2,sticky=NSEW)
    Posicion12=StringVar()
    ArregloPos12=Entry(VentanaCodificacionREL,textvariable=Posicion12,width=5)
    ArregloPos12.grid(row=4,column=3,sticky=NSEW)
    Posicion13=StringVar()
    ArregloPos13=Entry(VentanaCodificacionREL,textvariable=Posicion13,width=5)
    ArregloPos13.grid(row=4,column=4,sticky=NSEW)
    Posicion14=StringVar()
    ArregloPos14=Entry(VentanaCodificacionREL,textvariable=Posicion14,width=5)
    ArregloPos14.grid(row=4,column=5,sticky=NSEW)
    Posicion15=StringVar()
    ArregloPos15=Entry(VentanaCodificacionREL,textvariable=Posicion15,width=5)
    ArregloPos15.grid(row=4,column=6,sticky=NSEW)
    Posicion16=StringVar()
    ArregloPos16=Entry(VentanaCodificacionREL,textvariable=Posicion16,width=5)
    ArregloPos16.grid(row=4,column=7,sticky=NSEW)
    Posicion17=StringVar()
    ArregloPos17=Entry(VentanaCodificacionREL,textvariable=Posicion17,width=5)
    ArregloPos17.grid(row=4,column=8,sticky=NSEW)
    Posicion18=StringVar()
    ArregloPos18=Entry(VentanaCodificacionREL,textvariable=Posicion18,width=5)
    ArregloPos18.grid(row=4,column=9,sticky=NSEW)
    Posicion19=StringVar()
    ArregloPos19=Entry(VentanaCodificacionREL,textvariable=Posicion19,width=5)
    ArregloPos19.grid(row=4,column=10,sticky=NSEW)
    Posicion20=StringVar()
    ArregloPos20=Entry(VentanaCodificacionREL,textvariable=Posicion20,width=5)
    ArregloPos20.grid(row=4,column=11,sticky=NSEW)

    #ValoresMatrizFila3
    Posicion21=StringVar()
    ArregloPos21=Entry(VentanaCodificacionREL,textvariable=Posicion21,width=5)
    ArregloPos21.grid(row=5,column=2,sticky=NSEW)
    Posicion22=StringVar()
    ArregloPos22=Entry(VentanaCodificacionREL,textvariable=Posicion22,width=5)
    ArregloPos22.grid(row=5,column=3,sticky=NSEW)
    Posicion23=StringVar()
    ArregloPos23=Entry(VentanaCodificacionREL,textvariable=Posicion23,width=5)
    ArregloPos23.grid(row=5,column=4,sticky=NSEW)
    Posicion24=StringVar()
    ArregloPos24=Entry(VentanaCodificacionREL,textvariable=Posicion24,width=5)
    ArregloPos24.grid(row=5,column=5,sticky=NSEW)
    Posicion25=StringVar()
    ArregloPos25=Entry(VentanaCodificacionREL,textvariable=Posicion25,width=5)
    ArregloPos25.grid(row=5,column=6,sticky=NSEW)
    Posicion26=StringVar()
    ArregloPos26=Entry(VentanaCodificacionREL,textvariable=Posicion26,width=5)
    ArregloPos26.grid(row=5,column=7,sticky=NSEW)
    Posicion27=StringVar()
    ArregloPos27=Entry(VentanaCodificacionREL,textvariable=Posicion27,width=5)
    ArregloPos27.grid(row=5,column=8,sticky=NSEW)
    Posicion28=StringVar()
    ArregloPos28=Entry(VentanaCodificacionREL,textvariable=Posicion28,width=5)
    ArregloPos28.grid(row=5,column=9,sticky=NSEW)
    Posicion29=StringVar()
    ArregloPos29=Entry(VentanaCodificacionREL,textvariable=Posicion29,width=5)
    ArregloPos29.grid(row=5,column=10,sticky=NSEW)
    Posicion30=StringVar()
    ArregloPos30=Entry(VentanaCodificacionREL,textvariable=Posicion30,width=5)
    ArregloPos30.grid(row=5,column=11,sticky=NSEW)

    #ArregloMatrizFila4
    Posicion31=StringVar()
    ArregloPos31=Entry(VentanaCodificacionREL,textvariable=Posicion31,width=5)
    ArregloPos31.grid(row=6,column=2,sticky=NSEW)
    Posicion32=StringVar()
    ArregloPos32=Entry(VentanaCodificacionREL,textvariable=Posicion32,width=5)
    ArregloPos32.grid(row=6,column=3,sticky=NSEW)
    Posicion33=StringVar()
    ArregloPos33=Entry(VentanaCodificacionREL,textvariable=Posicion33,width=5)
    ArregloPos33.grid(row=6,column=4,sticky=NSEW)
    Posicion34=StringVar()
    ArregloPos34=Entry(VentanaCodificacionREL,textvariable=Posicion34,width=5)
    ArregloPos34.grid(row=6,column=5,sticky=NSEW)
    Posicion35=StringVar()
    ArregloPos35=Entry(VentanaCodificacionREL,textvariable=Posicion35,width=5)
    ArregloPos35.grid(row=6,column=6,sticky=NSEW)
    Posicion36=StringVar()
    ArregloPos36=Entry(VentanaCodificacionREL,textvariable=Posicion36,width=5)
    ArregloPos36.grid(row=6,column=7,sticky=NSEW)
    Posicion37=StringVar()
    ArregloPos37=Entry(VentanaCodificacionREL,textvariable=Posicion37,width=5)
    ArregloPos37.grid(row=6,column=8,sticky=NSEW)
    Posicion38=StringVar()
    ArregloPos38=Entry(VentanaCodificacionREL,textvariable=Posicion38,width=5)
    ArregloPos38.grid(row=6,column=9,sticky=NSEW)
    Posicion39=StringVar()
    ArregloPos39=Entry(VentanaCodificacionREL,textvariable=Posicion39,width=5)
    ArregloPos39.grid(row=6,column=10,sticky=NSEW)
    Posicion40=StringVar()
    ArregloPos40=Entry(VentanaCodificacionREL,textvariable=Posicion40,width=5)
    ArregloPos40.grid(row=6,column=11,sticky=NSEW)

    #ArregloMatrizFila5
    Posicion41=StringVar()
    ArregloPos41=Entry(VentanaCodificacionREL,textvariable=Posicion41,width=5)
    ArregloPos41.grid(row=7,column=2,sticky=NSEW)
    Posicion42=StringVar()
    ArregloPos42=Entry(VentanaCodificacionREL,textvariable=Posicion42,width=5)
    ArregloPos42.grid(row=7,column=3,sticky=NSEW)
    Posicion43=StringVar()
    ArregloPos43=Entry(VentanaCodificacionREL,textvariable=Posicion43,width=5)
    ArregloPos43.grid(row=7,column=4,sticky=NSEW)
    Posicion44=StringVar()
    ArregloPos44=Entry(VentanaCodificacionREL,textvariable=Posicion44,width=5)
    ArregloPos44.grid(row=7,column=5,sticky=NSEW)
    Posicion45=StringVar()
    ArregloPos45=Entry(VentanaCodificacionREL,textvariable=Posicion45,width=5)
    ArregloPos45.grid(row=7,column=6,sticky=NSEW)
    Posicion46=StringVar()
    ArregloPos46=Entry(VentanaCodificacionREL,textvariable=Posicion46,width=5)
    ArregloPos46.grid(row=7,column=7,sticky=NSEW)
    Posicion47=StringVar()
    ArregloPos47=Entry(VentanaCodificacionREL,textvariable=Posicion47,width=5)
    ArregloPos47.grid(row=7,column=8,sticky=NSEW)
    Posicion48=StringVar()
    ArregloPos48=Entry(VentanaCodificacionREL,textvariable=Posicion48,width=5)
    ArregloPos48.grid(row=7,column=9,sticky=NSEW)
    Posicion49=StringVar()
    ArregloPos49=Entry(VentanaCodificacionREL,textvariable=Posicion49,width=5)
    ArregloPos49.grid(row=7,column=10,sticky=NSEW)
    Posicion50=StringVar()
    ArregloPos50=Entry(VentanaCodificacionREL,textvariable=Posicion50,width=5)
    ArregloPos50.grid(row=7,column=11,sticky=NSEW)

    #ArregloMatrizFila6
    Posicion51=StringVar()
    ArregloPos51=Entry(VentanaCodificacionREL,textvariable=Posicion51,width=5)
    ArregloPos51.grid(row=8,column=2,sticky=NSEW)
    Posicion52=StringVar()
    ArregloPos52=Entry(VentanaCodificacionREL,textvariable=Posicion52,width=5)
    ArregloPos52.grid(row=8,column=3,sticky=NSEW)
    Posicion53=StringVar()
    ArregloPos53=Entry(VentanaCodificacionREL,textvariable=Posicion53,width=5)
    ArregloPos53.grid(row=8,column=4,sticky=NSEW)
    Posicion54=StringVar()
    ArregloPos54=Entry(VentanaCodificacionREL,textvariable=Posicion54,width=5)
    ArregloPos54.grid(row=8,column=5,sticky=NSEW)
    Posicion55=StringVar()
    ArregloPos55=Entry(VentanaCodificacionREL,textvariable=Posicion55,width=5)
    ArregloPos55.grid(row=8,column=6,sticky=NSEW)
    Posicion56=StringVar()
    ArregloPos56=Entry(VentanaCodificacionREL,textvariable=Posicion56,width=5)
    ArregloPos56.grid(row=8,column=7,sticky=NSEW)
    Posicion57=StringVar()
    ArregloPos57=Entry(VentanaCodificacionREL,textvariable=Posicion57,width=5)
    ArregloPos57.grid(row=8,column=8,sticky=NSEW)
    Posicion58=StringVar()
    ArregloPos58=Entry(VentanaCodificacionREL,textvariable=Posicion58,width=5)
    ArregloPos58.grid(row=8,column=9,sticky=NSEW)
    Posicion59=StringVar()
    ArregloPos59=Entry(VentanaCodificacionREL,textvariable=Posicion59,width=5)
    ArregloPos59.grid(row=8,column=10,sticky=NSEW)
    Posicion60=StringVar()
    ArregloPos60=Entry(VentanaCodificacionREL,textvariable=Posicion60,width=5)
    ArregloPos60.grid(row=8,column=11,sticky=NSEW)

    #MatrizArregloFila7
    Posicion61=StringVar()
    ArregloPos61=Entry(VentanaCodificacionREL,textvariable=Posicion61,width=5)
    ArregloPos61.grid(row=9,column=2,sticky=NSEW)
    Posicion62=StringVar()
    ArregloPos62=Entry(VentanaCodificacionREL,textvariable=Posicion62,width=5)
    ArregloPos62.grid(row=9,column=3,sticky=NSEW)
    Posicion63=StringVar()
    ArregloPos63=Entry(VentanaCodificacionREL,textvariable=Posicion63,width=5)
    ArregloPos63.grid(row=9,column=4,sticky=NSEW)
    Posicion64=StringVar()
    ArregloPos64=Entry(VentanaCodificacionREL,textvariable=Posicion64,width=5)
    ArregloPos64.grid(row=9,column=5,sticky=NSEW)
    Posicion65=StringVar()
    ArregloPos65=Entry(VentanaCodificacionREL,textvariable=Posicion65,width=5)
    ArregloPos65.grid(row=9,column=6,sticky=NSEW)
    Posicion66=StringVar()
    ArregloPos66=Entry(VentanaCodificacionREL,textvariable=Posicion66,width=5)
    ArregloPos66.grid(row=9,column=7,sticky=NSEW)
    Posicion67=StringVar()
    ArregloPos67=Entry(VentanaCodificacionREL,textvariable=Posicion67,width=5)
    ArregloPos67.grid(row=9,column=8,sticky=NSEW)
    Posicion68=StringVar()
    ArregloPos68=Entry(VentanaCodificacionREL,textvariable=Posicion68,width=5)
    ArregloPos68.grid(row=9,column=9,sticky=NSEW)
    Posicion69=StringVar()
    ArregloPos69=Entry(VentanaCodificacionREL,textvariable=Posicion69,width=5)
    ArregloPos69.grid(row=9,column=10,sticky=NSEW)
    Posicion70=StringVar()
    ArregloPos70=Entry(VentanaCodificacionREL,textvariable=Posicion70,width=5)
    ArregloPos70.grid(row=9,column=11,sticky=NSEW)

    #ArregloMatrizFila8
    Posicion71=StringVar()
    ArregloPos71=Entry(VentanaCodificacionREL,textvariable=Posicion71,width=5)
    ArregloPos71.grid(row=10,column=2,sticky=NSEW)
    Posicion72=StringVar()
    ArregloPos72=Entry(VentanaCodificacionREL,textvariable=Posicion72,width=5)
    ArregloPos72.grid(row=10,column=3,sticky=NSEW)
    Posicion73=StringVar()
    ArregloPos73=Entry(VentanaCodificacionREL,textvariable=Posicion73,width=5)
    ArregloPos73.grid(row=10,column=4,sticky=NSEW)
    Posicion74=StringVar()
    ArregloPos74=Entry(VentanaCodificacionREL,textvariable=Posicion74,width=5)
    ArregloPos74.grid(row=10,column=5,sticky=NSEW)
    Posicion75=StringVar()
    ArregloPos75=Entry(VentanaCodificacionREL,textvariable=Posicion75,width=5)
    ArregloPos75.grid(row=10,column=6,sticky=NSEW)
    Posicion76=StringVar()
    ArregloPos76=Entry(VentanaCodificacionREL,textvariable=Posicion76,width=5)
    ArregloPos76.grid(row=10,column=7,sticky=NSEW)
    Posicion77=StringVar()
    ArregloPos77=Entry(VentanaCodificacionREL,textvariable=Posicion77,width=5)
    ArregloPos77.grid(row=10,column=8,sticky=NSEW)
    Posicion78=StringVar()
    ArregloPos78=Entry(VentanaCodificacionREL,textvariable=Posicion78,width=5)
    ArregloPos78.grid(row=10,column=9,sticky=NSEW)
    Posicion79=StringVar()
    ArregloPos79=Entry(VentanaCodificacionREL,textvariable=Posicion79,width=5)
    ArregloPos79.grid(row=10,column=10,sticky=NSEW)
    Posicion80=StringVar()
    ArregloPos80=Entry(VentanaCodificacionREL,textvariable=Posicion80,width=5)
    ArregloPos80.grid(row=10,column=11,sticky=NSEW)

    #ArregloMatrizFila9
    Posicion81=StringVar()
    ArregloPos81=Entry(VentanaCodificacionREL,textvariable=Posicion81,width=5)
    ArregloPos81.grid(row=11,column=2,sticky=NSEW)
    Posicion82=StringVar()
    ArregloPos82=Entry(VentanaCodificacionREL,textvariable=Posicion82,width=5)
    ArregloPos82.grid(row=11,column=3,sticky=NSEW)
    Posicion83=StringVar()
    ArregloPos83=Entry(VentanaCodificacionREL,textvariable=Posicion83,width=5)
    ArregloPos83.grid(row=11,column=4,sticky=NSEW)
    Posicion84=StringVar()
    ArregloPos84=Entry(VentanaCodificacionREL,textvariable=Posicion84,width=5)
    ArregloPos84.grid(row=11,column=5,sticky=NSEW)
    Posicion85=StringVar()
    ArregloPos85=Entry(VentanaCodificacionREL,textvariable=Posicion85,width=5)
    ArregloPos85.grid(row=11,column=6,sticky=NSEW)
    Posicion86=StringVar()
    ArregloPos86=Entry(VentanaCodificacionREL,textvariable=Posicion86,width=5)
    ArregloPos86.grid(row=11,column=7,sticky=NSEW)
    Posicion87=StringVar()
    ArregloPos87=Entry(VentanaCodificacionREL,textvariable=Posicion87,width=5)
    ArregloPos87.grid(row=11,column=8,sticky=NSEW)
    Posicion88=StringVar()
    ArregloPos88=Entry(VentanaCodificacionREL,textvariable=Posicion88,width=5)
    ArregloPos88.grid(row=11,column=9,sticky=NSEW)
    Posicion89=StringVar()
    ArregloPos89=Entry(VentanaCodificacionREL,textvariable=Posicion89,width=5)
    ArregloPos89.grid(row=11,column=10,sticky=NSEW)
    Posicion90=StringVar()
    ArregloPos90=Entry(VentanaCodificacionREL,textvariable=Posicion90,width=5)
    ArregloPos90.grid(row=11,column=11,sticky=NSEW)

    #ArregloMatrizFila10
    Posicion91=StringVar()
    ArregloPos91=Entry(VentanaCodificacionREL,textvariable=Posicion91,width=5)
    ArregloPos91.grid(row=12,column=2,sticky=NSEW)
    Posicion92=StringVar()
    ArregloPos92=Entry(VentanaCodificacionREL,textvariable=Posicion92,width=5)
    ArregloPos92.grid(row=12,column=3,sticky=NSEW)
    Posicion93=StringVar()
    ArregloPos93=Entry(VentanaCodificacionREL,textvariable=Posicion93,width=5)
    ArregloPos93.grid(row=12,column=4,sticky=NSEW)
    Posicion94=StringVar()
    ArregloPos94=Entry(VentanaCodificacionREL,textvariable=Posicion94,width=5)
    ArregloPos94.grid(row=12,column=5,sticky=NSEW)
    Posicion95=StringVar()
    ArregloPos95=Entry(VentanaCodificacionREL,textvariable=Posicion95,width=5)
    ArregloPos95.grid(row=12,column=6,sticky=NSEW)
    Posicion96=StringVar()
    ArregloPos96=Entry(VentanaCodificacionREL,textvariable=Posicion96,width=5)
    ArregloPos96.grid(row=12,column=7,sticky=NSEW)
    Posicion97=StringVar()
    ArregloPos97=Entry(VentanaCodificacionREL,textvariable=Posicion97,width=5)
    ArregloPos97.grid(row=12,column=8,sticky=NSEW)
    Posicion98=StringVar()
    ArregloPos98=Entry(VentanaCodificacionREL,textvariable=Posicion98,width=5)
    ArregloPos98.grid(row=12,column=9,sticky=NSEW)
    Posicion99=StringVar()
    ArregloPos99=Entry(VentanaCodificacionREL,textvariable=Posicion99,width=5)
    ArregloPos99.grid(row=12,column=10,sticky=NSEW)
    Posicion100=StringVar()
    ArregloPos100=Entry(VentanaCodificacionREL,textvariable=Posicion100,width=5)
    ArregloPos100.grid(row=12,column=11,sticky=NSEW)

    LabelMostrarGrupos=Label(VentanaCodificacionREL, text=" ")
    LabelMostrarGrupos.grid(row=4,column=0)
    LabelMostrarValores=Label(VentanaCodificacionREL, text=" ")
    LabelMostrarValores.grid(row=5,column=0)
    LabelMostrarMayorGrupo=Label(VentanaCodificacionREL, text=" ")
    LabelMostrarMayorGrupo.grid(row=6,column=0)
    LabelMostrarCaracteresTotales=Label(VentanaCodificacionREL, text=" ")
    LabelMostrarCaracteresTotales.grid(row=7,column=0)
    LabelMostrarTasaCompresion=Label(VentanaCodificacionREL, text=" ")
    LabelMostrarTasaCompresion.grid(row=8,column=0)
    LabelMostrarTramaTotal=Label(VentanaCodificacionREL, text=" ")
    LabelMostrarTramaTotal.grid(row=15,column=0,columnspan=20)

    Boton=Button(VentanaCodificacionREL, text="Iniciar Filas", command=lambda : RandomArregloFilas())
    Boton.grid(row=9, column=0)
    Boton2=Button(VentanaCodificacionREL, text="Iniciar Columnas", command=lambda : RandomArregloColumnas())
    Boton2.grid(row=10, column=0)
    Boton3=Button(VentanaCodificacionREL, text="Iniciar Zig Zag", command=lambda : RandomArregloZigZag())
    Boton3.grid(row=11,column=0)
    BotonCalculo=Button(VentanaCodificacionREL, text="Calculo Por Filas", command=lambda : AgruparLecturaFilas(CrearMatriz()))
    BotonCalculo.grid(row=12, column=0)
    BotonCalculo2=Button(VentanaCodificacionREL, text="Calculo Por Columnas", command=lambda : AgruparLecturaColumnas(CrearMatriz()))
    BotonCalculo2.grid(row=13, column=0)
    BotonCalculo3=Button(VentanaCodificacionREL, text="Calculo Por Zig Zag", command=lambda : AgruparLecturaZigZag(CrearMatriz()))
    BotonCalculo3.grid(row=14,column=0)

    BotonGuardar3=Button(framecito, text="Guardar Trama Final", width=25, command=Guardar)
    BotonGuardar3.grid(row=16, column=0)
    LabelGuardarTramaTotal3=Label(VentanaCodificacionREL, text=" ") 
    LabelGuardarTramaTotal3.grid(row=17, column=0)
    BotonVolver3=Button(framecito, text="Regresar", width=25, command=Volver)
    BotonVolver3.grid(row=18, column=0)
    LabelError=Label(VentanaCodificacionREL, text=" Se sugiere que use la matriz por filas")
    LabelError.grid(row=20, column=0)

    VentanaCodificacionREL.mainloop()

#Funcion Codificacion DCPM
def CodificacionDCPM():
    ventana.withdraw()
    #Funcion crear matrices
    def CreacionMatrices():
        Matriz=np.array([
        [Posicion1.get(), Posicion2.get(), Posicion3.get(), Posicion4.get(), Posicion5.get(), Posicion6.get(), Posicion7.get(), Posicion8.get(), Posicion9.get(), Posicion10.get()],
        [Posicion11.get(), Posicion12.get(), Posicion13.get(), Posicion14.get(), Posicion15.get(), Posicion16.get(), Posicion17.get(), Posicion18.get(), Posicion19.get(), Posicion20.get()],
        [Posicion21.get(), Posicion22.get(), Posicion23.get(), Posicion24.get(), Posicion25.get(), Posicion26.get(), Posicion27.get(), Posicion28.get(), Posicion29.get(), Posicion30.get()],
        [Posicion31.get(), Posicion32.get(), Posicion33.get(), Posicion34.get(), Posicion35.get(), Posicion36.get(), Posicion37.get(), Posicion38.get(), Posicion39.get(), Posicion40.get()],
        [Posicion41.get(), Posicion42.get(), Posicion43.get(), Posicion44.get(), Posicion45.get(), Posicion46.get(), Posicion47.get(), Posicion48.get(), Posicion49.get(), Posicion50.get()],
        [Posicion51.get(), Posicion52.get(), Posicion53.get(), Posicion54.get(), Posicion55.get(), Posicion56.get(), Posicion57.get(), Posicion58.get(), Posicion59.get(), Posicion60.get()],
        [Posicion61.get(), Posicion62.get(), Posicion63.get(), Posicion64.get(), Posicion65.get(), Posicion66.get(), Posicion67.get(), Posicion68.get(), Posicion69.get(), Posicion70.get()],
        [Posicion71.get(), Posicion72.get(), Posicion73.get(), Posicion74.get(), Posicion75.get(), Posicion76.get(), Posicion77.get(), Posicion78.get(), Posicion79.get(), Posicion80.get()],
        [Posicion81.get(), Posicion82.get(), Posicion83.get(), Posicion84.get(), Posicion85.get(), Posicion86.get(), Posicion87.get(), Posicion88.get(), Posicion89.get(), Posicion90.get()],
        [Posicion91.get(), Posicion92.get(), Posicion93.get(), Posicion94.get(), Posicion95.get(), Posicion96.get(), Posicion97.get(), Posicion98.get(), Posicion99.get(), Posicion100.get()]],dtype=np.dtype('U100'))
        
        Matriz2=np.array([
        [Posicion1.get(), Posicion2.get(), Posicion3.get(), Posicion4.get(), Posicion5.get(), Posicion6.get(), Posicion7.get(), Posicion8.get(), Posicion9.get(), Posicion10.get()],
        [Posicion11.get(), Posicion12.get(), Posicion13.get(), Posicion14.get(), Posicion15.get(), Posicion16.get(), Posicion17.get(), Posicion18.get(), Posicion19.get(), Posicion20.get()],
        [Posicion21.get(), Posicion22.get(), Posicion23.get(), Posicion24.get(), Posicion25.get(), Posicion26.get(), Posicion27.get(), Posicion28.get(), Posicion29.get(), Posicion30.get()],
        [Posicion31.get(), Posicion32.get(), Posicion33.get(), Posicion34.get(), Posicion35.get(), Posicion36.get(), Posicion37.get(), Posicion38.get(), Posicion39.get(), Posicion40.get()],
        [Posicion41.get(), Posicion42.get(), Posicion43.get(), Posicion44.get(), Posicion45.get(), Posicion46.get(), Posicion47.get(), Posicion48.get(), Posicion49.get(), Posicion50.get()],
        [Posicion51.get(), Posicion52.get(), Posicion53.get(), Posicion54.get(), Posicion55.get(), Posicion56.get(), Posicion57.get(), Posicion58.get(), Posicion59.get(), Posicion60.get()],
        [Posicion61.get(), Posicion62.get(), Posicion63.get(), Posicion64.get(), Posicion65.get(), Posicion66.get(), Posicion67.get(), Posicion68.get(), Posicion69.get(), Posicion70.get()],
        [Posicion71.get(), Posicion72.get(), Posicion73.get(), Posicion74.get(), Posicion75.get(), Posicion76.get(), Posicion77.get(), Posicion78.get(), Posicion79.get(), Posicion80.get()],
        [Posicion81.get(), Posicion82.get(), Posicion83.get(), Posicion84.get(), Posicion85.get(), Posicion86.get(), Posicion87.get(), Posicion88.get(), Posicion89.get(), Posicion90.get()],
        [Posicion91.get(), Posicion92.get(), Posicion93.get(), Posicion94.get(), Posicion95.get(), Posicion96.get(), Posicion97.get(), Posicion98.get(), Posicion99.get(), Posicion100.get()]],dtype=np.dtype('U100'))

        Minimo=ValorMinimoRandom.get()
        Maximo=ValorMaximoRandom.get()
        MaximaDiferencia=Intervalo.get()
        validar=0
        i=0
        while i<=9:
            j=0
            while j<=9:   
                Val=random.randint(int(Minimo),int(Maximo))
                Matriz[i,j]=Val        
                if (i==0 and j==0):
                    Matriz2[i,j]=Matriz[i,j]
                else:
                    if(j!=0):
                        Actual=int(Matriz[i,j])
                        Anterior=int(Matriz[i,j-1])
                    else:
                        Actual=int(Matriz[i,j])
                        Anterior=int(Matriz[i-1,9])
                    Diferencia=int(Actual-Anterior)
                    if(Diferencia*-1)>int(MaximaDiferencia):
                        validar=1
                    elif(Diferencia)>int(MaximaDiferencia):
                        validar=1
                    else:
                        validar=0
                    while validar==1:
                        Val=random.randint(int(Minimo),int(Maximo))
                        Matriz[i,j]=Val
                        if (i==0 and j==0):
                            Matriz2[i,j]=Matriz[i,j]
                        else:
                            if(j!=0):
                                Actual=int(Matriz[i,j])
                                Anterior=int(Matriz[i,j-1])
                            else:
                                Actual=int(Matriz[i,j])
                                Anterior=int(Matriz[i-1,9])
                            Diferencia=int(Actual-Anterior)
                        if(Diferencia*-1)>int(MaximaDiferencia):
                            validar=1
                        elif(Diferencia)>int(MaximaDiferencia):
                            validar=1
                        else:
                            validar=0
                    Matriz2[i,j]=Diferencia          
                j=j+1
            i=i+1
        
        lista1=[Matriz[0,0],Matriz[0,1],Matriz[0,2],Matriz[0,3],Matriz[0,4],Matriz[0,5],Matriz[0,6],Matriz[0,7],Matriz[0,8],Matriz[0,9]]        
        lista2=[Matriz[1,0],Matriz[1,1],Matriz[1,2],Matriz[1,3],Matriz[1,4],Matriz[1,5],Matriz[1,6],Matriz[1,7],Matriz[1,8],Matriz[1,9]]
        lista3=[Matriz[2,0],Matriz[2,1],Matriz[2,2],Matriz[2,3],Matriz[2,4],Matriz[2,5],Matriz[2,6],Matriz[2,7],Matriz[2,8],Matriz[2,9]]
        lista4=[Matriz[3,0],Matriz[3,1],Matriz[3,2],Matriz[3,3],Matriz[3,4],Matriz[3,5],Matriz[3,6],Matriz[3,7],Matriz[3,8],Matriz[3,9]]
        lista5=[Matriz[4,0],Matriz[4,1],Matriz[4,2],Matriz[4,3],Matriz[4,4],Matriz[4,5],Matriz[4,6],Matriz[4,7],Matriz[4,8],Matriz[4,9]]
        lista6=[Matriz[5,0],Matriz[5,1],Matriz[5,2],Matriz[5,3],Matriz[5,4],Matriz[5,5],Matriz[5,6],Matriz[5,7],Matriz[5,8],Matriz[5,9]]
        lista7=[Matriz[6,0],Matriz[6,1],Matriz[6,2],Matriz[6,3],Matriz[6,4],Matriz[6,5],Matriz[6,6],Matriz[6,7],Matriz[6,8],Matriz[6,9]]
        lista8=[Matriz[7,0],Matriz[7,1],Matriz[7,2],Matriz[7,3],Matriz[7,4],Matriz[7,5],Matriz[7,6],Matriz[7,7],Matriz[7,8],Matriz[7,9]]
        lista9=[Matriz[8,0],Matriz[8,1],Matriz[8,2],Matriz[8,3],Matriz[8,4],Matriz[8,5],Matriz[8,6],Matriz[8,7],Matriz[8,8],Matriz[8,9]]
        lista10=[Matriz[9,0],Matriz[9,1],Matriz[9,2],Matriz[9,3],Matriz[9,4],Matriz[9,5],Matriz[9,6],Matriz[9,7],Matriz[9,8],Matriz[9,9]]

        Dlista1=[Matriz2[0,0],Matriz2[0,1],Matriz2[0,2],Matriz2[0,3],Matriz2[0,4],Matriz2[0,5],Matriz2[0,6],Matriz2[0,7],Matriz2[0,8],Matriz2[0,9]]        
        Dlista2=[Matriz2[1,0],Matriz2[1,1],Matriz2[1,2],Matriz2[1,3],Matriz2[1,4],Matriz2[1,5],Matriz2[1,6],Matriz2[1,7],Matriz2[1,8],Matriz2[1,9]]
        Dlista3=[Matriz2[2,0],Matriz2[2,1],Matriz2[2,2],Matriz2[2,3],Matriz2[2,4],Matriz2[2,5],Matriz2[2,6],Matriz2[2,7],Matriz2[2,8],Matriz2[2,9]]
        Dlista4=[Matriz2[3,0],Matriz2[3,1],Matriz2[3,2],Matriz2[3,3],Matriz2[3,4],Matriz2[3,5],Matriz2[3,6],Matriz2[3,7],Matriz2[3,8],Matriz2[3,9]]
        Dlista5=[Matriz2[4,0],Matriz2[4,1],Matriz2[4,2],Matriz2[4,3],Matriz2[4,4],Matriz2[4,5],Matriz2[4,6],Matriz2[4,7],Matriz2[4,8],Matriz2[4,9]]
        Dlista6=[Matriz2[5,0],Matriz2[5,1],Matriz2[5,2],Matriz2[5,3],Matriz2[5,4],Matriz2[5,5],Matriz2[5,6],Matriz2[5,7],Matriz2[5,8],Matriz2[5,9]]
        Dlista7=[Matriz2[6,0],Matriz2[6,1],Matriz2[6,2],Matriz2[6,3],Matriz2[6,4],Matriz2[6,5],Matriz2[6,6],Matriz2[6,7],Matriz2[6,8],Matriz2[6,9]]
        Dlista8=[Matriz2[7,0],Matriz2[7,1],Matriz2[7,2],Matriz2[7,3],Matriz2[7,4],Matriz2[7,5],Matriz2[7,6],Matriz2[7,7],Matriz2[7,8],Matriz2[7,9]]
        Dlista9=[Matriz2[8,0],Matriz2[8,1],Matriz2[8,2],Matriz2[8,3],Matriz2[8,4],Matriz2[8,5],Matriz2[8,6],Matriz2[8,7],Matriz2[8,8],Matriz2[8,9]]
        Dlista10=[Matriz2[9,0],Matriz2[9,1],Matriz2[9,2],Matriz2[9,3],Matriz2[9,4],Matriz2[9,5],Matriz2[9,6],Matriz2[9,7],Matriz2[9,8],Matriz2[9,9]]

        #Textos Matriz Diferencias
        Dtexto1=str(Dlista1[0])
        DArregloPos1.delete(0,END)
        DArregloPos1.insert(0,Dtexto1)
        Dtexto2=str(Dlista1[1])
        DArregloPos2.delete(0,END)
        DArregloPos2.insert(0,Dtexto2)
        Dtexto3=str(Dlista1[2])
        DArregloPos3.delete(0,END)
        DArregloPos3.insert(0,Dtexto3)
        Dtexto4=str(Dlista1[3])
        DArregloPos4.delete(0,END)
        DArregloPos4.insert(0,Dtexto4)
        Dtexto5=str(Dlista1[4])
        DArregloPos5.delete(0,END)
        DArregloPos5.insert(0,Dtexto5)
        Dtexto6=str(Dlista1[5])
        DArregloPos6.delete(0,END)
        DArregloPos6.insert(0,Dtexto6)
        Dtexto7=str(Dlista1[6])
        DArregloPos7.delete(0,END)
        DArregloPos7.insert(0,Dtexto7)
        Dtexto8=str(Dlista1[7])
        DArregloPos8.delete(0,END)
        DArregloPos8.insert(0,Dtexto8)
        Dtexto9=str(Dlista1[8])
        DArregloPos9.delete(0,END)
        DArregloPos9.insert(0,Dtexto9)
        Dtexto10=str(Dlista1[9])
        DArregloPos10.delete(0,END)
        DArregloPos10.insert(0,Dtexto10)

        Dtexto11=str(Dlista2[0])
        DArregloPos11.delete(0,END)
        DArregloPos11.insert(0,Dtexto11)
        Dtexto12=str(Dlista2[1])
        DArregloPos12.delete(0,END)
        DArregloPos12.insert(0,Dtexto12)
        Dtexto13=str(Dlista2[2])
        DArregloPos13.delete(0,END)
        DArregloPos13.insert(0,Dtexto13)
        Dtexto14=str(Dlista2[3])
        DArregloPos14.delete(0,END)
        DArregloPos14.insert(0,Dtexto14)
        Dtexto15=str(Dlista2[4])
        DArregloPos15.delete(0,END)
        DArregloPos15.insert(0,Dtexto15)
        Dtexto16=str(Dlista2[5])
        DArregloPos16.delete(0,END)
        DArregloPos16.insert(0,Dtexto16)
        Dtexto17=str(Dlista2[6])
        DArregloPos17.delete(0,END)
        DArregloPos17.insert(0,Dtexto17)
        Dtexto18=str(Dlista2[7])
        DArregloPos18.delete(0,END)
        DArregloPos18.insert(0,Dtexto18)
        Dtexto19=str(Dlista2[8])
        DArregloPos19.delete(0,END)
        DArregloPos19.insert(0,Dtexto19)
        Dtexto20=str(Dlista2[9])
        DArregloPos20.delete(0,END)
        DArregloPos20.insert(0,Dtexto20)

        Dtexto21=str(Dlista3[0])
        DArregloPos21.delete(0,END)
        DArregloPos21.insert(0,Dtexto21)
        Dtexto22=str(Dlista3[1])
        DArregloPos22.delete(0,END)
        DArregloPos22.insert(0,Dtexto22)
        Dtexto23=str(Dlista3[2])
        DArregloPos23.delete(0,END)
        DArregloPos23.insert(0,Dtexto23)
        Dtexto24=str(Dlista3[3])
        DArregloPos24.delete(0,END)
        DArregloPos24.insert(0,Dtexto24)
        Dtexto25=str(Dlista3[4])
        DArregloPos25.delete(0,END)
        DArregloPos25.insert(0,Dtexto25)
        Dtexto26=str(Dlista3[5])
        DArregloPos26.delete(0,END)
        DArregloPos26.insert(0,Dtexto26)
        Dtexto27=str(Dlista3[6])
        DArregloPos27.delete(0,END)
        DArregloPos27.insert(0,Dtexto27)
        Dtexto28=str(Dlista3[7])
        DArregloPos28.delete(0,END)
        DArregloPos28.insert(0,Dtexto28)
        Dtexto29=str(Dlista3[8])
        DArregloPos29.delete(0,END)
        DArregloPos29.insert(0,Dtexto29)
        Dtexto30=str(Dlista3[9])
        DArregloPos30.delete(0,END)
        DArregloPos30.insert(0,Dtexto30)

        Dtexto31=str(Dlista4[0])
        DArregloPos31.delete(0,END)
        DArregloPos31.insert(0,Dtexto31)
        Dtexto32=str(Dlista4[1])
        DArregloPos32.delete(0,END)
        DArregloPos32.insert(0,Dtexto32)
        Dtexto33=str(Dlista4[2])
        DArregloPos33.delete(0,END)
        DArregloPos33.insert(0,Dtexto33)
        Dtexto34=str(Dlista4[3])
        DArregloPos34.delete(0,END)
        DArregloPos34.insert(0,Dtexto34)
        Dtexto35=str(Dlista4[4])
        DArregloPos35.delete(0,END)
        DArregloPos35.insert(0,Dtexto35)
        Dtexto36=str(Dlista4[5])
        DArregloPos36.delete(0,END)
        DArregloPos36.insert(0,Dtexto36)
        Dtexto37=str(Dlista4[6])
        DArregloPos37.delete(0,END)
        DArregloPos37.insert(0,Dtexto37)
        Dtexto38=str(Dlista4[7])
        DArregloPos38.delete(0,END)
        DArregloPos38.insert(0,Dtexto38)
        Dtexto39=str(Dlista4[8])
        DArregloPos39.delete(0,END)
        DArregloPos39.insert(0,Dtexto39)
        Dtexto40=str(Dlista4[9])
        DArregloPos40.delete(0,END)
        DArregloPos40.insert(0,Dtexto40)

        Dtexto41=str(Dlista5[0])
        DArregloPos41.delete(0,END)
        DArregloPos41.insert(0,Dtexto41)
        Dtexto42=str(Dlista5[1])
        DArregloPos42.delete(0,END)
        DArregloPos42.insert(0,Dtexto42)
        Dtexto43=str(Dlista5[2])
        DArregloPos43.delete(0,END)
        DArregloPos43.insert(0,Dtexto43)
        Dtexto44=str(Dlista5[3])
        DArregloPos44.delete(0,END)
        DArregloPos44.insert(0,Dtexto44)
        Dtexto45=str(Dlista5[4])
        DArregloPos45.delete(0,END)
        DArregloPos45.insert(0,Dtexto45)
        Dtexto46=str(Dlista5[5])
        DArregloPos46.delete(0,END)
        DArregloPos46.insert(0,Dtexto46)
        Dtexto47=str(Dlista5[6])
        DArregloPos47.delete(0,END)
        DArregloPos47.insert(0,Dtexto47)
        Dtexto48=str(Dlista5[7])
        DArregloPos48.delete(0,END)
        DArregloPos48.insert(0,Dtexto48)
        Dtexto49=str(Dlista5[8])
        DArregloPos49.delete(0,END)
        DArregloPos49.insert(0,Dtexto49)
        Dtexto50=str(Dlista5[9])
        DArregloPos50.delete(0,END)
        DArregloPos50.insert(0,Dtexto50)

        Dtexto51=str(Dlista6[0])
        DArregloPos51.delete(0,END)
        DArregloPos51.insert(0,Dtexto51)
        Dtexto52=str(Dlista6[1])
        DArregloPos52.delete(0,END)
        DArregloPos52.insert(0,Dtexto52)
        Dtexto53=str(Dlista6[2])
        DArregloPos53.delete(0,END)
        DArregloPos53.insert(0,Dtexto53)
        Dtexto54=str(Dlista6[3])
        DArregloPos54.delete(0,END)
        DArregloPos54.insert(0,Dtexto54)
        Dtexto55=str(Dlista6[4])
        DArregloPos55.delete(0,END)
        DArregloPos55.insert(0,Dtexto55)
        Dtexto56=str(Dlista6[5])
        DArregloPos56.delete(0,END)
        DArregloPos56.insert(0,Dtexto56)
        Dtexto57=str(Dlista6[6])
        DArregloPos57.delete(0,END)
        DArregloPos57.insert(0,Dtexto57)
        Dtexto58=str(Dlista6[7])
        DArregloPos58.delete(0,END)
        DArregloPos58.insert(0,Dtexto58)
        Dtexto59=str(Dlista6[8])
        DArregloPos59.delete(0,END)
        DArregloPos59.insert(0,Dtexto59)
        Dtexto60=str(Dlista6[9])
        DArregloPos60.delete(0,END)
        DArregloPos60.insert(0,Dtexto60)

        Dtexto61=str(Dlista7[0])
        DArregloPos61.delete(0,END)
        DArregloPos61.insert(0,Dtexto61)
        Dtexto62=str(Dlista7[1])
        DArregloPos62.delete(0,END)
        DArregloPos62.insert(0,Dtexto62)
        Dtexto63=str(Dlista7[2])
        DArregloPos63.delete(0,END)
        DArregloPos63.insert(0,Dtexto63)
        Dtexto64=str(Dlista7[3])
        DArregloPos64.delete(0,END)
        DArregloPos64.insert(0,Dtexto64)
        Dtexto65=str(Dlista7[4])
        DArregloPos65.delete(0,END)
        DArregloPos65.insert(0,Dtexto65)
        Dtexto66=str(Dlista7[5])
        DArregloPos66.delete(0,END)
        DArregloPos66.insert(0,Dtexto66)
        Dtexto67=str(Dlista7[6])
        DArregloPos67.delete(0,END)
        DArregloPos67.insert(0,Dtexto67)
        Dtexto68=str(Dlista7[7])
        DArregloPos68.delete(0,END)
        DArregloPos68.insert(0,Dtexto68)
        Dtexto69=str(Dlista7[8])
        DArregloPos69.delete(0,END)
        DArregloPos69.insert(0,Dtexto69)
        Dtexto70=str(Dlista7[9])
        DArregloPos70.delete(0,END)
        DArregloPos70.insert(0,Dtexto70)

        Dtexto71=str(Dlista8[0])
        DArregloPos71.delete(0,END)
        DArregloPos71.insert(0,Dtexto71)
        Dtexto72=str(Dlista8[1])
        DArregloPos72.delete(0,END)
        DArregloPos72.insert(0,Dtexto72)
        Dtexto73=str(Dlista8[2])
        DArregloPos73.delete(0,END)
        DArregloPos73.insert(0,Dtexto73)
        Dtexto74=str(Dlista8[3])
        DArregloPos74.delete(0,END)
        DArregloPos74.insert(0,Dtexto74)
        Dtexto75=str(Dlista8[4])
        DArregloPos75.delete(0,END)
        DArregloPos75.insert(0,Dtexto75)
        Dtexto76=str(Dlista8[5])
        DArregloPos76.delete(0,END)
        DArregloPos76.insert(0,Dtexto76)
        Dtexto77=str(Dlista8[6])
        DArregloPos77.delete(0,END)
        DArregloPos77.insert(0,Dtexto77)
        Dtexto78=str(Dlista8[7])
        DArregloPos78.delete(0,END)
        DArregloPos78.insert(0,Dtexto78)
        Dtexto79=str(Dlista8[8])
        DArregloPos79.delete(0,END)
        DArregloPos79.insert(0,Dtexto79)
        Dtexto80=str(Dlista8[9])
        DArregloPos80.delete(0,END)
        DArregloPos80.insert(0,Dtexto80)

        Dtexto81=str(Dlista9[0])
        DArregloPos81.delete(0,END)
        DArregloPos81.insert(0,Dtexto81)
        Dtexto82=str(Dlista9[1])
        DArregloPos82.delete(0,END)
        DArregloPos82.insert(0,Dtexto82)
        Dtexto83=str(Dlista9[2])
        DArregloPos83.delete(0,END)
        DArregloPos83.insert(0,Dtexto83)
        Dtexto84=str(Dlista9[3])
        DArregloPos84.delete(0,END)
        DArregloPos84.insert(0,Dtexto84)
        Dtexto85=str(Dlista9[4])
        DArregloPos85.delete(0,END)
        DArregloPos85.insert(0,Dtexto85)
        Dtexto86=str(Dlista9[5])
        DArregloPos86.delete(0,END)
        DArregloPos86.insert(0,Dtexto86)
        Dtexto87=str(Dlista9[6])
        DArregloPos87.delete(0,END)
        DArregloPos87.insert(0,Dtexto87)
        Dtexto88=str(Dlista9[7])
        DArregloPos88.delete(0,END)
        DArregloPos88.insert(0,Dtexto88)
        Dtexto89=str(Dlista9[8])
        DArregloPos89.delete(0,END)
        DArregloPos89.insert(0,Dtexto89)
        Dtexto90=str(Dlista9[9])
        DArregloPos90.delete(0,END)
        DArregloPos90.insert(0,Dtexto90)

        Dtexto91=str(Dlista10[0])
        DArregloPos91.delete(0,END)
        DArregloPos91.insert(0,Dtexto91)
        Dtexto92=str(Dlista10[1])
        DArregloPos92.delete(0,END)
        DArregloPos92.insert(0,Dtexto92)
        Dtexto93=str(Dlista10[2])
        DArregloPos93.delete(0,END)
        DArregloPos93.insert(0,Dtexto93)
        Dtexto94=str(Dlista10[3])
        DArregloPos94.delete(0,END)
        DArregloPos94.insert(0,Dtexto94)
        Dtexto95=str(Dlista10[4])
        DArregloPos95.delete(0,END)
        DArregloPos95.insert(0,Dtexto95)
        Dtexto96=str(Dlista10[5])
        DArregloPos96.delete(0,END)
        DArregloPos96.insert(0,Dtexto96)
        Dtexto97=str(Dlista10[6])
        DArregloPos97.delete(0,END)
        DArregloPos97.insert(0,Dtexto97)
        Dtexto98=str(Dlista10[7])
        DArregloPos98.delete(0,END)
        DArregloPos98.insert(0,Dtexto98)
        Dtexto99=str(Dlista10[8])
        DArregloPos99.delete(0,END)
        DArregloPos99.insert(0,Dtexto99)
        Dtexto100=str(Dlista10[9])
        DArregloPos100.delete(0,END)
        DArregloPos100.insert(0,Dtexto100)

        #Textos Matriz Original
        texto1=str(lista1[0])
        ArregloPos1.delete(0,END)
        ArregloPos1.insert(0,texto1)
        texto2=str(lista1[1])
        ArregloPos2.delete(0,END)
        ArregloPos2.insert(0,texto2)
        texto3=str(lista1[2])
        ArregloPos3.delete(0,END)
        ArregloPos3.insert(0,texto3)
        texto4=str(lista1[3])
        ArregloPos4.delete(0,END)
        ArregloPos4.insert(0,texto4)
        texto5=str(lista1[4])
        ArregloPos5.delete(0,END)
        ArregloPos5.insert(0,texto5)
        texto6=str(lista1[5])
        ArregloPos6.delete(0,END)
        ArregloPos6.insert(0,texto6)
        texto7=str(lista1[6])
        ArregloPos7.delete(0,END)
        ArregloPos7.insert(0,texto7)
        texto8=str(lista1[7])
        ArregloPos8.delete(0,END)
        ArregloPos8.insert(0,texto8)
        texto9=str(lista1[8])
        ArregloPos9.delete(0,END)
        ArregloPos9.insert(0,texto9)
        texto10=str(lista1[9])
        ArregloPos10.delete(0,END)
        ArregloPos10.insert(0,texto10)

        texto11=str(lista2[0])
        ArregloPos11.delete(0,END)
        ArregloPos11.insert(0,texto11)
        texto12=str(lista2[1])
        ArregloPos12.delete(0,END)
        ArregloPos12.insert(0,texto12)
        texto13=str(lista2[2])
        ArregloPos13.delete(0,END)
        ArregloPos13.insert(0,texto13)
        texto14=str(lista2[3])
        ArregloPos14.delete(0,END)
        ArregloPos14.insert(0,texto14)
        texto15=str(lista2[4])
        ArregloPos15.delete(0,END)
        ArregloPos15.insert(0,texto15)
        texto16=str(lista2[5])
        ArregloPos16.delete(0,END)
        ArregloPos16.insert(0,texto16)
        texto17=str(lista2[6])
        ArregloPos17.delete(0,END)
        ArregloPos17.insert(0,texto17)
        texto18=str(lista2[7])
        ArregloPos18.delete(0,END)
        ArregloPos18.insert(0,texto18)
        texto19=str(lista2[8])
        ArregloPos19.delete(0,END)
        ArregloPos19.insert(0,texto19)
        texto20=str(lista2[9])
        ArregloPos20.delete(0,END)
        ArregloPos20.insert(0,texto20)

        texto21=str(lista3[0])
        ArregloPos21.delete(0,END)
        ArregloPos21.insert(0,texto21)
        texto22=str(lista3[1])
        ArregloPos22.delete(0,END)
        ArregloPos22.insert(0,texto22)
        texto23=str(lista3[2])
        ArregloPos23.delete(0,END)
        ArregloPos23.insert(0,texto23)
        texto24=str(lista3[3])
        ArregloPos24.delete(0,END)
        ArregloPos24.insert(0,texto24)
        texto25=str(lista3[4])
        ArregloPos25.delete(0,END)
        ArregloPos25.insert(0,texto25)
        texto26=str(lista3[5])
        ArregloPos26.delete(0,END)
        ArregloPos26.insert(0,texto26)
        texto27=str(lista3[6])
        ArregloPos27.delete(0,END)
        ArregloPos27.insert(0,texto27)
        texto28=str(lista3[7])
        ArregloPos28.delete(0,END)
        ArregloPos28.insert(0,texto28)
        texto29=str(lista3[8])
        ArregloPos29.delete(0,END)
        ArregloPos29.insert(0,texto29)
        texto30=str(lista3[9])
        ArregloPos30.delete(0,END)
        ArregloPos30.insert(0,texto30)

        texto31=str(lista4[0])
        ArregloPos31.delete(0,END)
        ArregloPos31.insert(0,texto31)
        texto32=str(lista4[1])
        ArregloPos32.delete(0,END)
        ArregloPos32.insert(0,texto32)
        texto33=str(lista4[2])
        ArregloPos33.delete(0,END)
        ArregloPos33.insert(0,texto33)
        texto34=str(lista4[3])
        ArregloPos34.delete(0,END)
        ArregloPos34.insert(0,texto34)
        texto35=str(lista4[4])
        ArregloPos35.delete(0,END)
        ArregloPos35.insert(0,texto35)
        texto36=str(lista4[5])
        ArregloPos36.delete(0,END)
        ArregloPos36.insert(0,texto36)
        texto37=str(lista4[6])
        ArregloPos37.delete(0,END)
        ArregloPos37.insert(0,texto37)
        texto38=str(lista4[7])
        ArregloPos38.delete(0,END)
        ArregloPos38.insert(0,texto38)
        texto39=str(lista4[8])
        ArregloPos39.delete(0,END)
        ArregloPos39.insert(0,texto39)
        texto40=str(lista4[9])
        ArregloPos40.delete(0,END)
        ArregloPos40.insert(0,texto40)

        texto41=str(lista5[0])
        ArregloPos41.delete(0,END)
        ArregloPos41.insert(0,texto41)
        texto42=str(lista5[1])
        ArregloPos42.delete(0,END)
        ArregloPos42.insert(0,texto42)
        texto43=str(lista5[2])
        ArregloPos43.delete(0,END)
        ArregloPos43.insert(0,texto43)
        texto44=str(lista5[3])
        ArregloPos44.delete(0,END)
        ArregloPos44.insert(0,texto44)
        texto45=str(lista5[4])
        ArregloPos45.delete(0,END)
        ArregloPos45.insert(0,texto45)
        texto46=str(lista5[5])
        ArregloPos46.delete(0,END)
        ArregloPos46.insert(0,texto46)
        texto47=str(lista5[6])
        ArregloPos47.delete(0,END)
        ArregloPos47.insert(0,texto47)
        texto48=str(lista5[7])
        ArregloPos48.delete(0,END)
        ArregloPos48.insert(0,texto48)
        texto49=str(lista5[8])
        ArregloPos49.delete(0,END)
        ArregloPos49.insert(0,texto49)
        texto50=str(lista5[9])
        ArregloPos50.delete(0,END)
        ArregloPos50.insert(0,texto50)

        texto51=str(lista6[0])
        ArregloPos51.delete(0,END)
        ArregloPos51.insert(0,texto51)
        texto52=str(lista6[1])
        ArregloPos52.delete(0,END)
        ArregloPos52.insert(0,texto52)
        texto53=str(lista6[2])
        ArregloPos53.delete(0,END)
        ArregloPos53.insert(0,texto53)
        texto54=str(lista6[3])
        ArregloPos54.delete(0,END)
        ArregloPos54.insert(0,texto54)
        texto55=str(lista6[4])
        ArregloPos55.delete(0,END)
        ArregloPos55.insert(0,texto55)
        texto56=str(lista6[5])
        ArregloPos56.delete(0,END)
        ArregloPos56.insert(0,texto56)
        texto57=str(lista6[6])
        ArregloPos57.delete(0,END)
        ArregloPos57.insert(0,texto57)
        texto58=str(lista6[7])
        ArregloPos58.delete(0,END)
        ArregloPos58.insert(0,texto58)
        texto59=str(lista6[8])
        ArregloPos59.delete(0,END)
        ArregloPos59.insert(0,texto59)
        texto60=str(lista6[9])
        ArregloPos60.delete(0,END)
        ArregloPos60.insert(0,texto60)

        texto61=str(lista7[0])
        ArregloPos61.delete(0,END)
        ArregloPos61.insert(0,texto61)
        texto62=str(lista7[1])
        ArregloPos62.delete(0,END)
        ArregloPos62.insert(0,texto62)
        texto63=str(lista7[2])
        ArregloPos63.delete(0,END)
        ArregloPos63.insert(0,texto63)
        texto64=str(lista7[3])
        ArregloPos64.delete(0,END)
        ArregloPos64.insert(0,texto64)
        texto65=str(lista7[4])
        ArregloPos65.delete(0,END)
        ArregloPos65.insert(0,texto65)
        texto66=str(lista7[5])
        ArregloPos66.delete(0,END)
        ArregloPos66.insert(0,texto66)
        texto67=str(lista7[6])
        ArregloPos67.delete(0,END)
        ArregloPos67.insert(0,texto67)
        texto68=str(lista7[7])
        ArregloPos68.delete(0,END)
        ArregloPos68.insert(0,texto68)
        texto69=str(lista7[8])
        ArregloPos69.delete(0,END)
        ArregloPos69.insert(0,texto69)
        texto70=str(lista7[9])
        ArregloPos70.delete(0,END)
        ArregloPos70.insert(0,texto70)

        texto71=str(lista8[0])
        ArregloPos71.delete(0,END)
        ArregloPos71.insert(0,texto71)
        texto72=str(lista8[1])
        ArregloPos72.delete(0,END)
        ArregloPos72.insert(0,texto72)
        texto73=str(lista8[2])
        ArregloPos73.delete(0,END)
        ArregloPos73.insert(0,texto73)
        texto74=str(lista8[3])
        ArregloPos74.delete(0,END)
        ArregloPos74.insert(0,texto74)
        texto75=str(lista8[4])
        ArregloPos75.delete(0,END)
        ArregloPos75.insert(0,texto75)
        texto76=str(lista8[5])
        ArregloPos76.delete(0,END)
        ArregloPos76.insert(0,texto76)
        texto77=str(lista8[6])
        ArregloPos77.delete(0,END)
        ArregloPos77.insert(0,texto77)
        texto78=str(lista8[7])
        ArregloPos78.delete(0,END)
        ArregloPos78.insert(0,texto78)
        texto79=str(lista8[8])
        ArregloPos79.delete(0,END)
        ArregloPos79.insert(0,texto79)
        texto80=str(lista8[9])
        ArregloPos80.delete(0,END)
        ArregloPos80.insert(0,texto80)

        texto81=str(lista9[0])
        ArregloPos81.delete(0,END)
        ArregloPos81.insert(0,texto81)
        texto82=str(lista9[1])
        ArregloPos82.delete(0,END)
        ArregloPos82.insert(0,texto82)
        texto83=str(lista9[2])
        ArregloPos83.delete(0,END)
        ArregloPos83.insert(0,texto83)
        texto84=str(lista9[3])
        ArregloPos84.delete(0,END)
        ArregloPos84.insert(0,texto84)
        texto85=str(lista9[4])
        ArregloPos85.delete(0,END)
        ArregloPos85.insert(0,texto85)
        texto86=str(lista9[5])
        ArregloPos86.delete(0,END)
        ArregloPos86.insert(0,texto86)
        texto87=str(lista9[6])
        ArregloPos87.delete(0,END)
        ArregloPos87.insert(0,texto87)
        texto88=str(lista9[7])
        ArregloPos88.delete(0,END)
        ArregloPos88.insert(0,texto88)
        texto89=str(lista9[8])
        ArregloPos89.delete(0,END)
        ArregloPos89.insert(0,texto89)
        texto90=str(lista9[9])
        ArregloPos90.delete(0,END)
        ArregloPos90.insert(0,texto90)

        texto91=str(lista10[0])
        ArregloPos91.delete(0,END)
        ArregloPos91.insert(0,texto91)
        texto92=str(lista10[1])
        ArregloPos92.delete(0,END)
        ArregloPos92.insert(0,texto92)
        texto93=str(lista10[2])
        ArregloPos93.delete(0,END)
        ArregloPos93.insert(0,texto93)
        texto94=str(lista10[3])
        ArregloPos94.delete(0,END)
        ArregloPos94.insert(0,texto94)
        texto95=str(lista10[4])
        ArregloPos95.delete(0,END)
        ArregloPos95.insert(0,texto95)
        texto96=str(lista10[5])
        ArregloPos96.delete(0,END)
        ArregloPos96.insert(0,texto96)
        texto97=str(lista10[6])
        ArregloPos97.delete(0,END)
        ArregloPos97.insert(0,texto97)
        texto98=str(lista10[7])
        ArregloPos98.delete(0,END)
        ArregloPos98.insert(0,texto98)
        texto99=str(lista10[8])
        ArregloPos99.delete(0,END)
        ArregloPos99.insert(0,texto99)
        texto100=str(lista10[9])
        ArregloPos100.delete(0,END)
        ArregloPos100.insert(0,texto100)
        
        return Matriz2

    #Proceso Por Filas
    def AgruparLecturaFilas(matriz):
        Valores=list()
        i=0
        while i < 10:
            j=0
            while j < 10:        
                valor=matriz[i,j]
                Valores.append(valor)                          
                j=j+1
            i=i+1

        ValoresMax=[int(val) for val in Valores]
        cont=0
        for i in ValoresMax:
            if i<0:
                ValoresMax[cont]=i*-1
            cont=cont+1

        MaximoVal = None
        for pos, num in enumerate(ValoresMax):
            if(MaximoVal is None or num > MaximoVal):
                MaximoVal=num

        BinarioVal=bin(int(MaximoVal))[2:]
        NumBits=(len(str(BinarioVal)))
        ResultadoBits=list()
        Valores=[int(val) for val in Valores]
        i=0
        while i<len(Valores):
            valorcito=ValoresMax[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumBits):
                valorcito=str(valorcito).zfill(NumBits)  
            if(Valores[i]<0):
                valorcito="1"+valorcito
                ResultadoBits.append(valorcito)  
            elif(Valores[i]>=0):
                valorcito="0"+valorcito         
                ResultadoBits.append(valorcito)      
            i=i+1
        Resultado=""
        i=0
        while i<26:
            Resultado=Resultado+ResultadoBits[i]
            i=i+1
        lista1=ResultadoBits[0:10]
        lista2=ResultadoBits[10:20]
        lista3=ResultadoBits[20:30]
        lista4=ResultadoBits[30:40]
        lista5=ResultadoBits[40:50]
        lista6=ResultadoBits[50:60]
        lista7=ResultadoBits[60:70]
        lista8=ResultadoBits[70:80]
        lista9=ResultadoBits[80:90]
        lista10=ResultadoBits[90:100]
        
        TextoLabelMostrarNumeroBits=("La cantidad de bits es de ",NumBits, " y el bit de signo")
        LabelMostrarNumeroBits.configure(text=TextoLabelMostrarNumeroBits)
        LabelGuardarTramaTotal3.configure(text=Resultado)
        LabelGuardarTramaTotal3.grid_remove()
        TextoLabelMostrarTramaTotal=("La trama resultante es: ",lista1,"\n",lista2,"\n",lista3,"\n",lista4,"\n",lista5,"\n",lista6,"\n",lista7,"\n",lista8,"\n",lista9,"\n",lista10)
        LabelMostrarTramaTotal.configure(text=TextoLabelMostrarTramaTotal)

    #Proceso Por Columnas
    def AgruparLecturaColumnas(matriz):
        Valores=list()
        i=0
        while i < 10:
            j=0
            while j < 10:        
                valor=matriz[j,i]
                Valores.append(valor)                          
                j=j+1
            i=i+1
    
        ValoresMax=[int(val) for val in Valores]
        cont=0
        for i in ValoresMax:
            if i<0:
                ValoresMax[cont]=i*-1
            cont=cont+1

        MaximoVal = None
        for pos, num in enumerate(ValoresMax):
            if(MaximoVal is None or num > MaximoVal):
                MaximoVal=num

        BinarioVal=bin(int(MaximoVal))[2:]
        NumBits=(len(str(BinarioVal)))
        ResultadoBits=list()
        i=0
        Valores=[int(val) for val in Valores]
        while i< len(Valores):
            valorcito=ValoresMax[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumBits):
                valorcito=str(valorcito).zfill(NumBits)  
            if(Valores[i]<0):
                valorcito="1"+valorcito  
            elif(Valores[i]>=0):
                valorcito="0"+valorcito         
            ResultadoBits.append(valorcito)      
            i=i+1
        Resultado=""
        i=0
        while i<26:
            Resultado=Resultado+ResultadoBits[i]
            i=i+1
        lista1=ResultadoBits[0:10]
        lista2=ResultadoBits[10:20]
        lista3=ResultadoBits[20:30]
        lista4=ResultadoBits[30:40]
        lista5=ResultadoBits[40:50]
        lista6=ResultadoBits[50:60]
        lista7=ResultadoBits[60:70]
        lista8=ResultadoBits[70:80]
        lista9=ResultadoBits[80:90]
        lista10=ResultadoBits[90:100]
        
        TextoLabelMostrarNumeroBits=("La cantidad de bits es de ",NumBits, " y el bit de signo")
        LabelMostrarNumeroBits.configure(text=TextoLabelMostrarNumeroBits)
        LabelGuardarTramaTotal3.configure(text=Resultado)
        LabelGuardarTramaTotal3.grid_remove()
        TextoLabelMostrarTramaTotal=("La trama resultante es: ",lista1,"\n",lista2,"\n",lista3,"\n",lista4,"\n",lista5,"\n",lista6,"\n",lista7,"\n",lista8,"\n",lista9,"\n",lista10)
        LabelMostrarTramaTotal.configure(text=TextoLabelMostrarTramaTotal)


    #Proceso Por Zig Zag
    def AgruparLecturaZigZag(matriz):
        alto=10
        ancho=10
        MatrizSolucion=[[] for i in range(ancho+alto-1)]

        for i in range(ancho):
            for j in range(alto):
                sum=i+j
                if(sum%2 ==0):
                    MatrizSolucion[sum].insert(0,matriz[i][j])
                else:
                    MatrizSolucion[sum].append(matriz[i][j])		
        Valores=list()
        for i in MatrizSolucion:
            for j in i:
                    Valores.append(j)   
    
        ValoresMax=[int(val) for val in Valores]
        cont=0
        for i in ValoresMax:
            if i<0:
                ValoresMax[cont]=i*-1
            cont=cont+1

        MaximoVal = None
        for pos, num in enumerate(ValoresMax):
            if(MaximoVal is None or num > MaximoVal):
                MaximoVal=num

        BinarioVal=bin(int(MaximoVal))[2:]
        NumBits=(len(str(BinarioVal)))
        ResultadoBits=list()
        i=0
        Valores=[int(val) for val in Valores]
        while i< len(Valores):
            valorcito=ValoresMax[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumBits):
                valorcito=str(valorcito).zfill(NumBits)  
            if(Valores[i]<0):
                valorcito="1"+valorcito  
            elif(Valores[i]>=0):
                valorcito="0"+valorcito         
            ResultadoBits.append(valorcito)      
            i=i+1
        Resultado=""
        i=0
        while i<26:
            Resultado=Resultado+ResultadoBits[i]
            i=i+1
        lista1=ResultadoBits[0:10]
        lista2=ResultadoBits[10:20]
        lista3=ResultadoBits[20:30]
        lista4=ResultadoBits[30:40]
        lista5=ResultadoBits[40:50]
        lista6=ResultadoBits[50:60]
        lista7=ResultadoBits[60:70]
        lista8=ResultadoBits[70:80]
        lista9=ResultadoBits[80:90]
        lista10=ResultadoBits[90:100]
        
        TextoLabelMostrarNumeroBits=("La cantidad de bits es de ",NumBits, " y el bit de signo")
        LabelMostrarNumeroBits.configure(text=TextoLabelMostrarNumeroBits)
        LabelGuardarTramaTotal3.configure(text=Resultado)
        LabelGuardarTramaTotal3.grid_remove()
        TextoLabelMostrarTramaTotal=("La trama resultante es: ",lista1,"\n",lista2,"\n",lista3,"\n",lista4,"\n",lista5,"\n",lista6,"\n",lista7,"\n",lista8,"\n",lista9,"\n",lista10)
        LabelMostrarTramaTotal.configure(text=TextoLabelMostrarTramaTotal)
    
    #Funcion Guardar Trama
    def Guardar():
        LabelGuardarTramaTotal3.grid()
        TextoTrama=LabelGuardarTramaTotal3.cget("text")
        TextoTrama=TextoTrama.replace(" ", "")
        characters = "][',"
        for x in range(len(characters)):
            TextoTrama = TextoTrama.replace(characters[x],"")
        clipboard.copy(TextoTrama)

    #Funcion Volver    
    def Volver():
        VentanaCodificacionDCPM.destroy()
        ventana.deiconify()

    #Creación ventana
    VentanaCodificacionDCPM=Toplevel()
    VentanaCodificacionDCPM.title("Codificación DCPM")
    VentanaCodificacionDCPM.geometry('1500x770')
    TituloInterfaz=Label(VentanaCodificacionDCPM, text="Codificación DCPM", bd=10, fg='black', font=("Helvetica", 16))
    TituloInterfaz.grid(row=0, column=0)

    #Instrucciones
    LabelInstrucciones=Label(VentanaCodificacionDCPM, text="ingrese la maxima diferencia para sus valores")
    LabelInstrucciones.grid(row=1, column=0)
    Espacio=Label(VentanaCodificacionDCPM,text="ingrese el valor minimo de los valores que desea")
    Espacio.grid(row=3,column=0)
    Intervalo=StringVar()
    EntradaIntervalo=Entry(VentanaCodificacionDCPM,textvariable=Intervalo,width=20)
    EntradaIntervalo.grid(row=2,column=0)

    #Mostrar Matriz Inicial
    #ValoresMatrizfila1
    Posicion1=StringVar()
    ArregloPos1=Entry(VentanaCodificacionDCPM,textvariable=Posicion1,width=5)
    ArregloPos1.grid(row=3,column=2,sticky=NSEW)
    Posicion2=StringVar()
    ArregloPos2=Entry(VentanaCodificacionDCPM,textvariable=Posicion2,width=5)
    ArregloPos2.grid(row=3,column=3,sticky=NSEW)
    Posicion3=StringVar()
    ArregloPos3=Entry(VentanaCodificacionDCPM,textvariable=Posicion3,width=5)
    ArregloPos3.grid(row=3,column=4,sticky=NSEW)
    Posicion4=StringVar()
    ArregloPos4=Entry(VentanaCodificacionDCPM,textvariable=Posicion4,width=5)
    ArregloPos4.grid(row=3,column=5,sticky=NSEW)
    Posicion5=StringVar()
    ArregloPos5=Entry(VentanaCodificacionDCPM,textvariable=Posicion5,width=5)
    ArregloPos5.grid(row=3,column=6,sticky=NSEW)
    Posicion6=StringVar()
    ArregloPos6=Entry(VentanaCodificacionDCPM,textvariable=Posicion6,width=5)
    ArregloPos6.grid(row=3,column=7,sticky=NSEW)
    Posicion7=StringVar()
    ArregloPos7=Entry(VentanaCodificacionDCPM,textvariable=Posicion7,width=5)
    ArregloPos7.grid(row=3,column=8,sticky=NSEW)
    Posicion8=StringVar()
    ArregloPos8=Entry(VentanaCodificacionDCPM,textvariable=Posicion8,width=5)
    ArregloPos8.grid(row=3,column=9,sticky=NSEW)
    Posicion9=StringVar()
    ArregloPos9=Entry(VentanaCodificacionDCPM,textvariable=Posicion9,width=5)
    ArregloPos9.grid(row=3,column=10,sticky=NSEW)
    Posicion10=StringVar()
    ArregloPos10=Entry(VentanaCodificacionDCPM,textvariable=Posicion10,width=5)
    ArregloPos10.grid(row=3,column=11,sticky=NSEW)

    #ValoresMatrizFila2
    Posicion11=StringVar()
    ArregloPos11=Entry(VentanaCodificacionDCPM,textvariable=Posicion11,width=5)
    ArregloPos11.grid(row=4,column=2,sticky=NSEW)
    Posicion12=StringVar()
    ArregloPos12=Entry(VentanaCodificacionDCPM,textvariable=Posicion12,width=5)
    ArregloPos12.grid(row=4,column=3,sticky=NSEW)
    Posicion13=StringVar()
    ArregloPos13=Entry(VentanaCodificacionDCPM,textvariable=Posicion13,width=5)
    ArregloPos13.grid(row=4,column=4,sticky=NSEW)
    Posicion14=StringVar()
    ArregloPos14=Entry(VentanaCodificacionDCPM,textvariable=Posicion14,width=5)
    ArregloPos14.grid(row=4,column=5,sticky=NSEW)
    Posicion15=StringVar()
    ArregloPos15=Entry(VentanaCodificacionDCPM,textvariable=Posicion15,width=5)
    ArregloPos15.grid(row=4,column=6,sticky=NSEW)
    Posicion16=StringVar()
    ArregloPos16=Entry(VentanaCodificacionDCPM,textvariable=Posicion16,width=5)
    ArregloPos16.grid(row=4,column=7,sticky=NSEW)
    Posicion17=StringVar()
    ArregloPos17=Entry(VentanaCodificacionDCPM,textvariable=Posicion17,width=5)
    ArregloPos17.grid(row=4,column=8,sticky=NSEW)
    Posicion18=StringVar()
    ArregloPos18=Entry(VentanaCodificacionDCPM,textvariable=Posicion18,width=5)
    ArregloPos18.grid(row=4,column=9,sticky=NSEW)
    Posicion19=StringVar()
    ArregloPos19=Entry(VentanaCodificacionDCPM,textvariable=Posicion19,width=5)
    ArregloPos19.grid(row=4,column=10,sticky=NSEW)
    Posicion20=StringVar()
    ArregloPos20=Entry(VentanaCodificacionDCPM,textvariable=Posicion20,width=5)
    ArregloPos20.grid(row=4,column=11,sticky=NSEW)

    #ValoresMatrizFila3
    Posicion21=StringVar()
    ArregloPos21=Entry(VentanaCodificacionDCPM,textvariable=Posicion21,width=5)
    ArregloPos21.grid(row=5,column=2,sticky=NSEW)
    Posicion22=StringVar()
    ArregloPos22=Entry(VentanaCodificacionDCPM,textvariable=Posicion22,width=5)
    ArregloPos22.grid(row=5,column=3,sticky=NSEW)
    Posicion23=StringVar()
    ArregloPos23=Entry(VentanaCodificacionDCPM,textvariable=Posicion23,width=5)
    ArregloPos23.grid(row=5,column=4,sticky=NSEW)
    Posicion24=StringVar()
    ArregloPos24=Entry(VentanaCodificacionDCPM,textvariable=Posicion24,width=5)
    ArregloPos24.grid(row=5,column=5,sticky=NSEW)
    Posicion25=StringVar()
    ArregloPos25=Entry(VentanaCodificacionDCPM,textvariable=Posicion25,width=5)
    ArregloPos25.grid(row=5,column=6,sticky=NSEW)
    Posicion26=StringVar()
    ArregloPos26=Entry(VentanaCodificacionDCPM,textvariable=Posicion26,width=5)
    ArregloPos26.grid(row=5,column=7,sticky=NSEW)
    Posicion27=StringVar()
    ArregloPos27=Entry(VentanaCodificacionDCPM,textvariable=Posicion27,width=5)
    ArregloPos27.grid(row=5,column=8,sticky=NSEW)
    Posicion28=StringVar()
    ArregloPos28=Entry(VentanaCodificacionDCPM,textvariable=Posicion28,width=5)
    ArregloPos28.grid(row=5,column=9,sticky=NSEW)
    Posicion29=StringVar()
    ArregloPos29=Entry(VentanaCodificacionDCPM,textvariable=Posicion29,width=5)
    ArregloPos29.grid(row=5,column=10,sticky=NSEW)
    Posicion30=StringVar()
    ArregloPos30=Entry(VentanaCodificacionDCPM,textvariable=Posicion30,width=5)
    ArregloPos30.grid(row=5,column=11,sticky=NSEW)

    #ArregloMatrizFila4
    Posicion31=StringVar()
    ArregloPos31=Entry(VentanaCodificacionDCPM,textvariable=Posicion31,width=5)
    ArregloPos31.grid(row=6,column=2,sticky=NSEW)
    Posicion32=StringVar()
    ArregloPos32=Entry(VentanaCodificacionDCPM,textvariable=Posicion32,width=5)
    ArregloPos32.grid(row=6,column=3,sticky=NSEW)
    Posicion33=StringVar()
    ArregloPos33=Entry(VentanaCodificacionDCPM,textvariable=Posicion33,width=5)
    ArregloPos33.grid(row=6,column=4,sticky=NSEW)
    Posicion34=StringVar()
    ArregloPos34=Entry(VentanaCodificacionDCPM,textvariable=Posicion34,width=5)
    ArregloPos34.grid(row=6,column=5,sticky=NSEW)
    Posicion35=StringVar()
    ArregloPos35=Entry(VentanaCodificacionDCPM,textvariable=Posicion35,width=5)
    ArregloPos35.grid(row=6,column=6,sticky=NSEW)
    Posicion36=StringVar()
    ArregloPos36=Entry(VentanaCodificacionDCPM,textvariable=Posicion36,width=5)
    ArregloPos36.grid(row=6,column=7,sticky=NSEW)
    Posicion37=StringVar()
    ArregloPos37=Entry(VentanaCodificacionDCPM,textvariable=Posicion37,width=5)
    ArregloPos37.grid(row=6,column=8,sticky=NSEW)
    Posicion38=StringVar()
    ArregloPos38=Entry(VentanaCodificacionDCPM,textvariable=Posicion38,width=5)
    ArregloPos38.grid(row=6,column=9,sticky=NSEW)
    Posicion39=StringVar()
    ArregloPos39=Entry(VentanaCodificacionDCPM,textvariable=Posicion39,width=5)
    ArregloPos39.grid(row=6,column=10,sticky=NSEW)
    Posicion40=StringVar()
    ArregloPos40=Entry(VentanaCodificacionDCPM,textvariable=Posicion40,width=5)
    ArregloPos40.grid(row=6,column=11,sticky=NSEW)

    #ArregloMatrizFila5
    Posicion41=StringVar()
    ArregloPos41=Entry(VentanaCodificacionDCPM,textvariable=Posicion41,width=5)
    ArregloPos41.grid(row=7,column=2,sticky=NSEW)
    Posicion42=StringVar()
    ArregloPos42=Entry(VentanaCodificacionDCPM,textvariable=Posicion42,width=5)
    ArregloPos42.grid(row=7,column=3,sticky=NSEW)
    Posicion43=StringVar()
    ArregloPos43=Entry(VentanaCodificacionDCPM,textvariable=Posicion43,width=5)
    ArregloPos43.grid(row=7,column=4,sticky=NSEW)
    Posicion44=StringVar()
    ArregloPos44=Entry(VentanaCodificacionDCPM,textvariable=Posicion44,width=5)
    ArregloPos44.grid(row=7,column=5,sticky=NSEW)
    Posicion45=StringVar()
    ArregloPos45=Entry(VentanaCodificacionDCPM,textvariable=Posicion45,width=5)
    ArregloPos45.grid(row=7,column=6,sticky=NSEW)
    Posicion46=StringVar()
    ArregloPos46=Entry(VentanaCodificacionDCPM,textvariable=Posicion46,width=5)
    ArregloPos46.grid(row=7,column=7,sticky=NSEW)
    Posicion47=StringVar()
    ArregloPos47=Entry(VentanaCodificacionDCPM,textvariable=Posicion47,width=5)
    ArregloPos47.grid(row=7,column=8,sticky=NSEW)
    Posicion48=StringVar()
    ArregloPos48=Entry(VentanaCodificacionDCPM,textvariable=Posicion48,width=5)
    ArregloPos48.grid(row=7,column=9,sticky=NSEW)
    Posicion49=StringVar()
    ArregloPos49=Entry(VentanaCodificacionDCPM,textvariable=Posicion49,width=5)
    ArregloPos49.grid(row=7,column=10,sticky=NSEW)
    Posicion50=StringVar()
    ArregloPos50=Entry(VentanaCodificacionDCPM,textvariable=Posicion50,width=5)
    ArregloPos50.grid(row=7,column=11,sticky=NSEW)

    #ArregloMatrizFila6
    Posicion51=StringVar()
    ArregloPos51=Entry(VentanaCodificacionDCPM,textvariable=Posicion51,width=5)
    ArregloPos51.grid(row=8,column=2,sticky=NSEW)
    Posicion52=StringVar()
    ArregloPos52=Entry(VentanaCodificacionDCPM,textvariable=Posicion52,width=5)
    ArregloPos52.grid(row=8,column=3,sticky=NSEW)
    Posicion53=StringVar()
    ArregloPos53=Entry(VentanaCodificacionDCPM,textvariable=Posicion53,width=5)
    ArregloPos53.grid(row=8,column=4,sticky=NSEW)
    Posicion54=StringVar()
    ArregloPos54=Entry(VentanaCodificacionDCPM,textvariable=Posicion54,width=5)
    ArregloPos54.grid(row=8,column=5,sticky=NSEW)
    Posicion55=StringVar()
    ArregloPos55=Entry(VentanaCodificacionDCPM,textvariable=Posicion55,width=5)
    ArregloPos55.grid(row=8,column=6,sticky=NSEW)
    Posicion56=StringVar()
    ArregloPos56=Entry(VentanaCodificacionDCPM,textvariable=Posicion56,width=5)
    ArregloPos56.grid(row=8,column=7,sticky=NSEW)
    Posicion57=StringVar()
    ArregloPos57=Entry(VentanaCodificacionDCPM,textvariable=Posicion57,width=5)
    ArregloPos57.grid(row=8,column=8,sticky=NSEW)
    Posicion58=StringVar()
    ArregloPos58=Entry(VentanaCodificacionDCPM,textvariable=Posicion58,width=5)
    ArregloPos58.grid(row=8,column=9,sticky=NSEW)
    Posicion59=StringVar()
    ArregloPos59=Entry(VentanaCodificacionDCPM,textvariable=Posicion59,width=5)
    ArregloPos59.grid(row=8,column=10,sticky=NSEW)
    Posicion60=StringVar()
    ArregloPos60=Entry(VentanaCodificacionDCPM,textvariable=Posicion60,width=5)
    ArregloPos60.grid(row=8,column=11,sticky=NSEW)

    #MatrizArregloFila7
    Posicion61=StringVar()
    ArregloPos61=Entry(VentanaCodificacionDCPM,textvariable=Posicion61,width=5)
    ArregloPos61.grid(row=9,column=2,sticky=NSEW)
    Posicion62=StringVar()
    ArregloPos62=Entry(VentanaCodificacionDCPM,textvariable=Posicion62,width=5)
    ArregloPos62.grid(row=9,column=3,sticky=NSEW)
    Posicion63=StringVar()
    ArregloPos63=Entry(VentanaCodificacionDCPM,textvariable=Posicion63,width=5)
    ArregloPos63.grid(row=9,column=4,sticky=NSEW)
    Posicion64=StringVar()
    ArregloPos64=Entry(VentanaCodificacionDCPM,textvariable=Posicion64,width=5)
    ArregloPos64.grid(row=9,column=5,sticky=NSEW)
    Posicion65=StringVar()
    ArregloPos65=Entry(VentanaCodificacionDCPM,textvariable=Posicion65,width=5)
    ArregloPos65.grid(row=9,column=6,sticky=NSEW)
    Posicion66=StringVar()
    ArregloPos66=Entry(VentanaCodificacionDCPM,textvariable=Posicion66,width=5)
    ArregloPos66.grid(row=9,column=7,sticky=NSEW)
    Posicion67=StringVar()
    ArregloPos67=Entry(VentanaCodificacionDCPM,textvariable=Posicion67,width=5)
    ArregloPos67.grid(row=9,column=8,sticky=NSEW)
    Posicion68=StringVar()
    ArregloPos68=Entry(VentanaCodificacionDCPM,textvariable=Posicion68,width=5)
    ArregloPos68.grid(row=9,column=9,sticky=NSEW)
    Posicion69=StringVar()
    ArregloPos69=Entry(VentanaCodificacionDCPM,textvariable=Posicion69,width=5)
    ArregloPos69.grid(row=9,column=10,sticky=NSEW)
    Posicion70=StringVar()
    ArregloPos70=Entry(VentanaCodificacionDCPM,textvariable=Posicion70,width=5)
    ArregloPos70.grid(row=9,column=11,sticky=NSEW)

    #ArregloMatrizFila8
    Posicion71=StringVar()
    ArregloPos71=Entry(VentanaCodificacionDCPM,textvariable=Posicion71,width=5)
    ArregloPos71.grid(row=10,column=2,sticky=NSEW)
    Posicion72=StringVar()
    ArregloPos72=Entry(VentanaCodificacionDCPM,textvariable=Posicion72,width=5)
    ArregloPos72.grid(row=10,column=3,sticky=NSEW)
    Posicion73=StringVar()
    ArregloPos73=Entry(VentanaCodificacionDCPM,textvariable=Posicion73,width=5)
    ArregloPos73.grid(row=10,column=4,sticky=NSEW)
    Posicion74=StringVar()
    ArregloPos74=Entry(VentanaCodificacionDCPM,textvariable=Posicion74,width=5)
    ArregloPos74.grid(row=10,column=5,sticky=NSEW)
    Posicion75=StringVar()
    ArregloPos75=Entry(VentanaCodificacionDCPM,textvariable=Posicion75,width=5)
    ArregloPos75.grid(row=10,column=6,sticky=NSEW)
    Posicion76=StringVar()
    ArregloPos76=Entry(VentanaCodificacionDCPM,textvariable=Posicion76,width=5)
    ArregloPos76.grid(row=10,column=7,sticky=NSEW)
    Posicion77=StringVar()
    ArregloPos77=Entry(VentanaCodificacionDCPM,textvariable=Posicion77,width=5)
    ArregloPos77.grid(row=10,column=8,sticky=NSEW)
    Posicion78=StringVar()
    ArregloPos78=Entry(VentanaCodificacionDCPM,textvariable=Posicion78,width=5)
    ArregloPos78.grid(row=10,column=9,sticky=NSEW)
    Posicion79=StringVar()
    ArregloPos79=Entry(VentanaCodificacionDCPM,textvariable=Posicion79,width=5)
    ArregloPos79.grid(row=10,column=10,sticky=NSEW)
    Posicion80=StringVar()
    ArregloPos80=Entry(VentanaCodificacionDCPM,textvariable=Posicion80,width=5)
    ArregloPos80.grid(row=10,column=11,sticky=NSEW)

    #ArregloMatrizFila9
    Posicion81=StringVar()
    ArregloPos81=Entry(VentanaCodificacionDCPM,textvariable=Posicion81,width=5)
    ArregloPos81.grid(row=11,column=2,sticky=NSEW)
    Posicion82=StringVar()
    ArregloPos82=Entry(VentanaCodificacionDCPM,textvariable=Posicion82,width=5)
    ArregloPos82.grid(row=11,column=3,sticky=NSEW)
    Posicion83=StringVar()
    ArregloPos83=Entry(VentanaCodificacionDCPM,textvariable=Posicion83,width=5)
    ArregloPos83.grid(row=11,column=4,sticky=NSEW)
    Posicion84=StringVar()
    ArregloPos84=Entry(VentanaCodificacionDCPM,textvariable=Posicion84,width=5)
    ArregloPos84.grid(row=11,column=5,sticky=NSEW)
    Posicion85=StringVar()
    ArregloPos85=Entry(VentanaCodificacionDCPM,textvariable=Posicion85,width=5)
    ArregloPos85.grid(row=11,column=6,sticky=NSEW)
    Posicion86=StringVar()
    ArregloPos86=Entry(VentanaCodificacionDCPM,textvariable=Posicion86,width=5)
    ArregloPos86.grid(row=11,column=7,sticky=NSEW)
    Posicion87=StringVar()
    ArregloPos87=Entry(VentanaCodificacionDCPM,textvariable=Posicion87,width=5)
    ArregloPos87.grid(row=11,column=8,sticky=NSEW)
    Posicion88=StringVar()
    ArregloPos88=Entry(VentanaCodificacionDCPM,textvariable=Posicion88,width=5)
    ArregloPos88.grid(row=11,column=9,sticky=NSEW)
    Posicion89=StringVar()
    ArregloPos89=Entry(VentanaCodificacionDCPM,textvariable=Posicion89,width=5)
    ArregloPos89.grid(row=11,column=10,sticky=NSEW)
    Posicion90=StringVar()
    ArregloPos90=Entry(VentanaCodificacionDCPM,textvariable=Posicion90,width=5)
    ArregloPos90.grid(row=11,column=11,sticky=NSEW)

    #ArregloMatrizFila10
    Posicion91=StringVar()
    ArregloPos91=Entry(VentanaCodificacionDCPM,textvariable=Posicion91,width=5)
    ArregloPos91.grid(row=12,column=2,sticky=NSEW)
    Posicion92=StringVar()
    ArregloPos92=Entry(VentanaCodificacionDCPM,textvariable=Posicion92,width=5)
    ArregloPos92.grid(row=12,column=3,sticky=NSEW)
    Posicion93=StringVar()
    ArregloPos93=Entry(VentanaCodificacionDCPM,textvariable=Posicion93,width=5)
    ArregloPos93.grid(row=12,column=4,sticky=NSEW)
    Posicion94=StringVar()
    ArregloPos94=Entry(VentanaCodificacionDCPM,textvariable=Posicion94,width=5)
    ArregloPos94.grid(row=12,column=5,sticky=NSEW)
    Posicion95=StringVar()
    ArregloPos95=Entry(VentanaCodificacionDCPM,textvariable=Posicion95,width=5)
    ArregloPos95.grid(row=12,column=6,sticky=NSEW)
    Posicion96=StringVar()
    ArregloPos96=Entry(VentanaCodificacionDCPM,textvariable=Posicion96,width=5) 
    ArregloPos96.grid(row=12,column=7,sticky=NSEW)
    Posicion97=StringVar()
    ArregloPos97=Entry(VentanaCodificacionDCPM,textvariable=Posicion97,width=5)
    ArregloPos97.grid(row=12,column=8,sticky=NSEW)
    Posicion98=StringVar()
    ArregloPos98=Entry(VentanaCodificacionDCPM,textvariable=Posicion98,width=5)
    ArregloPos98.grid(row=12,column=9,sticky=NSEW)
    Posicion99=StringVar()
    ArregloPos99=Entry(VentanaCodificacionDCPM,textvariable=Posicion99,width=5)
    ArregloPos99.grid(row=12,column=10,sticky=NSEW)
    Posicion100=StringVar()
    ArregloPos100=Entry(VentanaCodificacionDCPM,textvariable=Posicion100,width=5)
    ArregloPos100.grid(row=12,column=11,sticky=NSEW)

    #Mostrar Matriz Diferencia
    #ValoresMatrizfila1
    DPosicion1=StringVar()
    DArregloPos1=Entry(VentanaCodificacionDCPM,textvariable=DPosicion1,width=5)
    DArregloPos1.grid(row=14,column=2,sticky=NSEW)
    DPosicion2=StringVar()
    DArregloPos2=Entry(VentanaCodificacionDCPM,textvariable=DPosicion2,width=5)
    DArregloPos2.grid(row=14,column=3,sticky=NSEW)
    DPosicion3=StringVar()
    DArregloPos3=Entry(VentanaCodificacionDCPM,textvariable=DPosicion3,width=5)
    DArregloPos3.grid(row=14,column=4,sticky=NSEW)
    DPosicion4=StringVar()
    DArregloPos4=Entry(VentanaCodificacionDCPM,textvariable=DPosicion4,width=5)
    DArregloPos4.grid(row=14,column=5,sticky=NSEW)
    DPosicion5=StringVar()
    DArregloPos5=Entry(VentanaCodificacionDCPM,textvariable=DPosicion5,width=5)
    DArregloPos5.grid(row=14,column=6,sticky=NSEW)
    DPosicion6=StringVar()
    DArregloPos6=Entry(VentanaCodificacionDCPM,textvariable=DPosicion6,width=5)
    DArregloPos6.grid(row=14,column=7,sticky=NSEW)
    DPosicion7=StringVar()
    DArregloPos7=Entry(VentanaCodificacionDCPM,textvariable=DPosicion7,width=5)
    DArregloPos7.grid(row=14,column=8,sticky=NSEW)
    DPosicion8=StringVar()
    DArregloPos8=Entry(VentanaCodificacionDCPM,textvariable=DPosicion8,width=5)
    DArregloPos8.grid(row=14,column=9,sticky=NSEW)
    DPosicion9=StringVar()
    DArregloPos9=Entry(VentanaCodificacionDCPM,textvariable=DPosicion9,width=5)
    DArregloPos9.grid(row=14,column=10,sticky=NSEW)
    DPosicion10=StringVar()
    DArregloPos10=Entry(VentanaCodificacionDCPM,textvariable=DPosicion10,width=5)
    DArregloPos10.grid(row=14,column=11,sticky=NSEW)

    #ValoresMatrizFila2
    DPosicion11=StringVar()
    DArregloPos11=Entry(VentanaCodificacionDCPM,textvariable=DPosicion11,width=5)
    DArregloPos11.grid(row=15,column=2,sticky=NSEW)
    DPosicion12=StringVar()
    DArregloPos12=Entry(VentanaCodificacionDCPM,textvariable=DPosicion12,width=5)
    DArregloPos12.grid(row=15,column=3,sticky=NSEW)
    DPosicion13=StringVar()
    DArregloPos13=Entry(VentanaCodificacionDCPM,textvariable=DPosicion13,width=5)
    DArregloPos13.grid(row=15,column=4,sticky=NSEW)
    DPosicion14=StringVar()
    DArregloPos14=Entry(VentanaCodificacionDCPM,textvariable=DPosicion14,width=5)
    DArregloPos14.grid(row=15,column=5,sticky=NSEW)
    DPosicion15=StringVar()
    DArregloPos15=Entry(VentanaCodificacionDCPM,textvariable=DPosicion15,width=5)
    DArregloPos15.grid(row=15,column=6,sticky=NSEW)
    DPosicion16=StringVar()
    DArregloPos16=Entry(VentanaCodificacionDCPM,textvariable=DPosicion16,width=5)
    DArregloPos16.grid(row=15,column=7,sticky=NSEW)
    DPosicion17=StringVar()
    DArregloPos17=Entry(VentanaCodificacionDCPM,textvariable=DPosicion17,width=5)
    DArregloPos17.grid(row=15,column=8,sticky=NSEW)
    DPosicion18=StringVar()
    DArregloPos18=Entry(VentanaCodificacionDCPM,textvariable=DPosicion18,width=5)
    DArregloPos18.grid(row=15,column=9,sticky=NSEW)
    DPosicion19=StringVar()
    DArregloPos19=Entry(VentanaCodificacionDCPM,textvariable=DPosicion19,width=5)
    DArregloPos19.grid(row=15,column=10,sticky=NSEW)
    DPosicion20=StringVar()
    DArregloPos20=Entry(VentanaCodificacionDCPM,textvariable=DPosicion20,width=5)
    DArregloPos20.grid(row=15,column=11,sticky=NSEW)

    #ValoresMatrizFila3
    DPosicion21=StringVar()
    DArregloPos21=Entry(VentanaCodificacionDCPM,textvariable=DPosicion21,width=5)
    DArregloPos21.grid(row=16,column=2,sticky=NSEW)
    DPosicion22=StringVar()
    DArregloPos22=Entry(VentanaCodificacionDCPM,textvariable=DPosicion22,width=5)
    DArregloPos22.grid(row=16,column=3,sticky=NSEW)
    DPosicion23=StringVar()
    DArregloPos23=Entry(VentanaCodificacionDCPM,textvariable=DPosicion23,width=5)
    DArregloPos23.grid(row=16,column=4,sticky=NSEW)
    DPosicion24=StringVar()
    DArregloPos24=Entry(VentanaCodificacionDCPM,textvariable=DPosicion24,width=5)
    DArregloPos24.grid(row=16,column=5,sticky=NSEW)
    DPosicion25=StringVar()
    DArregloPos25=Entry(VentanaCodificacionDCPM,textvariable=DPosicion25,width=5)
    DArregloPos25.grid(row=16,column=6,sticky=NSEW)
    DPosicion26=StringVar()
    DArregloPos26=Entry(VentanaCodificacionDCPM,textvariable=DPosicion26,width=5)
    DArregloPos26.grid(row=16,column=7,sticky=NSEW)
    DPosicion27=StringVar()
    DArregloPos27=Entry(VentanaCodificacionDCPM,textvariable=DPosicion27,width=5)
    DArregloPos27.grid(row=16,column=8,sticky=NSEW)
    DPosicion28=StringVar()
    DArregloPos28=Entry(VentanaCodificacionDCPM,textvariable=DPosicion28,width=5)
    DArregloPos28.grid(row=16,column=9,sticky=NSEW)
    DPosicion29=StringVar()
    DArregloPos29=Entry(VentanaCodificacionDCPM,textvariable=DPosicion29,width=5)
    DArregloPos29.grid(row=16,column=10,sticky=NSEW)
    DPosicion30=StringVar()
    DArregloPos30=Entry(VentanaCodificacionDCPM,textvariable=DPosicion30,width=5)
    DArregloPos30.grid(row=16,column=11,sticky=NSEW)

    #ArregloMatrizFila4
    DPosicion31=StringVar()
    DArregloPos31=Entry(VentanaCodificacionDCPM,textvariable=DPosicion31,width=5)
    DArregloPos31.grid(row=17,column=2,sticky=NSEW)
    DPosicion32=StringVar()
    DArregloPos32=Entry(VentanaCodificacionDCPM,textvariable=DPosicion32,width=5)
    DArregloPos32.grid(row=17,column=3,sticky=NSEW)
    DPosicion33=StringVar()
    DArregloPos33=Entry(VentanaCodificacionDCPM,textvariable=DPosicion33,width=5)
    DArregloPos33.grid(row=17,column=4,sticky=NSEW)
    DPosicion34=StringVar()
    DArregloPos34=Entry(VentanaCodificacionDCPM,textvariable=DPosicion34,width=5)
    DArregloPos34.grid(row=17,column=5,sticky=NSEW)
    DPosicion35=StringVar()
    DArregloPos35=Entry(VentanaCodificacionDCPM,textvariable=DPosicion35,width=5)
    DArregloPos35.grid(row=17,column=6,sticky=NSEW)
    DPosicion36=StringVar()
    DArregloPos36=Entry(VentanaCodificacionDCPM,textvariable=DPosicion36,width=5)
    DArregloPos36.grid(row=17,column=7,sticky=NSEW)
    DPosicion37=StringVar()
    DArregloPos37=Entry(VentanaCodificacionDCPM,textvariable=DPosicion37,width=5)
    DArregloPos37.grid(row=17,column=8,sticky=NSEW)
    DPosicion38=StringVar()
    DArregloPos38=Entry(VentanaCodificacionDCPM,textvariable=DPosicion38,width=5)
    DArregloPos38.grid(row=17,column=9,sticky=NSEW)
    DPosicion39=StringVar()
    DArregloPos39=Entry(VentanaCodificacionDCPM,textvariable=DPosicion39,width=5)
    DArregloPos39.grid(row=17,column=10,sticky=NSEW)
    DPosicion40=StringVar()
    DArregloPos40=Entry(VentanaCodificacionDCPM,textvariable=DPosicion40,width=5)
    DArregloPos40.grid(row=17,column=11,sticky=NSEW)

    #ArregloMatrizFila5
    DPosicion41=StringVar()
    DArregloPos41=Entry(VentanaCodificacionDCPM,textvariable=DPosicion41,width=5)
    DArregloPos41.grid(row=18,column=2,sticky=NSEW)
    DPosicion42=StringVar()
    DArregloPos42=Entry(VentanaCodificacionDCPM,textvariable=DPosicion42,width=5)
    DArregloPos42.grid(row=18,column=3,sticky=NSEW)
    DPosicion43=StringVar()
    DArregloPos43=Entry(VentanaCodificacionDCPM,textvariable=DPosicion43,width=5)
    DArregloPos43.grid(row=18,column=4,sticky=NSEW)
    DPosicion44=StringVar()
    DArregloPos44=Entry(VentanaCodificacionDCPM,textvariable=DPosicion44,width=5)
    DArregloPos44.grid(row=18,column=5,sticky=NSEW)
    DPosicion45=StringVar()
    DArregloPos45=Entry(VentanaCodificacionDCPM,textvariable=DPosicion45,width=5)
    DArregloPos45.grid(row=18,column=6,sticky=NSEW)
    DPosicion46=StringVar()
    DArregloPos46=Entry(VentanaCodificacionDCPM,textvariable=DPosicion46,width=5)
    DArregloPos46.grid(row=18,column=7,sticky=NSEW)
    DPosicion47=StringVar()
    DArregloPos47=Entry(VentanaCodificacionDCPM,textvariable=DPosicion47,width=5)
    DArregloPos47.grid(row=18,column=8,sticky=NSEW)
    DPosicion48=StringVar()
    DArregloPos48=Entry(VentanaCodificacionDCPM,textvariable=DPosicion48,width=5)
    DArregloPos48.grid(row=18,column=9,sticky=NSEW)
    DPosicion49=StringVar()
    DArregloPos49=Entry(VentanaCodificacionDCPM,textvariable=DPosicion49,width=5)
    DArregloPos49.grid(row=18,column=10,sticky=NSEW)
    DPosicion50=StringVar()
    DArregloPos50=Entry(VentanaCodificacionDCPM,textvariable=DPosicion50,width=5)
    DArregloPos50.grid(row=18,column=11,sticky=NSEW)

    #ArregloMatrizFila6
    DPosicion51=StringVar()
    DArregloPos51=Entry(VentanaCodificacionDCPM,textvariable=DPosicion51,width=5)
    DArregloPos51.grid(row=19,column=2,sticky=NSEW)
    DPosicion52=StringVar()
    DArregloPos52=Entry(VentanaCodificacionDCPM,textvariable=DPosicion52,width=5)
    DArregloPos52.grid(row=19,column=3,sticky=NSEW)
    DPosicion53=StringVar()
    DArregloPos53=Entry(VentanaCodificacionDCPM,textvariable=DPosicion53,width=5)
    DArregloPos53.grid(row=19,column=4,sticky=NSEW)
    DPosicion54=StringVar()
    DArregloPos54=Entry(VentanaCodificacionDCPM,textvariable=DPosicion54,width=5)
    DArregloPos54.grid(row=19,column=5,sticky=NSEW)
    DPosicion55=StringVar()
    DArregloPos55=Entry(VentanaCodificacionDCPM,textvariable=DPosicion55,width=5)
    DArregloPos55.grid(row=19,column=6,sticky=NSEW)
    DPosicion56=StringVar()
    DArregloPos56=Entry(VentanaCodificacionDCPM,textvariable=DPosicion56,width=5)
    DArregloPos56.grid(row=19,column=7,sticky=NSEW)
    DPosicion57=StringVar()
    DArregloPos57=Entry(VentanaCodificacionDCPM,textvariable=DPosicion57,width=5)
    DArregloPos57.grid(row=19,column=8,sticky=NSEW)
    DPosicion58=StringVar()
    DArregloPos58=Entry(VentanaCodificacionDCPM,textvariable=DPosicion58,width=5)
    DArregloPos58.grid(row=19,column=9,sticky=NSEW)
    DPosicion59=StringVar()
    DArregloPos59=Entry(VentanaCodificacionDCPM,textvariable=DPosicion59,width=5)
    DArregloPos59.grid(row=19,column=10,sticky=NSEW)
    DPosicion60=StringVar()
    DArregloPos60=Entry(VentanaCodificacionDCPM,textvariable=DPosicion60,width=5)
    DArregloPos60.grid(row=19,column=11,sticky=NSEW)

    #MatrizArregloFila7
    DPosicion61=StringVar()
    DArregloPos61=Entry(VentanaCodificacionDCPM,textvariable=DPosicion61,width=5)
    DArregloPos61.grid(row=20,column=2,sticky=NSEW)
    DPosicion62=StringVar()
    DArregloPos62=Entry(VentanaCodificacionDCPM,textvariable=DPosicion62,width=5)
    DArregloPos62.grid(row=20,column=3,sticky=NSEW)
    DPosicion63=StringVar()
    DArregloPos63=Entry(VentanaCodificacionDCPM,textvariable=DPosicion63,width=5)
    DArregloPos63.grid(row=20,column=4,sticky=NSEW)
    DPosicion64=StringVar()
    DArregloPos64=Entry(VentanaCodificacionDCPM,textvariable=DPosicion64,width=5)
    DArregloPos64.grid(row=20,column=5,sticky=NSEW)
    DPosicion65=StringVar()
    DArregloPos65=Entry(VentanaCodificacionDCPM,textvariable=DPosicion65,width=5)
    DArregloPos65.grid(row=20,column=6,sticky=NSEW)
    DPosicion66=StringVar()
    DArregloPos66=Entry(VentanaCodificacionDCPM,textvariable=DPosicion66,width=5)
    DArregloPos66.grid(row=20,column=7,sticky=NSEW)
    DPosicion67=StringVar()
    DArregloPos67=Entry(VentanaCodificacionDCPM,textvariable=DPosicion67,width=5)
    DArregloPos67.grid(row=20,column=8,sticky=NSEW)
    DPosicion68=StringVar()
    DArregloPos68=Entry(VentanaCodificacionDCPM,textvariable=DPosicion68,width=5)
    DArregloPos68.grid(row=20,column=9,sticky=NSEW)
    DPosicion69=StringVar()
    DArregloPos69=Entry(VentanaCodificacionDCPM,textvariable=DPosicion69,width=5)
    DArregloPos69.grid(row=20,column=10,sticky=NSEW)
    DPosicion70=StringVar()
    DArregloPos70=Entry(VentanaCodificacionDCPM,textvariable=DPosicion70,width=5)
    DArregloPos70.grid(row=20,column=11,sticky=NSEW)

    #ArregloMatrizFila8
    DPosicion71=StringVar()
    DArregloPos71=Entry(VentanaCodificacionDCPM,textvariable=DPosicion71,width=5)
    DArregloPos71.grid(row=21,column=2,sticky=NSEW)
    DPosicion72=StringVar()
    DArregloPos72=Entry(VentanaCodificacionDCPM,textvariable=DPosicion72,width=5)
    DArregloPos72.grid(row=21,column=3,sticky=NSEW)
    DPosicion73=StringVar()
    DArregloPos73=Entry(VentanaCodificacionDCPM,textvariable=DPosicion73,width=5)
    DArregloPos73.grid(row=21,column=4,sticky=NSEW)
    DPosicion74=StringVar()
    DArregloPos74=Entry(VentanaCodificacionDCPM,textvariable=DPosicion74,width=5)
    DArregloPos74.grid(row=21,column=5,sticky=NSEW)
    DPosicion75=StringVar()
    DArregloPos75=Entry(VentanaCodificacionDCPM,textvariable=DPosicion75,width=5)
    DArregloPos75.grid(row=21,column=6,sticky=NSEW)
    DPosicion76=StringVar()
    DArregloPos76=Entry(VentanaCodificacionDCPM,textvariable=DPosicion76,width=5)
    DArregloPos76.grid(row=21,column=7,sticky=NSEW)
    DPosicion77=StringVar()
    DArregloPos77=Entry(VentanaCodificacionDCPM,textvariable=DPosicion77,width=5)
    DArregloPos77.grid(row=21,column=8,sticky=NSEW)
    DPosicion78=StringVar()
    DArregloPos78=Entry(VentanaCodificacionDCPM,textvariable=DPosicion78,width=5)
    DArregloPos78.grid(row=21,column=9,sticky=NSEW)
    DPosicion79=StringVar()
    DArregloPos79=Entry(VentanaCodificacionDCPM,textvariable=DPosicion79,width=5)
    DArregloPos79.grid(row=21,column=10,sticky=NSEW)
    DPosicion80=StringVar()
    DArregloPos80=Entry(VentanaCodificacionDCPM,textvariable=DPosicion80,width=5)
    DArregloPos80.grid(row=21,column=11,sticky=NSEW)

    #ArregloMatrizFila9
    DPosicion81=StringVar()
    DArregloPos81=Entry(VentanaCodificacionDCPM,textvariable=DPosicion81,width=5)
    DArregloPos81.grid(row=22,column=2,sticky=NSEW)
    DPosicion82=StringVar()
    DArregloPos82=Entry(VentanaCodificacionDCPM,textvariable=DPosicion82,width=5)
    DArregloPos82.grid(row=22,column=3,sticky=NSEW)
    DPosicion83=StringVar()
    DArregloPos83=Entry(VentanaCodificacionDCPM,textvariable=DPosicion83,width=5)
    DArregloPos83.grid(row=22,column=4,sticky=NSEW)
    DPosicion84=StringVar()
    DArregloPos84=Entry(VentanaCodificacionDCPM,textvariable=DPosicion84,width=5)
    DArregloPos84.grid(row=22,column=5,sticky=NSEW)
    DPosicion85=StringVar()
    DArregloPos85=Entry(VentanaCodificacionDCPM,textvariable=DPosicion85,width=5)
    DArregloPos85.grid(row=22,column=6,sticky=NSEW)
    DPosicion86=StringVar()
    DArregloPos86=Entry(VentanaCodificacionDCPM,textvariable=DPosicion86,width=5)
    DArregloPos86.grid(row=22,column=7,sticky=NSEW)
    DPosicion87=StringVar()
    DArregloPos87=Entry(VentanaCodificacionDCPM,textvariable=DPosicion87,width=5)
    DArregloPos87.grid(row=22,column=8,sticky=NSEW)
    DPosicion88=StringVar()
    DArregloPos88=Entry(VentanaCodificacionDCPM,textvariable=DPosicion88,width=5)
    DArregloPos88.grid(row=22,column=9,sticky=NSEW)
    DPosicion89=StringVar()
    DArregloPos89=Entry(VentanaCodificacionDCPM,textvariable=DPosicion89,width=5)
    DArregloPos89.grid(row=22,column=10,sticky=NSEW)
    DPosicion90=StringVar()
    DArregloPos90=Entry(VentanaCodificacionDCPM,textvariable=DPosicion90,width=5)
    DArregloPos90.grid(row=22,column=11,sticky=NSEW)

    #ArregloMatrizFila10
    DPosicion91=StringVar()
    DArregloPos91=Entry(VentanaCodificacionDCPM,textvariable=DPosicion91,width=5)
    DArregloPos91.grid(row=23,column=2,sticky=NSEW)
    DPosicion92=StringVar()
    DArregloPos92=Entry(VentanaCodificacionDCPM,textvariable=DPosicion92,width=5)
    DArregloPos92.grid(row=23,column=3,sticky=NSEW)
    DPosicion93=StringVar()
    DArregloPos93=Entry(VentanaCodificacionDCPM,textvariable=DPosicion93,width=5)
    DArregloPos93.grid(row=23,column=4,sticky=NSEW)
    DPosicion94=StringVar()
    DArregloPos94=Entry(VentanaCodificacionDCPM,textvariable=DPosicion94,width=5)
    DArregloPos94.grid(row=23,column=5,sticky=NSEW)
    DPosicion95=StringVar()
    DArregloPos95=Entry(VentanaCodificacionDCPM,textvariable=DPosicion95,width=5)
    DArregloPos95.grid(row=23,column=6,sticky=NSEW)
    DPosicion96=StringVar()
    DArregloPos96=Entry(VentanaCodificacionDCPM,textvariable=DPosicion96,width=5) 
    DArregloPos96.grid(row=23,column=7,sticky=NSEW)
    DPosicion97=StringVar()
    DArregloPos97=Entry(VentanaCodificacionDCPM,textvariable=DPosicion97,width=5)
    DArregloPos97.grid(row=23,column=8,sticky=NSEW)
    DPosicion98=StringVar()
    DArregloPos98=Entry(VentanaCodificacionDCPM,textvariable=DPosicion98,width=5)
    DArregloPos98.grid(row=23,column=9,sticky=NSEW)
    DPosicion99=StringVar()
    DArregloPos99=Entry(VentanaCodificacionDCPM,textvariable=DPosicion99,width=5)
    DArregloPos99.grid(row=23,column=10,sticky=NSEW)
    DPosicion100=StringVar()
    DArregloPos100=Entry(VentanaCodificacionDCPM,textvariable=DPosicion100,width=5)
    DArregloPos100.grid(row=23,column=11,sticky=NSEW)

    ValorMinimoRandom=StringVar()
    EntryMinimoVal=Entry(VentanaCodificacionDCPM, textvariable=ValorMinimoRandom)
    EntryMinimoVal.grid(row=4, column=0)
    Espacio2=Label(VentanaCodificacionDCPM,text="ingrese el valor maximo de los valores que desea")
    Espacio2.grid(row=5,column=0)
    ValorMaximoRandom=StringVar()
    EntryMaximoVal=Entry(VentanaCodificacionDCPM, textvariable=ValorMaximoRandom)
    EntryMaximoVal.grid(row=6,column=0)

    LabelMostrarNumeroBits=Label(VentanaCodificacionDCPM, text=" ")
    LabelMostrarNumeroBits.grid(row=10, column=0)

    BotonCalculo=Button(VentanaCodificacionDCPM, text="Calculo Por Filas", command=lambda : AgruparLecturaFilas(CreacionMatrices()))
    BotonCalculo.grid(row=7, column=0)
    BotonCalculo2=Button(VentanaCodificacionDCPM, text="Calculo Por Columnas", command=lambda : AgruparLecturaColumnas(CreacionMatrices()))
    BotonCalculo2.grid(row=8, column=0)
    BotonCalculo3=Button(VentanaCodificacionDCPM, text="Calculo Por Zig Zag", command=lambda : AgruparLecturaZigZag(CreacionMatrices()))
    BotonCalculo3.grid(row=9,column=0)
    EntryTecnica=Entry(VentanaCodificacionDCPM)

    LabelMostrarTramaTotal=Label(VentanaCodificacionDCPM, text=" ")
    LabelMostrarTramaTotal.grid(row=13, column=0)

    BotonGuardar3=Button(VentanaCodificacionDCPM, text="Guardar Trama Final", width=25, command=Guardar)
    BotonGuardar3.grid(row=24, column=0)
    LabelGuardarTramaTotal3=Label(VentanaCodificacionDCPM, text=" ") 
    LabelGuardarTramaTotal3.grid(row=25, column=0)
    BotonVolver3=Button(VentanaCodificacionDCPM, text="Regresar", width=25, command=Volver)
    BotonVolver3.grid(row=26, column=0)

    LabelError=Label(VentanaCodificacionDCPM, text=" ")
    LabelError.grid(row=27, column=0)

    VentanaCodificacionDCPM.mainloop()

#Funcion CodificacionHamming
def CodificacionHamming():
    ventana.withdraw()
    
    def Hamming():
        Mensaje=TramaUsuario.get()
        if(len(Mensaje)>25):
            LabelError.configure(text="La trama ingresada es de mas de 25 bits, se eliminaran bits")
            while(len(Mensaje)>25):
                Mensaje=Mensaje[:-1]
        i=0
        while i<len(Mensaje):
            if(Mensaje[i]!="1"):
                if(Mensaje[i]!="0"):
                    LabelError.configure(text="La trama ingresada tiene caracteres diferentes a 1 o 0, se cambiaran a 0")
                    a=Mensaje[i]
                    Mensaje=Mensaje.replace(a,"0")
            i=i+1
        MensajeConParidad=""
        MensajeConParidadYDatos=""
        ListaMensaje=list()
        ListaMensaje2=list()
        ListaDatos=list()
        ListaDatos2=list()
        Posiciones2N=[1, 2, 4, 8, 16, 32, 64, 128, 256]
        Fila1=list()
        Fila2=list()
        Fila3=list()
        Fila4=list()
        Fila5=list()
        DFila1=list()
        DFila2=list()
        DFila3=list()
        DFila4=list()
        DFila5=list()
        DatosMenFila1=""
        DatosMenFila2=""
        DatosMenFila3=""
        DatosMenFila4=""
        DatosMenFila5=""
        ParidadFila1=0
        ParidadFila2=0
        ParidadFila3=0
        ParidadFila4=0
        ParidadFila5=0
        TramaFinal=""
        ListaTramaFinal=list()
        MParte2=""
        MParte3=""
        MParte4=""
        MParte5=""
        N="N"

        i=0
        par=0
        while i < len(Mensaje):
            ListaDatos.append(Mensaje[i])
            par=par+1
            Datos=("D"+str(par))
            ListaDatos2.append(Datos)
            i=i+1
        i=0
        par=0
        while i < len(Mensaje):
            ListaMensaje.append(Mensaje[i])
            par=par+1
            Datos=("D"+str(par))
            ListaMensaje2.append(Datos)
            i=i+1
        i=0
        pos=0
        par=0
        while i < len(Mensaje)+4:
            pos=i+1  
            if pos in Posiciones2N:
                par=par+1
                Paridad=("P"+str(par))
                Paridad2="P"
                ListaMensaje.insert(pos-1,Paridad2)
                ListaMensaje2.insert(pos-1,Paridad)
                ListaDatos.insert(pos-1,Paridad)
            i=i+1
        MensajeConParidad=MensajeConParidad.join(ListaMensaje)
        MensajeConParidadYDatos=MensajeConParidadYDatos.join(ListaMensaje2)

        if(len(ListaMensaje2)>0):
            Posicion34.set(ListaMensaje2[0])
        else:
            Posicion34.set(N)
        if(len(ListaMensaje2)>1):
            Posicion35.set(ListaMensaje2[1])
        else:
            Posicion35.set(N)
        if(len(ListaMensaje2)>2):
            Posicion36.set(ListaMensaje2[2])
        else:
            Posicion36.set(N)
        if(len(ListaMensaje2)>3):
            Posicion37.set(ListaMensaje2[3])
        else:
            Posicion37.set(N)
        if(len(ListaMensaje2)>4):
            Posicion38.set(ListaMensaje2[4])
        else:
            Posicion38.set(N)
        if(len(ListaMensaje2)>5):
            Posicion39.set(ListaMensaje2[5])
        else:
            Posicion39.set(N)
        if(len(ListaMensaje2)>6):
            Posicion40.set(ListaMensaje2[6])
        else:
            Posicion40.set(N)
        if(len(ListaMensaje2)>7):
            Posicion41.set(ListaMensaje2[7])
        else:
            Posicion41.set(N)
        if(len(ListaMensaje2)>8):
            Posicion42.set(ListaMensaje2[8])
        else:
            Posicion42.set(N)
        if(len(ListaMensaje2)>9):
            Posicion43.set(ListaMensaje2[9])
        else:
            Posicion43.set(N)
        if(len(ListaMensaje2)>10):
            Posicion44.set(ListaMensaje2[10])
        else:
            Posicion44.set(N)
        if(len(ListaMensaje2)>11):
            Posicion45.set(ListaMensaje2[11])
        else:
            Posicion45.set(N)
        if(len(ListaMensaje2)>12):
            Posicion46.set(ListaMensaje2[12])
        else:
            Posicion46.set(N)
        if(len(ListaMensaje2)>13):
            Posicion47.set(ListaMensaje2[13])
        else:
            Posicion47.set(N)
        if(len(ListaMensaje2)>14):
            Posicion48.set(ListaMensaje2[14])
        else:
            Posicion48.set(N)
        if(len(ListaMensaje2)>15):
            Posicion49.set(ListaMensaje2[15])
        else:
            Posicion49.set(N)
        if(len(ListaMensaje2)>16):
            Posicion50.set(ListaMensaje2[16])
        else:
            Posicion50.set(N)
        if(len(ListaMensaje2)>17):
            Posicion51.set(ListaMensaje2[17])
        else:
            Posicion51.set(N)
        if(len(ListaMensaje2)>18):
            Posicion52.set(ListaMensaje2[18])
        else:
            Posicion52.set(N)
        if(len(ListaMensaje2)>19):
            Posicion53.set(ListaMensaje2[19])
        else:
            Posicion53.set(N)
        if(len(ListaMensaje2)>20):
            Posicion54.set(ListaMensaje2[20])
        else:
            Posicion54.set(N)
        if(len(ListaMensaje2)>21):
            Posicion55.set(ListaMensaje2[21])
        else:
            Posicion55.set(N)
        if(len(ListaMensaje2)>22):
            Posicion56.set(ListaMensaje2[22])
        else:
            Posicion56.set(N)
        if(len(ListaMensaje2)>23):
            Posicion57.set(ListaMensaje2[23])
        else:
            Posicion57.set(N)
        if(len(ListaMensaje2)>24):
            Posicion58.set(ListaMensaje2[24])
        else:
            Posicion58.set(N)
        if(len(ListaMensaje2)>25):
            Posicion59.set(ListaMensaje2[25])
        else:
            Posicion59.set(N)
        if(len(ListaMensaje2)>26):
            Posicion60.set(ListaMensaje2[26])
        else:
            Posicion60.set(N)
        if(len(ListaMensaje2)>27):
            Posicion61.set(ListaMensaje2[27])
        else:
            Posicion61.set(N)
        if(len(ListaMensaje2)>28):
            Posicion62.set(ListaMensaje2[28])
        else:
            Posicion62.set(N)
        if(len(ListaMensaje2)>29):
            Posicion63.set(ListaMensaje2[29])
        else:
            Posicion63.set(N)
        if(len(ListaMensaje2)>30):
            Posicion64.set(ListaMensaje2[30])
        else:
            Posicion64.set(N)
            
        if(len(ListaMensaje2)>0):
            VPosicion34.set(ListaMensaje2[0])
        else:
            VPosicion34.set(N)
        if(len(ListaMensaje2)>1):
            VPosicion35.set(ListaMensaje2[1])
        else:
            VPosicion35.set(N)
        if(len(ListaMensaje2)>2):
            VPosicion36.set(ListaMensaje2[2])
        else:
            VPosicion36.set(N)
        if(len(ListaMensaje2)>3):
            VPosicion37.set(ListaMensaje2[3])
        else:
            VPosicion37.set(N)
        if(len(ListaMensaje2)>4):
            VPosicion38.set(ListaMensaje2[4])
        else:
            VPosicion38.set(N)
        if(len(ListaMensaje2)>5):
            VPosicion39.set(ListaMensaje2[5])
        else:
            VPosicion39.set(N)
        if(len(ListaMensaje2)>6):
            VPosicion40.set(ListaMensaje2[6])
        else:
            VPosicion40.set(N)
        if(len(ListaMensaje2)>7):
            VPosicion41.set(ListaMensaje2[7])
        else:
            VPosicion41.set(N)
        if(len(ListaMensaje2)>8):
            VPosicion42.set(ListaMensaje2[8])
        else:
            VPosicion42.set(N)
        if(len(ListaMensaje2)>9):
            VPosicion43.set(ListaMensaje2[9])
        else:
            VPosicion43.set(N)
        if(len(ListaMensaje2)>10):
            VPosicion44.set(ListaMensaje2[10])
        else:
            VPosicion44.set(N)
        if(len(ListaMensaje2)>11):
            VPosicion45.set(ListaMensaje2[11])
        else:
            VPosicion45.set(N)
        if(len(ListaMensaje2)>12):
            VPosicion46.set(ListaMensaje2[12])
        else:
            VPosicion46.set(N)
        if(len(ListaMensaje2)>13):
            VPosicion47.set(ListaMensaje2[13])
        else:
            VPosicion47.set(N)
        if(len(ListaMensaje2)>14):
            VPosicion48.set(ListaMensaje2[14])
        else:
            VPosicion48.set(N)
        if(len(ListaMensaje2)>15):
            VPosicion49.set(ListaMensaje2[15])
        else:
            VPosicion49.set(N)
        if(len(ListaMensaje2)>16):
            VPosicion50.set(ListaMensaje2[16])
        else:
            VPosicion50.set(N)
        if(len(ListaMensaje2)>17):
            VPosicion51.set(ListaMensaje2[17])
        else:
            VPosicion51.set(N)
        if(len(ListaMensaje2)>18):
            VPosicion52.set(ListaMensaje2[18])
        else:
            VPosicion52.set(N)
        if(len(ListaMensaje2)>19):
            VPosicion53.set(ListaMensaje2[19])
        else:
            VPosicion53.set(N)
        if(len(ListaMensaje2)>20):
            VPosicion54.set(ListaMensaje2[20])
        else:
            VPosicion54.set(N)
        if(len(ListaMensaje2)>21):
            VPosicion55.set(ListaMensaje2[21])
        else:
            VPosicion55.set(N)
        if(len(ListaMensaje2)>22):
            VPosicion56.set(ListaMensaje2[22])
        else:
            VPosicion56.set(N)
        if(len(ListaMensaje2)>23):
            VPosicion57.set(ListaMensaje2[23])
        else:
            VPosicion57.set(N)
        if(len(ListaMensaje2)>24):
            VPosicion58.set(ListaMensaje2[24])
        else:
            VPosicion58.set(N)
        if(len(ListaMensaje2)>25):
            VPosicion59.set(ListaMensaje2[25])
        else:
            VPosicion59.set(N)
        if(len(ListaMensaje2)>26):
            VPosicion60.set(ListaMensaje2[26])
        else:
            VPosicion60.set(N)
        if(len(ListaMensaje2)>27):
            VPosicion61.set(ListaMensaje2[27])
        else:
            VPosicion61.set(N)
        if(len(ListaMensaje2)>28):
            VPosicion62.set(ListaMensaje2[28])
        else:
            VPosicion62.set(N)
        if(len(ListaMensaje2)>29):
            VPosicion63.set(ListaMensaje2[29])
        else:
            VPosicion63.set(N)
        
        i=0
        while i<len(ListaDatos):
            if i%2==0:
                Fila1.append(ListaDatos[i])
            else:
                Fila1.append("-")
                cont=1    
            i=i+1

        i=0
        val=0
        cont=1
        while i<len(ListaDatos):
            if val<1:
                Fila2.append("-")
                val=val+1
            elif(val==1):
                Fila2.append(ListaDatos[i])  
                cont=cont+1      
                if(cont>2):
                    val=2
                    cont=1
            elif(val==2):
                Fila2.append("-")   
                cont=cont+1
                if(cont>2):
                    val=1
                    cont=1
            i=i+1

        i=0
        val=0
        cont=1
        while i<len(ListaDatos):
            if val<4:
                Fila3.append("-")
                val=val+1
            elif(val==4):
                Fila3.append(ListaDatos[i])  
                cont=cont+1      
                if(cont==4):
                    val=5
                    cont=0
            elif(val==5):
                Fila3.append("-")   
                cont=cont+1
                if(cont==4):
                    val=4
                    cont=0
            i=i+1
        if(len(Fila3)>3):
            Fila3[3]="P3"

        i=0
        val=0
        cont=1
        while i<len(ListaDatos):
            if val<8:
                Fila4.append("-")
                val=val+1
            elif(val==8):
                Fila4.append(ListaDatos[i])  
                cont=cont+1      
                if(cont==8):
                    val=9
                    cont=0
            elif(val==9):
                Fila4.append("-")   
                cont=cont+1
                if(cont==8):
                    val=8
                    cont=0
            i=i+1
        if(len(Fila4)>7):
            Fila4[7]="P4"

        i=0
        val=0
        cont=1
        while i<len(ListaDatos):
            if val<16:
                Fila5.append("-")
                val=val+1
            elif(val==16):
                Fila5.append(ListaDatos[i])  
                cont=cont+1      
                if(cont==16):
                    val=17
                    cont=0
            elif(val==16):
                Fila5.append("-")   
                cont=cont+1
                if(cont==16):
                    val=16
                    cont=0
            i=i+1
        if(len(Fila5)>15):
            Fila5[15]="P5"

        if(len(Fila1)>0):
            Posicion66.set(Fila1[0])
        else:
            Posicion66.set(N)
        if(len(Fila1)>1):
            Posicion67.set(Fila1[1])
        else:
            Posicion67.set(N)
        if(len(Fila1)>2):
            Posicion68.set(Fila1[2])
        else:
            Posicion68.set(N)
        if(len(Fila1)>3):
            Posicion69.set(Fila1[3])
        else:
            Posicion69.set(N)
        if(len(Fila1)>4):
            Posicion70.set(Fila1[4])
        else:
            Posicion70.set(N)
        if(len(Fila1)>5):
            Posicion71.set(Fila1[5])
        else:
            Posicion71.set(N)
        if(len(Fila1)>6):
            Posicion72.set(Fila1[6])
        else:
            Posicion72.set(N)
        if(len(Fila1)>7):
            Posicion73.set(Fila1[7])
        else:
            Posicion73.set(N)
        if(len(Fila1)>8):
            Posicion74.set(Fila1[8])
        else:
            Posicion74.set(N)
        if(len(Fila1)>9):
            Posicion75.set(Fila1[9])
        else:
            Posicion75.set(N)
        if(len(Fila1)>10):
            Posicion76.set(Fila1[10])
        else:
            Posicion76.set(N)
        if(len(Fila1)>11):
            Posicion77.set(Fila1[11])
        else:
            Posicion77.set(N)
        if(len(Fila1)>12):
            Posicion78.set(Fila1[12])
        else:
            Posicion78.set(N)
        if(len(Fila1)>13):
            Posicion79.set(Fila1[13])
        else:
            Posicion79.set(N)
        if(len(Fila1)>14):
            Posicion80.set(Fila1[14])
        else:
            Posicion80.set(N)
        if(len(Fila1)>15):
            Posicion81.set(Fila1[15])
        else:
            Posicion81.set(N)
        if(len(Fila1)>16):
            Posicion82.set(Fila1[16])
        else:
            Posicion82.set(N)
        if(len(Fila1)>17):
            Posicion83.set(Fila1[17])
        else:
            Posicion83.set(N)
        if(len(Fila1)>18):
            Posicion84.set(Fila1[18])
        else:
            Posicion84.set(N)
        if(len(Fila1)>19):
            Posicion85.set(Fila1[19])
        else:
            Posicion85.set(N)
        if(len(Fila1)>20):
            Posicion86.set(Fila1[20])
        else:
            Posicion86.set(N)
        if(len(Fila1)>21):
            Posicion87.set(Fila1[21])
        else:
            Posicion87.set(N)
        if(len(Fila1)>22):
            Posicion88.set(Fila1[22])
        else:
            Posicion88.set(N)
        if(len(Fila1)>23):
            Posicion89.set(Fila1[23])
        else:
            Posicion89.set(N)
        if(len(Fila1)>24):
            Posicion90.set(Fila1[24])
        else:
            Posicion90.set(N)
        if(len(Fila1)>25):
            Posicion91.set(Fila1[25])
        else:
            Posicion91.set(N)
        if(len(Fila1)>26):
            Posicion92.set(Fila1[26])
        else:
            Posicion92.set(N)
        if(len(Fila1)>27):
            Posicion93.set(Fila1[27])
        else:
            Posicion93.set(N)
        if(len(Fila1)>28):
            Posicion94.set(Fila1[28])
        else:
            Posicion94.set(N)
        if(len(Fila1)>28):
            Posicion95.set(Fila1[28])
        else:
            Posicion95.set(N)
        if(len(Fila2)>0):
            Posicion98.set(Fila2[0])
        else:
            Posicion98.set(N)
        if(len(Fila2)>1):
            Posicion99.set(Fila2[1])
        else:
            Posicion99.set(N)
        if(len(Fila2)>2):
            Posicion100.set(Fila2[2])
        else:
            Posicion100.set(N)
        if(len(Fila2)>3):
            Posicion101.set(Fila2[3])
        else:
            Posicion101.set(N)
        if(len(Fila2)>4):
            Posicion102.set(Fila2[4])
        else:
            Posicion102.set(N)
        if(len(Fila2)>5):
            Posicion103.set(Fila2[5])
        else:
            Posicion103.set(N)
        if(len(Fila2)>6):
            Posicion104.set(Fila2[6])
        else:
            Posicion104.set(N)
        if(len(Fila2)>7):
            Posicion105.set(Fila2[7])
        else:
            Posicion105.set(N)
        if(len(Fila2)>8):
            Posicion106.set(Fila2[8])
        else:
            Posicion106.set(N)
        if(len(Fila2)>9):
            Posicion107.set(Fila2[9])
        else:
            Posicion107.set(N)
        if(len(Fila2)>10):
            Posicion108.set(Fila2[10])
        else:
            Posicion108.set(N)
        if(len(Fila2)>11):
            Posicion109.set(Fila2[11])
        else:
            Posicion109.set(N)
        if(len(Fila2)>12):
            Posicion110.set(Fila2[12])
        else:
            Posicion110.set(N)
        if(len(Fila2)>13):
            Posicion111.set(Fila2[13])
        else:
            Posicion111.set(N)
        if(len(Fila2)>14):
            Posicion112.set(Fila2[14])
        else:
            Posicion112.set(N)
        if(len(Fila2)>15):
            Posicion113.set(Fila2[15])
        else:
            Posicion113.set(N)
        if(len(Fila2)>16):
            Posicion114.set(Fila2[16])
        else:
            Posicion114.set(N)
        if(len(Fila2)>17):
            Posicion115.set(Fila2[17])
        else:
            Posicion115.set(N)
        if(len(Fila2)>18):
            Posicion116.set(Fila2[18])
        else:
            Posicion116.set(N)
        if(len(Fila2)>19):
            Posicion117.set(Fila2[19])
        else:
            Posicion117.set(N)
        if(len(Fila2)>20):
            Posicion118.set(Fila2[20])
        else:
            Posicion118.set(N)
        if(len(Fila2)>21):
            Posicion119.set(Fila2[21])
        else:
            Posicion119.set(N)
        if(len(Fila2)>22):
            Posicion120.set(Fila2[22])
        else:
            Posicion120.set(N)
        if(len(Fila2)>23):
            Posicion121.set(Fila2[23])
        else:
            Posicion121.set(N)
        if(len(Fila2)>24):
            Posicion122.set(Fila2[24])
        else:
            Posicion122.set(N)
        if(len(Fila2)>25):
            Posicion123.set(Fila2[25])
        else:
            Posicion123.set(N)
        if(len(Fila2)>26):
            Posicion124.set(Fila2[26])
        else:
            Posicion124.set(N)
        if(len(Fila2)>27):
            Posicion125.set(Fila2[27])
        else:
            Posicion125.set(N)
        if(len(Fila2)>28):
            Posicion126.set(Fila2[28])
        else:
            Posicion126.set(N)
        if(len(Fila2)>29):
            Posicion127.set(Fila2[29])
        else:
            Posicion127.set(N)
        if(len(Fila3)>0):
            Posicion130.set(Fila3[0])
        else:
            Posicion130.set(N)
        if(len(Fila3)>1):
            Posicion131.set(Fila3[1])
        else:
            Posicion131.set(N)
        if(len(Fila3)>2):
            Posicion132.set(Fila3[2])
        else:
            Posicion132.set(N)
        if(len(Fila3)>3):
            Posicion133.set(Fila3[3])
        else:
            Posicion133.set(N)
        if(len(Fila3)>4):
            Posicion134.set(Fila3[4])
        else:
            Posicion134.set(N)
        if(len(Fila3)>5):
            Posicion135.set(Fila3[5])
        else:
            Posicion135.set(N)
        if(len(Fila3)>6):
            Posicion136.set(Fila3[6])
        else:
            Posicion136.set(N)
        if(len(Fila3)>7):
            Posicion137.set(Fila3[7])
        else:
            Posicion137.set(N)
        if(len(Fila3)>8):
            Posicion138.set(Fila3[8])
        else:
            Posicion138.set(N)
        if(len(Fila3)>9):
            Posicion139.set(Fila3[9])
        else:
            Posicion139.set(N)
        if(len(Fila3)>10):
            Posicion140.set(Fila3[10])
        else:
            Posicion140.set(N)
        if(len(Fila3)>11):
            Posicion141.set(Fila3[11])
        else:
            Posicion141.set(N)
        if(len(Fila3)>12):
            Posicion142.set(Fila3[12])
        else:
            Posicion142.set(N)
        if(len(Fila3)>13):
            Posicion143.set(Fila3[13])
        else:
            Posicion143.set(N)
        if(len(Fila3)>14):
            Posicion144.set(Fila3[14])
        else:
            Posicion144.set(N)
        if(len(Fila3)>15):
            Posicion145.set(Fila3[15])
        else:
            Posicion145.set(N)
        if(len(Fila3)>16):
            Posicion146.set(Fila3[16])
        else:
            Posicion146.set(N)
        if(len(Fila3)>17):
            Posicion147.set(Fila3[17])
        else:
            Posicion147.set(N)
        if(len(Fila3)>18):
            Posicion148.set(Fila3[18])
        else:
            Posicion148.set(N)
        if(len(Fila3)>19):
            Posicion149.set(Fila3[19])
        else:
            Posicion149.set(N)
        if(len(Fila3)>20):
            Posicion150.set(Fila3[20])
        else:
            Posicion150.set(N)
        if(len(Fila3)>21):
            Posicion151.set(Fila3[21])
        else:
            Posicion151.set(N)
        if(len(Fila3)>22):
            Posicion152.set(Fila3[22])
        else:
            Posicion152.set(N)
        if(len(Fila3)>23):
            Posicion153.set(Fila3[23])
        else:
            Posicion153.set(N)
        if(len(Fila3)>24):
            Posicion154.set(Fila3[24])
        else:
            Posicion154.set(N)
        if(len(Fila3)>25):
            Posicion155.set(Fila3[25])
        else:
            Posicion155.set(N)
        if(len(Fila3)>26):
            Posicion156.set(Fila3[26])
        else:
            Posicion156.set(N)
        if(len(Fila3)>27):
            Posicion157.set(Fila3[27])
        else:
            Posicion157.set(N)
        if(len(Fila3)>28):
            Posicion158.set(Fila3[28])
        else:
            Posicion158.set(N)
        if(len(Fila3)>29):
            Posicion159.set(Fila3[29])
        else:
            Posicion159.set(N)
        if(len(Fila4)>0):
            Posicion162.set(Fila4[0])
        else:
            Posicion162.set(N)
        if(len(Fila4)>1):
            Posicion163.set(Fila4[1])
        else:
            Posicion163.set(N)
        if(len(Fila4)>2):
            Posicion164.set(Fila4[2])
        else:
            Posicion164.set(N)
        if(len(Fila4)>3):
            Posicion165.set(Fila4[3])
        else:
            Posicion165.set(N)
        if(len(Fila4)>4):
            Posicion166.set(Fila4[4])
        else:
            Posicion166.set(N)
        if(len(Fila4)>5):
            Posicion167.set(Fila4[5])
        else:
            Posicion167.set(N)
        if(len(Fila4)>6):
            Posicion168.set(Fila4[6])
        else:
            Posicion168.set(N)
        if(len(Fila4)>7):
            Posicion169.set(Fila4[7])
        else:
            Posicion169.set(N)
        if(len(Fila4)>8):
            Posicion170.set(Fila4[8])
        else:
            Posicion170.set(N)
        if(len(Fila4)>9):
            Posicion171.set(Fila4[9])
        else:
            Posicion171.set(N)
        if(len(Fila4)>10):
            Posicion172.set(Fila4[10])
        else:
            Posicion172.set(N)
        if(len(Fila4)>11):
            Posicion173.set(Fila4[11])
        else:
            Posicion173.set(N)
        if(len(Fila4)>12):
            Posicion174.set(Fila4[12])
        else:
            Posicion174.set(N)
        if(len(Fila4)>13):
            Posicion175.set(Fila4[13])
        else:
            Posicion175.set(N)
        if(len(Fila4)>14):
            Posicion176.set(Fila4[14])
        else:
            Posicion176.set(N)
        if(len(Fila4)>15):
            Posicion177.set(Fila4[15])
        else:
            Posicion177.set(N)
        if(len(Fila4)>16):
            Posicion178.set(Fila4[16])
        else:
            Posicion178.set(N)
        if(len(Fila4)>17):
            Posicion179.set(Fila4[17])
        else:
            Posicion179.set(N)
        if(len(Fila4)>18):
            Posicion180.set(Fila4[18])
        else:
            Posicion180.set(N)
        if(len(Fila4)>19):
            Posicion181.set(Fila4[19])
        else:
            Posicion181.set(N)
        if(len(Fila4)>20):
            Posicion182.set(Fila4[20])
        else:
            Posicion182.set(N)
        if(len(Fila4)>21):
            Posicion183.set(Fila4[21])
        else:
            Posicion183.set(N)
        if(len(Fila4)>22):
            Posicion184.set(Fila4[22])
        else:
            Posicion184.set(N)
        if(len(Fila4)>23):
            Posicion185.set(Fila4[23])
        else:
            Posicion185.set(N)
        if(len(Fila4)>24):
            Posicion186.set(Fila4[24])
        else:
            Posicion186.set(N)
        if(len(Fila4)>25):
            Posicion187.set(Fila4[25])
        else:
            Posicion187.set(N)
        if(len(Fila4)>26):
            Posicion188.set(Fila4[26])
        else:
            Posicion188.set(N)
        if(len(Fila4)>27):
            Posicion189.set(Fila4[27])
        else:
            Posicion189.set(N)
        if(len(Fila4)>28):
            Posicion190.set(Fila4[28])
        else:
            Posicion190.set(N)
        if(len(Fila4)>29):
            Posicion191.set(Fila4[29])
        else:
            Posicion191.set(N)
        if(len(Fila5)>0):
            Posicion194.set(Fila5[0])
        else:
            Posicion194.set(N)
        if(len(Fila5)>1):
            Posicion195.set(Fila5[1])
        else:
            Posicion195.set(N)
        if(len(Fila5)>2):
            Posicion196.set(Fila5[2])
        else:
            Posicion196.set(N)
        if(len(Fila5)>3):
            Posicion197.set(Fila5[3])
        else:
            Posicion197.set(N)
        if(len(Fila5)>4):
            Posicion198.set(Fila5[4])
        else:
            Posicion198.set(N)
        if(len(Fila5)>5):
            Posicion199.set(Fila5[5])
        else:
            Posicion199.set(N)
        if(len(Fila5)>6):
            Posicion200.set(Fila5[6])
        else:
            Posicion200.set(N)
        if(len(Fila5)>7):
            Posicion201.set(Fila5[7])
        else:
            Posicion201.set(N)
        if(len(Fila5)>8):
            Posicion202.set(Fila5[8])
        else:
            Posicion202.set(N)
        if(len(Fila5)>9):
            Posicion203.set(Fila5[9])
        else:
            Posicion203.set(N)
        if(len(Fila5)>10):
            Posicion204.set(Fila5[10])
        else:
            Posicion204.set(N)
        if(len(Fila5)>11):
            Posicion205.set(Fila5[11])
        else:
            Posicion205.set(N)
        if(len(Fila5)>12):
            Posicion206.set(Fila5[12])
        else:
            Posicion206.set(N)
        if(len(Fila5)>13):
            Posicion207.set(Fila5[13])
        else:
            Posicion207.set(N)
        if(len(Fila5)>14):
            Posicion208.set(Fila5[14])
        else:
            Posicion208.set(N)
        if(len(Fila5)>15):
            Posicion209.set(Fila5[15])
        else:
            Posicion209.set(N)
        if(len(Fila5)>16):
            Posicion210.set(Fila5[16])
        else:
            Posicion210.set(N)
        if(len(Fila5)>17):
            Posicion211.set(Fila5[17])
        else:
            Posicion211.set(N)
        if(len(Fila5)>18):
            Posicion212.set(Fila5[18])
        else:
            Posicion212.set(N)
        if(len(Fila5)>19):
            Posicion213.set(Fila5[19])
        else:
            Posicion213.set(N)
        if(len(Fila5)>20):
            Posicion214.set(Fila5[20])
        else:
            Posicion214.set(N)
        if(len(Fila5)>21):
            Posicion215.set(Fila5[21])
        else:
            Posicion215.set(N)
        if(len(Fila5)>22):
            Posicion216.set(Fila5[22])
        else:
            Posicion216.set(N)
        if(len(Fila5)>23):
            Posicion217.set(Fila5[23])
        else:
            Posicion217.set(N)
        if(len(Fila5)>24):
            Posicion218.set(Fila5[24])
        else:
            Posicion218.set(N)
        if(len(Fila5)>25):
            Posicion219.set(Fila5[25])
        else:
            Posicion219.set(N)
        if(len(Fila5)>26):
            Posicion220.set(Fila5[26])
        else:
            Posicion220.set(N)
        if(len(Fila5)>27):
            Posicion221.set(Fila5[27])
        else:
            Posicion221.set(N)
        if(len(Fila5)>28):
            Posicion222.set(Fila5[28])
        else:
            Posicion222.set(N)
        if(len(Fila5)>29):
            Posicion223.set(Fila5[29])
        else:
            Posicion223.set(N)
        #Lista Datos
        i=0
        while i<len(ListaMensaje):
            if i%2==0:
                DFila1.append(ListaMensaje[i])
            else:
                DFila1.append("-")
                cont=1    
            i=i+1

        i=0
        val=0
        cont=1
        while i<len(ListaMensaje):
            if val<1:
                DFila2.append("-")
                val=val+1
            elif(val==1):
                DFila2.append(ListaMensaje[i])  
                cont=cont+1      
                if(cont>2):
                    val=2
                    cont=1
            elif(val==2):
                DFila2.append("-")   
                cont=cont+1
                if(cont>2):
                    val=1
                    cont=1
            i=i+1

        i=0
        val=0
        cont=1
        while i<len(ListaMensaje):
            if val<4:
                DFila3.append("-")
                val=val+1
            elif(val==4):
                DFila3.append(ListaMensaje[i])  
                cont=cont+1      
                if(cont==4):
                    val=5
                    cont=0
            elif(val==5):
                DFila3.append("-")   
                cont=cont+1
                if(cont==4):
                    val=4
                    cont=0
            i=i+1

        i=0
        val=0
        cont=1
        while i<len(ListaMensaje):
            if val<8:
                DFila4.append("-")
                val=val+1
            elif(val==8):
                DFila4.append(ListaMensaje[i])  
                cont=cont+1      
                if(cont==8):
                    val=9
                    cont=0
            elif(val==9):
                DFila4.append("-")   
                cont=cont+1
                if(cont==8):
                    val=8
                    cont=0
            i=i+1

        i=0
        val=0
        cont=1
        while i<len(ListaMensaje):
            if val<16:
                DFila5.append("-")
                val=val+1
            elif(val==16):
                DFila5.append(ListaMensaje[i])  
                cont=cont+1      
                if(cont==16):
                    val=17
                    cont=0
            elif(val==16):
                DFila5.append("-")   
                cont=cont+1
                if(cont==16):
                    val=16
                    cont=0
            i=i+1

        DatosMenFila1=DatosMenFila1.join(DFila1)
        DatosMenFila2=DatosMenFila2.join(DFila2)
        DatosMenFila3=DatosMenFila3.join(DFila3)
        DatosMenFila4=DatosMenFila4.join(DFila4)
        DatosMenFila5=DatosMenFila5.join(DFila5)

        ParidadFila1=DatosMenFila1.count("1")
        ParidadFila2=DatosMenFila2.count("1")
        ParidadFila3=DatosMenFila3.count("1")
        ParidadFila4=DatosMenFila4.count("1")
        ParidadFila5=DatosMenFila5.count("1")
        
        if(len(DFila1)>0):
            if(ParidadFila1%2==0):
                DFila1[0]="0"
            else:
                DFila1[0]="1"
        if(len(DFila2)>2):
            if(ParidadFila2%2==0):
                DFila2[1]="0"
            else:
                DFila2[1]="1"
        if(len(DFila3)>4):
            if(ParidadFila3%2==0):
                DFila3[3]="0"
            else:
                DFila3[3]="1"
        if(len(DFila4)>8):
            if(ParidadFila4%2==0):
                DFila4[7]="0"
            else:
                DFila4[7]="1"
        if(len(DFila5)>15):
            if(ParidadFila5%2==0):
                DFila5[15]="0"
            else:
                DFila5[15]="1"

        if(len(DFila1)>0):
            VPosicion98.set(DFila1[0])
        else:
            VPosicion98.set(N)
        if(len(DFila1)>1):
            VPosicion99.set(DFila1[1])
        else:
            VPosicion99.set(N)
        if(len(DFila1)>2):
            VPosicion100.set(DFila1[2])
        else:
            VPosicion100.set(N)
        if(len(DFila1)>3):
            VPosicion101.set(DFila1[3])
        else:
            VPosicion101.set(N)
        if(len(DFila1)>4):
            VPosicion102.set(DFila1[4])
        else:
            VPosicion102.set(N)
        if(len(DFila1)>5):
            VPosicion103.set(DFila1[5])
        else:
            VPosicion103.set(N)
        if(len(DFila1)>6):
            VPosicion104.set(DFila1[6])
        else:
            VPosicion104.set(N)
        if(len(DFila1)>7):
            VPosicion105.set(DFila1[7])
        else:
            VPosicion105.set(N)
        if(len(DFila1)>8):
            VPosicion106.set(DFila1[8])
        else:
            VPosicion106.set(N)
        if(len(DFila1)>9):
            VPosicion107.set(DFila1[9])
        else:
            VPosicion107.set(N)
        if(len(DFila1)>10):
            VPosicion108.set(DFila1[10])
        else:
            VPosicion108.set(N)
        if(len(DFila1)>11):
            VPosicion109.set(DFila1[11])
        else:
            VPosicion109.set(N)
        if(len(DFila1)>12):
            VPosicion110.set(DFila1[12])
        else:
            VPosicion110.set(N)
        if(len(DFila1)>13):
            VPosicion111.set(DFila1[13])
        else:
            VPosicion111.set(N)
        if(len(DFila1)>14):
            VPosicion112.set(DFila1[14])
        else:
            VPosicion112.set(N)
        if(len(DFila1)>15):
            VPosicion113.set(DFila1[15])
        else:
            VPosicion113.set(N)
        if(len(DFila1)>16):
            VPosicion114.set(DFila1[16])
        else:
            VPosicion114.set(N)
        if(len(DFila1)>17):
            VPosicion115.set(DFila1[17])
        else:
            VPosicion115.set(N)
        if(len(DFila1)>18):
            VPosicion116.set(DFila1[18])
        else:
            VPosicion116.set(N)
        if(len(DFila1)>19):
            VPosicion117.set(DFila1[19])
        else:
            VPosicion117.set(N)
        if(len(DFila1)>20):
            VPosicion118.set(DFila1[20])
        else:
            VPosicion118.set(N)
        if(len(DFila1)>21):
            VPosicion119.set(DFila1[21])
        else:
            VPosicion119.set(N)
        if(len(DFila1)>22):
            VPosicion120.set(DFila1[22])
        else:
            VPosicion120.set(N)
        if(len(DFila1)>23):
            VPosicion121.set(DFila1[23])
        else:
            VPosicion121.set(N)
        if(len(DFila1)>24):
            VPosicion122.set(DFila1[24])
        else:
            VPosicion122.set(N)
        if(len(DFila1)>25):
            VPosicion123.set(DFila1[25])
        else:
            VPosicion123.set(N)
        if(len(DFila1)>26):
            VPosicion124.set(DFila1[26])
        else:
            VPosicion124.set(N)
        if(len(DFila1)>27):
            VPosicion125.set(DFila1[27])
        else:
            VPosicion125.set(N)
        if(len(DFila1)>28):
            VPosicion126.set(DFila1[28])
        else:
            VPosicion126.set(N)
        if(len(DFila1)>29):
            VPosicion127.set(DFila1[29])
        else:
            VPosicion127.set(N)
        if(len(DFila2)>0):
            VPosicion130.set(DFila2[0])
        else:
            VPosicion130.set(N)
        if(len(DFila2)>1):
            VPosicion131.set(DFila2[1])
        else:
            VPosicion131.set(N)
        if(len(DFila2)>2):
            VPosicion132.set(DFila2[2])
        else:
            VPosicion132.set(N)
        if(len(DFila2)>3):
            VPosicion133.set(DFila2[3])
        else:
            VPosicion133.set(N)
        if(len(DFila2)>4):
            VPosicion134.set(DFila2[4])
        else:
            VPosicion134.set(N)
        if(len(DFila2)>5):
            VPosicion135.set(DFila2[5])
        else:
            VPosicion135.set(N)
        if(len(DFila2)>6):
            VPosicion136.set(DFila2[6])
        else:
            VPosicion136.set(N)
        if(len(DFila2)>7):
            VPosicion137.set(DFila2[7])
        else:
            VPosicion137.set(N)
        if(len(DFila2)>8):
            VPosicion138.set(DFila2[8])
        else:
            VPosicion138.set(N)
        if(len(DFila2)>9):
            VPosicion139.set(DFila2[9])
        else:
            VPosicion139.set(N)
        if(len(DFila2)>10):
            VPosicion140.set(DFila2[10])
        else:
            VPosicion140.set(N)
        if(len(DFila2)>11):
            VPosicion141.set(DFila2[11])
        else:
            VPosicion141.set(N)
        if(len(DFila2)>12):
            VPosicion142.set(DFila2[12])
        else:
            VPosicion142.set(N)
        if(len(DFila2)>13):
            VPosicion143.set(DFila2[13])
        else:
            VPosicion143.set(N)
        if(len(DFila2)>14):
            VPosicion144.set(DFila2[14])
        else:
            VPosicion144.set(N)
        if(len(DFila2)>15):
            VPosicion145.set(DFila2[15])
        else:
            VPosicion145.set(N)
        if(len(DFila2)>16):
            VPosicion146.set(DFila2[16])
        else:
            VPosicion146.set(N)
        if(len(DFila2)>17):
            VPosicion147.set(DFila2[17])
        else:
            VPosicion147.set(N)
        if(len(DFila2)>18):
            VPosicion148.set(DFila2[18])
        else:
            VPosicion148.set(N)
        if(len(DFila2)>19):
            VPosicion149.set(DFila2[19])
        else:
            VPosicion149.set(N)
        if(len(DFila2)>20):
            VPosicion150.set(DFila2[20])
        else:
            VPosicion150.set(N)
        if(len(DFila2)>21):
            VPosicion151.set(DFila2[21])
        else:
            VPosicion151.set(N)
        if(len(DFila2)>22):
            VPosicion152.set(DFila2[22])
        else:
            VPosicion152.set(N)
        if(len(DFila2)>23):
            VPosicion153.set(DFila2[23])
        else:
            VPosicion153.set(N)
        if(len(DFila2)>24):
            VPosicion154.set(DFila2[24])
        else:
            VPosicion154.set(N)
        if(len(DFila2)>25):
            VPosicion155.set(DFila2[25])
        else:
            VPosicion155.set(N)
        if(len(DFila2)>26):
            VPosicion156.set(DFila2[26])
        else:
            VPosicion156.set(N)
        if(len(DFila2)>27):
            VPosicion157.set(DFila2[27])
        else:
            VPosicion157.set(N)
        if(len(DFila2)>28):
            VPosicion158.set(DFila2[28])
        else:
            VPosicion158.set(N)
        if(len(DFila2)>29):
            VPosicion159.set(DFila2[29])
        else:
            VPosicion159.set(N)
        if(len(DFila3)>0):
            VPosicion162.set(DFila3[0])
        else:
            VPosicion162.set(N)
        if(len(DFila3)>1):
            VPosicion163.set(DFila3[1])
        else:
            VPosicion163.set(N)
        if(len(DFila3)>2):
            VPosicion164.set(DFila3[2])
        else:
            VPosicion164.set(N)
        if(len(DFila3)>3):
            VPosicion165.set(DFila3[3])
        else:
            VPosicion165.set(N)
        if(len(DFila3)>4):
            VPosicion166.set(DFila3[4])
        else:
            VPosicion166.set(N)
        if(len(DFila3)>5):
            VPosicion167.set(DFila3[5])
        else:
            VPosicion167.set(N)
        if(len(DFila3)>6):
            VPosicion168.set(DFila3[6])
        else:
            VPosicion168.set(N)
        if(len(DFila3)>7):
            VPosicion169.set(DFila3[7])
        else:
            VPosicion169.set(N)
        if(len(DFila3)>8):
            VPosicion170.set(DFila3[8])
        else:
            VPosicion170.set(N)
        if(len(DFila3)>9):
            VPosicion171.set(DFila3[9])
        else:
            VPosicion171.set(N)
        if(len(DFila3)>10):
            VPosicion172.set(DFila3[10])
        else:
            VPosicion172.set(N)
        if(len(DFila3)>11):
            VPosicion173.set(DFila3[11])
        else:
            VPosicion173.set(N)
        if(len(DFila3)>12):
            VPosicion174.set(DFila3[12])
        else:
            VPosicion174.set(N)
        if(len(DFila3)>13):
            VPosicion175.set(DFila3[13])
        else:
            VPosicion175.set(N)
        if(len(DFila3)>14):
            VPosicion176.set(DFila3[14])
        else:
            VPosicion176.set(N)
        if(len(DFila3)>15):
            VPosicion177.set(DFila3[15])
        else:
            VPosicion177.set(N)
        if(len(DFila3)>16):
            VPosicion178.set(DFila3[16])
        else:
            VPosicion178.set(N)
        if(len(DFila3)>17):
            VPosicion179.set(DFila3[17])
        else:
            VPosicion179.set(N)
        if(len(DFila3)>18):
            VPosicion180.set(DFila3[18])
        else:
            VPosicion180.set(N)
        if(len(DFila3)>19):
            VPosicion181.set(DFila3[19])
        else:
            VPosicion181.set(N)
        if(len(DFila3)>20):
            VPosicion182.set(DFila3[20])
        else:
            VPosicion182.set(N)
        if(len(DFila3)>21):
            VPosicion183.set(DFila3[21])
        else:
            VPosicion183.set(N)
        if(len(DFila3)>22):
            VPosicion184.set(DFila3[22])
        else:
            VPosicion184.set(N)
        if(len(DFila3)>23):
            VPosicion185.set(DFila3[23])
        else:
            VPosicion185.set(N)
        if(len(DFila3)>24):
            VPosicion186.set(DFila3[24])
        else:
            VPosicion186.set(N)
        if(len(DFila3)>25):
            VPosicion187.set(DFila3[25])
        else:
            VPosicion187.set(N)
        if(len(DFila3)>26):
            VPosicion188.set(DFila3[26])
        else:
            VPosicion188.set(N)
        if(len(DFila3)>27):
            VPosicion189.set(DFila3[27])
        else:
            VPosicion189.set(N)
        if(len(DFila3)>28):
            VPosicion190.set(DFila3[28])
        else:
            VPosicion190.set(N)
        if(len(DFila3)>29):
            VPosicion191.set(DFila3[29])
        else:
            VPosicion191.set(N)
        if(len(DFila4)>0):
            VPosicion194.set(DFila4[0])
        else:
            VPosicion194.set(N)
        if(len(DFila4)>1):
            VPosicion195.set(DFila4[1])
        else:
            VPosicion195.set(N)
        if(len(DFila4)>2):
            VPosicion196.set(DFila4[2])
        else:
            VPosicion196.set(N)
        if(len(DFila4)>3):
            VPosicion197.set(DFila4[3])
        else:
            VPosicion197.set(N)
        if(len(DFila4)>4):
            VPosicion198.set(DFila4[4])
        else:
            VPosicion198.set(N)
        if(len(DFila4)>5):
            VPosicion199.set(DFila4[5])
        else:
            VPosicion199.set(N)
        if(len(DFila4)>6):
            VPosicion200.set(DFila4[6])
        else:
            VPosicion200.set(N)
        if(len(DFila4)>7):
            VPosicion201.set(DFila4[7])
        else:
            VPosicion201.set(N)
        if(len(DFila4)>8):
            VPosicion202.set(DFila4[8])
        else:
            VPosicion202.set(N)
        if(len(DFila4)>9):
            VPosicion203.set(DFila4[9])
        else:
            VPosicion203.set(N)
        if(len(DFila4)>10):
            VPosicion204.set(DFila4[10])
        else:
            VPosicion204.set(N)
        if(len(DFila4)>11):
            VPosicion205.set(DFila4[11])
        else:
            VPosicion205.set(N)
        if(len(DFila4)>12):
            VPosicion206.set(DFila4[12])
        else:
            VPosicion206.set(N)
        if(len(DFila4)>13):
            VPosicion207.set(DFila4[13])
        else:
            VPosicion207.set(N)
        if(len(DFila4)>14):
            VPosicion208.set(DFila4[14])
        else:
            VPosicion208.set(N)
        if(len(DFila4)>15):
            VPosicion209.set(DFila4[15])
        else:
            VPosicion209.set(N)
        if(len(DFila4)>16):
            VPosicion210.set(DFila4[16])
        else:
            VPosicion210.set(N)
        if(len(DFila4)>17):
            VPosicion211.set(DFila4[17])
        else:
            VPosicion211.set(N)
        if(len(DFila4)>18):
            VPosicion212.set(DFila4[18])
        else:
            VPosicion212.set(N)
        if(len(DFila4)>19):
            VPosicion213.set(DFila4[19])
        else:
            VPosicion213.set(N)
        if(len(DFila4)>20):
            VPosicion214.set(DFila4[20])
        else:
            VPosicion214.set(N)
        if(len(DFila4)>21):
            VPosicion215.set(DFila4[21])
        else:
            VPosicion215.set(N)
        if(len(DFila4)>22):
            VPosicion216.set(DFila4[22])
        else:
            VPosicion216.set(N)
        if(len(DFila4)>23):
            VPosicion217.set(DFila4[23])
        else:
            VPosicion217.set(N)
        if(len(DFila4)>24):
            VPosicion218.set(DFila4[24])
        else:
            VPosicion218.set(N)
        if(len(DFila4)>25):
            VPosicion219.set(DFila4[25])
        else:
            VPosicion219.set(N)
        if(len(DFila4)>26):
            VPosicion220.set(DFila4[26])
        else:
            VPosicion220.set(N)
        if(len(DFila4)>27):
            VPosicion221.set(DFila4[27])
        else:
            VPosicion221.set(N)
        if(len(DFila4)>28):
            VPosicion222.set(DFila4[28])
        else:
            VPosicion222.set(N)
        if(len(DFila4)>29):
            VPosicion223.set(DFila4[29])
        else:
            VPosicion223.set(N)
        if(len(DFila5)>0):
            VPosicion226.set(DFila5[0])
        else:
            VPosicion226.set(N)
        if(len(DFila5)>1):
            VPosicion227.set(DFila5[1])
        else:
            VPosicion227.set(N)
        if(len(DFila5)>2):
            VPosicion228.set(DFila5[2])
        else:
            VPosicion228.set(N)
        if(len(DFila5)>3):
            VPosicion229.set(DFila5[3])
        else:
            VPosicion229.set(N)
        if(len(DFila5)>4):
            VPosicion230.set(DFila5[4])
        else:
            VPosicion230.set(N)
        if(len(DFila5)>5):
            VPosicion231.set(DFila5[5])
        else:
            VPosicion231.set(N)
        if(len(DFila5)>6):
            VPosicion232.set(DFila5[6])
        else:
            VPosicion232.set(N)
        if(len(DFila5)>7):
            VPosicion233.set(DFila5[7])
        else:
            VPosicion233.set(N)
        if(len(DFila5)>8):
            VPosicion234.set(DFila5[8])
        else:
            VPosicion234.set(N)
        if(len(DFila5)>9):
            VPosicion235.set(DFila5[9])
        else:
            VPosicion235.set(N)
        if(len(DFila5)>10):
            VPosicion236.set(DFila5[10])
        else:
            VPosicion236.set(N)
        if(len(DFila5)>11):
            VPosicion237.set(DFila5[11])
        else:
            VPosicion237.set(N)
        if(len(DFila5)>12):
            VPosicion238.set(DFila5[12])
        else:
            VPosicion238.set(N)
        if(len(DFila5)>13):
            VPosicion239.set(DFila5[13])
        else:
            VPosicion239.set(N)
        if(len(DFila5)>14):
            VPosicion240.set(DFila5[14])
        else:
            VPosicion240.set(N)
        if(len(DFila5)>15):
            VPosicion241.set(DFila5[15])
        else:
            VPosicion241.set(N)
        if(len(DFila5)>16):
            VPosicion242.set(DFila5[16])
        else:
            VPosicion242.set(N)
        if(len(DFila5)>17):
            VPosicion243.set(DFila5[17])
        else:
            VPosicion243.set(N)
        if(len(DFila5)>18):
            VPosicion244.set(DFila5[18])
        else:
            VPosicion244.set(N)
        if(len(DFila5)>19):
            VPosicion245.set(DFila5[19])
        else:
            VPosicion245.set(N)
        if(len(DFila5)>20):
            VPosicion246.set(DFila5[20])
        else:
            VPosicion246.set(N)
        if(len(DFila5)>21):
            VPosicion247.set(DFila5[21])
        else:
            VPosicion247.set(N)
        if(len(DFila5)>22):
            VPosicion248.set(DFila5[22])
        else:
            VPosicion248.set(N)
        if(len(DFila5)>23):
            VPosicion249.set(DFila5[23])
        else:
            VPosicion249.set(N)
        if(len(DFila5)>24):
            VPosicion250.set(DFila5[24])
        else:
            VPosicion250.set(N)
        if(len(DFila5)>25):
            VPosicion251.set(DFila5[25])
        else:
            VPosicion251.set(N)
        if(len(DFila5)>26):
            VPosicion252.set(DFila5[26])
        else:
            VPosicion252.set(N)
        if(len(DFila5)>27):
            VPosicion253.set(DFila5[27])
        else:
            VPosicion253.set(N)
        if(len(DFila5)>28):
            VPosicion254.set(DFila5[28])
        else:
            VPosicion254.set(N)
        if(len(DFila5)>29):
            VPosicion255.set(DFila5[29])
        else:
            VPosicion255.set(N)    

        DatosMenFila1="".join(DFila1)
        DatosMenFila2="".join(DFila2)
        DatosMenFila3="".join(DFila3)
        DatosMenFila4="".join(DFila4)
        DatosMenFila5="".join(DFila5)

        TramaFinal=str(DFila1[0])
        Parte2=DFila2[1:3]
        MParte2=MParte2.join(Parte2)
        TramaFinal=TramaFinal+MParte2
        Parte3=DFila3[3:7]
        MParte3=MParte3.join(Parte3)
        TramaFinal=TramaFinal+MParte3
        Parte4=DFila4[7:15]
        MParte4=MParte4.join(Parte4)
        TramaFinal=TramaFinal+MParte4
        Parte5=DFila5[15:-1]
        MParte5=MParte5.join(Parte5)
        TramaFinal=TramaFinal+MParte5+str(DFila5[-1])
        TextoTramaFinal=("La trama final es: ")
        MostrarTramaTotalMensaje.configure(text=TextoTramaFinal)
        TramaTotal.set(TramaFinal)
        ListaTramaFinal.extend(DFila1[0])
        ListaTramaFinal.extend(Parte2)
        ListaTramaFinal.extend(Parte3)
        ListaTramaFinal.extend(Parte4)
        ListaTramaFinal.extend(Parte5)
        if(DFila5[-1]!="-"):
            ListaTramaFinal.extend(DFila5[-1])

        if(len(ListaTramaFinal)>0):
            VPosicion66.set(ListaTramaFinal[0])
        else:
            VPosicion66.set(N)
        if(len(ListaTramaFinal)>1):
            VPosicion67.set(ListaTramaFinal[1])
        else:
            VPosicion67.set(N)
        if(len(ListaTramaFinal)>2):
            VPosicion68.set(ListaTramaFinal[2])
        else:
            VPosicion68.set(N)
        if(len(ListaTramaFinal)>3):
            VPosicion69.set(ListaTramaFinal[3])
        else:
            VPosicion69.set(N)
        if(len(ListaTramaFinal)>4):
            VPosicion70.set(ListaTramaFinal[4])
        else:
            VPosicion70.set(N)
        if(len(ListaTramaFinal)>5):
            VPosicion71.set(ListaTramaFinal[5])
        else:
            VPosicion71.set(N)
        if(len(ListaTramaFinal)>6):
            VPosicion72.set(ListaTramaFinal[6])
        else:
            VPosicion72.set(N)
        if(len(ListaTramaFinal)>7):
            VPosicion73.set(ListaTramaFinal[7])
        else:
            VPosicion73.set(N)
        if(len(ListaTramaFinal)>8):
            VPosicion74.set(ListaTramaFinal[8])
        else:
            VPosicion74.set(N)
        if(len(ListaTramaFinal)>9):
            VPosicion75.set(ListaTramaFinal[9])
        else:
            VPosicion75.set(N)
        if(len(ListaTramaFinal)>10):
            VPosicion76.set(ListaTramaFinal[10])
        else:
            VPosicion76.set(N)
        if(len(ListaTramaFinal)>11):
            VPosicion77.set(ListaTramaFinal[11])
        else:
            VPosicion77.set(N)
        if(len(ListaTramaFinal)>12):
            VPosicion78.set(ListaTramaFinal[12])
        else:
            VPosicion78.set(N)
        if(len(ListaTramaFinal)>13):
            VPosicion79.set(ListaTramaFinal[13])
        else:
            VPosicion79.set(N)
        if(len(ListaTramaFinal)>14):
            VPosicion80.set(ListaTramaFinal[14])
        else:
            VPosicion80.set(N)
        if(len(ListaTramaFinal)>15):
            VPosicion81.set(ListaTramaFinal[15])
        else:
            VPosicion81.set(N)
        if(len(ListaTramaFinal)>16):
            VPosicion82.set(ListaTramaFinal[16])
        else:
            VPosicion82.set(N)
        if(len(ListaTramaFinal)>17):
            VPosicion83.set(ListaTramaFinal[17])
        else:
            VPosicion83.set(N)
        if(len(ListaTramaFinal)>18):
            VPosicion84.set(ListaTramaFinal[18])
        else:
            VPosicion84.set(N)
        if(len(ListaTramaFinal)>19):
            VPosicion85.set(ListaTramaFinal[19])
        else:
            VPosicion85.set(N)
        if(len(ListaTramaFinal)>20):
            VPosicion86.set(ListaTramaFinal[20])
        else:
            VPosicion86.set(N)
        if(len(ListaTramaFinal)>21):
            VPosicion87.set(ListaTramaFinal[21])
        else:
            VPosicion87.set(N)
        if(len(ListaTramaFinal)>22):
            VPosicion88.set(ListaTramaFinal[22])
        else:
            VPosicion88.set(N)
        if(len(ListaTramaFinal)>23):
            VPosicion89.set(ListaTramaFinal[23])
        else:
            VPosicion89.set(N)
        if(len(ListaTramaFinal)>24):
            VPosicion90.set(ListaTramaFinal[24])
        else:
            VPosicion90.set(N)
        if(len(ListaTramaFinal)>25):
            VPosicion91.set(ListaTramaFinal[25])
        else:
            VPosicion91.set(N)
        if(len(ListaTramaFinal)>26):
            VPosicion92.set(ListaTramaFinal[26])
        else:
            VPosicion92.set(N)
        if(len(ListaTramaFinal)>27):
            VPosicion93.set(ListaTramaFinal[27])
        else:
            VPosicion93.set(N)
        if(len(ListaTramaFinal)>28):
            VPosicion94.set(ListaTramaFinal[28])
        else:
            VPosicion94.set(N)
        if(len(ListaTramaFinal)>29):
            VPosicion95.set(ListaTramaFinal[29])
        else:
            VPosicion95.set(N)
        
        check1=""
        check2=""
        check3=""
        check4=""
        check5=""
        if(len(DFila1)>0):
            if(TramaFinal[0]!=DFila1[0]):
                check1=1
            else:
                check1=0
        if(len(DFila2)>2):
            if(TramaFinal[1]!=DFila2[1]):
                check2=1
            else:
                check2=0
        if(len(DFila3)>4):
            if(TramaFinal[3]!=DFila3[3]):
                check3=1
            else:
                check3=0        
        if(len(DFila4)>8):
            if(TramaFinal[7]!=DFila4[7]):
                check4=1
            else:
                check4=0
        if(len(DFila5)>15):         
            if(TramaFinal[15]!=DFila5[15]):
                check5=1
            else:
                check5=0
        VPosicion128.set(check1)
        VPosicion160.set(check2)
        VPosicion192.set(check3)
        VPosicion224.set(check4)
        VPosicion256.set(check5)

    def check():
        check1=""
        check2=""
        check3=""
        check4=""
        check5=""
        if(VPosicion66.get()!=VPosicion98.get()):
            check1=1
            VArregloPos66.configure(bg="red")
            VArregloPos98.configure(bg="red")
        elif(VPosicion66.get()==VPosicion98.get()):
            check1=0
            VArregloPos66.configure(bg="White")
            VArregloPos98.configure(bg="White")
        if(VPosicion67.get()!=VPosicion131.get()):
            check2=1
            VArregloPos67.configure(bg="red")
            VArregloPos131.configure(bg="red")
        elif(VPosicion67.get()==VPosicion131.get()):
            check2=0
            VArregloPos67.configure(bg="White")
            VArregloPos131.configure(bg="White")
        if(VPosicion69.get()!=VPosicion165.get()):
            check3=1
            VArregloPos69.configure(bg="red")
            VArregloPos165.configure(bg="red")
        elif(VPosicion69.get()==VPosicion165.get()):
            check3=0
            VArregloPos69.configure(bg="White")
            VArregloPos165.configure(bg="White")
        if(VPosicion73.get()!=VPosicion201.get()):
            check4=1
            VArregloPos73.configure(bg="red")
            VArregloPos201.configure(bg="red")
        elif(VPosicion73.get()==VPosicion201.get()):
            check4=0
            VArregloPos73.configure(bg="White")
            VArregloPos201.configure(bg="White")
        if(VPosicion81.get()!=VPosicion241.get()):
            check5=1
            VArregloPos81.configure(bg="red")
            VArregloPos241.configure(bg="red")
        elif(VPosicion81.get()==VPosicion241.get()):
            check5=0
            VArregloPos81.configure(bg="White")
            VArregloPos241.configure(bg="White")
        VPosicion128.set(check1)
        VPosicion160.set(check2)
        VPosicion192.set(check3)
        VPosicion224.set(check4)
        VPosicion256.set(check5)

    #Funcion UNRZ
    def UNRZ():
        mensaje=TramaTotal.get()
        Respuesta=list()
        i=0
        while i<len(mensaje):
            Respuesta.append(mensaje[i])
            i=i+1
        TextoTramaUNRZ=("La codificacion URNZ de su trama es: ",Respuesta)
        LabelCodificacionCanal.configure(text=TextoTramaUNRZ)

    #Funcion AMI
    def AMI():
        mensaje=TramaTotal.get()
        Respuesta=list()
        ValAnt="-1"
        i=0
        while i<len(mensaje):
            if(mensaje[i]=="0"):
                Respuesta.append("0")
            elif(mensaje[i]=="1"):
                if(ValAnt=="-1"):
                    Respuesta.append("1")
                    ValAnt="1"
                elif(ValAnt=="1"):
                    Respuesta.append("-1")
                    ValAnt="-1"            
            i=i+1
        TextoTramaAMI=("La codificacion URNZ de su trama es: ",Respuesta)
        LabelCodificacionCanal.configure(text=TextoTramaAMI)

    #Funcion HDB3
    def HDB3():
        mensaje=TramaTotal.get()
        Respuesta=list()
        i=0
        ValAnt="1"
        while i<len(mensaje):
            if(mensaje[i]=="1"):
                if(ValAnt=="1"):
                    Respuesta.append("-1")
                    ValAnt="-1"
                elif(ValAnt=="-1"):
                    Respuesta.append("1")
                    ValAnt="1"
            elif(mensaje[i]=="0"): 
                Respuesta.append("0")      
            i=i+1

        cont=0
        for pos, i in enumerate(Respuesta):
            if i=="0":
                cont=cont+1
                if(cont==4):
                    if(pos+1==len(Respuesta)):
                        Respuesta[-1]="P"
                        cont=1
                    else:    
                        Respuesta[pos+1]="P"
                        cont=1

        ValAnt="1"
        inicio=TRUE
        unos=0
        for pos, i in enumerate(Respuesta):
            if i=="1":
                ValAnt="1"
                unos=unos+1
            elif i=="-1":
                ValAnt="-1"
                unos=unos+1
            if i=="P":
                if(inicio==True):
                    if(ValAnt=="1"):
                        Respuesta[pos]="V"
                    elif(ValAnt=="-1"):
                        Respuesta[pos]="-V"
                    inicio=False
                elif(unos%2==0):
                    if(ValAnt=="1"):
                        Respuesta[pos]="-V"
                        Respuesta[pos-3]="-B"
                        Respuesta[pos+1]="1"
                    elif(ValAnt=="-1"):
                        Respuesta[pos]="V"
                        Respuesta[pos-3]="B"
                        Respuesta[pos+1]="-1"
                elif(unos%2!=0):
                    if(ValAnt=="1"):
                        Respuesta[pos]="V"
                    elif(ValAnt=="-1"):
                        Respuesta[pos]="-V"            
                if(cont==4):
                    Respuesta[pos+1]="P"
                    cont=0
        TextoTramaHDB3=("La codificacion URNZ de su trama es: ",Respuesta)
        LabelCodificacionCanal.configure(text=TextoTramaHDB3)

    #Funcion Volver    
    def Volver():
        VentanaCodificacionHamming.destroy()
        ventana.deiconify()

    #Creación ventana
    VentanaCodificacionHamming=Toplevel()
    VentanaCodificacionHamming.title("Codificación Hamming")
    VentanaCodificacionHamming.geometry('1750x700')
    Frame1 = Frame(VentanaCodificacionHamming, bg='black')
    Frame2 = Frame(VentanaCodificacionHamming)
    Frame3 = Frame(VentanaCodificacionHamming)
    Frame4 = Frame(VentanaCodificacionHamming)
    Frame5 = Frame(VentanaCodificacionHamming)
    Frame6 = Frame(VentanaCodificacionHamming)
    Frame7 = Frame(VentanaCodificacionHamming)
    Frame1.grid(row=0, column=0, padx=(230, 0), pady=(0, 0))
    Frame2.grid(row=1, column=0, padx=(230, 0), pady=(0, 0))
    Frame3.grid(row=2, column=0, padx=(80, 0), pady=(10, 10))
    Frame4.grid(row=3, column=0, padx=(80, 0), pady=(10, 10))
    Frame5.grid(row=4, column=0, padx=(230, 0), pady=(0, 0))
    Frame6.grid(row=5, column=0, padx=(230, 0), pady=(0, 0))
    Frame7.grid(row=6, column=0, padx=(230, 0), pady=(0, 0))
    TituloInterfaz=Label(Frame1, text="Codificación Hamming", bd=10, fg='black', font=("Helvetica", 24))
    TituloInterfaz.grid(pady=(8, 8))
    LabelInstrucciones = Label(Frame2, text="Ingrese la trama de hasta 25 bits que desea ver: ", font=("Helvetica", 16))
    LabelInstrucciones.grid(row=0, column=1, pady=(10,10))
    TramaUsuario=StringVar()
    EntryInstrucciones = Entry(Frame2, textvariable=TramaUsuario)
    EntryInstrucciones.grid(row=0, column=2)

    #Mostrar Matriz Inicial
    #ValoresMatrizfila1
    Posicion1=StringVar()
    ArregloPos1=Entry(Frame3,textvariable=Posicion1,width=5)
    ArregloPos1.grid(row=0,column=0,sticky=NSEW)
    Posicion2=StringVar()
    ArregloPos2=Entry(Frame3,textvariable=Posicion2,width=5)
    ArregloPos2.grid(row=0,column=1,sticky=NSEW)
    Posicion3=StringVar()
    ArregloPos3=Entry(Frame3,textvariable=Posicion3,width=5)
    ArregloPos3.grid(row=0,column=2,sticky=NSEW)
    Posicion4=StringVar()
    ArregloPos4=Entry(Frame3,textvariable=Posicion4,width=5)
    ArregloPos4.grid(row=0,column=3,sticky=NSEW)
    Posicion5=StringVar()
    ArregloPos5=Entry(Frame3,textvariable=Posicion5,width=5)
    ArregloPos5.grid(row=0,column=4,sticky=NSEW)
    Posicion6=StringVar()
    ArregloPos6=Entry(Frame3,textvariable=Posicion6,width=5)
    ArregloPos6.grid(row=0,column=5,sticky=NSEW)
    Posicion7=StringVar()
    ArregloPos7=Entry(Frame3,textvariable=Posicion7,width=5)
    ArregloPos7.grid(row=0,column=6,sticky=NSEW)
    Posicion8=StringVar()
    ArregloPos8=Entry(Frame3,textvariable=Posicion8,width=5)
    ArregloPos8.grid(row=0,column=7,sticky=NSEW)
    Posicion9=StringVar()
    ArregloPos9=Entry(Frame3,textvariable=Posicion9,width=5)
    ArregloPos9.grid(row=0,column=8,sticky=NSEW)
    Posicion10=StringVar()
    ArregloPos10=Entry(Frame3,textvariable=Posicion10,width=5)
    ArregloPos10.grid(row=0,column=9,sticky=NSEW)
    Posicion11=StringVar()
    ArregloPos11=Entry(Frame3,textvariable=Posicion11,width=5)
    ArregloPos11.grid(row=0,column=10,sticky=NSEW)
    Posicion12=StringVar()
    ArregloPos12=Entry(Frame3,textvariable=Posicion12,width=5)
    ArregloPos12.grid(row=0,column=11,sticky=NSEW)
    Posicion13=StringVar()
    ArregloPos13=Entry(Frame3,textvariable=Posicion13,width=5)
    ArregloPos13.grid(row=0,column=12,sticky=NSEW)
    Posicion14=StringVar()
    ArregloPos14=Entry(Frame3,textvariable=Posicion14,width=5)
    ArregloPos14.grid(row=0,column=13,sticky=NSEW)
    Posicion15=StringVar()
    ArregloPos15=Entry(Frame3,textvariable=Posicion15,width=5)
    ArregloPos15.grid(row=0,column=14,sticky=NSEW)
    Posicion16=StringVar()
    ArregloPos16=Entry(Frame3,textvariable=Posicion16,width=5)
    ArregloPos16.grid(row=0,column=15,sticky=NSEW)
    Posicion17=StringVar()
    ArregloPos17=Entry(Frame3,textvariable=Posicion17,width=5)
    ArregloPos17.grid(row=0,column=16,sticky=NSEW)
    Posicion18=StringVar()
    ArregloPos18=Entry(Frame3,textvariable=Posicion18,width=5)
    ArregloPos18.grid(row=0,column=17,sticky=NSEW)
    Posicion19=StringVar()
    ArregloPos19=Entry(Frame3,textvariable=Posicion19,width=5)
    ArregloPos19.grid(row=0,column=18,sticky=NSEW)
    Posicion20=StringVar()
    ArregloPos20=Entry(Frame3,textvariable=Posicion20,width=5)
    ArregloPos20.grid(row=0,column=19,sticky=NSEW)
    Posicion21=StringVar()
    ArregloPos21=Entry(Frame3,textvariable=Posicion21,width=5)
    ArregloPos21.grid(row=0,column=20,sticky=NSEW)
    Posicion22=StringVar()
    ArregloPos22=Entry(Frame3,textvariable=Posicion22,width=5)
    ArregloPos22.grid(row=0,column=21,sticky=NSEW)
    Posicion23=StringVar()
    ArregloPos23=Entry(Frame3,textvariable=Posicion23,width=5)
    ArregloPos23.grid(row=0,column=22,sticky=NSEW)
    Posicion24=StringVar()
    ArregloPos24=Entry(Frame3,textvariable=Posicion24,width=5)
    ArregloPos24.grid(row=0,column=23,sticky=NSEW)
    Posicion25=StringVar()
    ArregloPos25=Entry(Frame3,textvariable=Posicion25,width=5)
    ArregloPos25.grid(row=0,column=24,sticky=NSEW)
    Posicion26=StringVar()
    ArregloPos26=Entry(Frame3,textvariable=Posicion26,width=5)
    ArregloPos26.grid(row=0,column=25,sticky=NSEW)
    Posicion27=StringVar()
    ArregloPos27=Entry(Frame3,textvariable=Posicion27,width=5)
    ArregloPos27.grid(row=0,column=26,sticky=NSEW)
    Posicion28=StringVar()
    ArregloPos28=Entry(Frame3,textvariable=Posicion28,width=5)
    ArregloPos28.grid(row=0,column=27,sticky=NSEW)
    Posicion29=StringVar()
    ArregloPos29=Entry(Frame3,textvariable=Posicion29,width=5)
    ArregloPos29.grid(row=0,column=28,sticky=NSEW)
    Posicion30=StringVar()
    ArregloPos30=Entry(Frame3,textvariable=Posicion30,width=5)
    ArregloPos30.grid(row=0,column=29,sticky=NSEW)
    Posicion31=StringVar()
    ArregloPos31=Entry(Frame3,textvariable=Posicion31,width=5)
    ArregloPos31.grid(row=0,column=30,sticky=NSEW)

    Posicion2.set(1)
    Posicion3.set(2)
    Posicion4.set(3)
    Posicion5.set(4)
    Posicion6.set(5)
    Posicion7.set(6)
    Posicion8.set(7)
    Posicion9.set(8)
    Posicion10.set(9)
    Posicion11.set(10)
    Posicion12.set(11)
    Posicion13.set(12)
    Posicion14.set(13)
    Posicion15.set(14)
    Posicion16.set(15)
    Posicion17.set(16)
    Posicion18.set(17)
    Posicion19.set(18)
    Posicion20.set(19)
    Posicion21.set(20)
    Posicion22.set(21)
    Posicion23.set(22)
    Posicion24.set(23)
    Posicion25.set(24)
    Posicion26.set(25)
    Posicion27.set(26)
    Posicion28.set(27)
    Posicion29.set(28)
    Posicion30.set(29)
    Posicion31.set(30)

    #ArregloMatrizFila2
    Posicion33=StringVar()
    ArregloPos33=Entry(Frame3,textvariable=Posicion33,width=5)
    ArregloPos33.grid(row=1,column=0,sticky=NSEW)
    Posicion34=StringVar()
    ArregloPos34=Entry(Frame3,textvariable=Posicion34,width=5)
    ArregloPos34.grid(row=1,column=1,sticky=NSEW)
    Posicion35=StringVar()
    ArregloPos35=Entry(Frame3,textvariable=Posicion35,width=5)
    ArregloPos35.grid(row=1,column=2,sticky=NSEW)
    Posicion36=StringVar()
    ArregloPos36=Entry(Frame3,textvariable=Posicion36,width=5)
    ArregloPos36.grid(row=1,column=3,sticky=NSEW)
    Posicion37=StringVar()
    ArregloPos37=Entry(Frame3,textvariable=Posicion37,width=5)
    ArregloPos37.grid(row=1,column=4,sticky=NSEW)
    Posicion38=StringVar()
    ArregloPos38=Entry(Frame3,textvariable=Posicion38,width=5)
    ArregloPos38.grid(row=1,column=5,sticky=NSEW)
    Posicion39=StringVar()
    ArregloPos39=Entry(Frame3,textvariable=Posicion39,width=5)
    ArregloPos39.grid(row=1,column=6,sticky=NSEW)
    Posicion40=StringVar()
    ArregloPos40=Entry(Frame3,textvariable=Posicion40,width=5)
    ArregloPos40.grid(row=1,column=7,sticky=NSEW)
    Posicion41=StringVar()
    ArregloPos41=Entry(Frame3,textvariable=Posicion41,width=5)
    ArregloPos41.grid(row=1,column=8,sticky=NSEW)
    Posicion42=StringVar()
    ArregloPos42=Entry(Frame3,textvariable=Posicion42,width=5)
    ArregloPos42.grid(row=1,column=9,sticky=NSEW)
    Posicion43=StringVar()
    ArregloPos43=Entry(Frame3,textvariable=Posicion43,width=5)
    ArregloPos43.grid(row=1,column=10,sticky=NSEW)
    Posicion44=StringVar()
    ArregloPos44=Entry(Frame3,textvariable=Posicion44,width=5)
    ArregloPos44.grid(row=1,column=11,sticky=NSEW)
    Posicion45=StringVar()
    ArregloPos45=Entry(Frame3,textvariable=Posicion45,width=5)
    ArregloPos45.grid(row=1,column=12,sticky=NSEW)
    Posicion46=StringVar()
    ArregloPos46=Entry(Frame3,textvariable=Posicion46,width=5)
    ArregloPos46.grid(row=1,column=13,sticky=NSEW)
    Posicion47=StringVar()
    ArregloPos47=Entry(Frame3,textvariable=Posicion47,width=5)
    ArregloPos47.grid(row=1,column=14,sticky=NSEW)
    Posicion48=StringVar()
    ArregloPos48=Entry(Frame3,textvariable=Posicion48,width=5)
    ArregloPos48.grid(row=1,column=15,sticky=NSEW)
    Posicion49=StringVar()
    ArregloPos49=Entry(Frame3,textvariable=Posicion49,width=5)
    ArregloPos49.grid(row=1,column=16,sticky=NSEW)
    Posicion50=StringVar()
    ArregloPos50=Entry(Frame3,textvariable=Posicion50,width=5)
    ArregloPos50.grid(row=1,column=17,sticky=NSEW)
    Posicion51=StringVar()
    ArregloPos51=Entry(Frame3,textvariable=Posicion51,width=5)
    ArregloPos51.grid(row=1,column=18,sticky=NSEW)
    Posicion52=StringVar()
    ArregloPos52=Entry(Frame3,textvariable=Posicion52,width=5)
    ArregloPos52.grid(row=1,column=19,sticky=NSEW)
    Posicion53=StringVar()
    ArregloPos53=Entry(Frame3,textvariable=Posicion53,width=5)
    ArregloPos53.grid(row=1,column=20,sticky=NSEW)
    Posicion54=StringVar()
    ArregloPos54=Entry(Frame3,textvariable=Posicion54,width=5)
    ArregloPos54.grid(row=1,column=21,sticky=NSEW)
    Posicion55=StringVar()
    ArregloPos55=Entry(Frame3,textvariable=Posicion55,width=5)
    ArregloPos55.grid(row=1,column=22,sticky=NSEW)
    Posicion56=StringVar()
    ArregloPos56=Entry(Frame3,textvariable=Posicion56,width=5)
    ArregloPos56.grid(row=1,column=23,sticky=NSEW)
    Posicion57=StringVar()
    ArregloPos57=Entry(Frame3,textvariable=Posicion57,width=5)
    ArregloPos57.grid(row=1,column=24,sticky=NSEW)
    Posicion58=StringVar()
    ArregloPos58=Entry(Frame3,textvariable=Posicion58,width=5)
    ArregloPos58.grid(row=1,column=25,sticky=NSEW)
    Posicion59=StringVar()
    ArregloPos59=Entry(Frame3,textvariable=Posicion59,width=5)
    ArregloPos59.grid(row=1,column=26,sticky=NSEW)
    Posicion60=StringVar()
    ArregloPos60=Entry(Frame3,textvariable=Posicion60,width=5)
    ArregloPos60.grid(row=1,column=27,sticky=NSEW)
    Posicion61=StringVar()
    ArregloPos61=Entry(Frame3,textvariable=Posicion61,width=5)
    ArregloPos61.grid(row=1,column=28,sticky=NSEW)
    Posicion62=StringVar()
    ArregloPos62=Entry(Frame3,textvariable=Posicion62,width=5)
    ArregloPos62.grid(row=1,column=29,sticky=NSEW)
    Posicion63=StringVar()
    ArregloPos63=Entry(Frame3,textvariable=Posicion63,width=5)
    ArregloPos63.grid(row=1,column=30,sticky=NSEW)
    Posicion64=StringVar()

    #ArregloMatrizFila3
    Posicion65=StringVar()
    ArregloPos65=Entry(Frame3,textvariable=Posicion65,width=5)
    ArregloPos65.grid(row=2,column=0,sticky=NSEW)
    Posicion65.set("Fp1")
    Posicion66=StringVar()
    ArregloPos66=Entry(Frame3,textvariable=Posicion66,width=5)
    ArregloPos66.grid(row=2,column=1,sticky=NSEW)
    Posicion67=StringVar()
    ArregloPos67=Entry(Frame3,textvariable=Posicion67,width=5)
    ArregloPos67.grid(row=2,column=2,sticky=NSEW)
    Posicion68=StringVar()
    ArregloPos68=Entry(Frame3,textvariable=Posicion68,width=5)
    ArregloPos68.grid(row=2,column=3,sticky=NSEW)
    Posicion69=StringVar()
    ArregloPos69=Entry(Frame3,textvariable=Posicion69,width=5)
    ArregloPos69.grid(row=2,column=4,sticky=NSEW)
    Posicion70=StringVar()
    ArregloPos70=Entry(Frame3,textvariable=Posicion70,width=5)
    ArregloPos70.grid(row=2,column=5,sticky=NSEW)
    Posicion71=StringVar()
    ArregloPos71=Entry(Frame3,textvariable=Posicion71,width=5)
    ArregloPos71.grid(row=2,column=6,sticky=NSEW)
    Posicion72=StringVar()
    ArregloPos72=Entry(Frame3,textvariable=Posicion72,width=5)
    ArregloPos72.grid(row=2,column=7,sticky=NSEW)
    Posicion73=StringVar()
    ArregloPos73=Entry(Frame3,textvariable=Posicion73,width=5)
    ArregloPos73.grid(row=2,column=8,sticky=NSEW)
    Posicion74=StringVar()
    ArregloPos74=Entry(Frame3,textvariable=Posicion74,width=5)
    ArregloPos74.grid(row=2,column=9,sticky=NSEW)
    Posicion75=StringVar()
    ArregloPos75=Entry(Frame3,textvariable=Posicion75,width=5)
    ArregloPos75.grid(row=2,column=10,sticky=NSEW)
    Posicion76=StringVar()
    ArregloPos76=Entry(Frame3,textvariable=Posicion76,width=5)
    ArregloPos76.grid(row=2,column=11,sticky=NSEW)
    Posicion77=StringVar()
    ArregloPos77=Entry(Frame3,textvariable=Posicion77,width=5)
    ArregloPos77.grid(row=2,column=12,sticky=NSEW)
    Posicion78=StringVar()
    ArregloPos78=Entry(Frame3,textvariable=Posicion78,width=5)
    ArregloPos78.grid(row=2,column=13,sticky=NSEW)
    Posicion79=StringVar()
    ArregloPos79=Entry(Frame3,textvariable=Posicion79,width=5)
    ArregloPos79.grid(row=2,column=14,sticky=NSEW)
    Posicion80=StringVar()
    ArregloPos80=Entry(Frame3,textvariable=Posicion80,width=5)
    ArregloPos80.grid(row=2,column=15,sticky=NSEW)
    Posicion81=StringVar()
    ArregloPos81=Entry(Frame3,textvariable=Posicion81,width=5)
    ArregloPos81.grid(row=2,column=16,sticky=NSEW)
    Posicion82=StringVar()
    ArregloPos82=Entry(Frame3,textvariable=Posicion82,width=5)
    ArregloPos82.grid(row=2,column=17,sticky=NSEW)
    Posicion83=StringVar()
    ArregloPos83=Entry(Frame3,textvariable=Posicion83,width=5)
    ArregloPos83.grid(row=2,column=18,sticky=NSEW)
    Posicion84=StringVar()
    ArregloPos84=Entry(Frame3,textvariable=Posicion84,width=5)
    ArregloPos84.grid(row=2,column=19,sticky=NSEW)
    Posicion85=StringVar()
    ArregloPos85=Entry(Frame3,textvariable=Posicion85,width=5)
    ArregloPos85.grid(row=2,column=20,sticky=NSEW)
    Posicion86=StringVar()
    ArregloPos86=Entry(Frame3,textvariable=Posicion86,width=5)
    ArregloPos86.grid(row=2,column=21,sticky=NSEW)
    Posicion87=StringVar()
    ArregloPos87=Entry(Frame3,textvariable=Posicion87,width=5)
    ArregloPos87.grid(row=2,column=22,sticky=NSEW)
    Posicion88=StringVar()
    ArregloPos88=Entry(Frame3,textvariable=Posicion88,width=5)
    ArregloPos88.grid(row=2,column=23,sticky=NSEW)
    Posicion89=StringVar()
    ArregloPos89=Entry(Frame3,textvariable=Posicion89,width=5)
    ArregloPos89.grid(row=2,column=24,sticky=NSEW)
    Posicion90=StringVar()
    ArregloPos90=Entry(Frame3,textvariable=Posicion90,width=5)
    ArregloPos90.grid(row=2,column=25,sticky=NSEW)
    Posicion91=StringVar()
    ArregloPos91=Entry(Frame3,textvariable=Posicion91,width=5)
    ArregloPos91.grid(row=2,column=26,sticky=NSEW)
    Posicion92=StringVar()
    ArregloPos92=Entry(Frame3,textvariable=Posicion92,width=5)
    ArregloPos92.grid(row=2,column=27,sticky=NSEW)
    Posicion93=StringVar()
    ArregloPos93=Entry(Frame3,textvariable=Posicion93,width=5)
    ArregloPos93.grid(row=2,column=28,sticky=NSEW)
    Posicion94=StringVar()
    ArregloPos94=Entry(Frame3,textvariable=Posicion94,width=5)
    ArregloPos94.grid(row=2,column=29,sticky=NSEW)
    Posicion95=StringVar()
    ArregloPos95=Entry(Frame3,textvariable=Posicion95,width=5)
    ArregloPos95.grid(row=2,column=30,sticky=NSEW)

    #ArregloMatrizFila4
    Posicion97=StringVar()
    ArregloPos97=Entry(Frame3,textvariable=Posicion97,width=5)
    ArregloPos97.grid(row=3,column=0,sticky=NSEW)
    Posicion97.set("Fp2")
    Posicion98=StringVar()
    ArregloPos98=Entry(Frame3,textvariable=Posicion98,width=5)
    ArregloPos98.grid(row=3,column=1,sticky=NSEW)
    Posicion99=StringVar()
    ArregloPos99=Entry(Frame3,textvariable=Posicion99,width=5)
    ArregloPos99.grid(row=3,column=2,sticky=NSEW)
    Posicion100=StringVar()
    ArregloPos100=Entry(Frame3,textvariable=Posicion100,width=5)
    ArregloPos100.grid(row=3,column=3,sticky=NSEW)
    Posicion101=StringVar()
    ArregloPos101=Entry(Frame3,textvariable=Posicion101,width=5)
    ArregloPos101.grid(row=3,column=4,sticky=NSEW)
    Posicion102=StringVar()
    ArregloPos102=Entry(Frame3,textvariable=Posicion102,width=5)
    ArregloPos102.grid(row=3,column=5,sticky=NSEW)
    Posicion103=StringVar()
    ArregloPos103=Entry(Frame3,textvariable=Posicion103,width=5)
    ArregloPos103.grid(row=3,column=6,sticky=NSEW)
    Posicion104=StringVar()
    ArregloPos104=Entry(Frame3,textvariable=Posicion104,width=5)
    ArregloPos104.grid(row=3,column=7,sticky=NSEW)
    Posicion105=StringVar()
    ArregloPos105=Entry(Frame3,textvariable=Posicion105,width=5)
    ArregloPos105.grid(row=3,column=8,sticky=NSEW)
    Posicion106=StringVar()
    ArregloPos106=Entry(Frame3,textvariable=Posicion106,width=5)
    ArregloPos106.grid(row=3,column=9,sticky=NSEW)
    Posicion107=StringVar()
    ArregloPos107=Entry(Frame3,textvariable=Posicion107,width=5)
    ArregloPos107.grid(row=3,column=10,sticky=NSEW)
    Posicion108=StringVar()
    ArregloPos108=Entry(Frame3,textvariable=Posicion108,width=5)
    ArregloPos108.grid(row=3,column=11,sticky=NSEW)
    Posicion109=StringVar()
    ArregloPos109=Entry(Frame3,textvariable=Posicion109,width=5)
    ArregloPos109.grid(row=3,column=12,sticky=NSEW)
    Posicion110=StringVar()
    ArregloPos110=Entry(Frame3,textvariable=Posicion110,width=5)
    ArregloPos110.grid(row=3,column=13,sticky=NSEW)
    Posicion111=StringVar()
    ArregloPos111=Entry(Frame3,textvariable=Posicion111,width=5)
    ArregloPos111.grid(row=3,column=14,sticky=NSEW)
    Posicion112=StringVar()
    ArregloPos112=Entry(Frame3,textvariable=Posicion112,width=5)
    ArregloPos112.grid(row=3,column=15,sticky=NSEW)
    Posicion113=StringVar()
    ArregloPos113=Entry(Frame3,textvariable=Posicion113,width=5)
    ArregloPos113.grid(row=3,column=16,sticky=NSEW)
    Posicion114=StringVar()
    ArregloPos114=Entry(Frame3,textvariable=Posicion114,width=5)
    ArregloPos114.grid(row=3,column=17,sticky=NSEW)
    Posicion115=StringVar()
    ArregloPos115=Entry(Frame3,textvariable=Posicion115,width=5)
    ArregloPos115.grid(row=3,column=18,sticky=NSEW)
    Posicion116=StringVar()
    ArregloPos116=Entry(Frame3,textvariable=Posicion116,width=5)
    ArregloPos116.grid(row=3,column=19,sticky=NSEW)
    Posicion117=StringVar()
    ArregloPos117=Entry(Frame3,textvariable=Posicion117,width=5)
    ArregloPos117.grid(row=3,column=20,sticky=NSEW)
    Posicion118=StringVar()
    ArregloPos118=Entry(Frame3,textvariable=Posicion118,width=5)
    ArregloPos118.grid(row=3,column=21,sticky=NSEW)
    Posicion119=StringVar()
    ArregloPos119=Entry(Frame3,textvariable=Posicion119,width=5)
    ArregloPos119.grid(row=3,column=22,sticky=NSEW)
    Posicion120=StringVar()
    ArregloPos120=Entry(Frame3,textvariable=Posicion120,width=5)
    ArregloPos120.grid(row=3,column=23,sticky=NSEW)
    Posicion121=StringVar()
    ArregloPos121=Entry(Frame3,textvariable=Posicion121,width=5)
    ArregloPos121.grid(row=3,column=24,sticky=NSEW)
    Posicion122=StringVar()
    ArregloPos122=Entry(Frame3,textvariable=Posicion122,width=5)
    ArregloPos122.grid(row=3,column=25,sticky=NSEW)
    Posicion123=StringVar()
    ArregloPos123=Entry(Frame3,textvariable=Posicion123,width=5)
    ArregloPos123.grid(row=3,column=26,sticky=NSEW)
    Posicion124=StringVar()
    ArregloPos124=Entry(Frame3,textvariable=Posicion124,width=5)
    ArregloPos124.grid(row=3,column=27,sticky=NSEW)
    Posicion125=StringVar()
    ArregloPos125=Entry(Frame3,textvariable=Posicion125,width=5)
    ArregloPos125.grid(row=3,column=28,sticky=NSEW)
    Posicion126=StringVar()
    ArregloPos126=Entry(Frame3,textvariable=Posicion126,width=5)
    ArregloPos126.grid(row=3,column=29,sticky=NSEW)
    Posicion127=StringVar()
    ArregloPos127=Entry(Frame3,textvariable=Posicion127,width=5)
    ArregloPos127.grid(row=3,column=30,sticky=NSEW)

    #ArregloMatrizFila5
    Posicion129=StringVar()
    ArregloPos129=Entry(Frame3,textvariable=Posicion129,width=5)
    ArregloPos129.grid(row=4,column=0,sticky=NSEW)
    Posicion129.set("Fp4")
    Posicion130=StringVar()
    ArregloPos130=Entry(Frame3,textvariable=Posicion130,width=5)
    ArregloPos130.grid(row=4,column=1,sticky=NSEW)
    Posicion131=StringVar()
    ArregloPos131=Entry(Frame3,textvariable=Posicion131,width=5)
    ArregloPos131.grid(row=4,column=2,sticky=NSEW)
    Posicion132=StringVar()
    ArregloPos132=Entry(Frame3,textvariable=Posicion132,width=5)
    ArregloPos132.grid(row=4,column=3,sticky=NSEW)
    Posicion133=StringVar()
    ArregloPos133=Entry(Frame3,textvariable=Posicion133,width=5)
    ArregloPos133.grid(row=4,column=4,sticky=NSEW)
    Posicion134=StringVar()
    ArregloPos134=Entry(Frame3,textvariable=Posicion134,width=5)
    ArregloPos134.grid(row=4,column=5,sticky=NSEW)
    Posicion135=StringVar()
    ArregloPos135=Entry(Frame3,textvariable=Posicion135,width=5)
    ArregloPos135.grid(row=4,column=6,sticky=NSEW)
    Posicion136=StringVar()
    ArregloPos136=Entry(Frame3,textvariable=Posicion136,width=5)
    ArregloPos136.grid(row=4,column=7,sticky=NSEW)
    Posicion137=StringVar()
    ArregloPos137=Entry(Frame3,textvariable=Posicion137,width=5)
    ArregloPos137.grid(row=4,column=8,sticky=NSEW)
    Posicion138=StringVar()
    ArregloPos138=Entry(Frame3,textvariable=Posicion138,width=5)
    ArregloPos138.grid(row=4,column=9,sticky=NSEW)
    Posicion139=StringVar()
    ArregloPos139=Entry(Frame3,textvariable=Posicion139,width=5)
    ArregloPos139.grid(row=4,column=10,sticky=NSEW)
    Posicion140=StringVar()
    ArregloPos140=Entry(Frame3,textvariable=Posicion140,width=5)
    ArregloPos140.grid(row=4,column=11,sticky=NSEW)
    Posicion141=StringVar()
    ArregloPos141=Entry(Frame3,textvariable=Posicion141,width=5)
    ArregloPos141.grid(row=4,column=12,sticky=NSEW)
    Posicion142=StringVar()
    ArregloPos142=Entry(Frame3,textvariable=Posicion142,width=5)
    ArregloPos142.grid(row=4,column=13,sticky=NSEW)
    Posicion143=StringVar()
    ArregloPos143=Entry(Frame3,textvariable=Posicion143,width=5)
    ArregloPos143.grid(row=4,column=14,sticky=NSEW)
    Posicion144=StringVar()
    ArregloPos144=Entry(Frame3,textvariable=Posicion144,width=5)
    ArregloPos144.grid(row=4,column=15,sticky=NSEW)
    Posicion145=StringVar()
    ArregloPos145=Entry(Frame3,textvariable=Posicion145,width=5)
    ArregloPos145.grid(row=4,column=16,sticky=NSEW)
    Posicion146=StringVar()
    ArregloPos146=Entry(Frame3,textvariable=Posicion146,width=5)
    ArregloPos146.grid(row=4,column=17,sticky=NSEW)
    Posicion147=StringVar()
    ArregloPos147=Entry(Frame3,textvariable=Posicion147,width=5)
    ArregloPos147.grid(row=4,column=18,sticky=NSEW)
    Posicion148=StringVar()
    ArregloPos148=Entry(Frame3,textvariable=Posicion148,width=5)
    ArregloPos148.grid(row=4,column=19,sticky=NSEW)
    Posicion149=StringVar()
    ArregloPos149=Entry(Frame3,textvariable=Posicion149,width=5)
    ArregloPos149.grid(row=4,column=20,sticky=NSEW)
    Posicion150=StringVar()
    ArregloPos150=Entry(Frame3,textvariable=Posicion150,width=5)
    ArregloPos150.grid(row=4,column=21,sticky=NSEW)
    Posicion151=StringVar()
    ArregloPos151=Entry(Frame3,textvariable=Posicion151,width=5)
    ArregloPos151.grid(row=4,column=22,sticky=NSEW)
    Posicion152=StringVar()
    ArregloPos152=Entry(Frame3,textvariable=Posicion152,width=5)
    ArregloPos152.grid(row=4,column=23,sticky=NSEW)
    Posicion153=StringVar()
    ArregloPos153=Entry(Frame3,textvariable=Posicion153,width=5)
    ArregloPos153.grid(row=4,column=24,sticky=NSEW)
    Posicion154=StringVar()
    ArregloPos154=Entry(Frame3,textvariable=Posicion154,width=5)
    ArregloPos154.grid(row=4,column=25,sticky=NSEW)
    Posicion155=StringVar()
    ArregloPos155=Entry(Frame3,textvariable=Posicion155,width=5)
    ArregloPos155.grid(row=4,column=26,sticky=NSEW)
    Posicion156=StringVar()
    ArregloPos156=Entry(Frame3,textvariable=Posicion156,width=5)
    ArregloPos156.grid(row=4,column=27,sticky=NSEW)
    Posicion157=StringVar()
    ArregloPos157=Entry(Frame3,textvariable=Posicion157,width=5)
    ArregloPos157.grid(row=4,column=28,sticky=NSEW)
    Posicion158=StringVar()
    ArregloPos158=Entry(Frame3,textvariable=Posicion158,width=5)
    ArregloPos158.grid(row=4,column=29,sticky=NSEW)
    Posicion159=StringVar()
    ArregloPos159=Entry(Frame3,textvariable=Posicion159,width=5)
    ArregloPos159.grid(row=4,column=30,sticky=NSEW)

    #ArregloMatrizFila6
    Posicion161=StringVar()
    ArregloPos161=Entry(Frame3,textvariable=Posicion161,width=5)
    ArregloPos161.grid(row=5,column=0,sticky=NSEW)
    Posicion161.set("Fp8")
    Posicion162=StringVar()
    ArregloPos162=Entry(Frame3,textvariable=Posicion162,width=5)
    ArregloPos162.grid(row=5,column=1,sticky=NSEW)
    Posicion163=StringVar()
    ArregloPos163=Entry(Frame3,textvariable=Posicion163,width=5)
    ArregloPos163.grid(row=5,column=2,sticky=NSEW)
    Posicion164=StringVar()
    ArregloPos164=Entry(Frame3,textvariable=Posicion164,width=5)
    ArregloPos164.grid(row=5,column=3,sticky=NSEW)
    Posicion165=StringVar()
    ArregloPos165=Entry(Frame3,textvariable=Posicion165,width=5)
    ArregloPos165.grid(row=5,column=4,sticky=NSEW)
    Posicion166=StringVar()
    ArregloPos166=Entry(Frame3,textvariable=Posicion166,width=5)
    ArregloPos166.grid(row=5,column=5,sticky=NSEW)
    Posicion167=StringVar()
    ArregloPos167=Entry(Frame3,textvariable=Posicion167,width=5)
    ArregloPos167.grid(row=5,column=6,sticky=NSEW)
    Posicion168=StringVar()
    ArregloPos168=Entry(Frame3,textvariable=Posicion168,width=5)
    ArregloPos168.grid(row=5,column=7,sticky=NSEW)
    Posicion169=StringVar()
    ArregloPos169=Entry(Frame3,textvariable=Posicion169,width=5)
    ArregloPos169.grid(row=5,column=8,sticky=NSEW)
    Posicion170=StringVar()
    ArregloPos170=Entry(Frame3,textvariable=Posicion170,width=5)
    ArregloPos170.grid(row=5,column=9,sticky=NSEW)
    Posicion171=StringVar()
    ArregloPos171=Entry(Frame3,textvariable=Posicion171,width=5)
    ArregloPos171.grid(row=5,column=10,sticky=NSEW)
    Posicion172=StringVar()
    ArregloPos172=Entry(Frame3,textvariable=Posicion172,width=5)
    ArregloPos172.grid(row=5,column=11,sticky=NSEW)
    Posicion173=StringVar()
    ArregloPos173=Entry(Frame3,textvariable=Posicion173,width=5)
    ArregloPos173.grid(row=5,column=12,sticky=NSEW)
    Posicion174=StringVar()
    ArregloPos174=Entry(Frame3,textvariable=Posicion174,width=5)
    ArregloPos174.grid(row=5,column=13,sticky=NSEW)
    Posicion175=StringVar()
    ArregloPos175=Entry(Frame3,textvariable=Posicion175,width=5)
    ArregloPos175.grid(row=5,column=14,sticky=NSEW)
    Posicion176=StringVar()
    ArregloPos176=Entry(Frame3,textvariable=Posicion176,width=5)
    ArregloPos176.grid(row=5,column=15,sticky=NSEW)
    Posicion177=StringVar()
    ArregloPos177=Entry(Frame3,textvariable=Posicion177,width=5)
    ArregloPos177.grid(row=5,column=16,sticky=NSEW)
    Posicion178=StringVar()
    ArregloPos178=Entry(Frame3,textvariable=Posicion178,width=5)
    ArregloPos178.grid(row=5,column=17,sticky=NSEW)
    Posicion179=StringVar()
    ArregloPos179=Entry(Frame3,textvariable=Posicion179,width=5)
    ArregloPos179.grid(row=5,column=18,sticky=NSEW)
    Posicion180=StringVar()
    ArregloPos180=Entry(Frame3,textvariable=Posicion180,width=5)
    ArregloPos180.grid(row=5,column=19,sticky=NSEW)
    Posicion181=StringVar()
    ArregloPos181=Entry(Frame3,textvariable=Posicion181,width=5)
    ArregloPos181.grid(row=5,column=20,sticky=NSEW)
    Posicion182=StringVar()
    ArregloPos182=Entry(Frame3,textvariable=Posicion182,width=5)
    ArregloPos182.grid(row=5,column=21,sticky=NSEW)
    Posicion183=StringVar()
    ArregloPos183=Entry(Frame3,textvariable=Posicion183,width=5)
    ArregloPos183.grid(row=5,column=22,sticky=NSEW)
    Posicion184=StringVar()
    ArregloPos184=Entry(Frame3,textvariable=Posicion184,width=5)
    ArregloPos184.grid(row=5,column=23,sticky=NSEW)
    Posicion185=StringVar()
    ArregloPos185=Entry(Frame3,textvariable=Posicion185,width=5)
    ArregloPos185.grid(row=5,column=24,sticky=NSEW)
    Posicion186=StringVar()
    ArregloPos186=Entry(Frame3,textvariable=Posicion186,width=5)
    ArregloPos186.grid(row=5,column=25,sticky=NSEW)
    Posicion187=StringVar()
    ArregloPos187=Entry(Frame3,textvariable=Posicion187,width=5)
    ArregloPos187.grid(row=5,column=26,sticky=NSEW)
    Posicion188=StringVar()
    ArregloPos188=Entry(Frame3,textvariable=Posicion188,width=5)
    ArregloPos188.grid(row=5,column=27,sticky=NSEW)
    Posicion189=StringVar()
    ArregloPos189=Entry(Frame3,textvariable=Posicion189,width=5)
    ArregloPos189.grid(row=5,column=28,sticky=NSEW)
    Posicion190=StringVar()
    ArregloPos190=Entry(Frame3,textvariable=Posicion190,width=5)
    ArregloPos190.grid(row=5,column=29,sticky=NSEW)
    Posicion191=StringVar()
    ArregloPos191=Entry(Frame3,textvariable=Posicion191,width=5)
    ArregloPos191.grid(row=5,column=30,sticky=NSEW)

    #ArregloMatrizFila7
    Posicion193=StringVar()
    ArregloPos193=Entry(Frame3,textvariable=Posicion193,width=5)
    ArregloPos193.grid(row=6,column=0,sticky=NSEW)
    Posicion193.set("Fp16")
    Posicion194=StringVar()
    ArregloPos194=Entry(Frame3,textvariable=Posicion194,width=5)
    ArregloPos194.grid(row=6,column=1,sticky=NSEW)
    Posicion195=StringVar()
    ArregloPos195=Entry(Frame3,textvariable=Posicion195,width=5)
    ArregloPos195.grid(row=6,column=2,sticky=NSEW)
    Posicion196=StringVar()
    ArregloPos196=Entry(Frame3,textvariable=Posicion196,width=5)
    ArregloPos196.grid(row=6,column=3,sticky=NSEW)
    Posicion197=StringVar()
    ArregloPos197=Entry(Frame3,textvariable=Posicion197,width=5)
    ArregloPos197.grid(row=6,column=4,sticky=NSEW)
    Posicion198=StringVar()
    ArregloPos198=Entry(Frame3,textvariable=Posicion198,width=5)
    ArregloPos198.grid(row=6,column=5,sticky=NSEW)
    Posicion199=StringVar()
    ArregloPos199=Entry(Frame3,textvariable=Posicion199,width=5)
    ArregloPos199.grid(row=6,column=6,sticky=NSEW)
    Posicion200=StringVar()
    ArregloPos200=Entry(Frame3,textvariable=Posicion200,width=5)
    ArregloPos200.grid(row=6,column=7,sticky=NSEW)
    Posicion201=StringVar()
    ArregloPos201=Entry(Frame3,textvariable=Posicion201,width=5)
    ArregloPos201.grid(row=6,column=8,sticky=NSEW)
    Posicion202=StringVar()
    ArregloPos202=Entry(Frame3,textvariable=Posicion202,width=5)
    ArregloPos202.grid(row=6,column=9,sticky=NSEW)
    Posicion203=StringVar()
    ArregloPos203=Entry(Frame3,textvariable=Posicion203,width=5)
    ArregloPos203.grid(row=6,column=10,sticky=NSEW)
    Posicion204=StringVar()
    ArregloPos204=Entry(Frame3,textvariable=Posicion204,width=5)
    ArregloPos204.grid(row=6,column=11,sticky=NSEW)
    Posicion205=StringVar()
    ArregloPos205=Entry(Frame3,textvariable=Posicion205,width=5)
    ArregloPos205.grid(row=6,column=12,sticky=NSEW)
    Posicion206=StringVar()
    ArregloPos206=Entry(Frame3,textvariable=Posicion206,width=5)
    ArregloPos206.grid(row=6,column=13,sticky=NSEW)
    Posicion207=StringVar()
    ArregloPos207=Entry(Frame3,textvariable=Posicion207,width=5)
    ArregloPos207.grid(row=6,column=14,sticky=NSEW)
    Posicion208=StringVar()
    ArregloPos208=Entry(Frame3,textvariable=Posicion208,width=5)
    ArregloPos208.grid(row=6,column=15,sticky=NSEW)
    Posicion209=StringVar()
    ArregloPos209=Entry(Frame3,textvariable=Posicion209,width=5)
    ArregloPos209.grid(row=6,column=16,sticky=NSEW)
    Posicion210=StringVar()
    ArregloPos210=Entry(Frame3,textvariable=Posicion210,width=5)
    ArregloPos210.grid(row=6,column=17,sticky=NSEW)
    Posicion211=StringVar()
    ArregloPos211=Entry(Frame3,textvariable=Posicion211,width=5)
    ArregloPos211.grid(row=6,column=18,sticky=NSEW)
    Posicion212=StringVar()
    ArregloPos212=Entry(Frame3,textvariable=Posicion212,width=5)
    ArregloPos212.grid(row=6,column=19,sticky=NSEW)
    Posicion213=StringVar()
    ArregloPos213=Entry(Frame3,textvariable=Posicion213,width=5)
    ArregloPos213.grid(row=6,column=20,sticky=NSEW)
    Posicion214=StringVar()
    ArregloPos214=Entry(Frame3,textvariable=Posicion214,width=5)
    ArregloPos214.grid(row=6,column=21,sticky=NSEW)
    Posicion215=StringVar()
    ArregloPos215=Entry(Frame3,textvariable=Posicion215,width=5)
    ArregloPos215.grid(row=6,column=22,sticky=NSEW)
    Posicion216=StringVar()
    ArregloPos216=Entry(Frame3,textvariable=Posicion216,width=5)
    ArregloPos216.grid(row=6,column=23,sticky=NSEW)
    Posicion217=StringVar()
    ArregloPos217=Entry(Frame3,textvariable=Posicion217,width=5)
    ArregloPos217.grid(row=6,column=24,sticky=NSEW)
    Posicion218=StringVar()
    ArregloPos218=Entry(Frame3,textvariable=Posicion218,width=5)
    ArregloPos218.grid(row=6,column=25,sticky=NSEW)
    Posicion219=StringVar()
    ArregloPos219=Entry(Frame3,textvariable=Posicion219,width=5)
    ArregloPos219.grid(row=6,column=26,sticky=NSEW)
    Posicion220=StringVar()
    ArregloPos220=Entry(Frame3,textvariable=Posicion220,width=5)
    ArregloPos220.grid(row=6,column=27,sticky=NSEW)
    Posicion221=StringVar()
    ArregloPos221=Entry(Frame3,textvariable=Posicion221,width=5)
    ArregloPos221.grid(row=6,column=28,sticky=NSEW)
    Posicion222=StringVar()
    ArregloPos222=Entry(Frame3,textvariable=Posicion222,width=5)
    ArregloPos222.grid(row=6,column=29,sticky=NSEW)
    Posicion223=StringVar()
    ArregloPos223=Entry(Frame3,textvariable=Posicion223,width=5)
    ArregloPos223.grid(row=6,column=30,sticky=NSEW)

    #Mostrar Matriz Verficacion
    #ArregloMatrizFila1
    VPosicion1=StringVar()
    VArregloPos1=Entry(Frame4,textvariable=VPosicion1,width=5)
    VArregloPos1.grid(row=0,column=0,sticky=NSEW)
    VPosicion2=StringVar()
    VArregloPos2=Entry(Frame4,textvariable=VPosicion2,width=5)
    VArregloPos2.grid(row=0,column=1,sticky=NSEW)
    VPosicion3=StringVar()
    VArregloPos3=Entry(Frame4,textvariable=VPosicion3,width=5)
    VArregloPos3.grid(row=0,column=2,sticky=NSEW)
    VPosicion4=StringVar()
    VArregloPos4=Entry(Frame4,textvariable=VPosicion4,width=5)
    VArregloPos4.grid(row=0,column=3,sticky=NSEW)
    VPosicion5=StringVar()
    VArregloPos5=Entry(Frame4,textvariable=VPosicion5,width=5)
    VArregloPos5.grid(row=0,column=4,sticky=NSEW)
    VPosicion6=StringVar()
    VArregloPos6=Entry(Frame4,textvariable=VPosicion6,width=5)
    VArregloPos6.grid(row=0,column=5,sticky=NSEW)
    VPosicion7=StringVar()
    VArregloPos7=Entry(Frame4,textvariable=VPosicion7,width=5)
    VArregloPos7.grid(row=0,column=6,sticky=NSEW)
    VPosicion8=StringVar()
    VArregloPos8=Entry(Frame4,textvariable=VPosicion8,width=5)
    VArregloPos8.grid(row=0,column=7,sticky=NSEW)
    VPosicion9=StringVar()
    VArregloPos9=Entry(Frame4,textvariable=VPosicion9,width=5)
    VArregloPos9.grid(row=0,column=8,sticky=NSEW)
    VPosicion10=StringVar()
    VArregloPos10=Entry(Frame4,textvariable=VPosicion10,width=5)
    VArregloPos10.grid(row=0,column=9,sticky=NSEW)
    VPosicion11=StringVar()
    VArregloPos11=Entry(Frame4,textvariable=VPosicion11,width=5)
    VArregloPos11.grid(row=0,column=10,sticky=NSEW)
    VPosicion12=StringVar()
    VArregloPos12=Entry(Frame4,textvariable=VPosicion12,width=5)
    VArregloPos12.grid(row=0,column=11,sticky=NSEW)
    VPosicion13=StringVar()
    VArregloPos13=Entry(Frame4,textvariable=VPosicion13,width=5)
    VArregloPos13.grid(row=0,column=12,sticky=NSEW)
    VPosicion14=StringVar()
    VArregloPos14=Entry(Frame4,textvariable=VPosicion14,width=5)
    VArregloPos14.grid(row=0,column=13,sticky=NSEW)
    VPosicion15=StringVar()
    VArregloPos15=Entry(Frame4,textvariable=VPosicion15,width=5)
    VArregloPos15.grid(row=0,column=14,sticky=NSEW)
    VPosicion16=StringVar()
    VArregloPos16=Entry(Frame4,textvariable=VPosicion16,width=5)
    VArregloPos16.grid(row=0,column=15,sticky=NSEW)
    VPosicion17=StringVar()
    VArregloPos17=Entry(Frame4,textvariable=VPosicion17,width=5)
    VArregloPos17.grid(row=0,column=16,sticky=NSEW)
    VPosicion18=StringVar()
    VArregloPos18=Entry(Frame4,textvariable=VPosicion18,width=5)
    VArregloPos18.grid(row=0,column=17,sticky=NSEW)
    VPosicion19=StringVar()
    VArregloPos19=Entry(Frame4,textvariable=VPosicion19,width=5)
    VArregloPos19.grid(row=0,column=18,sticky=NSEW)
    VPosicion20=StringVar()
    VArregloPos20=Entry(Frame4,textvariable=VPosicion20,width=5)
    VArregloPos20.grid(row=0,column=19,sticky=NSEW)
    VPosicion21=StringVar()
    VArregloPos21=Entry(Frame4,textvariable=VPosicion21,width=5)
    VArregloPos21.grid(row=0,column=20,sticky=NSEW)
    VPosicion22=StringVar()
    VArregloPos22=Entry(Frame4,textvariable=VPosicion22,width=5)
    VArregloPos22.grid(row=0,column=21,sticky=NSEW)
    VPosicion23=StringVar()
    VArregloPos23=Entry(Frame4,textvariable=VPosicion23,width=5)
    VArregloPos23.grid(row=0,column=22,sticky=NSEW)
    VPosicion24=StringVar()
    VArregloPos24=Entry(Frame4,textvariable=VPosicion24,width=5)
    VArregloPos24.grid(row=0,column=23,sticky=NSEW)
    VPosicion25=StringVar()
    VArregloPos25=Entry(Frame4,textvariable=VPosicion25,width=5)
    VArregloPos25.grid(row=0,column=24,sticky=NSEW)
    VPosicion26=StringVar()
    VArregloPos26=Entry(Frame4,textvariable=VPosicion26,width=5)
    VArregloPos26.grid(row=0,column=25,sticky=NSEW)
    VPosicion27=StringVar()
    VArregloPos27=Entry(Frame4,textvariable=VPosicion27,width=5)
    VArregloPos27.grid(row=0,column=26,sticky=NSEW)
    VPosicion28=StringVar()
    VArregloPos28=Entry(Frame4,textvariable=VPosicion28,width=5)
    VArregloPos28.grid(row=0,column=27,sticky=NSEW)
    VPosicion29=StringVar()
    VArregloPos29=Entry(Frame4,textvariable=VPosicion29,width=5)
    VArregloPos29.grid(row=0,column=28,sticky=NSEW)
    VPosicion30=StringVar()
    VArregloPos30=Entry(Frame4,textvariable=VPosicion30,width=5)
    VArregloPos30.grid(row=0,column=29,sticky=NSEW)
    VPosicion31=StringVar()
    VArregloPos31=Entry(Frame4,textvariable=VPosicion31,width=5)
    VArregloPos31.grid(row=0,column=30,sticky=NSEW)
    VPosicion32=StringVar()
    VArregloPos32=Entry(Frame4,textvariable=VPosicion32,width=5)
    VArregloPos32.grid(row=0,column=31,sticky=NSEW)
    VPosicion2.set(1)
    VPosicion3.set(2)
    VPosicion4.set(3)
    VPosicion5.set(4)
    VPosicion6.set(5)
    VPosicion7.set(6)
    VPosicion8.set(7)
    VPosicion9.set(8)
    VPosicion10.set(9)
    VPosicion11.set(10)
    VPosicion12.set(11)
    VPosicion13.set(12)
    VPosicion14.set(13)
    VPosicion15.set(14)
    VPosicion16.set(15)
    VPosicion17.set(16)
    VPosicion18.set(17)
    VPosicion19.set(18)
    VPosicion20.set(19)
    VPosicion21.set(20)
    VPosicion22.set(21)
    VPosicion23.set(22)
    VPosicion24.set(23)
    VPosicion25.set(24)
    VPosicion26.set(25)
    VPosicion27.set(26)
    VPosicion28.set(27)
    VPosicion29.set(28)
    VPosicion30.set(29)
    VPosicion31.set(30)
    VPosicion32.set("Check")

    #ArregloMatrizFila2
    VPosicion33=StringVar()
    VArregloPos33=Entry(Frame4,textvariable=VPosicion33,width=5)
    VArregloPos33.grid(row=1,column=0,sticky=NSEW)
    VPosicion34=StringVar()
    VArregloPos34=Entry(Frame4,textvariable=VPosicion34,width=5)
    VArregloPos34.grid(row=1,column=1,sticky=NSEW)
    VPosicion35=StringVar()
    VArregloPos35=Entry(Frame4,textvariable=VPosicion35,width=5)
    VArregloPos35.grid(row=1,column=2,sticky=NSEW)
    VPosicion36=StringVar()
    VArregloPos36=Entry(Frame4,textvariable=VPosicion36,width=5)
    VArregloPos36.grid(row=1,column=3,sticky=NSEW)
    VPosicion37=StringVar()
    VArregloPos37=Entry(Frame4,textvariable=VPosicion37,width=5)
    VArregloPos37.grid(row=1,column=4,sticky=NSEW)
    VPosicion38=StringVar()
    VArregloPos38=Entry(Frame4,textvariable=VPosicion38,width=5)
    VArregloPos38.grid(row=1,column=5,sticky=NSEW)
    VPosicion39=StringVar()
    VArregloPos39=Entry(Frame4,textvariable=VPosicion39,width=5)
    VArregloPos39.grid(row=1,column=6,sticky=NSEW)
    VPosicion40=StringVar()
    VArregloPos40=Entry(Frame4,textvariable=VPosicion40,width=5)
    VArregloPos40.grid(row=1,column=7,sticky=NSEW)
    VPosicion41=StringVar()
    VArregloPos41=Entry(Frame4,textvariable=VPosicion41,width=5)
    VArregloPos41.grid(row=1,column=8,sticky=NSEW)
    VPosicion42=StringVar()
    VArregloPos42=Entry(Frame4,textvariable=VPosicion42,width=5)
    VArregloPos42.grid(row=1,column=9,sticky=NSEW)
    VPosicion43=StringVar()
    VArregloPos43=Entry(Frame4,textvariable=VPosicion43,width=5)
    VArregloPos43.grid(row=1,column=10,sticky=NSEW)
    VPosicion44=StringVar()
    VArregloPos44=Entry(Frame4,textvariable=VPosicion44,width=5)
    VArregloPos44.grid(row=1,column=11,sticky=NSEW)
    VPosicion45=StringVar()
    VArregloPos45=Entry(Frame4,textvariable=VPosicion45,width=5)
    VArregloPos45.grid(row=1,column=12,sticky=NSEW)
    VPosicion46=StringVar()
    VArregloPos46=Entry(Frame4,textvariable=VPosicion46,width=5)
    VArregloPos46.grid(row=1,column=13,sticky=NSEW)
    VPosicion47=StringVar()
    VArregloPos47=Entry(Frame4,textvariable=VPosicion47,width=5)
    VArregloPos47.grid(row=1,column=14,sticky=NSEW)
    VPosicion48=StringVar()
    VArregloPos48=Entry(Frame4,textvariable=VPosicion48,width=5)
    VArregloPos48.grid(row=1,column=15,sticky=NSEW)
    VPosicion49=StringVar()
    VArregloPos49=Entry(Frame4,textvariable=VPosicion49,width=5)
    VArregloPos49.grid(row=1,column=16,sticky=NSEW)
    VPosicion50=StringVar()
    VArregloPos50=Entry(Frame4,textvariable=VPosicion50,width=5)
    VArregloPos50.grid(row=1,column=17,sticky=NSEW)
    VPosicion51=StringVar()
    VArregloPos51=Entry(Frame4,textvariable=VPosicion51,width=5)
    VArregloPos51.grid(row=1,column=18,sticky=NSEW)
    VPosicion52=StringVar()
    VArregloPos52=Entry(Frame4,textvariable=VPosicion52,width=5)
    VArregloPos52.grid(row=1,column=19,sticky=NSEW)
    VPosicion53=StringVar()
    VArregloPos53=Entry(Frame4,textvariable=VPosicion53,width=5)
    VArregloPos53.grid(row=1,column=20,sticky=NSEW)
    VPosicion54=StringVar()
    VArregloPos54=Entry(Frame4,textvariable=VPosicion54,width=5)
    VArregloPos54.grid(row=1,column=21,sticky=NSEW)
    VPosicion55=StringVar()
    VArregloPos55=Entry(Frame4,textvariable=VPosicion55,width=5)
    VArregloPos55.grid(row=1,column=22,sticky=NSEW)
    VPosicion56=StringVar()
    VArregloPos56=Entry(Frame4,textvariable=VPosicion56,width=5)
    VArregloPos56.grid(row=1,column=23,sticky=NSEW)
    VPosicion57=StringVar()
    VArregloPos57=Entry(Frame4,textvariable=VPosicion57,width=5)
    VArregloPos57.grid(row=1,column=24,sticky=NSEW)
    VPosicion58=StringVar()
    VArregloPos58=Entry(Frame4,textvariable=VPosicion58,width=5)
    VArregloPos58.grid(row=1,column=25,sticky=NSEW)
    VPosicion59=StringVar()
    VArregloPos59=Entry(Frame4,textvariable=VPosicion59,width=5)
    VArregloPos59.grid(row=1,column=26,sticky=NSEW)
    VPosicion60=StringVar()
    VArregloPos60=Entry(Frame4,textvariable=VPosicion60,width=5)
    VArregloPos60.grid(row=1,column=27,sticky=NSEW)
    VPosicion61=StringVar()
    VArregloPos61=Entry(Frame4,textvariable=VPosicion61,width=5)
    VArregloPos61.grid(row=1,column=28,sticky=NSEW)
    VPosicion62=StringVar()
    VArregloPos62=Entry(Frame4,textvariable=VPosicion62,width=5)
    VArregloPos62.grid(row=1,column=29,sticky=NSEW)
    VPosicion63=StringVar()
    VArregloPos63=Entry(Frame4,textvariable=VPosicion63,width=5)
    VArregloPos63.grid(row=1,column=30,sticky=NSEW)
    VPosicion64=StringVar()
    VArregloPos64=Entry(Frame4,textvariable=VPosicion64,width=5)
    VArregloPos64.grid(row=1,column=31,sticky=NSEW)

    #ArregloMatrizFila3
    VPosicion65=StringVar()
    VArregloPos65=Entry(Frame4,textvariable=VPosicion65,width=5)
    VArregloPos65.grid(row=2,column=0,sticky=NSEW)
    VPosicion65.set("Trama")
    VPosicion66=StringVar()
    VArregloPos66=Entry(Frame4,textvariable=VPosicion66,width=5)
    VArregloPos66.grid(row=2,column=1,sticky=NSEW)
    VPosicion67=StringVar()
    VArregloPos67=Entry(Frame4,textvariable=VPosicion67,width=5)
    VArregloPos67.grid(row=2,column=2,sticky=NSEW)
    VPosicion68=StringVar()
    VArregloPos68=Entry(Frame4,textvariable=VPosicion68,width=5)
    VArregloPos68.grid(row=2,column=3,sticky=NSEW)
    VPosicion69=StringVar()
    VArregloPos69=Entry(Frame4,textvariable=VPosicion69,width=5)
    VArregloPos69.grid(row=2,column=4,sticky=NSEW)
    VPosicion70=StringVar()
    VArregloPos70=Entry(Frame4,textvariable=VPosicion70,width=5)
    VArregloPos70.grid(row=2,column=5,sticky=NSEW)
    VPosicion71=StringVar()
    VArregloPos71=Entry(Frame4,textvariable=VPosicion71,width=5)
    VArregloPos71.grid(row=2,column=6,sticky=NSEW)
    VPosicion72=StringVar()
    VArregloPos72=Entry(Frame4,textvariable=VPosicion72,width=5)
    VArregloPos72.grid(row=2,column=7,sticky=NSEW)
    VPosicion73=StringVar()
    VArregloPos73=Entry(Frame4,textvariable=VPosicion73,width=5)
    VArregloPos73.grid(row=2,column=8,sticky=NSEW)
    VPosicion74=StringVar()
    VArregloPos74=Entry(Frame4,textvariable=VPosicion74,width=5)
    VArregloPos74.grid(row=2,column=9,sticky=NSEW)
    VPosicion75=StringVar()
    VArregloPos75=Entry(Frame4,textvariable=VPosicion75,width=5)
    VArregloPos75.grid(row=2,column=10,sticky=NSEW)
    VPosicion76=StringVar()
    VArregloPos76=Entry(Frame4,textvariable=VPosicion76,width=5)
    VArregloPos76.grid(row=2,column=11,sticky=NSEW)
    VPosicion77=StringVar()
    VArregloPos77=Entry(Frame4,textvariable=VPosicion77,width=5)
    VArregloPos77.grid(row=2,column=12,sticky=NSEW)
    VPosicion78=StringVar()
    VArregloPos78=Entry(Frame4,textvariable=VPosicion78,width=5)
    VArregloPos78.grid(row=2,column=13,sticky=NSEW)
    VPosicion79=StringVar()
    VArregloPos79=Entry(Frame4,textvariable=VPosicion79,width=5)
    VArregloPos79.grid(row=2,column=14,sticky=NSEW)
    VPosicion80=StringVar()
    VArregloPos80=Entry(Frame4,textvariable=VPosicion80,width=5)
    VArregloPos80.grid(row=2,column=15,sticky=NSEW)
    VPosicion81=StringVar()
    VArregloPos81=Entry(Frame4,textvariable=VPosicion81,width=5)
    VArregloPos81.grid(row=2,column=16,sticky=NSEW)
    VPosicion82=StringVar()
    VArregloPos82=Entry(Frame4,textvariable=VPosicion82,width=5)
    VArregloPos82.grid(row=2,column=17,sticky=NSEW)
    VPosicion83=StringVar()
    VArregloPos83=Entry(Frame4,textvariable=VPosicion83,width=5)
    VArregloPos83.grid(row=2,column=18,sticky=NSEW)
    VPosicion84=StringVar()
    VArregloPos84=Entry(Frame4,textvariable=VPosicion84,width=5)
    VArregloPos84.grid(row=2,column=19,sticky=NSEW)
    VPosicion85=StringVar()
    VArregloPos85=Entry(Frame4,textvariable=VPosicion85,width=5)
    VArregloPos85.grid(row=2,column=20,sticky=NSEW)
    VPosicion86=StringVar()
    VArregloPos86=Entry(Frame4,textvariable=VPosicion86,width=5)
    VArregloPos86.grid(row=2,column=21,sticky=NSEW)
    VPosicion87=StringVar()
    VArregloPos87=Entry(Frame4,textvariable=VPosicion87,width=5)
    VArregloPos87.grid(row=2,column=22,sticky=NSEW)
    VPosicion88=StringVar()
    VArregloPos88=Entry(Frame4,textvariable=VPosicion88,width=5)
    VArregloPos88.grid(row=2,column=23,sticky=NSEW)
    VPosicion89=StringVar()
    VArregloPos89=Entry(Frame4,textvariable=VPosicion89,width=5)
    VArregloPos89.grid(row=2,column=24,sticky=NSEW)
    VPosicion90=StringVar()
    VArregloPos90=Entry(Frame4,textvariable=VPosicion90,width=5)
    VArregloPos90.grid(row=2,column=25,sticky=NSEW)
    VPosicion91=StringVar()
    VArregloPos91=Entry(Frame4,textvariable=VPosicion91,width=5)
    VArregloPos91.grid(row=2,column=26,sticky=NSEW)
    VPosicion92=StringVar()
    VArregloPos92=Entry(Frame4,textvariable=VPosicion92,width=5)
    VArregloPos92.grid(row=2,column=27,sticky=NSEW)
    VPosicion93=StringVar()
    VArregloPos93=Entry(Frame4,textvariable=VPosicion93,width=5)
    VArregloPos93.grid(row=2,column=28,sticky=NSEW)
    VPosicion94=StringVar()
    VArregloPos94=Entry(Frame4,textvariable=VPosicion94,width=5)
    VArregloPos94.grid(row=2,column=29,sticky=NSEW)
    VPosicion95=StringVar()
    VArregloPos95=Entry(Frame4,textvariable=VPosicion95,width=5)
    VArregloPos95.grid(row=2,column=30,sticky=NSEW)
    VPosicion96=StringVar()
    VArregloPos96=Entry(Frame4,textvariable=VPosicion96,width=5)
    VArregloPos96.grid(row=2,column=31,sticky=NSEW)

    #ArregloMatrizFila4
    VPosicion97=StringVar()
    VArregloPos97=Entry(Frame4,textvariable=VPosicion97,width=5)
    VArregloPos97.grid(row=3,column=0,sticky=NSEW)
    VPosicion97.set("Fp1")
    VPosicion98=StringVar()
    VArregloPos98=Entry(Frame4,textvariable=VPosicion98,width=5)
    VArregloPos98.grid(row=3,column=1,sticky=NSEW)
    VPosicion99=StringVar()
    VArregloPos99=Entry(Frame4,textvariable=VPosicion99,width=5)
    VArregloPos99.grid(row=3,column=2,sticky=NSEW)
    VPosicion100=StringVar()
    VArregloPos100=Entry(Frame4,textvariable=VPosicion100,width=5)
    VArregloPos100.grid(row=3,column=3,sticky=NSEW)
    VPosicion101=StringVar()
    VArregloPos101=Entry(Frame4,textvariable=VPosicion101,width=5)
    VArregloPos101.grid(row=3,column=4,sticky=NSEW)
    VPosicion102=StringVar()
    VArregloPos102=Entry(Frame4,textvariable=VPosicion102,width=5)
    VArregloPos102.grid(row=3,column=5,sticky=NSEW)
    VPosicion103=StringVar()
    VArregloPos103=Entry(Frame4,textvariable=VPosicion103,width=5)
    VArregloPos103.grid(row=3,column=6,sticky=NSEW)
    VPosicion104=StringVar()
    VArregloPos104=Entry(Frame4,textvariable=VPosicion104,width=5)
    VArregloPos104.grid(row=3,column=7,sticky=NSEW)
    VPosicion105=StringVar()
    VArregloPos105=Entry(Frame4,textvariable=VPosicion105,width=5)
    VArregloPos105.grid(row=3,column=8,sticky=NSEW)
    VPosicion106=StringVar()
    VArregloPos106=Entry(Frame4,textvariable=VPosicion106,width=5)
    VArregloPos106.grid(row=3,column=9,sticky=NSEW)
    VPosicion107=StringVar()
    VArregloPos107=Entry(Frame4,textvariable=VPosicion107,width=5)
    VArregloPos107.grid(row=3,column=10,sticky=NSEW)
    VPosicion108=StringVar()
    VArregloPos108=Entry(Frame4,textvariable=VPosicion108,width=5)
    VArregloPos108.grid(row=3,column=11,sticky=NSEW)
    VPosicion109=StringVar()
    VArregloPos109=Entry(Frame4,textvariable=VPosicion109,width=5)
    VArregloPos109.grid(row=3,column=12,sticky=NSEW)
    VPosicion110=StringVar()
    VArregloPos110=Entry(Frame4,textvariable=VPosicion110,width=5)
    VArregloPos110.grid(row=3,column=13,sticky=NSEW)
    VPosicion111=StringVar()
    VArregloPos111=Entry(Frame4,textvariable=VPosicion111,width=5)
    VArregloPos111.grid(row=3,column=14,sticky=NSEW)
    VPosicion112=StringVar()
    VArregloPos112=Entry(Frame4,textvariable=VPosicion112,width=5)
    VArregloPos112.grid(row=3,column=15,sticky=NSEW)
    VPosicion113=StringVar()
    VArregloPos113=Entry(Frame4,textvariable=VPosicion113,width=5)
    VArregloPos113.grid(row=3,column=16,sticky=NSEW)
    VPosicion114=StringVar()
    VArregloPos114=Entry(Frame4,textvariable=VPosicion114,width=5)
    VArregloPos114.grid(row=3,column=17,sticky=NSEW)
    VPosicion115=StringVar()
    VArregloPos115=Entry(Frame4,textvariable=VPosicion115,width=5)
    VArregloPos115.grid(row=3,column=18,sticky=NSEW)
    VPosicion116=StringVar()
    VArregloPos116=Entry(Frame4,textvariable=VPosicion116,width=5)
    VArregloPos116.grid(row=3,column=19,sticky=NSEW)
    VPosicion117=StringVar()
    VArregloPos117=Entry(Frame4,textvariable=VPosicion117,width=5)
    VArregloPos117.grid(row=3,column=20,sticky=NSEW)
    VPosicion118=StringVar()
    VArregloPos118=Entry(Frame4,textvariable=VPosicion118,width=5)
    VArregloPos118.grid(row=3,column=21,sticky=NSEW)
    VPosicion119=StringVar()
    VArregloPos119=Entry(Frame4,textvariable=VPosicion119,width=5)
    VArregloPos119.grid(row=3,column=22,sticky=NSEW)
    VPosicion120=StringVar()
    VArregloPos120=Entry(Frame4,textvariable=VPosicion120,width=5)
    VArregloPos120.grid(row=3,column=23,sticky=NSEW)
    VPosicion121=StringVar()
    VArregloPos121=Entry(Frame4,textvariable=VPosicion121,width=5)
    VArregloPos121.grid(row=3,column=24,sticky=NSEW)
    VPosicion122=StringVar()
    VArregloPos122=Entry(Frame4,textvariable=VPosicion122,width=5)
    VArregloPos122.grid(row=3,column=25,sticky=NSEW)
    VPosicion123=StringVar()
    VArregloPos123=Entry(Frame4,textvariable=VPosicion123,width=5)
    VArregloPos123.grid(row=3,column=26,sticky=NSEW)
    VPosicion124=StringVar()
    VArregloPos124=Entry(Frame4,textvariable=VPosicion124,width=5)
    VArregloPos124.grid(row=3,column=27,sticky=NSEW)
    VPosicion125=StringVar()
    VArregloPos125=Entry(Frame4,textvariable=VPosicion125,width=5)
    VArregloPos125.grid(row=3,column=28,sticky=NSEW)
    VPosicion126=StringVar()
    VArregloPos126=Entry(Frame4,textvariable=VPosicion126,width=5)
    VArregloPos126.grid(row=3,column=29,sticky=NSEW)
    VPosicion127=StringVar()
    VArregloPos127=Entry(Frame4,textvariable=VPosicion127,width=5)
    VArregloPos127.grid(row=3,column=30,sticky=NSEW)
    VPosicion128=StringVar()
    VArregloPos128=Entry(Frame4,textvariable=VPosicion128,width=5)
    VArregloPos128.grid(row=3,column=31,sticky=NSEW)

    #ArregloMatrizFila5
    VPosicion129=StringVar()
    VArregloPos129=Entry(Frame4,textvariable=VPosicion129,width=5)
    VArregloPos129.grid(row=4,column=0,sticky=NSEW)
    VPosicion129.set("Fp2")
    VPosicion130=StringVar()
    VArregloPos130=Entry(Frame4,textvariable=VPosicion130,width=5)
    VArregloPos130.grid(row=4,column=1,sticky=NSEW)
    VPosicion131=StringVar()
    VArregloPos131=Entry(Frame4,textvariable=VPosicion131,width=5)
    VArregloPos131.grid(row=4,column=2,sticky=NSEW)
    VPosicion132=StringVar()
    VArregloPos132=Entry(Frame4,textvariable=VPosicion132,width=5)
    VArregloPos132.grid(row=4,column=3,sticky=NSEW)
    VPosicion133=StringVar()
    VArregloPos133=Entry(Frame4,textvariable=VPosicion133,width=5)
    VArregloPos133.grid(row=4,column=4,sticky=NSEW)
    VPosicion134=StringVar()
    VArregloPos134=Entry(Frame4,textvariable=VPosicion134,width=5)
    VArregloPos134.grid(row=4,column=5,sticky=NSEW)
    VPosicion135=StringVar()
    VArregloPos135=Entry(Frame4,textvariable=VPosicion135,width=5)
    VArregloPos135.grid(row=4,column=6,sticky=NSEW)
    VPosicion136=StringVar()
    VArregloPos136=Entry(Frame4,textvariable=VPosicion136,width=5)
    VArregloPos136.grid(row=4,column=7,sticky=NSEW)
    VPosicion137=StringVar()
    VArregloPos137=Entry(Frame4,textvariable=VPosicion137,width=5)
    VArregloPos137.grid(row=4,column=8,sticky=NSEW)
    VPosicion138=StringVar()
    VArregloPos138=Entry(Frame4,textvariable=VPosicion138,width=5)
    VArregloPos138.grid(row=4,column=9,sticky=NSEW)
    VPosicion139=StringVar()
    VArregloPos139=Entry(Frame4,textvariable=VPosicion139,width=5)
    VArregloPos139.grid(row=4,column=10,sticky=NSEW)
    VPosicion140=StringVar()
    VArregloPos140=Entry(Frame4,textvariable=VPosicion140,width=5)
    VArregloPos140.grid(row=4,column=11,sticky=NSEW)
    VPosicion141=StringVar()
    VArregloPos141=Entry(Frame4,textvariable=VPosicion141,width=5)
    VArregloPos141.grid(row=4,column=12,sticky=NSEW)
    VPosicion142=StringVar()
    VArregloPos142=Entry(Frame4,textvariable=VPosicion142,width=5)
    VArregloPos142.grid(row=4,column=13,sticky=NSEW)
    VPosicion143=StringVar()
    VArregloPos143=Entry(Frame4,textvariable=VPosicion143,width=5)
    VArregloPos143.grid(row=4,column=14,sticky=NSEW)
    VPosicion144=StringVar()
    VArregloPos144=Entry(Frame4,textvariable=VPosicion144,width=5)
    VArregloPos144.grid(row=4,column=15,sticky=NSEW)
    VPosicion145=StringVar()
    VArregloPos145=Entry(Frame4,textvariable=VPosicion145,width=5)
    VArregloPos145.grid(row=4,column=16,sticky=NSEW)
    VPosicion146=StringVar()
    VArregloPos146=Entry(Frame4,textvariable=VPosicion146,width=5)
    VArregloPos146.grid(row=4,column=17,sticky=NSEW)
    VPosicion147=StringVar()
    VArregloPos147=Entry(Frame4,textvariable=VPosicion147,width=5)
    VArregloPos147.grid(row=4,column=18,sticky=NSEW)
    VPosicion148=StringVar()
    VArregloPos148=Entry(Frame4,textvariable=VPosicion148,width=5)
    VArregloPos148.grid(row=4,column=19,sticky=NSEW)
    VPosicion149=StringVar()
    VArregloPos149=Entry(Frame4,textvariable=VPosicion149,width=5)
    VArregloPos149.grid(row=4,column=20,sticky=NSEW)
    VPosicion150=StringVar()
    VArregloPos150=Entry(Frame4,textvariable=VPosicion150,width=5)
    VArregloPos150.grid(row=4,column=21,sticky=NSEW)
    VPosicion151=StringVar()
    VArregloPos151=Entry(Frame4,textvariable=VPosicion151,width=5)
    VArregloPos151.grid(row=4,column=22,sticky=NSEW)
    VPosicion152=StringVar()
    VArregloPos152=Entry(Frame4,textvariable=VPosicion152,width=5)
    VArregloPos152.grid(row=4,column=23,sticky=NSEW)
    VPosicion153=StringVar()
    VArregloPos153=Entry(Frame4,textvariable=VPosicion153,width=5)
    VArregloPos153.grid(row=4,column=24,sticky=NSEW)
    VPosicion154=StringVar()
    VArregloPos154=Entry(Frame4,textvariable=VPosicion154,width=5)
    VArregloPos154.grid(row=4,column=25,sticky=NSEW)
    VPosicion155=StringVar()
    VArregloPos155=Entry(Frame4,textvariable=VPosicion155,width=5)
    VArregloPos155.grid(row=4,column=26,sticky=NSEW)
    VPosicion156=StringVar()
    VArregloPos156=Entry(Frame4,textvariable=VPosicion156,width=5)
    VArregloPos156.grid(row=4,column=27,sticky=NSEW)
    VPosicion157=StringVar()
    VArregloPos157=Entry(Frame4,textvariable=VPosicion157,width=5)
    VArregloPos157.grid(row=4,column=28,sticky=NSEW)
    VPosicion158=StringVar()
    VArregloPos158=Entry(Frame4,textvariable=VPosicion158,width=5)
    VArregloPos158.grid(row=4,column=29,sticky=NSEW)
    VPosicion159=StringVar()
    VArregloPos159=Entry(Frame4,textvariable=VPosicion159,width=5)
    VArregloPos159.grid(row=4,column=30,sticky=NSEW)
    VPosicion160=StringVar()
    VArregloPos160=Entry(Frame4,textvariable=VPosicion160,width=5)
    VArregloPos160.grid(row=4,column=31,sticky=NSEW)

    #ArregloMatrizFila6
    VPosicion161=StringVar()
    VArregloPos161=Entry(Frame4,textvariable=VPosicion161,width=5)
    VArregloPos161.grid(row=5,column=0,sticky=NSEW)
    VPosicion161.set("Fp4")
    VPosicion162=StringVar()
    VArregloPos162=Entry(Frame4,textvariable=VPosicion162,width=5)
    VArregloPos162.grid(row=5,column=1,sticky=NSEW)
    VPosicion163=StringVar()
    VArregloPos163=Entry(Frame4,textvariable=VPosicion163,width=5)
    VArregloPos163.grid(row=5,column=2,sticky=NSEW)
    VPosicion164=StringVar()
    VArregloPos164=Entry(Frame4,textvariable=VPosicion164,width=5)
    VArregloPos164.grid(row=5,column=3,sticky=NSEW)
    VPosicion165=StringVar()
    VArregloPos165=Entry(Frame4,textvariable=VPosicion165,width=5)
    VArregloPos165.grid(row=5,column=4,sticky=NSEW)
    VPosicion166=StringVar()
    VArregloPos166=Entry(Frame4,textvariable=VPosicion166,width=5)
    VArregloPos166.grid(row=5,column=5,sticky=NSEW)
    VPosicion167=StringVar()
    VArregloPos167=Entry(Frame4,textvariable=VPosicion167,width=5)
    VArregloPos167.grid(row=5,column=6,sticky=NSEW)
    VPosicion168=StringVar()
    VArregloPos168=Entry(Frame4,textvariable=VPosicion168,width=5)
    VArregloPos168.grid(row=5,column=7,sticky=NSEW)
    VPosicion169=StringVar()
    VArregloPos169=Entry(Frame4,textvariable=VPosicion169,width=5)
    VArregloPos169.grid(row=5,column=8,sticky=NSEW)
    VPosicion170=StringVar()
    VArregloPos170=Entry(Frame4,textvariable=VPosicion170,width=5)
    VArregloPos170.grid(row=5,column=9,sticky=NSEW)
    VPosicion171=StringVar()
    VArregloPos171=Entry(Frame4,textvariable=VPosicion171,width=5)
    VArregloPos171.grid(row=5,column=10,sticky=NSEW)
    VPosicion172=StringVar()
    VArregloPos172=Entry(Frame4,textvariable=VPosicion172,width=5)
    VArregloPos172.grid(row=5,column=11,sticky=NSEW)
    VPosicion173=StringVar()
    VArregloPos173=Entry(Frame4,textvariable=VPosicion173,width=5)
    VArregloPos173.grid(row=5,column=12,sticky=NSEW)
    VPosicion174=StringVar()
    VArregloPos174=Entry(Frame4,textvariable=VPosicion174,width=5)
    VArregloPos174.grid(row=5,column=13,sticky=NSEW)
    VPosicion175=StringVar()
    VArregloPos175=Entry(Frame4,textvariable=VPosicion175,width=5)
    VArregloPos175.grid(row=5,column=14,sticky=NSEW)
    VPosicion176=StringVar()
    VArregloPos176=Entry(Frame4,textvariable=VPosicion176,width=5)
    VArregloPos176.grid(row=5,column=15,sticky=NSEW)
    VPosicion177=StringVar()
    VArregloPos177=Entry(Frame4,textvariable=VPosicion177,width=5)
    VArregloPos177.grid(row=5,column=16,sticky=NSEW)
    VPosicion178=StringVar()
    VArregloPos178=Entry(Frame4,textvariable=VPosicion178,width=5)
    VArregloPos178.grid(row=5,column=17,sticky=NSEW)
    VPosicion179=StringVar()
    VArregloPos179=Entry(Frame4,textvariable=VPosicion179,width=5)
    VArregloPos179.grid(row=5,column=18,sticky=NSEW)
    VPosicion180=StringVar()
    VArregloPos180=Entry(Frame4,textvariable=VPosicion180,width=5)
    VArregloPos180.grid(row=5,column=19,sticky=NSEW)
    VPosicion181=StringVar()
    VArregloPos181=Entry(Frame4,textvariable=VPosicion181,width=5)
    VArregloPos181.grid(row=5,column=20,sticky=NSEW)
    VPosicion182=StringVar()
    VArregloPos182=Entry(Frame4,textvariable=VPosicion182,width=5)
    VArregloPos182.grid(row=5,column=21,sticky=NSEW)
    VPosicion183=StringVar()
    VArregloPos183=Entry(Frame4,textvariable=VPosicion183,width=5)
    VArregloPos183.grid(row=5,column=22,sticky=NSEW)
    VPosicion184=StringVar()
    VArregloPos184=Entry(Frame4,textvariable=VPosicion184,width=5)
    VArregloPos184.grid(row=5,column=23,sticky=NSEW)
    VPosicion185=StringVar()
    VArregloPos185=Entry(Frame4,textvariable=VPosicion185,width=5)
    VArregloPos185.grid(row=5,column=24,sticky=NSEW)
    VPosicion186=StringVar()
    VArregloPos186=Entry(Frame4,textvariable=VPosicion186,width=5)
    VArregloPos186.grid(row=5,column=25,sticky=NSEW)
    VPosicion187=StringVar()
    VArregloPos187=Entry(Frame4,textvariable=VPosicion187,width=5)
    VArregloPos187.grid(row=5,column=26,sticky=NSEW)
    VPosicion188=StringVar()
    VArregloPos188=Entry(Frame4,textvariable=VPosicion188,width=5)
    VArregloPos188.grid(row=5,column=27,sticky=NSEW)
    VPosicion189=StringVar()
    VArregloPos189=Entry(Frame4,textvariable=VPosicion189,width=5)
    VArregloPos189.grid(row=5,column=28,sticky=NSEW)
    VPosicion190=StringVar()
    VArregloPos190=Entry(Frame4,textvariable=VPosicion190,width=5)
    VArregloPos190.grid(row=5,column=29,sticky=NSEW)
    VPosicion191=StringVar()
    VArregloPos191=Entry(Frame4,textvariable=VPosicion191,width=5)
    VArregloPos191.grid(row=5,column=30,sticky=NSEW)
    VPosicion192=StringVar()
    VArregloPos192=Entry(Frame4,textvariable=VPosicion192,width=5)
    VArregloPos192.grid(row=5,column=31,sticky=NSEW)

    #ArregloMatrizFila7
    VPosicion193=StringVar()
    VArregloPos193=Entry(Frame4,textvariable=VPosicion193,width=5)
    VArregloPos193.grid(row=6,column=0,sticky=NSEW)
    VPosicion193.set("Fp8")
    VPosicion194=StringVar()
    VArregloPos194=Entry(Frame4,textvariable=VPosicion194,width=5)
    VArregloPos194.grid(row=6,column=1,sticky=NSEW)
    VPosicion195=StringVar()
    VArregloPos195=Entry(Frame4,textvariable=VPosicion195,width=5)
    VArregloPos195.grid(row=6,column=2,sticky=NSEW)
    VPosicion196=StringVar()
    VArregloPos196=Entry(Frame4,textvariable=VPosicion196,width=5)
    VArregloPos196.grid(row=6,column=3,sticky=NSEW)
    VPosicion197=StringVar()
    VArregloPos197=Entry(Frame4,textvariable=VPosicion197,width=5)
    VArregloPos197.grid(row=6,column=4,sticky=NSEW)
    VPosicion198=StringVar()
    VArregloPos198=Entry(Frame4,textvariable=VPosicion198,width=5)
    VArregloPos198.grid(row=6,column=5,sticky=NSEW)
    VPosicion199=StringVar()
    VArregloPos199=Entry(Frame4,textvariable=VPosicion199,width=5)
    VArregloPos199.grid(row=6,column=6,sticky=NSEW)
    VPosicion200=StringVar()
    VArregloPos200=Entry(Frame4,textvariable=VPosicion200,width=5)
    VArregloPos200.grid(row=6,column=7,sticky=NSEW)
    VPosicion201=StringVar()
    VArregloPos201=Entry(Frame4,textvariable=VPosicion201,width=5)
    VArregloPos201.grid(row=6,column=8,sticky=NSEW)
    VPosicion202=StringVar()
    VArregloPos202=Entry(Frame4,textvariable=VPosicion202,width=5)
    VArregloPos202.grid(row=6,column=9,sticky=NSEW)
    VPosicion203=StringVar()
    VArregloPos203=Entry(Frame4,textvariable=VPosicion203,width=5)
    VArregloPos203.grid(row=6,column=10,sticky=NSEW)
    VPosicion204=StringVar()
    VArregloPos204=Entry(Frame4,textvariable=VPosicion204,width=5)
    VArregloPos204.grid(row=6,column=11,sticky=NSEW)
    VPosicion205=StringVar()
    VArregloPos205=Entry(Frame4,textvariable=VPosicion205,width=5)
    VArregloPos205.grid(row=6,column=12,sticky=NSEW)
    VPosicion206=StringVar()
    VArregloPos206=Entry(Frame4,textvariable=VPosicion206,width=5)
    VArregloPos206.grid(row=6,column=13,sticky=NSEW)
    VPosicion207=StringVar()
    VArregloPos207=Entry(Frame4,textvariable=VPosicion207,width=5)
    VArregloPos207.grid(row=6,column=14,sticky=NSEW)
    VPosicion208=StringVar()
    VArregloPos208=Entry(Frame4,textvariable=VPosicion208,width=5)
    VArregloPos208.grid(row=6,column=15,sticky=NSEW)
    VPosicion209=StringVar()
    VArregloPos209=Entry(Frame4,textvariable=VPosicion209,width=5)
    VArregloPos209.grid(row=6,column=16,sticky=NSEW)
    VPosicion210=StringVar()
    VArregloPos210=Entry(Frame4,textvariable=VPosicion210,width=5)
    VArregloPos210.grid(row=6,column=17,sticky=NSEW)
    VPosicion211=StringVar()
    VArregloPos211=Entry(Frame4,textvariable=VPosicion211,width=5)
    VArregloPos211.grid(row=6,column=18,sticky=NSEW)
    VPosicion212=StringVar()
    VArregloPos212=Entry(Frame4,textvariable=VPosicion212,width=5)
    VArregloPos212.grid(row=6,column=19,sticky=NSEW)
    VPosicion213=StringVar()
    VArregloPos213=Entry(Frame4,textvariable=VPosicion213,width=5)
    VArregloPos213.grid(row=6,column=20,sticky=NSEW)
    VPosicion214=StringVar()
    VArregloPos214=Entry(Frame4,textvariable=VPosicion214,width=5)
    VArregloPos214.grid(row=6,column=21,sticky=NSEW)
    VPosicion215=StringVar()
    VArregloPos215=Entry(Frame4,textvariable=VPosicion215,width=5)
    VArregloPos215.grid(row=6,column=22,sticky=NSEW)
    VPosicion216=StringVar()
    VArregloPos216=Entry(Frame4,textvariable=VPosicion216,width=5)
    VArregloPos216.grid(row=6,column=23,sticky=NSEW)
    VPosicion217=StringVar()
    VArregloPos217=Entry(Frame4,textvariable=VPosicion217,width=5)
    VArregloPos217.grid(row=6,column=24,sticky=NSEW)
    VPosicion218=StringVar()
    VArregloPos218=Entry(Frame4,textvariable=VPosicion218,width=5)
    VArregloPos218.grid(row=6,column=25,sticky=NSEW)
    VPosicion219=StringVar()
    VArregloPos219=Entry(Frame4,textvariable=VPosicion219,width=5)
    VArregloPos219.grid(row=6,column=26,sticky=NSEW)
    VPosicion220=StringVar()
    VArregloPos220=Entry(Frame4,textvariable=VPosicion220,width=5)
    VArregloPos220.grid(row=6,column=27,sticky=NSEW)
    VPosicion221=StringVar()
    VArregloPos221=Entry(Frame4,textvariable=VPosicion221,width=5)
    VArregloPos221.grid(row=6,column=28,sticky=NSEW)
    VPosicion222=StringVar()
    VArregloPos222=Entry(Frame4,textvariable=VPosicion222,width=5)
    VArregloPos222.grid(row=6,column=29,sticky=NSEW)
    VPosicion223=StringVar()
    VArregloPos223=Entry(Frame4,textvariable=VPosicion223,width=5)
    VArregloPos223.grid(row=6,column=30,sticky=NSEW)
    VPosicion224=StringVar()
    VArregloPos224=Entry(Frame4,textvariable=VPosicion224,width=5)
    VArregloPos224.grid(row=6,column=31,sticky=NSEW)

    #ArregloMatrizFila8
    VPosicion225=StringVar()
    VArregloPos225=Entry(Frame4,textvariable=VPosicion225,width=5)
    VArregloPos225.grid(row=7,column=0,sticky=NSEW)
    VPosicion225.set("Fp16")
    VPosicion226=StringVar()
    VArregloPos226=Entry(Frame4,textvariable=VPosicion226,width=5)
    VArregloPos226.grid(row=7,column=1,sticky=NSEW)
    VPosicion227=StringVar()
    VArregloPos227=Entry(Frame4,textvariable=VPosicion227,width=5)
    VArregloPos227.grid(row=7,column=2,sticky=NSEW)
    VPosicion228=StringVar()
    VArregloPos228=Entry(Frame4,textvariable=VPosicion228,width=5)
    VArregloPos228.grid(row=7,column=3,sticky=NSEW)
    VPosicion229=StringVar()
    VArregloPos229=Entry(Frame4,textvariable=VPosicion229,width=5)
    VArregloPos229.grid(row=7,column=4,sticky=NSEW)
    VPosicion230=StringVar()
    VArregloPos230=Entry(Frame4,textvariable=VPosicion230,width=5)
    VArregloPos230.grid(row=7,column=5,sticky=NSEW)
    VPosicion231=StringVar()
    VArregloPos231=Entry(Frame4,textvariable=VPosicion231,width=5)
    VArregloPos231.grid(row=7,column=6,sticky=NSEW)
    VPosicion232=StringVar()
    VArregloPos232=Entry(Frame4,textvariable=VPosicion232,width=5)
    VArregloPos232.grid(row=7,column=7,sticky=NSEW)
    VPosicion233=StringVar()
    VArregloPos233=Entry(Frame4,textvariable=VPosicion233,width=5)
    VArregloPos233.grid(row=7,column=8,sticky=NSEW)
    VPosicion234=StringVar()
    VArregloPos234=Entry(Frame4,textvariable=VPosicion234,width=5)
    VArregloPos234.grid(row=7,column=9,sticky=NSEW)
    VPosicion235=StringVar()
    VArregloPos235=Entry(Frame4,textvariable=VPosicion235,width=5)
    VArregloPos235.grid(row=7,column=10,sticky=NSEW)
    VPosicion236=StringVar()
    VArregloPos236=Entry(Frame4,textvariable=VPosicion236,width=5)
    VArregloPos236.grid(row=7,column=11,sticky=NSEW)
    VPosicion237=StringVar()
    VArregloPos237=Entry(Frame4,textvariable=VPosicion237,width=5)
    VArregloPos237.grid(row=7,column=12,sticky=NSEW)
    VPosicion238=StringVar()
    VArregloPos238=Entry(Frame4,textvariable=VPosicion238,width=5)
    VArregloPos238.grid(row=7,column=13,sticky=NSEW)
    VPosicion239=StringVar()
    VArregloPos239=Entry(Frame4,textvariable=VPosicion239,width=5)
    VArregloPos239.grid(row=7,column=14,sticky=NSEW)
    VPosicion240=StringVar()
    VArregloPos240=Entry(Frame4,textvariable=VPosicion240,width=5)
    VArregloPos240.grid(row=7,column=15,sticky=NSEW)
    VPosicion241=StringVar()
    VArregloPos241=Entry(Frame4,textvariable=VPosicion241,width=5)
    VArregloPos241.grid(row=7,column=16,sticky=NSEW)
    VPosicion242=StringVar()
    VArregloPos242=Entry(Frame4,textvariable=VPosicion242,width=5)
    VArregloPos242.grid(row=7,column=17,sticky=NSEW)
    VPosicion243=StringVar()
    VArregloPos243=Entry(Frame4,textvariable=VPosicion243,width=5)
    VArregloPos243.grid(row=7,column=18,sticky=NSEW)
    VPosicion244=StringVar()
    VArregloPos244=Entry(Frame4,textvariable=VPosicion244,width=5)
    VArregloPos244.grid(row=7,column=19,sticky=NSEW)
    VPosicion245=StringVar()
    VArregloPos245=Entry(Frame4,textvariable=VPosicion245,width=5)
    VArregloPos245.grid(row=7,column=20,sticky=NSEW)
    VPosicion246=StringVar()
    VArregloPos246=Entry(Frame4,textvariable=VPosicion246,width=5)
    VArregloPos246.grid(row=7,column=21,sticky=NSEW)
    VPosicion247=StringVar()
    VArregloPos247=Entry(Frame4,textvariable=VPosicion247,width=5)
    VArregloPos247.grid(row=7,column=22,sticky=NSEW)
    VPosicion248=StringVar()
    VArregloPos248=Entry(Frame4,textvariable=VPosicion248,width=5)
    VArregloPos248.grid(row=7,column=23,sticky=NSEW)
    VPosicion249=StringVar()
    VArregloPos249=Entry(Frame4,textvariable=VPosicion249,width=5)
    VArregloPos249.grid(row=7,column=24,sticky=NSEW)
    VPosicion250=StringVar()
    VArregloPos250=Entry(Frame4,textvariable=VPosicion250,width=5)
    VArregloPos250.grid(row=7,column=25,sticky=NSEW)
    VPosicion251=StringVar()
    VArregloPos251=Entry(Frame4,textvariable=VPosicion251,width=5)
    VArregloPos251.grid(row=7,column=26,sticky=NSEW)
    VPosicion252=StringVar()
    VArregloPos252=Entry(Frame4,textvariable=VPosicion252,width=5)
    VArregloPos252.grid(row=7,column=27,sticky=NSEW)
    VPosicion253=StringVar()
    VArregloPos253=Entry(Frame4,textvariable=VPosicion253,width=5)
    VArregloPos253.grid(row=7,column=28,sticky=NSEW)
    VPosicion254=StringVar()
    VArregloPos254=Entry(Frame4,textvariable=VPosicion254,width=5)
    VArregloPos254.grid(row=7,column=29,sticky=NSEW)
    VPosicion255=StringVar()
    VArregloPos255=Entry(Frame4,textvariable=VPosicion255,width=5)
    VArregloPos255.grid(row=7,column=30,sticky=NSEW)
    VPosicion256=StringVar()
    VArregloPos256=Entry(Frame4,textvariable=VPosicion256,width=5)
    VArregloPos256.grid(row=7,column=31,sticky=NSEW)

    BotonCalculo=Button(Frame5, text="Cálculo Hamming", command=lambda : Hamming())
    BotonCalculo.grid(row=0, column=0)
    BotonCheck=Button(Frame5, text="Check", command=lambda : check())
    BotonCheck.grid(row=0, column=1)
    TramaTotal=StringVar()
    MostrarTramaTotalMensaje=Label(Frame6, text=" ")
    MostrarTramaTotalMensaje.grid(row=0, column=0)
    MostrarTramaTotal=Label(Frame6, textvariable=TramaTotal, text=" ")
    MostrarTramaTotal.grid(row=0, column=1)
    LabelError=Label(Frame6, text=" ")
    LabelError.grid(row=0, column=2)
    BotonUNRZ=Button(Frame7, text="UNRZ", command=lambda : UNRZ())
    BotonUNRZ.grid(row=0, column=0)
    BotonAMI=Button(Frame7, text="AMI", command=lambda : AMI())
    BotonAMI.grid(row=0, column=1)
    BotonHDB3=Button(Frame7, text="HDB3", command=lambda : HDB3())
    BotonHDB3.grid(row=0, column=2)
    LabelCodificacionCanal=Label(Frame7, text=" ")
    LabelCodificacionCanal.grid(row=8, column=0)
    BotonVolver3=Button(Frame7, text="Regresar", command=Volver)
    BotonVolver3.grid(row=9, column=0) 
    VentanaCodificacionHamming.mainloop()

#Funcion Instrucciones
def Instrucciones():
    #Funcion Volver
    ventana.withdraw()

    def Volver():
        VentanaInstrucciones.destroy()
        ventana.deiconify()
    
    def InstruccionesHuffman():
        VentanaInstrucciones.destroy()
        class InstruccionesHuffman1:
            def __init__(self):
                self.ventana1=Toplevel()
                self.agregar_menu()
                self.scrolledtext1=scrolledtext.ScrolledText(self.ventana1, width=80, height=20)
                self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
                self.ventana1.mainloop()

            def agregar_menu(self):
                menubar1 = Menu(self.ventana1)
                self.ventana1.config(menu=menubar1)
                opciones1 = Menu(menubar1, tearoff=0)
                opciones1.add_command(label="Abrir Instrucciones", command=self.recuperar)
                opciones1.add_separator()
                opciones1.add_command(label="Volver", command=self.salir)
                menubar1.add_cascade(label="Archivo", menu=opciones1)  

            def salir(self):
                self.ventana1.destroy()
                Instrucciones()

            def recuperar(self):
                full_path = os.path.realpath(__file__)
                path, filename = os.path.split(full_path)
                nombrearch=(path+"\\InstruccionesHuffman.txt")
                if nombrearch!='':
                    archi1=open(nombrearch, "r", encoding="utf-8")
                    contenido=archi1.read()
                    archi1.close()
                    self.scrolledtext1.delete("1.0", END) 
                    self.scrolledtext1.insert("1.0", contenido)
        InstruccionesHuffman1()

    def InstruccionesShannonFano():
        VentanaInstrucciones.destroy()
        class InstruccionesShannonFano1:
            def __init__(self):
                self.ventana2=Toplevel()
                self.agregar_menu()
                self.scrolledtext1=scrolledtext.ScrolledText(self.ventana2, width=80, height=20)
                self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
                self.ventana2.mainloop()

            def agregar_menu(self):
                menubar1 = Menu(self.ventana2)
                self.ventana2.config(menu=menubar1)
                opciones1 = Menu(menubar1, tearoff=0)
                opciones1.add_command(label="Abrir Instrucciones", command=self.recuperar)
                opciones1.add_separator()
                opciones1.add_command(label="Volver", command=self.salir)
                menubar1.add_cascade(label="Archivo", menu=opciones1)  

            def salir(self):
                self.ventana2.destroy()
                Instrucciones()

            def recuperar(self):
                full_path = os.path.realpath(__file__)
                path, filename = os.path.split(full_path)
                nombrearch=(path+"\\InstruccionesShannonFano.txt")
                if nombrearch!='':
                    archi1=open(nombrearch, "r", encoding="utf-8")
                    contenido=archi1.read()
                    archi1.close()
                    self.scrolledtext1.delete("1.0", END) 
                    self.scrolledtext1.insert("1.0", contenido)
        InstruccionesShannonFano1()

    def InstruccionesAritmetica():
            VentanaInstrucciones.destroy()
            class InstruccionesAritmetica1:
                def __init__(self):
                    self.ventana3=Toplevel()
                    self.agregar_menu()
                    self.scrolledtext1=scrolledtext.ScrolledText(self.ventana3, width=80, height=20)
                    self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
                    self.ventana3.mainloop()

                def agregar_menu(self):
                    menubar1 = Menu(self.ventana3)
                    self.ventana3.config(menu=menubar1)
                    opciones1 = Menu(menubar1, tearoff=0)
                    opciones1.add_command(label="Abrir Instrucciones", command=self.recuperar)
                    opciones1.add_separator()
                    opciones1.add_command(label="Volver", command=self.salir)
                    menubar1.add_cascade(label="Archivo", menu=opciones1)  

                def salir(self):
                    self.ventana3.destroy()
                    Instrucciones()

                def recuperar(self):
                    full_path = os.path.realpath(__file__)
                    path, filename = os.path.split(full_path)
                    nombrearch=(path+"\\InstruccionesAritmetica.txt")
                    if nombrearch!='':
                        archi1=open(nombrearch, "r", encoding="utf-8")
                        contenido=archi1.read()
                        archi1.close()
                        self.scrolledtext1.delete("1.0", END) 
                        self.scrolledtext1.insert("1.0", contenido)
            InstruccionesAritmetica1()

    def InstruccionesModificada():
        VentanaInstrucciones.destroy()
        class InstruccionesAritmeticaModificada1:
            def __init__(self):
                self.ventana4=Toplevel()
                self.agregar_menu()
                self.scrolledtext1=scrolledtext.ScrolledText(self.ventana4, width=80, height=20)
                self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
                self.ventana4.mainloop()

            def agregar_menu(self):
                menubar1 = Menu(self.ventana4)
                self.ventana4.config(menu=menubar1)
                opciones1 = Menu(menubar1, tearoff=0)
                opciones1.add_command(label="Abrir Instrucciones", command=self.recuperar)
                opciones1.add_separator()
                opciones1.add_command(label="Volver", command=self.salir)
                menubar1.add_cascade(label="Archivo", menu=opciones1)  

            def salir(self):
                self.ventana4.destroy()
                Instrucciones()

            def recuperar(self):
                full_path = os.path.realpath(__file__)
                path, filename = os.path.split(full_path)
                nombrearch=(path+"\\InstruccionesAritmeticaModificada.txt")
                if nombrearch!='':
                    archi1=open(nombrearch, "r", encoding="utf-8")
                    contenido=archi1.read()
                    archi1.close()
                    self.scrolledtext1.delete("1.0", END) 
                    self.scrolledtext1.insert("1.0", contenido)
        InstruccionesAritmeticaModificada1()

    def InstruccionesDCPM():
        VentanaInstrucciones.destroy()
        class InstruccionesDCPM1:
            def __init__(self):
                self.ventana5=Toplevel()
                self.agregar_menu()
                self.scrolledtext1=scrolledtext.ScrolledText(self.ventana5, width=80, height=20)
                self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
                self.ventana5.mainloop()

            def agregar_menu(self):
                menubar1 = Menu(self.ventana5)
                self.ventana5.config(menu=menubar1)
                opciones1 = Menu(menubar1, tearoff=0)
                opciones1.add_command(label="Abrir Instrucciones", command=self.recuperar)
                opciones1.add_separator()
                opciones1.add_command(label="Volver", command=self.salir)
                menubar1.add_cascade(label="Archivo", menu=opciones1)  

            def salir(self):
                self.ventana5.destroy()
                Instrucciones()

            def recuperar(self):
                full_path = os.path.realpath(__file__)
                path, filename = os.path.split(full_path)
                nombrearch=(path+"\\InstruccionesDCPM.txt")
                if nombrearch!='':
                    archi1=open(nombrearch, "r", encoding="utf-8")
                    contenido=archi1.read()
                    archi1.close()
                    self.scrolledtext1.delete("1.0", END) 
                    self.scrolledtext1.insert("1.0", contenido)
        InstruccionesDCPM1()   

    def InstruccionesRLE():
        VentanaInstrucciones.destroy()
        class InstruccionesRLE1:
            def __init__(self):
                self.ventana6=Toplevel()
                self.agregar_menu()
                self.scrolledtext1=scrolledtext.ScrolledText(self.ventana6, width=80, height=20)
                self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
                self.ventana6.mainloop()

            def agregar_menu(self):
                menubar1 = Menu(self.ventana6)
                self.ventana6.config(menu=menubar1)
                opciones1 = Menu(menubar1, tearoff=0)
                opciones1.add_command(label="Abrir Instrucciones", command=self.recuperar)
                opciones1.add_separator()
                opciones1.add_command(label="Volver", command=self.salir)
                menubar1.add_cascade(label="Archivo", menu=opciones1)  

            def salir(self):
                self.ventana6.destroy()
                Instrucciones()

            def recuperar(self):
                full_path = os.path.realpath(__file__)
                path, filename = os.path.split(full_path)
                nombrearch=(path+"\\InstruccionesRLE.txt")
                if nombrearch!='':
                    archi1=open(nombrearch, "r", encoding="utf-8")
                    contenido=archi1.read()
                    archi1.close()
                    self.scrolledtext1.delete("1.0", END) 
                    self.scrolledtext1.insert("1.0", contenido)
        InstruccionesRLE1()

    def InstruccionesHamming():
        VentanaInstrucciones.destroy()
        class InstruccionesHamming1:
            def __init__(self):
                self.ventana7=Toplevel()
                self.agregar_menu()
                self.scrolledtext1=scrolledtext.ScrolledText(self.ventana7, width=80, height=20)
                self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
                self.ventana7.mainloop()

            def agregar_menu(self):
                menubar1 = Menu(self.ventana7)
                self.ventana7.config(menu=menubar1)
                opciones1 = Menu(menubar1, tearoff=0)
                opciones1.add_command(label="Abrir Instrucciones", command=self.recuperar)
                opciones1.add_separator()
                opciones1.add_command(label="Volver", command=self.salir)
                menubar1.add_cascade(label="Archivo", menu=opciones1)  

            def salir(self):
                self.ventana7.destroy()
                Instrucciones()

            def recuperar(self):
                full_path = os.path.realpath(__file__)
                path, filename = os.path.split(full_path)
                nombrearch=(path+"\\InstruccionesHamming.txt")
                if nombrearch!='':
                    archi1=open(nombrearch, "r", encoding="utf-8")
                    contenido=archi1.read()
                    archi1.close()
                    self.scrolledtext1.delete("1.0", END) 
                    self.scrolledtext1.insert("1.0", contenido)
        InstruccionesHamming1()

    VentanaInstrucciones=Toplevel()
    VentanaInstrucciones.title("Instrucciones")
    VentanaInstrucciones.geometry('715x225')    
    frame11 = Frame(VentanaInstrucciones, bg='black')
    frame21 = Frame(VentanaInstrucciones)
    frame11.grid(row=0, column=0, padx=(0, 0), pady=(0, 0))
    frame21.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
    TituloInterfaz1=Label(frame11, text="Instrucciones Codificaciones Sistemas De Teleco", bd=10, fg='black', font=("Helvetica", 24))
    TituloInterfaz1.grid(pady=(8, 8))
    BotonHuffman1=Button(frame21, text="Huffman", command=lambda : InstruccionesHuffman(), width=25)
    BotonHuffman1.grid(row=0, column=0)
    BotonShannonFano1=Button(frame21, text="Shannon Fano", command=lambda : InstruccionesShannonFano(), width=25)
    BotonShannonFano1.grid(row=1, column=0)
    BotonAritmetica1=Button(frame21, text="Aritmetica", command=lambda : InstruccionesAritmetica(), width=25)
    BotonAritmetica1.grid(row=2, column=0)
    BotonAritmeticaModificada1=Button(frame21, text="Aritmetica Modificada", command=lambda : InstruccionesModificada(), width=25)
    BotonAritmeticaModificada1.grid(row=3, column=0)
    BotonRLE1=Button(frame21, text="RLE", command=lambda : InstruccionesRLE(), width=25)
    BotonRLE1.grid(row=0, column=1)
    BotonDCPM1=Button(frame21, text="DCPM", command=lambda : InstruccionesDCPM(), width=25)
    BotonDCPM1.grid(row=1, column=1)
    BotonHamming1=Button(frame21, text="Hamming", command=lambda : InstruccionesHamming(), width=25)
    BotonHamming1.grid(row=2, column=1)
    BotonVolver1=Button(frame21, text="Regresar", command=lambda : Volver(), width=25)
    BotonVolver1.grid(row=3, column=1) 

#Creacion Ventana General
ventana=Tk()
ventana.title("Codificación")
ventana.geometry('516x225')
frame1 = Frame(ventana, bg='black')
frame2 = Frame(ventana)
frame1.grid(row=0, column=0, padx=(0, 0), pady=(0, 0))
frame2.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
TituloInterfaz=Label(frame1, text="Codificaciones Sistemas De Teleco", bd=10, fg='black', font=("Helvetica", 24))
TituloInterfaz.grid(pady=(8, 8))
BotonHuffman=Button(frame2, text="Huffman", command=lambda : CodificacionHuffman(), width=25)
BotonHuffman.grid(row=0, column=0)
BotonShannonFano=Button(frame2, text="Shannon Fano", command=lambda : CodificacionShannonFano(), width=25)
BotonShannonFano.grid(row=1, column=0)
BotonAritmetica=Button(frame2, text="Aritmetica", command=lambda : CodificacionAritmetica(), width=25)
BotonAritmetica.grid(row=2, column=0)
BotonAritmeticaModificada=Button(frame2, text="Aritmetica Modificada", command=lambda : CodificacionAritmeticaModificada(), width=25)
BotonAritmeticaModificada.grid(row=3, column=0)
BotonRLE=Button(frame2, text="RLE", command=lambda : CodificacionRLE(), width=25)
BotonRLE.grid(row=0, column=1)
BotonDCPM=Button(frame2, text="DCPM", command=lambda : CodificacionDCPM(), width=25)
BotonDCPM.grid(row=1, column=1)
BotonHamming=Button(frame2, text="Hamming", command=lambda : CodificacionHamming(), width=25)
BotonHamming.grid(row=2, column=1)
BotonInstrucciones=Button(frame2, text="Instrucciones", command=lambda : Instrucciones(), width=25)
BotonInstrucciones.grid(row=3, column=1)

ventana.mainloop()  