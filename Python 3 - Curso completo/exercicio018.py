import random

a = input('Digite o nome do aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

list = [a, b, c, d]
choice = random.shuffle(list)

print('A ordem de apresentação será: ')
print(list)
