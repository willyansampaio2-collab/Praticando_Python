salario = float(input('Qual o salário do funcionário? R$'))
aumento = int(input("Quantos % de reajuste? %"))
reajuste = salario + (salario * aumento / 100)

print(f'Um funcionário que ganhava R${salario}, com {aumento}% de aumento, passa a receber R${reajuste:.2f}')