# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de uma tleta e mostre sua categoria, de acordo com a idade.
# - até 9 anos: MIRIM
# -  até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 25 anos: SENIOR
# - acima de 25 anos: MASTER

from datetime import date
print('==='*11)
print('\033[34mConfederação Nacional de Natação.\033[m')
print('==='*11)
anoat = date.today().year #ano atual
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = anoat - ano

if idade <= 9:
    print('\033[36mAtleta de categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('\033[34mAtleta de categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print('\033[32mAtleta de categoria JUNIOR.')
elif idade > 19 and idade <=25:
    print('\033[35mAtleta de categoria SENIOR.')
else:
    print('\033[31mAtleta de categoria MASTER.')