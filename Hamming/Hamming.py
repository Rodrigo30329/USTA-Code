#Codificación Hamming (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)

import tkinter
import numpy as np
import random
from tkinter import *
from typing import TextIO

def Hamming():
    #Mensaje="1001011010111010101011101"
    #Mensaje="100101101001"
    #Mensaje="100101101001100101101001"
    Mensaje="1001011010"
    #Mensaje="100101101010011101"
    
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
    check1=""
    check2=""
    check3=""
    check4=""
    check5=""
    Check=list

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
    while i < len(Mensaje):
        pos=i+1  
        if pos in Posiciones2N:
            par=par+1
            Paridad=("P"+str(par))
            Paridad2="P"
            ListaMensaje.insert(pos-1,Paridad2)
            ListaMensaje2.insert(pos-1,Paridad)
        i=i+1
    MensajeConParidad=MensajeConParidad.join(ListaMensaje)
    MensajeConParidadYDatos=MensajeConParidadYDatos.join(ListaMensaje2)
    print(ListaMensaje,"♥-♥")
    print(ListaMensaje2,"UwU")
    print(MensajeConParidad,"♥")
    print(MensajeConParidadYDatos,"U")
    print(len(ListaMensaje2))

    i=0
    while i<len(ListaMensaje2):
        if i%2==0:
            Fila1.append(ListaMensaje2[i])
        else:
            Fila1.append("-")
            cont=1    
        i=i+1

    i=0
    val=0
    cont=1
    while i<len(ListaMensaje2):
        if val<1:
            Fila2.append("-")
            val=val+1
        elif(val==1):
            Fila2.append(ListaMensaje2[i])  
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
    while i<len(ListaMensaje2):
        if val<4:
            Fila3.append("-")
            val=val+1
        elif(val==4):
            Fila3.append(ListaMensaje2[i])  
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

    i=0
    val=0
    cont=1
    while i<len(ListaMensaje2):
        if val<8:
            Fila4.append("-")
            val=val+1
        elif(val==8):
            Fila4.append(ListaMensaje2[i])  
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

    i=0
    val=0
    cont=1
    while i<len(ListaMensaje2):
        if val<16:
            Fila5.append("-")
            val=val+1
        elif(val==16):
            Fila5.append(ListaMensaje2[i])  
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

    print(DatosMenFila1)
    print(DatosMenFila2)
    print(DatosMenFila3)
    print(DatosMenFila4)
    print(DatosMenFila5)

    ParidadFila1=DatosMenFila1.count("1")
    ParidadFila2=DatosMenFila2.count("1")
    ParidadFila3=DatosMenFila3.count("1")
    ParidadFila4=DatosMenFila4.count("1")
    ParidadFila5=DatosMenFila5.count("1")

    print(ParidadFila1)
    print(ParidadFila2)
    print(ParidadFila3)
    print(ParidadFila4)
    print(ParidadFila5)
    
    if(len(DFila1)>0):
        if(ParidadFila1%2==0):
            DFila1[0]="0"
        else:
            DFila1[0]="1"
    if(len(DFila2)>=2):
        if(ParidadFila2%2==0):
            DFila2[1]="0"
        else:
            DFila2[1]="1"
    if(len(DFila3)>=4):
        if(ParidadFila3%2==0):
            DFila3[3]="0"
        else:
            DFila3[3]="1"
    if(len(DFila4)>=8):
        if(ParidadFila4%2==0):
            DFila4[7]="0"
        else:
            DFila4[7]="1"
    if(len(DFila5)>=15):
        if(ParidadFila5%2==0):
            DFila5[15]="0"
        else:
            DFila5[15]="1"
    
    DatosMenFila1="".join(DFila1)
    DatosMenFila2="".join(DFila2)
    DatosMenFila3="".join(DFila3)
    DatosMenFila4="".join(DFila4)
    DatosMenFila5="".join(DFila5)

    print(Mensaje)
    print(DatosMenFila1)
    print(DatosMenFila2)
    print(DatosMenFila3)
    print(DatosMenFila4)
    print(DatosMenFila5)

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
    print(TramaFinal)
    ListaTramaFinal.extend(DFila1[0])
    ListaTramaFinal.extend(Parte2)
    ListaTramaFinal.extend(Parte3)
    ListaTramaFinal.extend(Parte4)
    ListaTramaFinal.extend(Parte5)
    ListaTramaFinal.extend(DFila5[-1])
    print(ListaTramaFinal, len(ListaTramaFinal))

    if(len(DFila1)>0):
        if(TramaFinal[0]!=DFila1[0]):
            check1=1
        else:
            check1=0
    if(len(DFila2)>=2):
        if(TramaFinal[1]!=DFila2[1]):
            check2=1
        else:
            check2=0
    if(len(DFila3)>=4):
        if(TramaFinal[3]!=DFila3[3]):
            check3=1
        else:
            check3=0        
    if(len(DFila4)>=8):
        if(TramaFinal[7]!=DFila4[7]):
            check4=1
        else:
            check4=0
    if(len(DFila5)>=15):         
        if(TramaFinal[15]!=DFila5[15]):
            check5=1
        else:
            check5=0
    Check=[check1, check2, check3, check4, check5]
    print(Check)

Hamming()
