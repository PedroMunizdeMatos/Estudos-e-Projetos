# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista (dinheiro/débito/boleto): 10% de desconto.
# - Cartão de crédito à vista: 5% de desconto.
# - Em até 2x no cartão: Sem desconto.
# - 3x ou mais no cartão: 20% de juros.

print('=='*20)
print('Calcule o desconto, ou as parcelas aqui!')
print('=='*20)

nome = str(input('Digite seu nome: ')).strip().lower()
item = str(input('Qual o nome do item que gostaria de comprar? ')).strip().lower()
valor = float(input('Qual o valor do item ? R$: '))
print('Qual forma de pagamento ?')
print('[ 0 ] - Sair.')
print('[ 1 ] - À vista(dinheiro/débito/boleto).\033[32m 10% de desconto\033[m')
print('[ 2 ] - Cartão de crédito à vista. \033[32m5% de desconto\033[m')
print('[ 3 ] - Parcelado em 2x no cartão.')
print('[ 4 ] - Parcelado em 3x ou mais no cartão. \033[31m20% de juros\033[m')
n = int(input('Digite o número correspondente à forma de pagamento: '))
if n == 1:
    valor = valor*0.9
    print('\033[32m{}\033[m, você selecionou o pagamento à vista para {}.\033[33m um desconto de \033[32m10%\033[33m foi aplicado no valor total!\033[m'.format(nome.capitalize(), item.capitalize()))
    print('Portanto, o valor final da sua compra é de R${:.2f}'.format(valor))
elif n == 2:
    valor = valor*0.95
    print('\033[32m{}\033[m, você selecionou o pagamento à vista no cartão de crédito para {}. um desconto de \033[32m5%\033[m foi aplicado no valor total!'.format(nome.capitalize(), item.capitalize()))
    print('Portanto, o valor final da sua compra é de \033[33mR${:.2f}\033[m'.format(valor))
elif n == 3:
    valorp = valor/2
    print('\033[32m{}\033[m, você selecionou o pagamento parcelado em 2x para {}.'.format(nome.capitalize(), item.capitalize()))
    print('Portanto, o valor final da sua compra é de \033[33mR${:.2f}\033[m. e o valor de cada parcela será de \033[33mR${:.2f}\033[m.'.format(valor, valorp))
elif n == 4:
    p = int(input('Digite o número parcelas: '))
    if p < 3:
        print('\033[31mSe deseja parcelar em 2x ou menos, selecione o método de pagamento correto.\033[m')
    else:
        valor = valor*1.2
        valorp = valor / p
        print('\033[32m{}\033[m, você selecionou o pagamento parcelado em \033[31m{}x\033[m para {}.'.format(nome.capitalize(), p, item.capitalize()))
        print('Portanto, o valor final da sua compra é de \033[31mR${:.2f}\033[m. Parcelado em \033[31m{}x\033[m vezes de \033[31mR$:{:.2f}\033[m'.format(valor, p, valorp))
elif n == 0:
    print('Muito obrigado, tenha uma ótima semana!')
else:
    print('\033[31mO valor digitado é inválido.')
