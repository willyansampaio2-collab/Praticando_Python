salario = float(input('Digite seu salário: R$ '))
if salario > 1250:
    reajuste = salario*0.1
    print(f'você recebeu um aumento de R$ {reajuste:.2f}')
    print(f'Salário atualizado para {salario+reajuste:.2f}')
else:
    reajuste = salario*0.15
    print(f'você recebeu um aumento de R$ {reajuste:.2f}')
    print(f'Salário atualizado para {salario+reajuste:.2f}')