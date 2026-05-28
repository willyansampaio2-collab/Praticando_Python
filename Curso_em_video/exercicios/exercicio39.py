from datetime import date

hoje = date.today()
data = int(input('Digite o ano de seu nascimento: '))
idade = hoje.year - data

print(f'Você tem {idade} anos.')
if  idade < 18:
    print('Você é de menor, ainda vai se alistar ao serviço militar!')
    print(f'Falta {18 - idade} anos.')
elif idade == 18:
    print('Você deve se alistar ao serviço militar o quanto antes!')
else:
    print('Você passou do prazo para alistamento, procure uma junta militar mais proxima!')
    print(f'Já passou {idade - 18} anos.')
