'''crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
no final mostre quantos números foram digitados, e mostre qual foi a soma entre eles.'''
n = cont = soma = 0
while n != 999:
    n = int(input('''
    ---- Digite um número ----
    \033[33m[Digite 999 para parar]\033[m
    Número: '''))
    if n == 999:
        break
    elif n != 999:
        cont += 1
        soma += n
print('Você digitou \033[31m{}\033[m números ao todo. A soma entre eles é: \033[31m{}'.format(cont, soma))