nome = str(input('Qual é o seu nome ?')).strip().lower()

if nome == 'pedro':
    print('Que nome lindo!')
elif nome == 'thiago' or nome == 'gabriele' or nome == 'elda' or nome == 'heraldo' :
    print('Você tem um belo nome!')
elif nome == 'teciana':
    print('\033[35mVocê tem o nome da mulher mais linda do mundo! <3')
else:
    print('Seu nome é comum.')
print('Tenha um bom dia, {}!'.format(nome.capitalize()))
