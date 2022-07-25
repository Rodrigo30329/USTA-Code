#Código Shannon-Fano  (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)

from collections import Counter
import operator
import math

#"lanaanal"
#"casabienneibaasac"
#"caraarac"

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

#Funcion Hallar Entropia
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

#Encontrar longitud diccionario
def longitud(diccionario):
    resultado=0
    repeticiones=diccionario.values()
    for veces in range(len(repeticiones)):
       resultado=resultado+repeticiones(veces)
    return resultado

#Funcion Eficiencia
def eficiencia(entropias, longitudMinima):
    eficiencias = entropias / longitudMinima
    return eficiencias

#Funcion Tasa Compresion
def TasaDeCompresion(diccionario,longitudes):
    tasa = (math.log(len(diccionario),2))/longitudes
    return tasa

#Pedir Tipo de Ordenamiento
def PedirOpcion():
    opcion=1
    print("Escoja su Ordenamiento")
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

def ShannonFano():
    PalabraUsuario=input("Ingrese la serie de caracteres \n")
    while VerificarPalabra(PalabraUsuario) == False:
        print("PALABRA NO PALINDROMA INTENTE DE NUEVO")
        PalabraUsuario=input("Ingrese la serie de caracteres \n")     
    Ordenado=OrdenarFrecuenciasAparicion(PalabraUsuario)
    Directorio=[dict(Ordenado)] 
    FrecuenciasPalabra=DiccionarioPalabra(PalabraUsuario)  
    
    i=0
    while len(Directorio) < (len(PalabraUsuario)*3):
        Directorio[i]=sorted(Directorio[i].items(),key=operator.itemgetter(1), reverse=True)
        Mitad=ObtenerMitadFrecuencia(Directorio[i])
        FrecuenciasPalabra=Codificador(Mitad,FrecuenciasPalabra,Directorio[i])
        DirectorioDividido=PartirDiccionnario(Directorio[i],Mitad)
        Directorio.append(dict(DirectorioDividido[0]))
        Directorio.append(dict(DirectorioDividido[1]))
        i=i+1
    print(AjustarPalabra(FrecuenciasPalabra))
    return AjustarPalabra(FrecuenciasPalabra)
ShannonFano()