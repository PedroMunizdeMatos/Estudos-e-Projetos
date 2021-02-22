# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir.
# o programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
print('-=-'*15)
print('Vou pensar em um número entre 0 e 5!')
print('TENTE ADIVINHAR !')
print('-=-'*15)
y = random.randint(0,5)
time.sleep(1)
x = int(input('Em que número eu estou pensando?! '))
print('Processando...')
time.sleep(1)
if x == y :
    print('Parabéns, você conseguiu me vender!.')
else:
    print('Ganhei! O número escolhido foi o {} e não {}.'.format(y, x))
