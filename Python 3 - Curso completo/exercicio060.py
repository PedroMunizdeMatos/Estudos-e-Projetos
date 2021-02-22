'''Faça um programa que leia um número qualquer e mostre seu fatorial.'''
from math import factorial
print('----- Fatorial! -----')
n = 1
c = n
while n != 0:
    n = int(input('Digite um número: '))
    print('O número {} em fatorial ({}!) é igual a {}.'.format(n, n, factorial(n)))
