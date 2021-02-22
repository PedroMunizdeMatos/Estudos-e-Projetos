# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passegem, cobrando RS0,50 por Km para viagens de até 200Km.
# E R$0,45 para viagens mais longas.

print('Bem vindo ao Python Viagens!')
s = str(input('Gostaria de fazer um orçamento?:'))
if s == 'sim':
    print('Muito obrigado pela preferência!')
    n = float(input('Por favor, digite a distância até o local destino em Km: '))
    if n < 200:
        print('O valor da viagem será de R$:{:.2f}'.format(n*0.5))
    else:
        print('O valor da viagem será de R$:{:.2f}'.format(n*0.45))
    print('Obrigado, volte sempre! :)')
else:
    print('Obrigado, volte sempre ! :)')
