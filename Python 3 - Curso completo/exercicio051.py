 # Faça um programa que leia o primeiro termo, a razão de uma PA e imprima os 10 primeiros termos dessa PA.
print('=='*10)
print('Progressão Aritmética')
print('=='*10)
x = int(input('Digite o primeiro termo da PA: '))
y = int(input('Digite a Razão dessa PA: '))
n = x + (10 - 1) * y
print('PA:', end='')
for c in range(x, n+y, y):
    print(' {}'.format(c), end=' ->')
print('Acabou.')
