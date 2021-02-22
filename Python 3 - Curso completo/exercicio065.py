'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não digitar mais valores.'''
r = 's'
cont = soma = menor = maior = 0
while r =='s':
    r = str(input('Digite \033[32m[S]\033[m para continuar e\033[31m [N]\033[m se deseja parar.')).strip().lower()
    if r =='s':
        n = int(input('Digite um número: '))
        cont += 1
        soma += n
        if n > maior and n > menor:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif menor > n:
            menor = n
    elif r == 'n' and cont == 0:
        print('Tudo bem!')
    elif r == 'n' and cont != 0:
        print('''
Você digitou {} valores.
A média entre eles: {}.
\033[32mO maior número digitado foi: {}.\033[m
\033[33mO menor número digitado foi: {}.\033[m'''.format(cont, soma/cont, maior, menor))




