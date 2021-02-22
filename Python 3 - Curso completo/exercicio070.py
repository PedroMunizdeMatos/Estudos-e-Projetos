'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
- Qual é o total gasto na compra.
- Quantos produtos custam mais de R$1000,00
- Qual é o nome do produto mais barato'''
from time import sleep
total = totalmil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip().capitalize()
    valor = float(input('Digite o valor do produto R$: '))
    total += valor
    cont += 1
    if valor > 1000:
        totalmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    r = ' '
    while r not in 'sn':
        r = str(input('Quer continuar ? [S/N]')).strip().lower()[0]
    if r == 'n':
        print('\033[31mFinalizando o programa...\033[m')
        sleep(1)
        break
print('{:-^40}'.format(' FIM '))
print(f'O total da compra foi de R$:{total:.2f}')
print(f'Sua compra tem {totalmil} produtos custando mais de R$:1000.00')
print(f'{barato} é o produto mais barato desta compra e custa R$:{menor:.2f}')
