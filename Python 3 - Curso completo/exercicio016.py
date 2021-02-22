# faça u programa que leia um ângulo qualquer e mostre na etla o valor do seno, cosseno e tangente desse ângulo.

import math

n = int(input('Digite o ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('Sabendo que o ângulo vale {}º, o seno vale {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(n, sen, cos, tan))
