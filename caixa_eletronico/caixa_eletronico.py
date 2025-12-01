#IMPORTS
import time
import os
import platform
from decimal import Decimal


#VARIÁVEIS GLOBAIS
usuarios = [] #LISTA USUARIO

usuario_atual = None
admin_usuario = "Will1215@"
admin_senha = "W123@"


#FUNÇÕES
def limpar_tela(): #FUNÇÃO LIMPA TELA
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def cadastro_usuario(): #FUNÇÃO CADASTRO
    limpar_tela()
    print("-"*30)
    print("       BANCO DO BRASIL!")
    print("-"*30)
    print()
    print("=== CADASTRO DE USUARIOS ===")
    print()
    nome = input("primeiro nome: ")
    sobrenome = input("sobrenome: ")
    cpf = int(input("digite o seu CPF: "))
    senha = int(input("crie uma senha de 6 digitos: "))   
    confirmar_senha = int(input("confirme sua senha: "))
    if confirmar_senha != senha:
        print("as senhas não são iguais!")
    saldo = Decimal("0.00")

    usuario = {
        "nome": nome,
        "sobrenome": sobrenome,
        "cpf": cpf,
        "senha": senha,
        "saldo": saldo
    }

    usuarios.append(usuario)
    print(F"USUARIO {nome} CADASTRADO!")
    time.sleep(0.7)
    limpar_tela()
def login_usuario(): #LOGIN USUARIOS
        global usuario_atual
        print("-"*30)
        print("=== LOGIN BANCO DO BRASIL ===")
        print("-"*30)
        print()
        cpf_login = float(input("Digite seu cpf: "))
        senha_login = int(input("Digite sua senha: "))

        usuario_encontrado = None
        for usuario in usuarios:
            if usuario['cpf'] == cpf_login:
                usuario_encontrado = usuario
                break
        if usuario_encontrado is None:
            print("usuario não encontrado ou não cadastrado!")
            time.sleep(1)
            limpar_tela()
            tentativa = input("deseja tentar novamente? (s/n): ")
            if tentativa.lower() == "s":
                limpar_tela()
                return login_usuario()
            if tentativa.lower() == "n":
                limpar_tela()
                return False 
        else:
    
            if usuario["cpf"] != cpf_login and usuario["senha"] != senha_login:
                print("usuario ou senha incorretos!")
                time.sleep(1)
                limpar_tela()
                tentativa = input("deseja tentar novamente? (s/n): ")
                if tentativa.lower() == "s":
                    limpar_tela()
                    return login_usuario()
                else:
                    limpar_tela()
                    return False

            elif usuario["cpf"] == cpf_login and usuario["senha"] == senha_login:
                usuario_atual = usuario
                limpar_tela()
                time.sleep(0.6)
                print(f"Seja bem vindo {usuario_atual["nome"]}")
                print()
                time.sleep(0.6)
                print("estamos preparando tudo para você!")
                time.sleep(0.6)
                print("aguarde...")
                time.sleep(1.5)
                limpar_tela()            

def menu_usuario(): #MENU USUARIO
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return
    while True:
        print("-"*30)
        print(f"BEM VINDO AO BANCO DO BRASIL!")
        print('O QUE VC GOSTARIA DE FAZER HOJE?')
        print("-"*30)
        print("1 - FAZER UM SAQUE")
        print("2 - FAZER UM DEPOSITO")
        print("3 - EXTRATO DA CONTA")
        print("4 - DESCONECTAR")
        print()
        numero = int(input("Digite o número (1,2,3 ou 4): "))

        if numero == 1: # - OPÇÃO DE SAQUE
            saque_usuario()

        elif numero == 2: # - OPÇÃO DE DEPOSITO
            deposito_usuario()

        elif numero == 3: # - OPÇÃO DE EXTRATO
            extrato_usuario()

        elif numero == 4: # - OPÇÃO DE DESCONECTAR
            usuario_atual = None
            limpar_tela()
            print("desconectando...")
            time.sleep(1.5)
            limpar_tela()
            break
def saque_usuario():#FUNÇÃO DE SAQUE
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return
        
    while True:
        limpar_tela()
        time.sleep(0.6)
        print(f"Seu saldo atual é de: {usuario_atual["saldo"]} R$")
        print()
        time.sleep(0.6)

        saque = Decimal(input("Qual valor gostaria de sacar? R$ "))
        if saque > usuario_atual['saldo']:
            print()
            print("Saldo insuficiente!")
            print()
            time.sleep(0.6)
            falha1 = input('deseja tentar novamente? (s/n): ').lower()
            if falha1 == "s":
                limpar_tela()
                continue
            elif falha1 == "n":
                limpar_tela()
                print("aguarde, estamos te direcionando para o menu principal ...")
                time.sleep(1.5)
                limpar_tela()
                break
            else:
                print("opção inválida!")
                time.sleep(0.6)
                limpar_tela()
                continue

        elif saque <= usuario_atual['saldo']:
            confirmar_saque = input("deseja confirmar o saque? (s/n): ").lower()
            if confirmar_saque == "n":
                limpar_tela()
                time.sleep(0.6)
                continue
            elif confirmar_saque == "s":
                confirmar_senha = int(input("por favor, confirme sua senha: "))
                if confirmar_senha != usuario_atual["senha"]:
                    print()
                    print("senha incorreta!")
                    print()
                    time.sleep(1)
                    continue
                elif confirmar_senha == usuario_atual["senha"]:
                    usuario_atual["saldo"] -= saque
                    print()
                    print(f"Saque de R${saque} realizado com sucesso!")
                    print(f"Seu saldo atual é de: R${usuario_atual['saldo']}")
                    print()
                    time.sleep(1.5)
                    break
def deposito_usuario(): #FUNÇÃO DE DEPOSITO
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return

    while True:
        limpar_tela()
        time.sleep(0.6)
        print(f"Seu saldo atual é de: {usuario_atual['saldo']} R$")
        print()
        time.sleep(0.6)

        deposito = Decimal(input("Qual valor gostaria de depositar? R$"))
        confirmar_deposito = input("deseja confirmar o deposito? (s/n): ").lower()
        if confirmar_deposito == "n":
            limpar_tela()
            time.sleep(0.6)
            continue
        elif confirmar_deposito == "s":
            senha_deposito = int(input("por favor, confirme sua senha: "))
            if senha_deposito != usuario_atual["senha"]:
                print()
                print("senha incorreta!")
                print()
                time.sleep(1)
                continue
            elif senha_deposito == usuario_atual["senha"]:
                usuario_atual["saldo"] += deposito
                print()
                print(f"Deposito de R${deposito} realizado com sucesso!")
                print(f"Seu saldo atual é de: R${usuario_atual['saldo']}")
                print()
                time.sleep(1.5)
                print('Gostaria de realizar outro deposito?')
                continuar = (input('s ou n: ').lower())
                if continuar == "s":
                    print()
                    print('aguarde...')
                    time.sleep(1.5)
                    limpar_tela()
                    continue
                elif continuar == "n":
                    print()
                    print("estamos lhe encaminhando ao menu principal.")
                    print("aguarde...")
                    time.sleep(1.5)
                    limpar_tela()
                    break
def extrato_usuario(): #FUNÇÃO EXTRATO
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return
    saldo = usuario_atual["saldo"]
    limpar_tela()
    time.sleep(0.6)
    print(f'seu saldo é de: {saldo} R$')
    print()
    menu = input('Pressione "Enter" para voltar ao menu principal:')
    print('voltando...')
    time.sleep(1.5)
    limpar_tela()
def tela_inicial(): #FUNÇÃO TELA INICIAL 
    while True:
        print("-"*30)
        print("BEM VINDO AO BANCO DO BRASIL!")
        print('VOCÊ JÁ POSSUI UMA CONTA?')
        print("-"*30)
        resposta = input('s ou n: ').lower()
        if resposta == "n":
            limpar_tela()
            cadastro_usuario()
            continue
        if resposta == "w#":
            limpar_tela()
            time.sleep(0.5)
            print("redirecionando para o modo ADMIN...")
            time.sleep(1.5)
            admin()
        if resposta == "s":
            limpar_tela()
            login_usuario()
            if usuario_atual:
                menu_usuario()                

def admin(): #LOGIN ADMIN
    while True:
        limpar_tela()
        print("-"*30)
        print("🔐 BANCO DO BRASIL(ADM) 🔐")
        print("-"*30)
        print()
        login_admin = input("Digite o usuário admin: ")
        senha_admin = input("digite a senha admin: ")
        if login_admin == admin_usuario and senha_admin == admin_senha:
            print()
            time.sleep(0.3)
            print("verificando...")
            time.sleep(1.5)
            limpar_tela()
            print("🔓 Acesso Liberado!")
            time.sleep(1)
            print()
            print("Bem vindo, Administrador!")
            time.sleep(1.5)
            limpar_tela()
            menu_admin()
        else:
            print()
            print("🔒 Acesso Negado!")
            time.sleep(1)
            limpar_tela()
            voltar = input('deseja tentar novamente? (s/n): ').lower()
            if voltar == "s":
                limpar_tela()
                continue
            if voltar == "n":
                limpar_tela()
                break
def menu_admin(): #MENU ADMIN
    while True:
        print("-"*30)
        print(f"BEM VINDO AO BANCO DO BRASIL!")
        print('O QUE VC GOSTARIA DE FAZER HOJE?')
        print("-"*30)
        print()
        print("1 - FAZER CADASTRO(S)")
        print("2 - EXCLUIR CADASTRO(S)")
        print("3 - CONSULTAR CADASTROS")
        print("4 - DESCONECTAR")
        print()
        escolha = int(input("escolha umas das opções (1,2,3 ou 4): "))
        if escolha == 1:
            while True:
                cadastro_usuario()
                repetir_cadastro = input("deseja realizar um novo cadastro? (s/n): ").lower()
                if repetir_cadastro == "s":
                    limpar_tela()
                    time.sleep(0.5)
                    continue
                elif repetir_cadastro == "n":
                    limpar_tela()
                    print("voltando...")
                    time.sleep(1)
                    limpar_tela()
                    break
        if escolha == 2:
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                time.sleep(1.2)
                continue
            limpar_tela()
            print("=== EXCLUIR CADASTRO ===")
            for i, u in enumerate(usuarios, start=1):
                print(f"{i}) {u['nome']} {u['sobrenome']} - CPF: {u['cpf']}")
            cpf_del = input("Digite o CPF do usuário a excluir (ou Enter para cancelar): ").strip()
            if not cpf_del:
                limpar_tela()
                continue
            try:
                cpf_del_val = int(cpf_del)
            except ValueError:
                print("CPF inválido.")
                time.sleep(1)
                limpar_tela()
                continue
            encontrado = None
            for u in usuarios:
                if u["cpf"] == cpf_del_val:
                    encontrado = u
                    break
            if encontrado:
                confirmar = input(f"Confirma a exclusão do usuário {encontrado['nome']} {encontrado['sobrenome']}? (s/n): ").lower()
                if confirmar == "s":
                    senha_confirma = input("Digite a senha admin para confirmar: ")
                    if senha_confirma == admin_senha:
                        usuarios.remove(encontrado)
                        print("Usuário removido com sucesso.")
                    else:
                        print("senha errada!")
                else:
                    print("Operação cancelada.")
            else:
                print("CPF não encontrado.")
            time.sleep(1.5)
            limpar_tela()
        if escolha == 3:
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                time.sleep(1.2)
                limpar_tela()
                continue
            limpar_tela()
            print("=== LISTA DE USUÁRIOS CADASTRADOS ===")
            for u in usuarios:
                print(f"Nome: {u['nome']} {u['sobrenome']}, CPF: {u['cpf']}, Saldo: R${u['saldo']}")
            print()
            input("Pressione Enter para voltar ao menu admin...")
            limpar_tela()
            
        if escolha == 4:
            limpar_tela()
            print("desconectando...")
            time.sleep(1.5)
            limpar_tela()
            break


#MENU PRINCIPAL
while True:
    tela_inicial()
    limpar_tela()