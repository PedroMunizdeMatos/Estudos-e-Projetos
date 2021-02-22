# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida

print('Calculadora de IMC.')

nome = str(input('Digite seu nome: ')).strip().lower()
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em KG: '))
imc = peso / (altura ** 2)

if imc <= 18.5 and imc > 17.5:
    print('\033[33m{}, seu IMC é de:{}Kg/m². Você está abaixo do peso.'.format(nome.capitalize(), imc))
elif imc <= 17.5:
    print('\033[31m{}, seu IMC é de:{}Kg/m². Você está em Anorexia. Procure um médico!'.format(nome.capitalize(), imc))
elif imc >= 18.5 and imc <= 25:
    print('\033[32m{}, seu IMC é de:{}Kg/m². Você está com o peso ideal!'.format(nome.capitalize(), imc))
elif imc >= 25 and imc <= 30:
    print('\033[33m{}, seu IMC é de:{}Kg/m². Você está em sobrepeso.'.format(nome.capitalize(), imc))
elif imc >= 30 and imc <= 40:
    print('\033[31m{}, seu IMC é de:{}Kg/m². Você está em obesidade!'.format(nome.capitalize(), imc))
else:
    print('\033[31m{}, seu IMC é de:{}Kg/m². Você está em obesidade mórbida, Procure um médico!'.format(nome.capitalize(), imc))