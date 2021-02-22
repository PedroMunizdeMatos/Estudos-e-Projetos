# len() - analisa o comprimento ex: len(frase)
# count -  ex: frase.count('p') conta quantas vezes aparece p na frase
# find - procura na string o valor digitado. caso não encontre, retorna -1.
# in - verifica ex: 'pedro' in frase
# strip remove todos os espaços inúteis na frase (começo e fim) [rstrip remove somente à direita, lstrip remove somente à esquerda]
# split -  divide a string em uma lista (divide a frase nos espaços em uma lista de palavras)

print("""Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum 
        Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum
Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum 
                    Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum Lorem Ypsum \b \b""")



frase = '   Curso em Vídeo Python  '
print(frase[3:13])
print(frase[2:10])
print(frase[:])
print(frase[::4])

print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.upper())
print(len(frase))
print(len(frase.strip()))
print(frase.split())
print(frase.replace('Python', 'Android'))
print(frase.find('Vídeo'))
print(frase.find('video'))
print(frase.lower().find('vídeo')) #mostra em qual posição da string se encontra 'vídeo'
dividido = frase.split()
print(dividido[2][3]) # divida a string em palavras, imprima a letra número 3 da palavra de número 2
