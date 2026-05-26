n = input('digite um número de 0 a 9999: ').zfill(4)
mil = n[0]
cen = n[1]
dez = n[2]
uni = n[3]
print(f'O numero {n} vai ser dividido em:')
print(f'Milhar: {mil}\nCentena: {cen}\nDezena: {dez}\nUnidade: {uni}')