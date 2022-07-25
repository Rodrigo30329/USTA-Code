import random

def listarNum(num):
    num = str(num)
    list_num = []
    for n in num:    
        n = int(n)    
        list_num.append(n)
    return list_num

a=listarNum(123141)
print(a)

b=list()
i=0
while i <= 5:
    c=a[i]*2
    i=i+1
    b.append(c)

print(b)

list1 = [2,4,5,3,5,4]
list2 = [4,1,2,9,7,5]
product = [x*y for x,y in zip(list1,list2)]
print(product)


def Base3():
    val=0    
    palabra="zapazapazapa"
    len1=len(palabra)
    if(len1<7):
        val=0
    elif(len1>12):
        val=0
    else:
        for i in range(len(palabra)):
            if(palabra[i]=="z" or palabra[i]=="a" or palabra[i]=="p"):            
                val=1
            else:
                val=0
    print(val)

Base3()


i=0
for i in range(10):
    a=random.randint(0,1)
    print(a)
    i=1+1

numero_decimal = 67
numero_binario = 0
multiplicador = 1

while numero_decimal != 0: # paso 3
    # pasos 1, 4 y 5 se multiplica el módulo por su multiplicador
    numero_binario = numero_binario + numero_decimal % 2 * multiplicador
    numero_decimal //= 2 # paso 1
    multiplicador *= 10 # paso 5

print(numero_binario)


length = 1
c=5
a=str(length).zfill(c)
print(a)