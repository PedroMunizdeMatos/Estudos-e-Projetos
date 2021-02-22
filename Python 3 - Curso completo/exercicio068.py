'''faça um programa que jogue par ou impar com o computador.
O jogo será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou ao fim do jogo.'''
import random
from time import sleep
print('----- Par ou Ímpar -----')
sleep(1)
print('\033[34mTente me vencer no Par ou Ímpar!\033[m')
cont = soma = 0
while True:
    n = random.randint(0,10)
    sleep(1)
    op = str(input('Par ou ímpar ? [P/I]')).strip().upper()
    x = int(input('Número de dedos: '))
    sleep(0.5)
    print(f'{n} !')
    soma = n + x
    if op == 'P' and soma % 2 == 0:
        print(f'\033[32mParabéns, você venceu! {soma} é par.\033[m')
        cont += 1
    elif op == 'P' and soma % 2 != 0:
        print(f'\033[31mVocê perdeu!\033[m Você conseguiu me vencer {cont} vezes.')
        break
    elif op == 'I' and soma % 2 != 0:
        print(f'\033[32mParabéns, você venceu! {soma} é Ímpar.\033[m')
        cont += 1
    elif op == 'I' and soma % 2 == 0:
        print(f'\033[31mVocê perdeu!\033[m Você conseguiu me vencer {cont} vezes.')
        break
    else:
        print('\033[31mEscolha uma opção válida!\033[m')