#Código Aritmetica  (José Rodrigo Ávila, Valentina Hernández y Valeria Tavera)

import re
from tkinter import *
from typing import TextIO

#Funcion verificación palabra
def VerificarPalabra():
    a=1
    palabra=PalabraUsuario.get()
    len1=len(palabra)
    if(len1<5):
        LabelPalabraUsuario.configure(text="Su palabra es de menos de 5 caracteres")
        a=1
    elif(len1>10):
        LabelPalabraUsuario.configure(text="Su palabra es de más de 10 caracteres")
        a=1
    else:
        for i in range(len(palabra)):
            if(palabra[i]=="a" or palabra[i]=="s" or palabra[i]=="m" or palabra[i]=="e" or palabra[i]=="l"):            
                LabelPalabraUsuario.configure(text="Por favor ingrese un texto de entre 5 y 10 caracteres usando solo a, s, m, e y l:")
                a=0
            else:
                LabelPalabraUsuario.configure(text="Su palabra tiene caracteres no permitidos")
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
        LabelTramaTotal.configure(text="La palabra ingresada no es valida")
    elif(a==0):
        mensaje=PalabraUsuario.get()
        palabra=mensaje
        patron = r'(\w)'
        mensaje = re.sub(patron, r'\1 ', mensaje)
        mensaje = mensaje.lower() 
        listaPalabras = mensaje.split()
        frecuenciaPalabra = []
        for w in listaPalabras:
            frecuenciaPalabra.append(listaPalabras.count(w))   

        TextoLabelA=("Probabilidad a : ",ProbabilidadA.get())
        TextoLabelS=("Probabilidad s : ",ProbabilidadS.get())
        TextoLabelM=("Probabilidad m : ",ProbabilidadM.get())
        TextoLabelE=("Probabilidad e : ",ProbabilidadE.get())
        TextoLabelL=("Probabilidad l : ",ProbabilidadL.get())
        LabelA.configure(text=TextoLabelA)
        LabelS.configure(text=TextoLabelS)
        LabelM.configure(text=TextoLabelM)
        LabelE.configure(text=TextoLabelE)
        LabelL.configure(text=TextoLabelL)        
    
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
        
        P1=float(ProbabilidadA.get())
        P2=float(ProbabilidadS.get())
        P3=float(ProbabilidadM.get())
        P4=float(ProbabilidadE.get())
        P5=float(ProbabilidadL.get())

        PT=P1+P2+P3+P4+P5
        b=1
        if(PT!=1):
            Espacio1.configure(text="la suma de las probabilidades no es de 1")
            b=1
        else:
            Espacio1.configure(text="La suma de las probabilidades es de 1")
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
            LabelTramaTotalCodificacion.configure(text=TextoLabelCodificacion)    
            TextoLabelCodificacion2=("Los maximos en la codificacion de su palabra son : ", CodificacionMax)
            LabelTramaTotalCodificacion2.configure(text=TextoLabelCodificacion2)  
            TextoLabelTramaTotal=("La decodificacion de su palabra es : ", ValoresDeco2)
            LabelTramaTotal.configure(text=TextoLabelTramaTotal)

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
            LabelMostrarBinario.configure(text=TextoLabelTramaBinaria)
        else:
            LabelTramaTotal.configure(text=" error ")
            LabelTramaTotalCodificacion.configure(text=" error ")
            LabelTramaTotalCodificacion2.configure(text=" error ")
            LabelMostrarBinario.configure(text=" error ")

#Creación ventana
ventana=Tk()
ventana.title("Codificación Aritmetica")
ventana.geometry('1250x500')
TituloInterfaz=Label(ventana, text="Codificación Aritmetica", bd=10, fg='black', font=("Helvetica", 16))
TituloInterfaz.grid(row=1, column=2)

PalabraUsuario=StringVar()
LabelPalabraUsuario=Label(ventana, text="Por favor ingrese un texto de entre 5 y 10 caracteres usando solo a, s, m, e y l:")
LabelPalabraUsuario.grid(row=2, column=2)
EntradaUsuario=Entry(ventana, textvariable=PalabraUsuario, width=50)
EntradaUsuario.grid(row=3, column=2)

Espacio=Label(ventana, text=" Ingrese las probabilidades en decimales para cada letra ")
Espacio.grid(row=4, column=2) 

Espacio1=Label(ventana, text=" la suma de las 5 probabilidades debe ser de 1 ")
Espacio1.grid(row=5, column=2)

ProbabilidadA=StringVar()
LabelA=Label(ventana, text=" Probabilidad a : ")
LabelA.grid(row=6, column=1)
EntradaUsuarioPA=Entry(ventana, textvariable=ProbabilidadA, width=10)
EntradaUsuarioPA.grid(row=6, column=2)

ProbabilidadS=StringVar()
LabelS=Label(ventana, text=" Probabilidad s : ")
LabelS.grid(row=7, column=1)
EntradaUsuarioPS=Entry(ventana, textvariable=ProbabilidadS, width=10)
EntradaUsuarioPS.grid(row=7, column=2)

ProbabilidadM=StringVar()
LabelM=Label(ventana, text=" Probabilidad m : ")
LabelM.grid(row=8, column=1)
EntradaUsuarioPM=Entry(ventana, textvariable=ProbabilidadM, width=10)
EntradaUsuarioPM.grid(row=8, column=2)

ProbabilidadE=StringVar()
LabelE=Label(ventana, text=" Probabilidad e : ")
LabelE.grid(row=9, column=1)
EntradaUsuarioPE=Entry(ventana, textvariable=ProbabilidadE, width=10)
EntradaUsuarioPE.grid(row=9, column=2)

ProbabilidadL=StringVar()
LabelL=Label(ventana, text=" Probabilidad l : ")
LabelL.grid(row=10, column=1)
EntradaUsuarioPL=Entry(ventana, textvariable=ProbabilidadL, width=10)
EntradaUsuarioPL.grid(row=10, column=2)

Espacio2=Label(ventana)
Espacio2.grid(row=11, column=2) 

LabelCodificacion=Label(ventana, text=" Codificacion Limites Minimos ")
LabelCodificacion.grid(row=13,column=1)
LabelTramaTotalCodificacion=Label(ventana, text=" ")
LabelTramaTotalCodificacion.grid(row=13,column=2)

LabelCodificacion2=Label(ventana, text=" Codificacion Limites Maximos ")
LabelCodificacion2.grid(row=14,column=1)
LabelTramaTotalCodificacion2=Label(ventana, text=" ")
LabelTramaTotalCodificacion2.grid(row=14,column=2)

LabelDecodificacion=Label(ventana, text=" Decodificacion ")
LabelDecodificacion.grid(row=15,column=1)
LabelTramaTotal=Label(ventana, text=" ")
LabelTramaTotal.grid(row=15,column=2)


LabelBinario=Label(ventana, text=" Codigo Binario ")
LabelBinario.grid(row=16,column=1)
LabelMostrarBinario=Label(ventana, text=" ")
LabelMostrarBinario.grid(row=16,column=2)


BotonTablaCodificacionAritmetica=Button(ventana, text="Mostrar Codificacion Aritmetica", width=25, command=lambda : Aritmetica())
BotonTablaCodificacionAritmetica.grid(row=12, column=2)

ventana.mainloop()