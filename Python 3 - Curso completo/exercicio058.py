'''Melhore o exercicio028 onde o computador irá sortear um número entre 0 e 10. só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para acertar.'''
import random
n = random.randint(0, 10)
print('---- Jogo de adivinhação! ----')
print('\033[33mTente até adivinhar o número que estou pensando...\033[m')
x = 0
cont = 0

while x != n:
    x = int(input('Escolha um número de 0 a 10: '))
    cont += 1
    if x == n:
        print('\033[32mPARABÉNS, você acertou !! O número que eu estou pensando é o \033[33m{} \033[m!'.format(n))
        print('Você fez {} tentativas.'.format(cont))
    else:
        print('\033[31mNão foi dessa vez ! tente novamente...\033[m')
