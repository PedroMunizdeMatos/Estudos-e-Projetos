# Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posiução ela aparece a última vez
frase = str(input('Digite uma frase: ')).strip()
print('A frase que você digitou contém {} letras A.'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez na {}ª casa.'.format(frase.lower().find('a') + 1))
print('A letra A aparece pela última vez na {}ª casa'.format(frase.lower().rfind('a') + 1))
