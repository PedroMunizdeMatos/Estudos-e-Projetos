# faça um programa que leia os catetos de um triângulo retângulo e calcule a hipotenusa.

import math

print('Calculadora de Hipotenusa.')
cato = int(input('Qual o tamanho do cateto oposto?: '))
catad = int(input('Qual o tamanho do cateto adjacente?: '))
hipot = math.hypot(cato, catad)
print('Sabendo que o Cateto oposto vale {}, e o adjacente {}. A hipotenusa vale {}'.format(cato, catad, hipot))
