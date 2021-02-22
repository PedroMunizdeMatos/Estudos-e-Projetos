# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

a = input('Digite o nome do aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

list = [a, b, c, d]
choice = random.choice(list)
print(' \b O aluno sorteado para apagar o quadro é: {}.'.format(choice))
