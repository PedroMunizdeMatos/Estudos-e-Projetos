# Crie um programa que faça o computador jogar JOKENPÔ com você.

import random
import time
print('\033[31mTE DESAFIO A ME VENCER NO JOKENPÔ!\033[m')
time.sleep(2)
print('\033[33mRegras do jogo: O participante deverá escolher entre as 3 opções:')
print('Pedra, papel e tesoura.')
print('Sendo que: Pedra vence tesoura; Tesoura vence papel; Papel vence pedra.\033[m')
time.sleep(2)
print('Então vamos lá! Vença-me se for capaz!')
escolhas = ['pedra', 'papel', 'tesoura']
x = random.choice(escolhas)
if x == 'pedra':
    y = str(input('Digite sua escolha: ')).strip().lower()
    print('Eu escolhi {} e você: {}!'.format(x, y).capitalize())
    if y == 'tesoura':
        print('\033[31mHAHAHA! EU VENCI! PEDRA VENCE TESOURA!\033[m')
    elif y == 'pedra':
        print('\033[31mNEM EU, NEM VOCÊ! UM EMPATE!\033[m')
    elif y == 'papel':
        print('\033[32mPARABÉNS, VOCÊ ME VENCEU! PAPEL VENCE PEDRA!\033[m')
    else:
        print('\033[31mOpção inválida!\033[m')

elif x == 'tesoura':
    y = str(input('Digite sua escolha: ')).strip().lower()
    print('Eu escolhi {} e você: {}!'.format(x, y).capitalize())
    if y == 'papel':
        print('\033[31mHAHAHA! EU VENCI! TESOURA VENCE PAPEL!\033[m')
    elif y == 'tesoura':
        print('\033[31mNEM EU, NEM VOCÊ! UM EMPATE!\033[m')
    elif y == 'pedra':
        print('\033[32mPARABÉNS, VOCÊ ME VENCEU! PEDRA VENCE TESOURA!\033[m')
    else:
        print('\033[31mOpção inválida!\033[m')

else:
    y = str(input('Digite sua escolha: ')).strip().lower()
    print('Eu escolhi {} e você: {}!'.format(x, y).capitalize())
    if y == 'pedra':
        print('\033[31mHAHAHA! EU VENCI! PAPEL VENCE PEDRA!\033[m')
    elif y == 'papel':
        print('\033[31mNEM EU, NEM VOCÊ! UM EMPATE!\033[m')
    elif y == 'tesoura':
        print('\033[32mPARABÉNS, VOCÊ ME VENCEU! TESOURA VENCE PAPEL!\033[m')
    else:
        print('\033[31mOpção inválida!\033[m')