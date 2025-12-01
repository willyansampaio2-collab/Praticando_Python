# Entradas
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
idade = int(input("Digite a idade: "))
sexo_input = input("Digite seu sexo (homem/mulher): ").lower()

# Converter sexo para número
if sexo_input == "homem":
    sexo = 1
elif sexo_input == "mulher":
    sexo = 0
else:
    print("Sexo inválido. Usando padrão feminino.")
    sexo = 0

# Calcular IMC
imc = peso / (altura ** 2)


# Calcular % de gordura corporal
percent_gordura = (1.2 * imc) + (0.23 * idade) - (10.83 * sexo) - 5.4

# Calcular TMB (Taxa Metabólica Basal) usando Harris-Benedict
altura_cm = altura * 100
if sexo == 1:  # homem
    TMB = 88.36 + (13.4 * peso) + (4.8 * altura_cm) - (5.7 * idade)
else:  # mulher
    TMB = 447.6 + (9.2 * peso) + (3.1 * altura_cm) - (4.3 * idade)

# Ajustar pelo nível de atividade
print("Escolha seu nível de atividade:")
print("1 - Sedentário")
print("2 - Levemente ativo")
print("3 - Moderadamente ativo")
print("4 - Muito ativo")
nivel = int(input("Digite o número correspondente: "))

if nivel == 1:
    fator = 1.2
elif nivel == 2:
    fator = 1.375
elif nivel == 3:
    fator = 1.55
elif nivel == 4:
    fator = 1.725
else:
    fator = 1.2  # padrão

GCT = TMB * fator

# Déficit calórico diário (redução de 500 kcal/dia)
deficit_calorico = GCT - 500

# Resultados
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade grau I")
elif 35 <= imc < 40:
    print("Obesidade grau II")
else:
    print("Obesidade grau III ou mórbida")
print(f"Sua % de gordura corporal estimada é: {percent_gordura:.2f}%")
print(f"Seu déficit calórico diário recomendado é: {deficit_calorico:.2f} calorias")
