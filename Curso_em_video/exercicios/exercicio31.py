d_viagem = float(input('Digite a distacia da viagem em Km: '))
if d_viagem > 200:
    print(f'A viagem custará: R$ {d_viagem*0.45:.2f}')
else:
    print(f'A viagem custará R$ {d_viagem*0.5:.2f}')