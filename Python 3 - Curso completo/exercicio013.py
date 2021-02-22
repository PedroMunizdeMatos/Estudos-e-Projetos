d = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos quilômetros foram rodados?'))
dias = d * 60
dist = km * 0.15
t = dias + dist
print('O valor total a pagar é R$: {:.2f} \b Sendo R$:{:.2f} das diárias e R$:{:.2f} dos Km rodados'.format(t, dias, dist))
