#desenvolva um programa que leia nome, idade e sexo de quatro pessoa e imprima:
#a média de idade do grupo.
#qual o nome do homem mais velho.
#quantas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
contmulher = 0
for p in range(1,5):
    print('------ {}ª Pessoa ------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de: {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('E {} mulheres tem menos de 20 anos.'.format(contmulher))