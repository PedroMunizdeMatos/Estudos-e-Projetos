# Faça um programa que mostre na tela, uma contagem regressiva para o ano novo de 10 a 0.

from time import sleep
print('Contagem Regressiva: ')
for c in range (10, -1, -1):
    print(c)
    if c == 0:
        print('\033[32mFeliz ano Novo!')
    sleep(1)