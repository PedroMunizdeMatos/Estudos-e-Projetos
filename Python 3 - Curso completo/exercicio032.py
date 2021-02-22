# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print('Descubra se este ano é bissexto!')
x = int(input('Digite o ano: '))
if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('O ano de {} é bissexto!'.format(x))
else:
    print('O ano de {} não é bissexto'.format(x))
