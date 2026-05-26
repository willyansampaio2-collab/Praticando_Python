numero = input('digite um número de 0 a 9999: ').zfill(4)
mil = numero[0]
cen = numero[1]
dez = numero[2]
uni = numero[3]
print(f'O numero {numero} vai ser dividido em:')
print(f'Milhar: {mil}\nCentena: {cen}\nDezena: {dez}\nUnidade: {uni}')