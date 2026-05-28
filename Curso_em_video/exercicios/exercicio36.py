v_emp = float(input('Qual o valor da casa: '))
salario = float(input('Quanto você recebe: R$ '))
parcela = int(input('Deseja em quantas prestações: '))
v_parcela = v_emp/parcela

if v_parcela > (salario * 0.30):
    print('NEGADO!!')
    print(f'Devido ao valor da parcela de R$ {v_parcela:.2f}, ultrapassar 30% do seu salario de R$ {salario:.2f}, o emprestimo foi negado.')
else:
    print('APROVADO!!')
    print(f'O seu emprestimo de R$ {v_emp:.2f} em {parcela}X foi aprovado, com as prestações custando R$ {v_parcela:.2f}, meus parabens!!')