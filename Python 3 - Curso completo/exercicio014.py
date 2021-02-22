# faça um programa que leia um número real e mostre somente a parte inteira deste número.

import math

n = float(input('Digite um número real: '))
print('A parte inteira de {} é: {}'.format(n, (n // 1)))
print('A parte inteira de {} é: {}'.format(n, math.floor(n)))
print('A parte inteira de {} é: {}'.format(n, math.trunc(n)))
print('A parte inteira de {} é: {}'.format(n, int(n)))
