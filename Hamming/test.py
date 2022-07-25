#Funcion crear filas matriz

# i=1
# cont=0
# while i <= 8:
#     j=1   
#     print("#ArregloMatrizFila"+str(i))
#     while j <= 32:
#         cont=cont+1
#         print("VPosicion"+str(cont)+"=StringVar()")
#         print("VArregloPos"+str(cont)+"=Entry(Frame4,textvariable="+"VPosicion"+str(cont)+","+"width=5)")
#         print("VArregloPos"+str(cont)+"."+"grid(row="+str(i-1)+","+"column="+str(j-1)+",sticky=NSEW)")        
#         j=j+1
#     i=i+1

#Funcion Posiciones

# i=194
# j=0
# val=223
# while i <= val:
#     print("if(len(Fila5)>"+str(j)+"):")
#     print("    "+"Posicion"+str(i)+".set(Fila5["+str(j)+"])")
#     print("else:")
#     print("    "+"Posicion"+str(i)+".set(N)")
#     i=i+1
#     j=j+1


# i=226
# j=0
# val=255
# while i <= val:
#     print("if(len(DFila5)>"+str(j)+"):")
#     print("    "+"VPosicion"+str(i)+".set(DFila5["+str(j)+"])")
#     print("else:")
#     print("    "+"VPosicion"+str(i)+".set(N)")
#     i=i+1
#     j=j+1

from tkinter.constants import TRUE, WORD
import numpy as np
import math
import matplotlib.pyplot as plt


#Funcion UNRZ
def UNRZ():
    mensaje="01001100011011"
    Respuesta=list()
    i=0
    while i<len(mensaje):
        Respuesta.append(mensaje[i])
        i=i+1
    print(Respuesta)
UNRZ()

#Funcion AMI
def AMI():
    mensaje="01001100011011"
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
    print(Respuesta)
AMI()

#Funcion HDB3
def HDB3():
    mensaje="011000011000010000"
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
    print(Respuesta)
HDB3()

