# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior.
# - o segundo valor é maior.
# não existe valor maior, os dois são iguais.

print('Seja bem vindo ao comparador de números.')
print('=-='*15)
n = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n > n2:
    print('O primeiro número "{}" é maior que o segundo "{}".'.format(n, n2))
elif n2 > n:
    print('O segundo número "{}" é maior que o primeiro "{}".'.format(n2, n))
else:
    print('\033[32mOs dois números são iguais!')
