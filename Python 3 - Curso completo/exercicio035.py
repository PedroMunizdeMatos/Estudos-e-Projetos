# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# A condição de existência de um triângulo é um conjunto de relações entre as medidas de seus lagos que possibilitam decidir se, com as medidas propostas,
# é possível construí-lo. Essa condição pode ser vista como uma propriedade chamada de desigualdade triangular.
# AB + BC > AC
# AB + AC > BC
# BC + AC > AB

import time

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'negativo':'\033[7m'}

print('\033[34m==\033[m' * 15)
print('\033[31mSeja bem vindo ao Triangulator!\033[m')
print('\033[31mO analisador de Triângulos!\033[m')
print('\033[34m==\033[m' * 15)
print('Agora digite o tamanho de 3 retas: ')
a = int(input('Reta A: '))
b = int(input('Reta B: '))
c = int(input('Reta C: '))
print('Para que um triângulo possa ser formado, as três retas que traçam os seus 3 lados precisam obedecer à "Desigualdade Triangular".')
print('Desigualdade triangular: A + B > C, A + C > B e B + C > A.')
time.sleep(4)
if a + b > c and a + c > b and b + c > a:
    print('Sabendo disso, posso afirmar que os valores digitados {}, {} e {} formam um triângulo com sucesso. Pois obedecem À desigualdade triangular.'.format(a, b, c))
else:
    print('Sabendo disso, posso afirmar que os valores digitados {}, {} e {} não formam um triângulo com sucesso. Pois não obedecem À desigualdade triangular.'.format(a, b, c))
