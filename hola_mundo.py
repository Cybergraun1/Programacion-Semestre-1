import os
os.system('cls')


plan_d=80000
radio=12000

edad=int(input('Su edad :'))
quintil=int(input('Su quintil : '))

if (quintil>=1 or quintil <=5):
    if (edad<=25) and (quintil==1 or quintil==2):
        print(f'su plan es de : {plan_d*0.82}')
    elif (edad<=25) and (quintil==3 or quintil==4):
        print(f'su plan es de : {plan_d*0.88}')
    elif (edad>=26 and edad<=45) and (quintil==1 or quintil==2):
        print(f'su plan es de : {plan_d*0.88}')
    elif (edad>=26 and edad<=45) and (quintil==3 or quintil==4):
        print(f'su plan es de : {plan_d*0.92}')
    elif (edad>=46):
        print(f'el valor de su plan es {plan_d}')
    else:
        print('El quintil ingresado no es valido tiene que estar en el rango de (1 a 5)')
else:
    print('cupalo')


if (quintil==1 or quintil==2 or quintil==3) and (edad>=40):
    print(f'la radio seria {radio*0.85}')
else:
    print(f'la radio seria {radio}')