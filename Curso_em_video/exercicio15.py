dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
valor_dia = dias * 60
valor_km = km * 0.15
valor_total = valor_dia + valor_km

print(f'O serviço ficou por R${valor_total:.2f}.')