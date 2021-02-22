# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
n = str(input('Digite o seu nome: ')).strip()
print('Você tem Silva no nome?: {}'.format('SILVA' in n.upper()))
