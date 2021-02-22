'''faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o valor solicitado for negativo.'''
from time import sleep
n = 0
cont = 0
while n >= 0:
    print('--' * 15)
    print('\033[33mPara cancelar, digite um número negativo.\033[m')
    n = int(input('Qual número deseja saber a tabuada ? '))
    print('--' * 15)
    if n < 0:
        print('\033[31mFinalizando o programa...\033[m')
        sleep(1)
        break
    else:
        for c in range (0,11):
            print(f'{n} x {c} = {n*c}')


