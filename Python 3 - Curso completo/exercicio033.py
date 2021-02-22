# faça um programa que leia três números e mostre qual é o maior e qual é o menor.
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite mais um número: '))

menor = z
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y

maior = z
if x > y and x > z:
    maior = x
if y > x and y > z:
    maior = y

print('\033[mO menor valor digitado foi {}.\033[m'.format(menor))
print('\033[mO maior valor digitado foi {}.\033[m'.format(maior))
