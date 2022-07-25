#Codificación RLE (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)

import tkinter
import numpy as np
import random
from tkinter import *
from typing import TextIO

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
    metodo=Tecnica.get()
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
        if metodo=="1":
            valorcito="1"+valorcito
        if metodo=="2":
            j=0
            bandera=""
            while j<NumbitsAnti:
                bandera="1"+bandera
                j=j+1
            ResultadoBits.append(bandera)
        ResultadoBits.append(valorcito)   
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
        if metodo=="1":
            Binario2="0"+str(Binario2)
        ResultadoBits.append(Binario2)
        i=i+1
    LongitudMatriz=len(ResultadoBits)
    NumBitsTotal=NumBitsTotal+NumBitsTotalVal
    NumbitsCompre=LongitudMatriz
    TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
    TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits)
    LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
    LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100   
    TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
    LabelMostrarTasaCompresion.configure(text=TextoCompresion) 
    if metodo=="3":
        NumBits=(len(str(Binario)))
        NumbitsCompre=NumBits+1
        NumBits2=(len(str(BinarioVal)))
        NumBitsTotal=0
        NumBitsTotalVal=0
        ResultadoBits2=list()
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
        ResultadoBits2.append(Anticipado)
        i=0
        while i< len(Grupos):
            valorcito=Valores[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumbitsAnti):
                valorcito=str(valorcito).zfill(NumbitsAnti)
            NumBitsTotalVal=NumBitsTotalVal+len(str(valorcito))
            ResultadoBits2.append(valorcito)  
            contadorant=contadorant+1 
            if(contadorant==NumbitsAnti):
                ResultadoBits2.append(Anticipado)
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
            if metodo=="1":
                Binario2="0"+str(Binario2)
            ResultadoBits2.append(Binario2)
            contadorant=contadorant+1
            if(contadorant==NumbitsAnti):
                ResultadoBits2.append(Anticipado)
                contadorant=0 
            i=i+1
    LongitudMatriz=len(ResultadoBits2)
    NumBitsTotal=NumBitsTotal+NumBitsTotalVal
    NumbitsCompre=LongitudMatriz
    TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
    TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits2)
    LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
    LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100   
    TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
    LabelMostrarTasaCompresion.configure(text=TextoCompresion)  

#Proceso Por Columnas
def AgruparLecturaColumnas(matriz):
    metodo=Tecnica.get()
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
        if metodo=="1":
            valorcito="1"+valorcito
        if metodo=="2":
            j=0
            bandera=""
            while j<NumbitsAnti:
                bandera="1"+bandera
                j=j+1
            ResultadoBits.append(bandera)
        ResultadoBits.append(valorcito)
        Decimal=Grupos[i]
        Binario2 = 0
        multiplicador2 = 1
        while Decimal != 0: 
            Binario2 = Binario2+ Decimal % 2 * multiplicador2
            Decimal //= 2 
            multiplicador2 *= 10 
        if(len(str(Binario2))<NumbitsAnti):
            Binario2=str(Binario2).zfill(NumbitsAnti)
        if metodo=="1":
            Binario2="0"+str(Binario2)
        NumBitsTotal=NumBitsTotal+len(str(Binario2))
        ResultadoBits.append(Binario2)
        i=i+1

    LongitudMatriz=len(ResultadoBits)
    NumBitsTotal=NumBitsTotal+NumBitsTotalVal
    NumbitsCompre=LongitudMatriz
    TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
    TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits)
    LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
    LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100 
    TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
    LabelMostrarTasaCompresion.configure(text=TextoCompresion)
    if metodo=="3":
        NumBits=(len(str(Binario)))
        NumbitsCompre=NumBits+1
        NumBits2=(len(str(BinarioVal)))
        NumBitsTotal=0
        NumBitsTotalVal=0
        ResultadoBits2=list()
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
        ResultadoBits2.append(Anticipado)

        i=0
        while i< len(Grupos):
            valorcito=Valores[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumbitsAnti):
                valorcito=str(valorcito).zfill(NumbitsAnti)
            NumBitsTotalVal=NumBitsTotalVal+len(str(valorcito))
            ResultadoBits2.append(valorcito)  
            contadorant=contadorant+1 
            if(contadorant==NumbitsAnti):
                ResultadoBits2.append(Anticipado)
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
            if metodo=="1":
                Binario2="0"+str(Binario2)
            ResultadoBits2.append(Binario2)
            contadorant=contadorant+1
            if(contadorant==NumbitsAnti):
                ResultadoBits2.append(Anticipado)
                contadorant=0 
            i=i+1
    LongitudMatriz=len(ResultadoBits2)
    NumBitsTotal=NumBitsTotal+NumBitsTotalVal
    NumbitsCompre=LongitudMatriz
    TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
    TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits2)
    LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
    LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100 
    TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
    LabelMostrarTasaCompresion.configure(text=TextoCompresion)  

#Proceso Por Zig Zag
def AgruparLecturaZigZag(matriz):
    metodo=Tecnica.get()
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
    while i< len(lista2):
        valorcito=lista3[i]
        valorcito=bin(int(valorcito))[2:]
        if(len(str(valorcito))<NumbitsAnti):
            valorcito=str(valorcito).zfill(NumbitsCompreVal)
        NumBitsTotalVal=NumBitsTotalVal+len(str(valorcito))
        if metodo=="1":
            valorcito="1"+valorcito
        if metodo=="2":
            j=0
            bandera=""
            while j<NumbitsAnti:
                bandera="1"+bandera
                j=j+1
            ResultadoBits.append(bandera)
        ResultadoBits.append(valorcito)
        Decimal=lista2[i]
        Binario2 = 0
        multiplicador2 = 1
        while Decimal != 0: 
            Binario2 = Binario2+ Decimal % 2 * multiplicador2
            Decimal //= 2 
            multiplicador2 *= 10 
        if(len(str(Binario2))<NumBits):
            Binario2=str(Binario2).zfill(NumBits)
        if metodo=="1":
            Binario2="0"+str(Binario2)
        NumBitsTotal=NumBitsTotal+len(str(Binario2))
        ResultadoBits.append(Binario2)
        i=i+1
    LongitudMatriz=len(ResultadoBits)
    NumBitsTotal=NumBitsTotal+NumBitsTotalVal
    NumbitsCompre=LongitudMatriz
    TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
    TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits)
    LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
    LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100 
    TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
    LabelMostrarTasaCompresion.configure(text=TextoCompresion)
    if metodo=="3":
        NumBits=(len(str(Binario)))
        NumbitsCompre=NumBits+1
        NumBits2=(len(str(BinarioVal)))
        NumBitsTotal=0
        NumBitsTotalVal=0
        ResultadoBits2=list()
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
        ResultadoBits2.append(Anticipado)
        i=0
        while i< len(lista2):
            valorcito=lista3[i]
            valorcito=bin(int(valorcito))[2:]
            if(len(str(valorcito))<NumbitsAnti):
                valorcito=str(valorcito).zfill(NumbitsAnti)
            NumBitsTotalVal=NumBitsTotalVal+len(str(valorcito))
            ResultadoBits2.append(valorcito)  
            contadorant=contadorant+1 
            if(contadorant==NumbitsAnti):
                ResultadoBits2.append(Anticipado)
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
            if metodo=="1":
                Binario2="0"+str(Binario2)
            ResultadoBits2.append(Binario2)
            contadorant=contadorant+1
            if(contadorant==NumbitsAnti):
                ResultadoBits2.append(Anticipado)
                contadorant=0 
            i=i+1
    LongitudMatriz=len(ResultadoBits2)
    NumBitsTotal=NumBitsTotal+NumBitsTotalVal
    NumbitsCompre=LongitudMatriz
    TextoNumeroBits=("El numero de bits sin comprimir es : ",NumBitsTotal)
    TextoTramaTotal=("La Trama total de la matriz es : ",ResultadoBits2)
    LabelMostrarCaracteresTotales.configure(text=TextoNumeroBits)
    LabelMostrarTramaTotal.configure(text=TextoTramaTotal)
    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100 
    TextoCompresion=("La tasa de compresion de la matriz es : ", Compresion)
    LabelMostrarTasaCompresion.configure(text=TextoCompresion) 

#Creación ventana
ventana=Tk()
ventana.title("Codificación RLE")
ventana.geometry('1500x600')
TituloInterfaz=Label(ventana, text="Codificación RLE", bd=10, fg='black', font=("Helvetica", 16))
TituloInterfaz.grid(row=0, column=0)

#Instrucciones
LabelInstrucciones=Label(ventana, text="Por favor ingrese sus valores en la matriz garantizando que siempre haya al menos 2 de cada uno juntos")
LabelInstrucciones.grid(row=1, column=0)
Espacio=Label(ventana,text="ingrese 1 para valores entre 1 y 0, 2 para valores entre 1 y 7 y 3 para valores entre 8 y 15 ")
Espacio.grid(row=2,column=0)
Intervalo=StringVar()
EntradaIntervalo=Entry(ventana,textvariable=Intervalo,width=20)
EntradaIntervalo.grid(row=3,column=0)

#ValoresMatrizfila1
Posicion1=StringVar()
ArregloPos1=Entry(ventana,textvariable=Posicion1,width=5)
ArregloPos1.grid(row=3,column=2,sticky=NSEW)
Posicion2=StringVar()
ArregloPos2=Entry(ventana,textvariable=Posicion2,width=5)
ArregloPos2.grid(row=3,column=3,sticky=NSEW)
Posicion3=StringVar()
ArregloPos3=Entry(ventana,textvariable=Posicion3,width=5)
ArregloPos3.grid(row=3,column=4,sticky=NSEW)
Posicion4=StringVar()
ArregloPos4=Entry(ventana,textvariable=Posicion4,width=5)
ArregloPos4.grid(row=3,column=5,sticky=NSEW)
Posicion5=StringVar()
ArregloPos5=Entry(ventana,textvariable=Posicion5,width=5)
ArregloPos5.grid(row=3,column=6,sticky=NSEW)
Posicion6=StringVar()
ArregloPos6=Entry(ventana,textvariable=Posicion6,width=5)
ArregloPos6.grid(row=3,column=7,sticky=NSEW)
Posicion7=StringVar()
ArregloPos7=Entry(ventana,textvariable=Posicion7,width=5)
ArregloPos7.grid(row=3,column=8,sticky=NSEW)
Posicion8=StringVar()
ArregloPos8=Entry(ventana,textvariable=Posicion8,width=5)
ArregloPos8.grid(row=3,column=9,sticky=NSEW)
Posicion9=StringVar()
ArregloPos9=Entry(ventana,textvariable=Posicion9,width=5)
ArregloPos9.grid(row=3,column=10,sticky=NSEW)
Posicion10=StringVar()
ArregloPos10=Entry(ventana,textvariable=Posicion10,width=5)
ArregloPos10.grid(row=3,column=11,sticky=NSEW)

#ValoresMatrizFila2
Posicion11=StringVar()
ArregloPos11=Entry(ventana,textvariable=Posicion11,width=5)
ArregloPos11.grid(row=4,column=2,sticky=NSEW)
Posicion12=StringVar()
ArregloPos12=Entry(ventana,textvariable=Posicion12,width=5)
ArregloPos12.grid(row=4,column=3,sticky=NSEW)
Posicion13=StringVar()
ArregloPos13=Entry(ventana,textvariable=Posicion13,width=5)
ArregloPos13.grid(row=4,column=4,sticky=NSEW)
Posicion14=StringVar()
ArregloPos14=Entry(ventana,textvariable=Posicion14,width=5)
ArregloPos14.grid(row=4,column=5,sticky=NSEW)
Posicion15=StringVar()
ArregloPos15=Entry(ventana,textvariable=Posicion15,width=5)
ArregloPos15.grid(row=4,column=6,sticky=NSEW)
Posicion16=StringVar()
ArregloPos16=Entry(ventana,textvariable=Posicion16,width=5)
ArregloPos16.grid(row=4,column=7,sticky=NSEW)
Posicion17=StringVar()
ArregloPos17=Entry(ventana,textvariable=Posicion17,width=5)
ArregloPos17.grid(row=4,column=8,sticky=NSEW)
Posicion18=StringVar()
ArregloPos18=Entry(ventana,textvariable=Posicion18,width=5)
ArregloPos18.grid(row=4,column=9,sticky=NSEW)
Posicion19=StringVar()
ArregloPos19=Entry(ventana,textvariable=Posicion19,width=5)
ArregloPos19.grid(row=4,column=10,sticky=NSEW)
Posicion20=StringVar()
ArregloPos20=Entry(ventana,textvariable=Posicion20,width=5)
ArregloPos20.grid(row=4,column=11,sticky=NSEW)

#ValoresMatrizFila3
Posicion21=StringVar()
ArregloPos21=Entry(ventana,textvariable=Posicion21,width=5)
ArregloPos21.grid(row=5,column=2,sticky=NSEW)
Posicion22=StringVar()
ArregloPos22=Entry(ventana,textvariable=Posicion22,width=5)
ArregloPos22.grid(row=5,column=3,sticky=NSEW)
Posicion23=StringVar()
ArregloPos23=Entry(ventana,textvariable=Posicion23,width=5)
ArregloPos23.grid(row=5,column=4,sticky=NSEW)
Posicion24=StringVar()
ArregloPos24=Entry(ventana,textvariable=Posicion24,width=5)
ArregloPos24.grid(row=5,column=5,sticky=NSEW)
Posicion25=StringVar()
ArregloPos25=Entry(ventana,textvariable=Posicion25,width=5)
ArregloPos25.grid(row=5,column=6,sticky=NSEW)
Posicion26=StringVar()
ArregloPos26=Entry(ventana,textvariable=Posicion26,width=5)
ArregloPos26.grid(row=5,column=7,sticky=NSEW)
Posicion27=StringVar()
ArregloPos27=Entry(ventana,textvariable=Posicion27,width=5)
ArregloPos27.grid(row=5,column=8,sticky=NSEW)
Posicion28=StringVar()
ArregloPos28=Entry(ventana,textvariable=Posicion28,width=5)
ArregloPos28.grid(row=5,column=9,sticky=NSEW)
Posicion29=StringVar()
ArregloPos29=Entry(ventana,textvariable=Posicion29,width=5)
ArregloPos29.grid(row=5,column=10,sticky=NSEW)
Posicion30=StringVar()
ArregloPos30=Entry(ventana,textvariable=Posicion30,width=5)
ArregloPos30.grid(row=5,column=11,sticky=NSEW)

#ArregloMatrizFila4
Posicion31=StringVar()
ArregloPos31=Entry(ventana,textvariable=Posicion31,width=5)
ArregloPos31.grid(row=6,column=2,sticky=NSEW)
Posicion32=StringVar()
ArregloPos32=Entry(ventana,textvariable=Posicion32,width=5)
ArregloPos32.grid(row=6,column=3,sticky=NSEW)
Posicion33=StringVar()
ArregloPos33=Entry(ventana,textvariable=Posicion33,width=5)
ArregloPos33.grid(row=6,column=4,sticky=NSEW)
Posicion34=StringVar()
ArregloPos34=Entry(ventana,textvariable=Posicion34,width=5)
ArregloPos34.grid(row=6,column=5,sticky=NSEW)
Posicion35=StringVar()
ArregloPos35=Entry(ventana,textvariable=Posicion35,width=5)
ArregloPos35.grid(row=6,column=6,sticky=NSEW)
Posicion36=StringVar()
ArregloPos36=Entry(ventana,textvariable=Posicion36,width=5)
ArregloPos36.grid(row=6,column=7,sticky=NSEW)
Posicion37=StringVar()
ArregloPos37=Entry(ventana,textvariable=Posicion37,width=5)
ArregloPos37.grid(row=6,column=8,sticky=NSEW)
Posicion38=StringVar()
ArregloPos38=Entry(ventana,textvariable=Posicion38,width=5)
ArregloPos38.grid(row=6,column=9,sticky=NSEW)
Posicion39=StringVar()
ArregloPos39=Entry(ventana,textvariable=Posicion39,width=5)
ArregloPos39.grid(row=6,column=10,sticky=NSEW)
Posicion40=StringVar()
ArregloPos40=Entry(ventana,textvariable=Posicion40,width=5)
ArregloPos40.grid(row=6,column=11,sticky=NSEW)

#ArregloMatrizFila5
Posicion41=StringVar()
ArregloPos41=Entry(ventana,textvariable=Posicion41,width=5)
ArregloPos41.grid(row=7,column=2,sticky=NSEW)
Posicion42=StringVar()
ArregloPos42=Entry(ventana,textvariable=Posicion42,width=5)
ArregloPos42.grid(row=7,column=3,sticky=NSEW)
Posicion43=StringVar()
ArregloPos43=Entry(ventana,textvariable=Posicion43,width=5)
ArregloPos43.grid(row=7,column=4,sticky=NSEW)
Posicion44=StringVar()
ArregloPos44=Entry(ventana,textvariable=Posicion44,width=5)
ArregloPos44.grid(row=7,column=5,sticky=NSEW)
Posicion45=StringVar()
ArregloPos45=Entry(ventana,textvariable=Posicion45,width=5)
ArregloPos45.grid(row=7,column=6,sticky=NSEW)
Posicion46=StringVar()
ArregloPos46=Entry(ventana,textvariable=Posicion46,width=5)
ArregloPos46.grid(row=7,column=7,sticky=NSEW)
Posicion47=StringVar()
ArregloPos47=Entry(ventana,textvariable=Posicion47,width=5)
ArregloPos47.grid(row=7,column=8,sticky=NSEW)
Posicion48=StringVar()
ArregloPos48=Entry(ventana,textvariable=Posicion48,width=5)
ArregloPos48.grid(row=7,column=9,sticky=NSEW)
Posicion49=StringVar()
ArregloPos49=Entry(ventana,textvariable=Posicion49,width=5)
ArregloPos49.grid(row=7,column=10,sticky=NSEW)
Posicion50=StringVar()
ArregloPos50=Entry(ventana,textvariable=Posicion50,width=5)
ArregloPos50.grid(row=7,column=11,sticky=NSEW)

#ArregloMatrizFila6
Posicion51=StringVar()
ArregloPos51=Entry(ventana,textvariable=Posicion51,width=5)
ArregloPos51.grid(row=8,column=2,sticky=NSEW)
Posicion52=StringVar()
ArregloPos52=Entry(ventana,textvariable=Posicion52,width=5)
ArregloPos52.grid(row=8,column=3,sticky=NSEW)
Posicion53=StringVar()
ArregloPos53=Entry(ventana,textvariable=Posicion53,width=5)
ArregloPos53.grid(row=8,column=4,sticky=NSEW)
Posicion54=StringVar()
ArregloPos54=Entry(ventana,textvariable=Posicion54,width=5)
ArregloPos54.grid(row=8,column=5,sticky=NSEW)
Posicion55=StringVar()
ArregloPos55=Entry(ventana,textvariable=Posicion55,width=5)
ArregloPos55.grid(row=8,column=6,sticky=NSEW)
Posicion56=StringVar()
ArregloPos56=Entry(ventana,textvariable=Posicion56,width=5)
ArregloPos56.grid(row=8,column=7,sticky=NSEW)
Posicion57=StringVar()
ArregloPos57=Entry(ventana,textvariable=Posicion57,width=5)
ArregloPos57.grid(row=8,column=8,sticky=NSEW)
Posicion58=StringVar()
ArregloPos58=Entry(ventana,textvariable=Posicion58,width=5)
ArregloPos58.grid(row=8,column=9,sticky=NSEW)
Posicion59=StringVar()
ArregloPos59=Entry(ventana,textvariable=Posicion59,width=5)
ArregloPos59.grid(row=8,column=10,sticky=NSEW)
Posicion60=StringVar()
ArregloPos60=Entry(ventana,textvariable=Posicion60,width=5)
ArregloPos60.grid(row=8,column=11,sticky=NSEW)

#MatrizArregloFila7
Posicion61=StringVar()
ArregloPos61=Entry(ventana,textvariable=Posicion61,width=5)
ArregloPos61.grid(row=9,column=2,sticky=NSEW)
Posicion62=StringVar()
ArregloPos62=Entry(ventana,textvariable=Posicion62,width=5)
ArregloPos62.grid(row=9,column=3,sticky=NSEW)
Posicion63=StringVar()
ArregloPos63=Entry(ventana,textvariable=Posicion63,width=5)
ArregloPos63.grid(row=9,column=4,sticky=NSEW)
Posicion64=StringVar()
ArregloPos64=Entry(ventana,textvariable=Posicion64,width=5)
ArregloPos64.grid(row=9,column=5,sticky=NSEW)
Posicion65=StringVar()
ArregloPos65=Entry(ventana,textvariable=Posicion65,width=5)
ArregloPos65.grid(row=9,column=6,sticky=NSEW)
Posicion66=StringVar()
ArregloPos66=Entry(ventana,textvariable=Posicion66,width=5)
ArregloPos66.grid(row=9,column=7,sticky=NSEW)
Posicion67=StringVar()
ArregloPos67=Entry(ventana,textvariable=Posicion67,width=5)
ArregloPos67.grid(row=9,column=8,sticky=NSEW)
Posicion68=StringVar()
ArregloPos68=Entry(ventana,textvariable=Posicion68,width=5)
ArregloPos68.grid(row=9,column=9,sticky=NSEW)
Posicion69=StringVar()
ArregloPos69=Entry(ventana,textvariable=Posicion69,width=5)
ArregloPos69.grid(row=9,column=10,sticky=NSEW)
Posicion70=StringVar()
ArregloPos70=Entry(ventana,textvariable=Posicion70,width=5)
ArregloPos70.grid(row=9,column=11,sticky=NSEW)

#ArregloMatrizFila8
Posicion71=StringVar()
ArregloPos71=Entry(ventana,textvariable=Posicion71,width=5)
ArregloPos71.grid(row=10,column=2,sticky=NSEW)
Posicion72=StringVar()
ArregloPos72=Entry(ventana,textvariable=Posicion72,width=5)
ArregloPos72.grid(row=10,column=3,sticky=NSEW)
Posicion73=StringVar()
ArregloPos73=Entry(ventana,textvariable=Posicion73,width=5)
ArregloPos73.grid(row=10,column=4,sticky=NSEW)
Posicion74=StringVar()
ArregloPos74=Entry(ventana,textvariable=Posicion74,width=5)
ArregloPos74.grid(row=10,column=5,sticky=NSEW)
Posicion75=StringVar()
ArregloPos75=Entry(ventana,textvariable=Posicion75,width=5)
ArregloPos75.grid(row=10,column=6,sticky=NSEW)
Posicion76=StringVar()
ArregloPos76=Entry(ventana,textvariable=Posicion76,width=5)
ArregloPos76.grid(row=10,column=7,sticky=NSEW)
Posicion77=StringVar()
ArregloPos77=Entry(ventana,textvariable=Posicion77,width=5)
ArregloPos77.grid(row=10,column=8,sticky=NSEW)
Posicion78=StringVar()
ArregloPos78=Entry(ventana,textvariable=Posicion78,width=5)
ArregloPos78.grid(row=10,column=9,sticky=NSEW)
Posicion79=StringVar()
ArregloPos79=Entry(ventana,textvariable=Posicion79,width=5)
ArregloPos79.grid(row=10,column=10,sticky=NSEW)
Posicion80=StringVar()
ArregloPos80=Entry(ventana,textvariable=Posicion80,width=5)
ArregloPos80.grid(row=10,column=11,sticky=NSEW)

#ArregloMatrizFila9
Posicion81=StringVar()
ArregloPos81=Entry(ventana,textvariable=Posicion81,width=5)
ArregloPos81.grid(row=11,column=2,sticky=NSEW)
Posicion82=StringVar()
ArregloPos82=Entry(ventana,textvariable=Posicion82,width=5)
ArregloPos82.grid(row=11,column=3,sticky=NSEW)
Posicion83=StringVar()
ArregloPos83=Entry(ventana,textvariable=Posicion83,width=5)
ArregloPos83.grid(row=11,column=4,sticky=NSEW)
Posicion84=StringVar()
ArregloPos84=Entry(ventana,textvariable=Posicion84,width=5)
ArregloPos84.grid(row=11,column=5,sticky=NSEW)
Posicion85=StringVar()
ArregloPos85=Entry(ventana,textvariable=Posicion85,width=5)
ArregloPos85.grid(row=11,column=6,sticky=NSEW)
Posicion86=StringVar()
ArregloPos86=Entry(ventana,textvariable=Posicion86,width=5)
ArregloPos86.grid(row=11,column=7,sticky=NSEW)
Posicion87=StringVar()
ArregloPos87=Entry(ventana,textvariable=Posicion87,width=5)
ArregloPos87.grid(row=11,column=8,sticky=NSEW)
Posicion88=StringVar()
ArregloPos88=Entry(ventana,textvariable=Posicion88,width=5)
ArregloPos88.grid(row=11,column=9,sticky=NSEW)
Posicion89=StringVar()
ArregloPos89=Entry(ventana,textvariable=Posicion89,width=5)
ArregloPos89.grid(row=11,column=10,sticky=NSEW)
Posicion90=StringVar()
ArregloPos90=Entry(ventana,textvariable=Posicion90,width=5)
ArregloPos90.grid(row=11,column=11,sticky=NSEW)

#ArregloMatrizFila10
Posicion91=StringVar()
ArregloPos91=Entry(ventana,textvariable=Posicion91,width=5)
ArregloPos91.grid(row=12,column=2,sticky=NSEW)
Posicion92=StringVar()
ArregloPos92=Entry(ventana,textvariable=Posicion92,width=5)
ArregloPos92.grid(row=12,column=3,sticky=NSEW)
Posicion93=StringVar()
ArregloPos93=Entry(ventana,textvariable=Posicion93,width=5)
ArregloPos93.grid(row=12,column=4,sticky=NSEW)
Posicion94=StringVar()
ArregloPos94=Entry(ventana,textvariable=Posicion94,width=5)
ArregloPos94.grid(row=12,column=5,sticky=NSEW)
Posicion95=StringVar()
ArregloPos95=Entry(ventana,textvariable=Posicion95,width=5)
ArregloPos95.grid(row=12,column=6,sticky=NSEW)
Posicion96=StringVar()
ArregloPos96=Entry(ventana,textvariable=Posicion96,width=5)
ArregloPos96.grid(row=12,column=7,sticky=NSEW)
Posicion97=StringVar()
ArregloPos97=Entry(ventana,textvariable=Posicion97,width=5)
ArregloPos97.grid(row=12,column=8,sticky=NSEW)
Posicion98=StringVar()
ArregloPos98=Entry(ventana,textvariable=Posicion98,width=5)
ArregloPos98.grid(row=12,column=9,sticky=NSEW)
Posicion99=StringVar()
ArregloPos99=Entry(ventana,textvariable=Posicion99,width=5)
ArregloPos99.grid(row=12,column=10,sticky=NSEW)
Posicion100=StringVar()
ArregloPos100=Entry(ventana,textvariable=Posicion100,width=5)
ArregloPos100.grid(row=12,column=11,sticky=NSEW)

LabelMostrarGrupos=Label(ventana, text=" ")
LabelMostrarGrupos.grid(row=4,column=0)
LabelMostrarValores=Label(ventana, text=" ")
LabelMostrarValores.grid(row=5,column=0)
LabelMostrarMayorGrupo=Label(ventana, text=" ")
LabelMostrarMayorGrupo.grid(row=6,column=0)
LabelMostrarCaracteresTotales=Label(ventana, text=" ")
LabelMostrarCaracteresTotales.grid(row=7,column=0)
LabelMostrarTasaCompresion=Label(ventana, text=" ")
LabelMostrarTasaCompresion.grid(row=8,column=0)
LabelMostrarTramaTotal=Label(ventana, text=" ")
LabelMostrarTramaTotal.grid(row=15,column=0,columnspan=20)

Boton=Button(ventana, text="Iniciar Filas", command=lambda : RandomArregloFilas())
Boton.grid(row=9, column=0)
Boton2=Button(ventana, text="Iniciar Columnas", command=lambda : RandomArregloColumnas())
Boton2.grid(row=10, column=0)
Boton3=Button(ventana, text="Iniciar Zig Zag", command=lambda : RandomArregloZigZag())
Boton3.grid(row=11,column=0)
BotonCalculo=Button(ventana, text="Calculo Por Filas", command=lambda : AgruparLecturaFilas(CrearMatriz()))
BotonCalculo.grid(row=12, column=0)
BotonCalculo2=Button(ventana, text="Calculo Por Columnas", command=lambda : AgruparLecturaColumnas(CrearMatriz()))
BotonCalculo2.grid(row=13, column=0)
BotonCalculo3=Button(ventana, text="Calculo Por Zig Zag", command=lambda : AgruparLecturaZigZag(CrearMatriz()))
BotonCalculo3.grid(row=14,column=0)
EntryTecnica=Entry(ventana)

Tecninstruccion=Label(ventana,text="ingrese 1 para bit bandera, 2 para byte bandera y 3 para byte anticipado")
Tecninstruccion.grid(row=18,column=0)
Tecnica=StringVar()
EntradaTecnicas=Entry(ventana,textvariable=Tecnica,width=20)
EntradaTecnicas.grid(row=19,column=0)

LabelError=Label(ventana, text=" Se sugire usar ordenamiento por filas ")
LabelError.grid(row=20, column=0)

ventana.mainloop()