from random import randint
import os
os.system('cls')

num1=int(input('Ingrese un numero: '))
num2=int(input('Ingrese un numero mayor al primero: '))

if (num1 < num2) :
    random=randint(num1,num2)
    if random % 2 != 0 :
        random = random + 1
    else:
        random = random -1
else:
    print('Invalido')
    exit()

print('Juego de Adivinanza')
intento1=int(input('Ingrese el primer intento:\n'))
if intento1==random:
    print(f'Felicitaciones, pudiste adivinar\n El numero secreto era {random}')
    exit()
else:
    if intento1>random:
        print('El numero ingresado es mayor al numero secreto')
    else:
        print('El numero ingresado es menor al numero secreto')





intento2=int(input('Ingrese su segundo intento:\n'))
if intento2==random:
    print(f'Felicitaciones, pudiste adivinar\n El numero secreto era {random}')
    exit()
else:
    if intento2>random:
        print('El numero ingresado es mayor al numero secreto')
    else:
        print('El numero ingresado es menor al numero secreto')


distancia_1=abs(intento1-random)
distancia_2=abs(intento2-random)

if distancia_1>distancia_2:
    print('El primer intento estuvo mas cerca del numero secreto que el segundo intento')
else:
    print('El segundo intento estuvo mas cerca del numero secreto que el primer intento')

intento3=int(input('Ingrese su trecer y ultimo intento:\n'))
if intento3==random:
    print(f'Felicitaciones, pudiste adivinar\n El numero secreto era {random}')
    exit()
else:
    print('Perdiste')
    print(f'El numero secreto era {random}')
    exit()

