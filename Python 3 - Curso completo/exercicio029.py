# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por casa Km Excedido.

print('Lombada Eletrônica! Velocidade limite: 80Km/h')
vel = int(input('Velocidade do veículo: '))
if vel > 80:
    m = (vel - 80) * 7
    print('Este veículo foi multado em R${:.2f} por exceder um total de {}Km/h da velocidade limite.'.format(m, vel - 80))
else:
    print('Este veículo está dentro do limite de velocidade.')
