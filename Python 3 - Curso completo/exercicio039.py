# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar.
# - se é a hora de se alistar.
# - se já passou do tempo do alistamento.
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('~~~'*15)
print('SERVIÇO DE ALISTAMENTO MILITAR.')
print('~~~'*15)
ano = int(input('Digite o ano de nascimento: '))
idade = 2021 - ano
n = 18 - idade
if idade == 18:
    print('\033[33mVocê deverá se alistar ainda este ano!')
elif idade <= 17:
    print('\033[32mainda falta(am) {} ano(os) para o seu alistamento.'.format(n))
elif idade > 18:
    n = n * (-1)
    print('\033[31mVocê já deveria ter se alistado há {} ano(os).'.format(n))
