import os
os.system('cls')
Estaciones_D=25
C_A=0
C_L=0
C_T=0
print('¡Bienvenido al sistema de gestión de estaciones del Centro de Cómputo!')
while True:
    try:
        print('------Menu Principal-------')
        print('Op 1 : Estaciones Disponibles ')
        print('Op 2 : Asignar Estacion')
        print('Op 3 : Liberar Estacion')
        print('Op 4 : Historial de uso')
        print('OP 5 : Salir')
        
        op=input('Ingrese una opcion\n')

        match op:
            case "1":
                
                print(f'Hay {Estaciones_D} Estaciones disponibles')
            
            case "2":
                if Estaciones_D <= 25 and Estaciones_D > 0:
                    print('Asignacion de estaciones')
                    Asignacion_E=int(input('Cuantas estaciones quiere solicitar\n'))
                    if Asignacion_E<=Estaciones_D:
                        Estaciones_D=Estaciones_D-Asignacion_E
                        print(f'usted a selecase "2":ccionado {Asignacion_E} estaciones y quedan disponibles {Estaciones_D} estaciones')
                        C_T=C_T+Asignacion_E
                    else:
                        print('La opcion tiene que ser mayor a 0 o un numero entero')
                else:
                    print('No hay estaciones disponibles')



            case "3":
                print('Asignacion de estaciones')
                Liberaciones_E=int(input('Ingrese cuantas estaciones quiere liberar\n'))
                if Liberaciones_E<=Asignacion_E:
                    Estaciones_D=Estaciones_D+Liberaciones_E
                    print(F'Se ha liberado {Liberaciones_E} asi dando en total {Estaciones_D} libres')
                    C_T=C_T-Liberaciones_E
                else:
                    print('la cantidad ha liberar se sale de la escala')



            case "4":
                print('----Historial de Uso----')
                print(f'La cantidad de Asignaciones que se ha hecho {C_T}')
                




            case "5":
                print('Gracias por utilizar nuestro software, hasta la proxima')
                break
            
            case _:
                print('Solo ingresar numeros del 1 al 5')
    except:
        print('solo ingresar numero')
