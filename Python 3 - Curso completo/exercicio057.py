'''Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F. Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''
sexo = ''
n = 1
while n != 0:
    sexo = str(input('''Escolha seu sexo:
    [ M ] - Masculino;
    [ F ] - Feminino.
    ''')).strip().upper()[0]
    if sexo == 'M':
        print('Você escolheu "Sexo Masculino".')
        n = 0
    elif sexo == 'F':
        print('Você escolheu "Sexo Feminino".')
        n = 0
    else:
        print('\033[31mDados inválidos! Digite novamente.\033[m')