#Codificación aritmetica modificada (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)
#Base 3, 6 y 9
#Entre 7 y 12 caracteres
from collections import Counter
import operator
import math
import re
from tkinter import *
from typing import TextIO

Alfabeto1="zap"
Alfabeto2="zapfet"
Alfabeto3="zapfetgud"

Numz=0
Numa=1
Nump=2
Numf=3
Nume=4
Numt=5
Numg=6
Numu=7
Numd=8

Base=3
Base2=6
Base3=9

mensaje1="zap"
mensaje2="zapafete"
mensaje3="zapafetegudu"


def AritmeticaModificada():
    Letras1=Alfabeto1
    Letras2=Alfabeto2
    Letras3=Alfabeto3

    Mensaje1=mensaje1.maketrans(Letras1,"012")
    men1=mensaje1.translate(Mensaje1)

    Mensaje2=mensaje2.maketrans(Letras2,"012345")
    men2=mensaje2.translate(Mensaje2)    

    Mensaje3=mensaje3.maketrans(Letras3,"012345678")
    men3=mensaje3.translate(Mensaje3)

    Entmen1=int(men1)
    Entmen2=int(men2)
    Entmen3=int(men3)

    len1=len(men1)
    len2=len(men2)
    len3=len(men3)

    Num1=float(Entmen1/(math.pow(10,(len1))))
    Num2=float(Entmen2/(math.pow(10,(len2))))
    Num3=float(Entmen3/(math.pow(10,(len3))))

    DigitosDComa1=len(str(Num1))
    DigitosDComa2=len(str(Num2))
    DigitosDComa3=len(str(Num3))

    L1=int(DigitosDComa1-2)
    L2=int(DigitosDComa2-2)
    L3=int(DigitosDComa3-2)

    print(men1)
    print(men2)
    print(men3)
    print(len1)
    print(len2)
    print(len3)
    print(Entmen1)
    print(Entmen2)
    print(Entmen3)
    print(Num1)
    print(Num2)
    print(Num3)
    print(DigitosDComa1)
    print(DigitosDComa2)
    print(DigitosDComa3)
    print(L1)
    print(L2)
    print(L3)

    Posiciones=[1,2,3,4,5,6,7,8,9,10,11,12] 
    Exponentes=[0,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
    ValoresPos=list()
    ValoresPos2=list()
    ValoresPos3=list()

    #ExponentesBase3
    i=2
    while i in range(len(Posiciones)):
        ValoresPos.append(math.pow(Posiciones[2],Exponentes[i]))  
        i=i+1
    print(ValoresPos)
    
    #ExponentesBase6
    i=2
    while i in range(len(Posiciones)):
        ValoresPos2.append(math.pow(Posiciones[5],Exponentes[i]))  
        i=i+1
    print(ValoresPos2)

    #ExponentesBase9
    i=2
    while i in range(len(Posiciones)):
        ValoresPos3.append(math.pow(Posiciones[8],Exponentes[i]))  
        i=i+1
    print(ValoresPos3)

    #Base3 
    LetrasNum1 = str(men1)
    ListaNum1 = []
    for n in LetrasNum1:    
        n = int(n)    
        ListaNum1.append(n)      
    print(ListaNum1)
    VectorSuma = [x*y for x,y in zip(ValoresPos,ListaNum1)]
    print(VectorSuma)    
    DecimalNum1=sum(VectorSuma)
    print(DecimalNum1)

    #Base6 
    LetrasNum2 = str(men2)
    ListaNum2 = []
    for n in LetrasNum2:    
        n = int(n)    
        ListaNum2.append(n)      
    print(ListaNum2)
    VectorSuma2 = [x*y for x,y in zip(ValoresPos2,ListaNum2)]
    print(VectorSuma2)    
    DecimalNum2=sum(VectorSuma2)
    print(DecimalNum2)

    #Base9 
    LetrasNum3 = str(men3)
    ListaNum3 = []
    for n in LetrasNum3:    
        n = int(n)    
        ListaNum3.append(n)      
    print(ListaNum3)
    VectorSuma3 = [x*y for x,y in zip(ValoresPos3,ListaNum3)]
    print(VectorSuma3)    
    DecimalNum3=sum(VectorSuma3)
    print(DecimalNum3)

    #Conversion a Binario
    Num1Bin = DecimalNum1*2
    Num2Bin = DecimalNum2*2
    Num3Bin = DecimalNum3*2
    ArregloBinario1=list()
    ArregloBinario2=list()
    ArregloBinario3=list()
    ArregloTramaBinariaNum1=list()
    ArregloTramaBinariaNum2=list()
    ArregloTramaBinariaNum3=list()
    ArregloNoInt1=list()
    ArregloNoInt2=list()
    ArregloNoInt3=list()

    i=0
    while i < 36:
        EnteroNum1=int(Num1Bin)
        EnteroNum2=int(Num2Bin)
        EnteroNum3=int(Num3Bin)
        TramaBinariaNum1NoInt=(Num1Bin-int(Num1Bin))
        TramaBinariaNum2NoInt=(Num2Bin-int(Num2Bin))
        TramaBinariaNum3NoInt=(Num3Bin-int(Num3Bin))
        Num1Bin=TramaBinariaNum1NoInt*2
        Num2Bin=TramaBinariaNum2NoInt*2
        Num3Bin=TramaBinariaNum3NoInt*2
        ArregloBinario1.append(Num1Bin)
        ArregloBinario2.append(Num2Bin)
        ArregloBinario3.append(Num3Bin)
        ArregloTramaBinariaNum1.append(EnteroNum1)
        ArregloTramaBinariaNum2.append(EnteroNum2)
        ArregloTramaBinariaNum3.append(EnteroNum3)        
        ArregloNoInt1.append(TramaBinariaNum1NoInt)
        ArregloNoInt2.append(TramaBinariaNum2NoInt)
        ArregloNoInt3.append(TramaBinariaNum3NoInt)       
        i=i+1
    print(ArregloBinario1)
    print(ArregloBinario2)
    print(ArregloBinario3)
    print(ArregloTramaBinariaNum1)
    print(ArregloTramaBinariaNum2)
    print(ArregloTramaBinariaNum3)     

    LongitudNum1=L1
    print(LongitudNum1)
    AproxNum1Inicio=round(DecimalNum1,LongitudNum1)
    print(AproxNum1Inicio)
    exponente=0
    cont1=0
    contbin=0
    Suma1Bin=0
    ArregloAproximados=list()
    BinarioAprox=list()
    for i in ArregloTramaBinariaNum1:
        print(i)
        exponente=exponente-1  
        if contbin==0:
            BinarioAprox.append(i)      
        if i==1:
            bin1=math.pow(2,exponente)            
            Aproximados=bin1*i                
            ArregloAproximados.append(Aproximados)
            Suma1Bin=Suma1Bin+Aproximados
            cont1=cont1+1
            AproxNum1=round(Suma1Bin,LongitudNum1)        
            if(AproxNum1==AproxNum1Inicio):
                contbin=contbin+1            
    print(ArregloAproximados)
    print(Suma1Bin)
    print(AproxNum1)
    print(BinarioAprox)

    LongitudNum2=L2
    print(LongitudNum2)
    AproxNum2Inicio=round(DecimalNum2,LongitudNum2)
    print(AproxNum2Inicio)
    exponente2=0
    cont2=0
    contbin2=0
    Suma2Bin=0
    ArregloAproximados2=list()
    BinarioAprox2=list()
    for i in ArregloTramaBinariaNum2:
        print(i)
        exponente2=exponente2-1  
        if contbin2==0:
            BinarioAprox2.append(i)      
        if i==1:
            bin2=math.pow(2,exponente2)            
            Aproximados2=bin2*i                
            ArregloAproximados2.append(Aproximados2)
            Suma2Bin=Suma2Bin+Aproximados2
            cont2=cont2+1
            AproxNum2=round(Suma2Bin,LongitudNum2)        
            if(AproxNum2==AproxNum2Inicio):
                contbin2=contbin2+1
    print(ArregloAproximados2)
    print(Suma2Bin)
    print(AproxNum2)
    print(BinarioAprox2)

    LongitudNum3=L3
    print(LongitudNum3)
    AproxNum3Inicio=round(DecimalNum3,LongitudNum3)
    print(AproxNum3Inicio)
    exponente3=0
    cont3=0
    contbin3=0
    Suma3Bin=0
    ArregloAproximados3=list()
    BinarioAprox3=list()
    for i in ArregloTramaBinariaNum3:
        print(i)
        exponente3=exponente3-1  
        if contbin3==0:
            BinarioAprox3.append(i)      
        if i==1:
            bin3=math.pow(2,exponente3)            
            Aproximados3=bin3*i                
            ArregloAproximados3.append(Aproximados3)
            Suma3Bin=Suma3Bin+Aproximados3
            cont3=cont3+1
            AproxNum3=round(Suma3Bin,LongitudNum3)        
            if(AproxNum3==AproxNum3Inicio):
                contbin3=contbin3+1
    print(ArregloAproximados3)
    print(Suma3Bin)
    print(AproxNum3)
    print(BinarioAprox3)

AritmeticaModificada()