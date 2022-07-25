import operator
import CalculosSecundarios

def contenedor(mensaje):
    caracteres=list(mensaje)
    diccionario={}
    for caracter in range(len(caracteres)):
        diccionario[mensaje[caracter]]=0
    return diccionario
        

def ordenador(mensaje):

    caracteres=list(mensaje)
    diccionario={}

    for posicion in range(len(caracteres)):

        repeticiones=0
        for caracter in range(len(caracteres)):
            if caracteres[posicion] == caracteres[caracter]:
                repeticiones=repeticiones+1
            else:
                repeticiones=repeticiones

        diccionario[caracteres[posicion]]=repeticiones
    
    diccionario=sorted(diccionario.items(),key=operator.itemgetter(1), reverse=True)

    print(diccionario,)

    return diccionario


def longitud(diccionario):

    resultado=0
    repeticiones=diccionario.values()

    for veces in range(len(repeticiones)):
       resultado=resultado+repeticiones(veces)

    return resultado

def encontrar_mitad(a_dict):
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


def codificacion (key_mitad,contenedor,diccionario):
    digito=0
    if len(diccionario)>1:
        for key in dict(diccionario):
            contenedor[key]=(str(contenedor[key])+str(digito))
            if key == key_mitad:
                digito=1    
    return contenedor

def partir_dict(diccionario,key_mitad):
    d1={}
    d2={}
    dictionary=dict(diccionario)
    selector=0
    for i in range(len(dictionary)):
        if str(list(dictionary.items())[i][0])==str(key_mitad):
            selector=i
        
    d1=dict(list(dictionary.items())[0:selector+1])
    d2=dict(list(dictionary.items())[selector+1:len(dictionary)])
        
    return [d1,d2]
   # for i in range(dictionary):

def ajuste(content):
    for key in content:
        content[key]=str(list(content[key])[1:len(list(content))])
    return content


def ejecutar():
    mensaje=input("Ingrese la serie de caracteres \n")
    while CalculosSecundarios.verificar_palindromo(mensaje) == False:
        print("PALABRA NO PALINDROMA INTENTE DE NUEVO")
        mensaje=input("Ingrese la serie de caracteres \n")
    mensaje_ordenado=ordenador(mensaje)
    print(mensaje_ordenado,"1")
    lista_padre=[dict(mensaje_ordenado)]
    print(lista_padre,"2")
    content=contenedor(mensaje)
    print(content,"3")
    
    i=0
    while len(lista_padre) < (len(mensaje)*3):
        lista_padre[i]=sorted(lista_padre[i].items(),key=operator.itemgetter(1), reverse=True)
        elemento_mitad=encontrar_mitad(lista_padre[i])
        content=codificacion(elemento_mitad,content,lista_padre[i])
        dividido=partir_dict(lista_padre[i],elemento_mitad)
        print(dividido,"director",content,"frequi")
        lista_padre.append(dict(dividido[0]))
        lista_padre.append(dict(dividido[1]))
        i=i+1
    print(ajuste(content))
    return ajuste(content)

ejecutar()