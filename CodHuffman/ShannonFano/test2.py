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

    Alfabeto1="zap"
    Alfabeto2="zapfet"
    Alfabeto3="zapfetgud"
    
    Letras1=Alfabeto1
    Letras2=Alfabeto2
    Letras3=Alfabeto3

    Posiciones=[1,2,3,4,5,6,7,8,9,10,11,12] 
    Exponentes=[0,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10] 

    if validacion==0:
        LabelError.configure(text=" Su palabra no es valida para la base pedida ")

    #Proceso Base3
    elif validacion==1:
        mensaje1=PalabraUsuario.get()
        Mensaje1=mensaje1.maketrans(Letras1,"012")
        men1=mensaje1.translate(Mensaje1)
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

        #Conversion Binario
        Num1Bin = DecimalNum1*2
        ArregloBinario1=list()
        ArregloTramaBinariaNum1=list()
        ArregloNoInt1=list()
        i=0
        while i < 36:
            EnteroNum1=int(Num1Bin)
            TramaBinariaNum1NoInt=(Num1Bin-int(Num1Bin))
            Num1Bin=TramaBinariaNum1NoInt*2
            ArregloBinario1.append(Num1Bin)
            ArregloTramaBinariaNum1.append(EnteroNum1)
            ArregloNoInt1.append(TramaBinariaNum1NoInt)
            i=i+1
        LongitudNum1=L1        
        AproxNum1Inicio=round(DecimalNum1,LongitudNum1)
        exponente=0
        cont1=0
        contbin=0
        Suma1Bin=0
        Minval1=0
        ArregloAproximados=list()
        BinarioAprox=list()
        for i in ArregloTramaBinariaNum1:
            exponente=exponente-1  
            if contbin==0:
                BinarioAprox.append(i)   
                Minval1=Minval1+1   
            if i==1:
                bin1=math.pow(2,exponente)            
                Aproximados=bin1*i                
                ArregloAproximados.append(Aproximados)
                Suma1Bin=Suma1Bin+Aproximados
                cont1=cont1+1 
                AproxNum1=round(Suma1Bin,LongitudNum1)
                ArregloAprox1=ArregloAproximados      
                if(AproxNum1==AproxNum1Inicio):
                    contbin=contbin+1
        A=ArregloAprox1.pop(-1)   
        TextoLabelMostrarValorMinimoCodificar1=("El valor en que se aproxima su palabra es :", A)    
        LabelMostrarValorMinimoCodificar.configure(text=TextoLabelMostrarValorMinimoCodificar1)
        TextoLabelMostrarTramaBinariaReducida1=("El numero binario de su palabra es :", BinarioAprox)
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
        TextoLabelMostrarValorBase6=("El valor de su palabra en base 6 es :",DecimalNum2)
        LabelMostrarValorBase.configure(text=TextoLabelMostrarValorBase6)

        #Conversion Binario
        Num2Bin = DecimalNum2*2
        ArregloBinario2=list()   
        ArregloTramaBinariaNum2=list()
        ArregloNoInt2=list()
        i=0
        while i < 36:
            EnteroNum2=int(Num2Bin)
            TramaBinariaNum2NoInt=(Num2Bin-int(Num2Bin))
            Num2Bin=TramaBinariaNum2NoInt*2
            ArregloBinario2.append(Num2Bin)
            ArregloTramaBinariaNum2.append(EnteroNum2)
            ArregloNoInt2.append(TramaBinariaNum2NoInt)
            i=i+1
        LongitudNum2=L2
        AproxNum2Inicio=round(DecimalNum2,LongitudNum2)
        exponente2=0
        cont2=0
        contbin2=0
        Suma2Bin=0
        Minval2=0
        ArregloAproximados2=list()
        BinarioAprox2=list()
        for i in ArregloTramaBinariaNum2:
            exponente2=exponente2-1  
            if contbin2==0:
                BinarioAprox2.append(i) 
                Minval2=Minval2+1     
            if i==1:
                bin2=math.pow(2,exponente2)            
                Aproximados2=bin2*i                
                ArregloAproximados2.append(Aproximados2)
                Suma2Bin=Suma2Bin+Aproximados2
                cont2=cont2+1
                ArregloAprox2=ArregloAproximados2
                AproxNum2=round(Suma2Bin,LongitudNum2)        
                if(AproxNum2==AproxNum2Inicio):
                    contbin2=contbin2+1
        B=ArregloAprox2.pop(-1)   
        TextoLabelMostrarValorMinimoCodificar2=("El valor en que se aproxima su palabra es :", B)    
        LabelMostrarValorMinimoCodificar.configure(text=TextoLabelMostrarValorMinimoCodificar2)
        TextoLabelMostrarTramaBinariaReducida2=("El numero binario de su palabra es :", BinarioAprox2)
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

        #Conversion Binario
        Num3Bin = DecimalNum3*2
        ArregloBinario3=list()
        ArregloTramaBinariaNum3=list()
        ArregloNoInt3=list()
        i=0
        while i < 36: 
            EnteroNum3=int(Num3Bin)       
            TramaBinariaNum3NoInt=(Num3Bin-int(Num3Bin))       
            Num3Bin=TramaBinariaNum3NoInt*2        
            ArregloBinario3.append(Num3Bin)        
            ArregloTramaBinariaNum3.append(EnteroNum3)        
            ArregloNoInt3.append(TramaBinariaNum3NoInt)       
            i=i+1  
        LongitudNum3=L3
        AproxNum3Inicio=round(DecimalNum3,LongitudNum3)
        exponente3=0
        cont3=0
        contbin3=0
        Suma3Bin=0
        Minval3=0
        ArregloAproximados3=list()
        BinarioAprox3=list()
        for i in ArregloTramaBinariaNum3:
            exponente3=exponente3-1  
            if contbin3==0:
                BinarioAprox3.append(i)
                Minval3=Minval3+1       
            if i==1:
                bin3=math.pow(2,exponente3)            
                Aproximados3=bin3*i                
                ArregloAproximados3.append(Aproximados3)
                Suma3Bin=Suma3Bin+Aproximados3
                cont3=cont3+1
                ArregloAprox3=ArregloAproximados3
                AproxNum3=round(Suma3Bin,LongitudNum3)        
                if(AproxNum3==AproxNum3Inicio):
                    contbin3=contbin3+1
        C=ArregloAprox3.pop(-1)   
        TextoLabelMostrarValorMinimoCodificar3=("El valor en que se aproxima su palabra es :", C)    
        LabelMostrarValorMinimoCodificar.configure(text=TextoLabelMostrarValorMinimoCodificar3)
        TextoLabelMostrarTramaBinariaReducida3=("El numero binario de su palabra es :", BinarioAprox3)
        LabelMostrarTramaBinariaReducida.configure(text=TextoLabelMostrarTramaBinariaReducida3)

#Creación ventana
ventana=Tk()
ventana.title("Codificación Aritmetica Modificada")
ventana.geometry('1250x500')
TituloInterfaz=Label(ventana, text="Codificación Aritmetica Modificada", bd=10, fg='black', font=("Helvetica", 16))
TituloInterfaz.grid(row=1, column=2)

PalabraUsuario=StringVar()
LabelPalabraUsuario=Label(ventana, text="Por favor ingrese un texto de entre 7 y 12 caracteres usando el alfabeto mostrado para la base que desee:")
LabelPalabraUsuario.grid(row=2, column=2)
EntradaUsuario=Entry(ventana, textvariable=PalabraUsuario, width=50)
EntradaUsuario.grid(row=7, column=2)

AlfabetoBase3=Label(ventana, text=" Alfabeto para Base 3 : ")
AlfabetoBase3.grid(row=4, column=1)
LabelAlfabetoBase3=Label(ventana, text=" z,a,p ") 
LabelAlfabetoBase3.grid(row=4, column=2)

AlfabetoBase6=Label(ventana, text=" Alfabeto para Base 6 : ")
AlfabetoBase6.grid(row=5, column=1)
LabelAlfabetoBase6=Label(ventana, text=" z,a,p,f,e,t ") 
LabelAlfabetoBase6.grid(row=5, column=2)

AlfabetoBase9=Label(ventana, text=" Alfabeto para Base 9 : ")
AlfabetoBase9.grid(row=6, column=1)
LabelAlfabetoBase9=Label(ventana, text=" z,a,p,f,e,t,g,u,d ") 
LabelAlfabetoBase9.grid(row=6, column=2)

Espacio2=Label(ventana)
Espacio2.grid(row=11, column=2) 

LabelTramaBinariaReducida=Label(ventana, text=" La trama binaria de su palabra es : ")
LabelTramaBinariaReducida.grid(row=14,column=1)
LabelMostrarTramaBinariaReducida=Label(ventana, text=" ")
LabelMostrarTramaBinariaReducida.grid(row=14,column=2)

LabelValorBase=Label(ventana, text=" El valor de su palabra en la base escogida es : ")
LabelValorBase.grid(row=15,column=1)
LabelMostrarValorBase=Label(ventana, text=" ")
LabelMostrarValorBase.grid(row=15,column=2)

LabelValorMinimoCodificar=Label(ventana, text=" El valor usado para mostrar su palabra es : ")
LabelValorMinimoCodificar.grid(row=16,column=1)
LabelMostrarValorMinimoCodificar=Label(ventana, text=" ")
LabelMostrarValorMinimoCodificar.grid(row=16,column=2)

BotonTablaCodificacionAritmetica=Button(ventana, text="Mostrar Codificacion Aritmetica Modificada Base 3", width=40, command=lambda : AritmeticaModificada(Base3()))
BotonTablaCodificacionAritmetica.grid(row=20, column=2)
BotonTablaCodificacionAritmetica=Button(ventana, text="Mostrar Codificacion Aritmetica Modificada Base 6", width=40, command=lambda : AritmeticaModificada(Base6()))
BotonTablaCodificacionAritmetica.grid(row=21, column=2)
BotonTablaCodificacionAritmetica=Button(ventana, text="Mostrar Codificacion Aritmetica Modificada Base 9", width=40, command=lambda : AritmeticaModificada(Base9()))
BotonTablaCodificacionAritmetica.grid(row=22, column=2)

LabelError=Label(ventana, text=" ")
LabelError.grid(row=23, column=2)

ventana.mainloop()