'''Melhore o exercicio 61, perguntando para o usuário quantos termos ele quer mostrar.
o programa encerra quando ele digitar 0.'''

print('\033[31m==\033[m'*11)
print('\033[33mProgressão Aritmética\033[m')
print('\033[31m==\033[m'*11)
n = int(input('Digite um número: '))
r = int(input('Digite a Razão da PA: '))
x = 1 #número de termos da PA
y = 0 #termos adicionais da PA
c = 1 #fator de termo adicional para Y
while x != 0:
    if c == 0:
        x = 0
    print('\033[32m {}\033[m'.format(n + r * (x-1)))
    x += 1
    if x > 10:
        c = int(input('Gostaria de adicionar quantos termos? '))
        if c == 0:
            x = 0
        else:
            y = x + c
            while x != y - 1:
                print('\033[32m {}\033[m'.format(n + r * (x - 1)))
                x += 1
print('Fim da progressão. você solicitou {} termos da PA.'.format(y))
