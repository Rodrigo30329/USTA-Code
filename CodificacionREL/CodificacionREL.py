
import numpy as np

L1=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
L2=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
L3=[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
L4=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
L5=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
L6=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
L7=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
L8=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
L9=[1, 0, 0, 0, 0, 0, 0, 1, 1, 1]
L10=[0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

matriz=np.array([
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]])

print(matriz[0,1])
print(matriz)

def AgruparLecturaZigZag(matriz):
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
    print(lista)
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
    print(lista2)
    print(lista3)
    Maximo = None
    for pos, num in enumerate(lista2):
        if(Maximo is None or num > Maximo):
            Maximo=num
            Indice=pos
    print(Maximo, "en", Indice)

    Binario = 0
    multiplicador = 1

    while Maximo != 0: 
        Binario = Binario + Maximo % 2 * multiplicador
        Maximo //= 2 
        multiplicador *= 10 
    print(Binario)

    NumBits=(len(str(Binario)))
    NumbitsCompre=NumBits+1
    print(NumBits)
    print(NumbitsCompre)

    NumBitsTotal=0
    ResultadoBits=list()
    i=0
    while i< len(lista2):
        valorcito=lista3[i]
        print(valorcito)
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
        print(Binario2)
        NumBitsTotal=NumBitsTotal+len(str(Binario2))
        ResultadoBits.append(Binario2)
        i=i+1
    NumBitsTotal=NumBitsTotal+len(lista3)
    print(NumBitsTotal)
    print(ResultadoBits) 

    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100   
    print(Compresion)

AgruparLecturaZigZag(matriz)

def AgruparLecturaFilas():
    Grupos=list()
    Valores=list()
    cont=0
    i=0
    while i < 10:
        j=0
        while j < 10:
            Pos1=matriz[i,j]
            if(j!=9):            
                Pos2=matriz[i,j+1]
            else:
                Pos2=2
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
    SumaRepeticiones=sum(Grupos)
    print(Grupos)
    print(Valores)
    print(SumaRepeticiones)

    Maximo = None
    for pos, num in enumerate(Grupos):
        if(Maximo is None or num > Maximo):
            Maximo=num
            Indice=pos
    print(Maximo, "en", Indice)

    Binario = 0
    multiplicador = 1

    while Maximo != 0: 
        Binario = Binario + Maximo % 2 * multiplicador
        Maximo //= 2 
        multiplicador *= 10 
    print(Binario)

    NumBits=(len(str(Binario)))
    NumbitsCompre=NumBits+1
    print(NumBits)
    print(NumbitsCompre)

    NumBitsTotal=0
    ResultadoBits=list()
    i=0
    while i< len(Grupos):
        valorcito=Valores[i]
        print(valorcito)
        ResultadoBits.append(valorcito)
        Decimal=Grupos[i]
        Binario2 = 0
        multiplicador2 = 1
        while Decimal != 0: 
            Binario2 = Binario2+ Decimal % 2 * multiplicador2
            Decimal //= 2 
            multiplicador2 *= 10 
        if(len(str(Binario2))<NumBits):
            Binario2=str(Binario2).zfill(NumBits)
        print(Binario2)
        NumBitsTotal=NumBitsTotal+len(str(Binario2))
        ResultadoBits.append(Binario2)
        i=i+1
    NumBitsTotal=NumBitsTotal+len(Valores)
    print(NumBitsTotal)
    print(ResultadoBits) 

    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100   
    print(Compresion)

AgruparLecturaFilas()

def AgruparLecturaColumnas():
    Grupos=list()
    Valores=list()
    cont=0
    j=0
    while j < 10:
        i=0
        while i < 10:
            Pos1=matriz[i,j]
            if(i!=9):            
                Pos2=matriz[i+1,j]
            else:
                Pos2=2
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
    SumaRepeticiones=sum(Grupos)
    print(Grupos)
    print(Valores)
    print(SumaRepeticiones)

    Maximo = None
    for pos, num in enumerate(Grupos):
        if(Maximo is None or num > Maximo):
            Maximo=num
            Indice=pos
    print(Maximo, "en", Indice)

    Binario = 0
    multiplicador = 1

    while Maximo != 0: 
        Binario = Binario + Maximo % 2 * multiplicador
        Maximo //= 2 
        multiplicador *= 10 
    print(Binario)

    NumBits=(len(str(Binario)))
    NumbitsCompre=NumBits+1
    print(NumBits)
    print(NumbitsCompre)

    NumBitsTotal=0
    ResultadoBits=list()
    i=0
    while i< len(Grupos):
        valorcito=Valores[i]
        print(valorcito)
        ResultadoBits.append(valorcito)
        Decimal=Grupos[i]
        Binario2 = 0
        multiplicador2 = 1
        while Decimal != 0: 
            Binario2 = Binario2+ Decimal % 2 * multiplicador2
            Decimal //= 2 
            multiplicador2 *= 10 
        if(len(str(Binario2))<NumBits):
            Binario2=str(Binario2).zfill(NumBits)
        print(Binario2)
        NumBitsTotal=NumBitsTotal+len(str(Binario2))
        ResultadoBits.append(Binario2)
        i=i+1
    NumBitsTotal=NumBitsTotal+len(Valores)
    print(NumBitsTotal)
    print(ResultadoBits) 

    Compresion=((NumBitsTotal-NumbitsCompre)/NumBitsTotal)*100   
    print(Compresion)

AgruparLecturaColumnas()

# Program to print matrix in Zig-zag pattern

matrix =[
			[ 1, 2, 3,],
			[ 4, 5, 6 ],
			[ 7, 8, 9 ],
		]
rows=3
columns=3

solution=[[] for i in range(rows+columns-1)]
cosas1=list()
cosas2=list()
for i in range(rows):
	for j in range(columns):
		sum=i+j
		if(sum%2==0):
			#add at beginning
			solution[sum].insert(0,matrix[i][j]),cosas1.append(matrix[i][j])           
		else:
			#add at end of the list
			solution[sum].append(matrix[i][j]),cosas2.append(matrix[i][j])

print(cosas1,"♥3♥", cosas2)		
			
# print the solution as it as
for i in solution:
	for j in i:
		print(j,end=" ")
		

	
print(solution)