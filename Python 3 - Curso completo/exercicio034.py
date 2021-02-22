# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# para salários superiores a R$1250.00, calcule um aumento de 10%.
# para os inferiores ou iguais, um aumento de 15%.

print('\033[32m==\033[m' * 15)
print('\033[33m     Correção Salarial!')
print('\033[32m==\033[m' * 15)
n = str(input('\033[32mDigite o nome do funcionário: \033[m')).strip()
s = float(input('Digite o salário atual: '))

if s >= 1250: #s = salário
    s = s + s*0.1
    print('\033[36mO novo salário de {} será de R${:.2f}.\033[m'.format(n, s))
else:
    s = s + s*0.15
    print('\033[34mO novo salário de {} será de R${:.2f}\033[m'.format(n, s))
