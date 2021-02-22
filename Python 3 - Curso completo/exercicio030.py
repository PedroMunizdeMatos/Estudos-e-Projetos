# crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

print('Número ímpar ou par ?')
n = int(input('Digite o número: '))
if n % 2 > 0:
    print('O número {} é Ímpar !'.format(n))
else:
    print('O número {} é Par !'.format(n))
