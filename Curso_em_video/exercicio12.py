valor = float(input('Qual o preço do produto? R$'))
porcentagem = int(input("Quantos % de desconto? %"))
desconto = valor * (porcentagem*0.01)
print(f'O produto que estava custando R${valor}, com o desconto de {porcentagem}%, fica saindo por apenas R${valor-desconto:.2f}')