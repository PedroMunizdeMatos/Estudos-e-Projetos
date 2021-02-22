# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for ímpar, desconsidere-o.
from time import sleep
s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('\033[32mCalculando...\033[m')
sleep(1)
print('A soma dos {} números pares digitados é: {}.'.format(cont, s))