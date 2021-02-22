'''crie um programa que leia o ano de nascimento de 7 pessoas. no final, mostre quantas pessoas
já atingiram maioridade e quantas ainda não atingiram.
- maioridade 21 anos.'''

from datetime import date
cont = 0
cont2 = 0
anoat = date.today().year
for c in range(0,7):
    ano = int(input('Digite o ano de seu nascimento: '))
    if anoat - ano >= 21:
        cont += 1
cont2 = 7 - cont
print('{} pessoas já atingiram a maioridade, e {} pessoas ainda não atingiram.'.format(cont, cont2))