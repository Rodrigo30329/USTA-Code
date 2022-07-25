#Código Shannon-Fano  (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)

from collections import Counter
import operator
import math
from tkinter import *
from typing import TextIO

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
    LabelLongitudPromedio.configure(text=TextoLabelLongitudPromedio)
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

#Pedir Tipo de Ordenamiento
def PedirOpcion():
    print("Escoja su Ordenamientos")
    print("1 para ordenamiento de mayor a menor")
    print("2 para ordenamiento de menor a mayor")
    print("3 para ordenamiento alfabético a-z")
    print("4 para ordenamiento alfabético z-a")
    opcion=input("Ingrese su ordenamiento : ")
    return opcion

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
    palabra=PalabraUsuario.get()
    Shan={}
    print(palabra)
    while VerificarPalabra(palabra) == False:
        LabelPalabraUsuario.configure(text="Su palabra no es palindroma")     
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
    Entro=entropia(Frecuencias(PalabraUsuario.get()))
    TextoLabelEntropia=('La Entropia de', PalabraUsuario.get(), 'es:', Entro)
    LabelEntropia.configure(text=TextoLabelEntropia)
    LPromedio=LongitudPromedio(Frecuencias(PalabraUsuario.get()),FrecuenciasPalabra)
    TasaComp=TasaDeCompresion(LPromedio,palabra)
    TextoLabelTasaCompresion=('La tasa de compresion de ', PalabraUsuario.get() , 'es', TasaComp)
    LabelTasaDeCompresion.configure(text=TextoLabelTasaCompresion)
    TextoLabelLongitudPromedio=('La longitud promedio de',PalabraUsuario.get() ,'es', LPromedio)
    LabelLongitudPromedio.configure(text=TextoLabelLongitudPromedio)
    TextoLabelTramaTotal=("La trama total de", PalabraUsuario.get() ," es : " , Shan)
    LabelTramaTotal.configure(text=TextoLabelTramaTotal)

#Creación ventana
ventana=Tk()
ventana.title("Código Shannon Fano")
ventana.geometry('900x500')
TituloInterfaz=Label(ventana, text="Código Shannon Fano", bd=10, fg='black', font=("Helvetica", 16))
TituloInterfaz.grid(row=1, column=2)

PalabraUsuario=StringVar()
LabelPalabraUsuario=Label(ventana, text="Por favor ingrese un texto de entre palindromo de hasta 25 caracteres :")
LabelPalabraUsuario.grid(row=2, column=2)
EntradaUsuario=Entry(ventana, textvariable=PalabraUsuario, width=50)
EntradaUsuario.grid(row=3, column=2)

Espacio=Label(ventana)
Espacio.grid(row=5, column=2) 

LabelEntropia=Label(ventana, text=" ")
LabelEntropia.grid(row=6, column=2)

LabelLongitudPromedio=Label(ventana, text=" ")
LabelLongitudPromedio.grid(row=7, column=2)

LabelTasaDeCompresion=Label(ventana, text=" ")
LabelTasaDeCompresion.grid(row=9, column=2)

BotonTablaCodigoHuffman=Button(ventana, text="Mostrar Shannon Fano", width=25, command=ShannonFano)
BotonTablaCodigoHuffman.grid(row=11, column=2)
LabelTramaTotal=Label(ventana, text=" ")
LabelTramaTotal.grid(row=10,column=2)

ventana.mainloop()