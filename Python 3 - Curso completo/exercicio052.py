# faça um programa que leia um número inteiro e diga se ele é ou não PRIMO.
cont = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, cont))
if cont > 2:
    print('O número {} não é primo.'.format(n))
else:
    print('O número {} é primo.'.format(n))