# Faça um programa que calcule a soma de todos os números ímpares múltiplos de 3.

from time import sleep
s = 0
cont = 0
print('Irei calcular a soma de todos os números ímpares entre 1 e 500 múltiplos de 3. ')
print('\033[32mCalculando...\033[m')
sleep(2)
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} ímpares multiplos de 3 é: \033[32m{}.'.format(cont, s))