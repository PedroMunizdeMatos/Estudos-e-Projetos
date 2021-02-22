#faça um programa que leia o peso de 5 pessoas. no final, mostre qual foi o menor e o maior peso.
p1 = 0
p2 = 0
for c in range(1,6):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        p1 = p
        p2 = p
    else:
        if p > p2:
            p2 = p
        if p < p1:
            p1 = p
print('O maior peso registrado foi de \033[31m{}Kg.\033[m'.format(p2))
print('E o menor peso registrado foi de \033[33m{}Kg.\033[m'.format(p1))
