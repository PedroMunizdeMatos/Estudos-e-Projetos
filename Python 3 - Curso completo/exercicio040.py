# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# média < 5.0 =  reprovado
# média > 5.0 < 6.9 =  recuperação
# média >= 7.0 =  aprovado

print('==== Média do aluno ====')
n = float(input('Digite a nota da p1: '))
n2 = float(input('Digite a nota da p2: '))
med = (n + n2) / 2

if med >= 7:
    print('\033[32mAluno Aprovado com média final {:.2f} .'.format(med))
elif med > 5 and med < 6.9:
    print('\033[33mAluno em Recuperação com média final {:.2f} .'.format(med))
else:
    print('\033[31mAluno Reprovado com média final {:.2f} .'.format(med))