import time
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def multiplicacao():
    valor = int(input("Digite um número inteiro: "))
    tabuada = int(input("Digite até que numero da tabuada que deseja ver: "))
    for i in range(tabuada):
        print(f"{valor} X {i+1} = {valor*(i+1)}")
    input("Pressione Enter para voltar ao menu: ")
    limpar_tela()
    print("Voltando ao menu...")
    time.sleep(1)
    limpar_tela()

def elevado():
    valor = int(input("Digite um número inteiro: "))
    elevado = int(input("Digite até que numero da tabuada que deseja ver: "))

    for i in range(elevado):
        print(f"{valor}^{i+1} = {valor ** (i+1)}")
    input("Pressione Enter para voltar ao menu: ")
    limpar_tela()
    print("Voltando ao menu...")
    time.sleep(1)
    limpar_tela()

def divisao():
    valor = int(input("Digite um número inteiro: "))
    divisor = int(input("Digite até que numero da tabuada que deseja ver: "))

    for i in range(divisor):
        print(f"{valor}/{i+1} = {valor/(i+1)}")
    input("Pressione Enter para voltar ao menu: ")
    limpar_tela()
    print("Voltando ao menu...")
    time.sleep(1)
    limpar_tela()

def raiz():
    valor = int(input("Digite um número inteiro: "))
    raiz = int(input("Digite até que numero da tabuada que deseja ver: "))
    for i in range(raiz):
        print(f"{valor}√{i+1} = {valor ** (1/(i+1))}")
    input("Pressione Enter para voltar ao menu: ")
    limpar_tela()
    print("Voltando ao menu...")
    time.sleep(1)
    limpar_tela()

while True:
    print("-"*30)
    print("Bem vindo ao gerador de tabuada!")
    print("-"*30)
    print("")
    print("Escolha uma das opções abaixo:")
    print("1 - Tabuada de multiplicação")
    print("2 - Tabuada de potenciação")
    print("3 - Tabuada de divisão")
    print("4 - Tabuada de radiciação")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada (1-4): "))
    if opcao == 1:
        limpar_tela()
        multiplicacao()
    elif opcao == 2:
        limpar_tela()
        elevado()
    elif opcao == 3:
        limpar_tela()
        divisao()
    elif opcao == 4:
        limpar_tela()
        raiz()
    elif opcao == 0:
        limpar_tela()
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        limpar_tela()