'''Refaça o desafio 051, lendo um número e a razão de uma PA, e mostrando os
10 primeiros termos dessa PA utilizando while'''

print('\033[31m==\033[m'*11)
print('\033[33mProgressão Aritmética\033[m')
print('\033[31m==\033[m'*11)
x = 0
resposta = ''
while resposta != 'n':
    resposta = str(input('''Gostaria de Calcular uma PA? 
    [ S ] Sim;
    [ N ] Não.
    Resposta: ''')).strip().lower()
    if resposta == 'n':
        x = 10
    else:
        n = int(input('Digite um número: '))
        r = int(input('Digite a Razão da PA: '))
        print('Progressão Aritmética: ')
    while x != 10:
        if x == 9:
            print('\033[32m {}\033[m'.format(n + r*x))
            x = 10
        else:
            print('\033[32m {}\033[m'.format(n + r*x), end=' ->')
            x += 1

