alunos_aprovados = 0
alunos_recuperacao = 0
alunos_reprovados = 0
total_alunos = 0
lista = []

while True: 

    print("=== Cadastro de Notas ===")
    print("1. Cadastrar notas de um aluno")
    print("2. Ver estatísticas")
    print("3. Sair")
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '1':
        while True:
            aluno = str(input("Digite o nome do aluno: "))
            lista.append(aluno)
            nota1 = float(input("Digite a nota do primeiro bimestre: "))
            nota2 = float(input("Digite a nota do segundo bimestre: "))
            nota3 = float(input("Digite a nota do terceiro bimestre: "))
            media = (nota1 + nota2 + nota3) / 3

            print("-" * 30)
            if media >= 7:
                status = "Aprovado"
                alunos_aprovados += 1
                print(f"O aluno {aluno} está {status} com média {media:.2f}")
            elif 5 <= media < 7:
                status = "Recuperação"
                alunos_recuperacao += 1
                print(f"O aluno {aluno} está {status} com média {media:.2f}")
            else:
                status = "Reprovado"
                alunos_reprovados += 1
                print(f"O aluno {aluno} está {status} com média {media:.2f}")
            print("-" * 30)

            total_alunos += 1

            continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
            if continuar != 's':
                print("Encerrando o programa...")
                break
    elif opcao == '2':
        if total_alunos == 0:
            print("Nenhum aluno cadastrado ainda.")
            voltar = input("Deseja voltar ao menu principal? (s/n): ").strip().lower()
            if voltar != 's':
                print("Encerrando o programa...")
                exit()
        else:
            print("================== Estatísticas ==================")
            print(f"Alunos cadastrados:")
            print(lista)
            print(f"Total de alunos cadastrados: {total_alunos}")
            print(f"Alunos Aprovados: {alunos_aprovados} ({(alunos_aprovados / total_alunos) * 100:.2f}%)")
            print(f"Alunos em Recuperação: {alunos_recuperacao} ({(alunos_recuperacao / total_alunos) * 100:.2f}%)")
            print(f"Alunos Reprovados: {alunos_reprovados} ({(alunos_reprovados / total_alunos) * 100:.2f}%)")
            voltar = input("Deseja voltar ao menu principal? (s/n): ").strip().lower()
            if voltar != 's':
                print("Encerrando o programa...")
                exit()
    else:
        print("Opção inválida. Encerrando o programa...")
        exit()