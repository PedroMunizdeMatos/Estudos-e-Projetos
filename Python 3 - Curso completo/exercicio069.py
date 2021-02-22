'''crie um programa que leia a idade e o sexo de várias pessoas.
a cada pessoa cadastrada, o programa deverá perguntar se o usuário que ou não continuar.
no final mostre:
- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos.'''
from time import sleep

contidade = conthomen = contmulher = p = 0
while True:
    p += 1
    print(f'--- {p}ª pessoa ---')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('[M]/[F]: ')).strip().lower()
    if idade >= 18:
        contidade += 1
    if sexo == 'm':
        conthomen += 1
    if sexo == 'f' and idade < 20:
        contmulher += 1
    x = ' '
    while x not in 'sn':
        x = str(input('Deseja continuar ? \033[32m[S]\033[m/\033[31m[N]\033[m')).strip().lower()
    if x == 'n':
        print('\033[31mFinalizando programa...\033[m')
        break

print('\033[33mProcessando informações cadastradas...\033[m.')
sleep(1)
print(f'Total de pessoas cadastradas: {p}')
sleep(1)
print(f'Total de maiores de idade: {contidade}')
sleep(1)
print(f'Total de Homens cadastrados: {conthomen}')
sleep(1)
print(f'Total de Mulheres cadastradas com menos de 20 anos: {contmulher}')