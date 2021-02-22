# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e sem quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será NEGADO.

print('\033[32m-=-'*15)
print('Seja bem vindo ao simulador de Financiamentos.')
print('-=-'*15)
r = str(input('\033[mGostaria de fazer uma simulação? ')).strip().lower()
if r == 'sim':
    print('Muito bem! vamos começar...')
    valor = float(input('Digite o valor do imóvel que deseja financiar: '))
    sal = float(input('Digite o seu salário atual em R$: ')) # sal == salário
    ano = int(input('Em quantos anos gostaria de financiar ?'))
    mes = ano * 12
    prest = (valor)/mes
    if prest > sal*0.3:
        print('\033[31mEste financiamento não seria aprovado, pois a parcela mensal excede 30% do seu salário atual!\033[m')
    else:
        print('\033[32mParabéns, seu financiamento de {} anos, no valor de R$:{:.2f} será aprovado com parcelas de R$:{:.2f} mensais.'.format(ano, valor, prest))
else:
    print('Tudo bem! Tenha uma ótima semana :)')

