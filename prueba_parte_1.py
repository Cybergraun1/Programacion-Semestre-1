import os
os.system('cls')

CS=12000
KI=15000

inte=int(input('Ingrese la cantidad de personas que viven en su hogar\n'))
quintil=int(input('Ingrese su quintil\n'))

if (quintil>=1 or quintil<=5) and (inte>=1 or inte<=5):
    if (quintil==1 or quintil==2) and (inte>=5):
        descuento_cs=(CS*0.75)
        print(f'Su Cuota Mensual quedaria en {round(descuento_cs)}')
    elif (quintil==3 or quintil==4) and (inte>=5):
        descuento_cs=(CS*0.82)
        print(f'Su Cuota Mensual quedaria en {round(descuento_cs)}')
    elif (quintil==1 or quintil==2) and (inte>=2 or inte<=5):
        descuento_cs=(CS*0.85)
        print(f'Su Cuota Mensual quedaria en {round(descuento_cs)}')
    elif (quintil==3 or quintil==4) and (inte>=2 or inte<=5):
        descuento_cs=(CS*0.90)
        print(f'Su Cuota Mensual quedaria en {round(descuento_cs)}')
else:
    print('Su quintil no es valido o sus integrantes supera la escala')
    exit()


if (inte>=4) and (quintil==1 or quintil==2 or quintil==3):
    descuento_ki=(KI*0.83) 
    print(f'El descuento de su Kit inicial es de {round(descuento_ki)}')
else:
    print(f'El precio de su Kit inicial es de {KI} ')