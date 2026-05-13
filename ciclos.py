for la in '123456':
    print(f'{la} ejemplo')

print('------------------------------')

lista3=[1,2,3,4]
lista3.append(5)

for i in lista3:
    print(f'lista {i}')
    print(lista3[3],lista3[1])

print('------------------------------')

a=5 
while (a>=0):
    print(f'el valor de a es : {a}')
    a=int(input('ingrese un valor: '))
