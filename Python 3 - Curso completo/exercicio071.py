'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual valor deverá ser sacado(int) e o programa vai informar
quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa tem cédulas de 50, 20, 10 e 1.'''
import math
cont50 = cont20 = cont10 = 0
res = ' '
while True:
    print('\033[33m----- Caixa Eletrônico -----\033[m')
    num = int(input('Digite o valor que deseja sacar: '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    if m > 0:
        m = m*20
    if c > 0:
        c = c*2
    if d % 2 == 0:
        cont20 = d/2
    if d % 2 != 0:
        cont20 = (d-1)/2
        cont10 = d - cont20*2
    cont50 = c + m
    if cont50 > 0:
        print(f'\033[33mTotal de cédulas de R$50: {cont50:.0f}\033[m')
    if cont20 > 0:
        print(f'\033[33mTotal de cédulas de R$20: {cont20:.0f}\033[m')
    if cont10 > 0:
        print(f'\033[33mTotal de cédulas de R$10: {cont10:.0f}\033[m')
    if u > 0:
        print(f'\033[33mTotal de cédulas de R$1: {u}\033[m')
    while res not in 'sn':
        res = str(input('Gostaria de fazer um novo saque ?')).strip().lower()[0]
    if res == 'n':
        print('Muito obrigado, volte sempre!')
        break