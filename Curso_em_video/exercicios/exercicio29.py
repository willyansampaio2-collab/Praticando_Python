v = int(input('Qual a velocidade do carro: '))
multa = 7*(v-80)
if v > 80:
    print(f'Você foi multado em R$ {multa:.2f}.')
print(f'Parabéns, a sua velocidade está dentro dos conformes.')