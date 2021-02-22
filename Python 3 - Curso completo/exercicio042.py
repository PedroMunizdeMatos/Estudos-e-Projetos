# Refaça o 'exercicio035' dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
# - Equilátero: Todos os lados iguais.
# - Isóceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

import time

print('\033[34m==\033[m' * 15)
print('\033[31mSeja bem vindo ao Triangulator!\033[m')
print('\033[31mO analisador de Triângulos!\033[m')
print('\033[34m==\033[m' * 15)
print('Agora digite o tamanho de 3 retas: ')
a = int(input('Reta A: '))
b = int(input('Reta B: '))
c = int(input('Reta C: '))
print('\033[33mPara que um triângulo possa ser formado, as três retas que traçam os seus 3 lados precisam obedecer à "Desigualdade Triangular".')
print('Desigualdade triangular: A + B > C, A + C > B e B + C > A.\033[m')
time.sleep(4)
if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c: # ou  a == b == b
        print('\033[32mSabendo disso, posso afirmar que os valores digitados {}, {} e {} formam um triângulo com sucesso. Pois obedecem À desigualdade triangular.'.format(a, b, c))
        print('Assim como posso afirmar que o triângulo formado é Equilátero, por possuir os três lados iguais.')
    elif a == b or b == c or c == a:
        print('\033[32mSabendo disso, posso afirmar que os valores digitados {}, {} e {} formam um triângulo com sucesso. Pois obedecem À desigualdade triangular.'.format(a, b, c))
        print('Assim como posso afirmar que o triângulo formado é Isóceles, por possuir dois lados iguais.')
    else: #ou elif a != b != c:
        print('\033[32mSabendo disso, posso afirmar que os valores digitados {}, {} e {} formam um triângulo com sucesso. Pois obedecem À desigualdade triangular.'.format(a, b, c))
        print('Assim como posso afirmar que o triângulo formado é Escaleno, por não possuir nenhum lado igual.')
else:
    print('\033[31mSabendo disso, posso afirmar que os valores digitados {}, {} e {} não formam um triângulo com sucesso. Pois não obedecem À desigualdade triangular.'.format(a, b, c))