from random import randint
import os 
os.system('cls')

num1=int(input('Ingrese el primero numero: '))
num2=int(input('Ingrese un segundo: '))

if (num1 < num2) :
    random=randint(num1,num2)
    if random % 2 != 0 :
        random = random + 1
    else:
        random = random -1
else:
    print('el primer numero tiene que ser menor al segundo numero')
    exit()

print('Adivine el numero')
intento1=int(input('Primer intento : '))
if intento1==random:
    print(f'Adivinaste el numero es {random}')
    exit()
else:
    if intento1>random:
        print('el numero es menor al que ingresaste')
        
    else:
        print('el numero es mayor al que ingresaste')

os.system('cls')
intento2=int(input('segundo intento : '))
if intento2==random:
    print(f'Adivinaste el numero es {random}')
    exit()
else:
    if intento1>random:
        print('el numero es menor al que ingresaste')
    else:
        print('el numero es mayor al que ingresaste')

distancia_1=abs(random-intento1)
distancia_2=abs(random-intento2)

if distancia_1<distancia_2:
    print('pista\n el primero intento estuvo mas cerca del numero que el intento 2')
else:
    print('pista\n el intento 2 estuvo mas cerca del numero que el intento 1')

os.system('cls')
intento3=int(input('tercer intento : '))
if intento3==random:
    print(f'Adivinaste el numero es {random}')
    exit()
else:
    print(f'perdiste el numero era {random}')