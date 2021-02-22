'''Crie um programa que leia valores e mostre um menu na tela:
[1]soma
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa.
o programa deverá realizar a operação solicitada em cada caso.'''
print('------ Calculadora ------')
n = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
while op != 5:
    print('''Selecione a operação que deseja realizar: 
    [ 1 ] - Soma;
    [ 2 ] - Multiplicação;
    [ 3 ] - Maior;
    [ 4 ] - Digitar novos números;
    [ 5 ] - Sair do programa.''')
    op = int(input())
    if op == 1:
        print('A soma de {} e {} é igual a {}.'.format(n, n2, n + n2))
    elif op == 2:
        print('A multiplicação entre {} e {} é igual a {}.'.format(n, n2, n * n2))
    elif op == 3:
        if n > n2:
            print('{} é maior que {}.'.format(n, n2))
        elif n < n2:
            print('{} é maior que {}.'.format(n2, n))
        else:
            print('{} é igual a {}.'.format(n, n2))
    elif op == 4:
        n = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif op == 5:
        op = 5
    else:
        print('\033[31mOpção inválida!\033[m')
print('Fim.')
