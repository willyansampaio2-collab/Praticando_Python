# Calcula a média de um aluno com base nas notas dos dois bimestres e informa se ele foi aprovado, está em recuperação ou reprovado.
# Se a média for 9 ou mais, exibe uma mensagem de parabéns.
nota1 = float(input("Digite a nota do primeiro bimestre do aluno: "))
nota2 = float(input("Digite a nota do segundo bimestre do aluno: "))
media = (nota1 + nota2) / 2

print("-" * 40)
if media >= 7:
    print(f"A média do aluno é {media}. Aluno aprovado!")
    if media >= 9:
        print("Meus Parabens!")
elif media >= 5:
    print(f"A média do aluno é {media}. Aluno em recuperação!")
else:
    print(f"A média do aluno é {media}. Aluno reprovado!")
    
print("-" * 40)