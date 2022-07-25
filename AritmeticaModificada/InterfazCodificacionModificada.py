#Codificación aritmetica modificada (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)
#Base 3, 6 y 9
#Entre 7 y 12 caracteres
from collections import Counter
import operator
import math
import re
from tkinter import *
from typing import TextIO

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
        TextoLabelMostrarTramaBinariaReducida3=("El numero binario de su palabra es :", BinarioFinal3)
        LabelMostrarTramaBinariaReducida.configure(text=TextoLabelMostrarTramaBinariaReducida3)

#Creación ventana
VentanaCodificacionAritmeticaModificada=Tk()
VentanaCodificacionAritmeticaModificada.title("Codificación Aritmetica Modificada")
VentanaCodificacionAritmeticaModificada.geometry('1250x500')
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

VentanaCodificacionAritmeticaModificada.mainloop()