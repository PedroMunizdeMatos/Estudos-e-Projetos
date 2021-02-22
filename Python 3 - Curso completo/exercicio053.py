# crie um programa que leia uma frase e diga se ela é um PALÍNDROMO, desconsiderando os espaços.
# palindromo e a frase que se pode ler  de tras pra frente da mesma forma.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
print(inverso, junto)
