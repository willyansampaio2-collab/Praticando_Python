import time
import os
import platform
from decimal import Decimal, InvalidOperation

# VARIÁVEIS GLOBAIS
usuarios = []  # LISTA USUARIO
usuario_atual = None
admin_usuario = "Will1215@"
admin_senha = "W123@"


# FUNÇÕES
def limpar_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def ler_int(prompt):
    s = input(prompt).strip()
    try:
        return int(s)
    except ValueError:
        raise


def ler_decimal(prompt):
    while True:
        s = input(prompt).strip().replace(",", ".")
        if s == "":
            return None
        try:
            d = Decimal(s)
            return d
        except InvalidOperation:
            print("Valor inválido. Tente novamente (ex.: 10.50).")
            time.sleep(0.8)


def format_saldo(d: Decimal):
    return format(d, ".2f")


def cadastro_usuario():
    limpar_tela()
    print("-" * 30)
    print("       BANCO DO BRASIL!")
    print("-" * 30)
    print()
    print("=== CADASTRO DE USUARIOS ===")
    print()
    nome = input("primeiro nome: ").strip()
    sobrenome = input("sobrenome: ").strip()
    try:
        cpf = ler_int("digite o seu CPF (apenas números): ")
    except Exception:
        print("CPF inválido. Cadastro cancelado.")
        time.sleep(1)
        limpar_tela()
        return

    # checar duplicado
    for u in usuarios:
        if u["cpf"] == cpf:
            print("CPF já cadastrado.")
            time.sleep(1)
            limpar_tela()
            return

    try:
        senha = ler_int("crie uma senha numérica de 6 digitos: ")
        confirmar_senha = ler_int("confirme sua senha: ")
    except Exception:
        print("Senha inválida. Cadastro cancelado.")
        time.sleep(1)
        limpar_tela()
        return

    if confirmar_senha != senha:
        print("As senhas não são iguais. Cadastro cancelado.")
        time.sleep(1)
        limpar_tela()
        return

    usuario = {
        "nome": nome,
        "sobrenome": sobrenome,
        "cpf": cpf,
        "senha": senha,
        "saldo": Decimal("0.00"),
    }
    usuarios.append(usuario)
    print(f"USUARIO {nome} CADASTRADO!")
    time.sleep(0.8)
    limpar_tela()


def login_usuario():
    global usuario_atual
    while True:
        limpar_tela()
        print("-" * 30)
        print("=== LOGIN BANCO DO BRASIL ===")
        print("-" * 30)
        print()
        cpf_input = input("Digite seu cpf: ").strip()
        senha_input = input("Digite sua senha: ").strip()

        # validar CPF
        try:
            cpf_login = int(cpf_input)
        except ValueError:
            print("CPF inválido. Use apenas números.")
            time.sleep(1)
            if input("Deseja tentar novamente? (s/n): ").lower().strip() == "s":
                continue
            limpar_tela()
            return False

        # procurar usuário
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario["cpf"] == cpf_login:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            print("CPF não registrado.")
            time.sleep(0.8)
            tentar = input("Deseja tentar logar em outra conta? (s/n): ").lower().strip()
            if tentar == "s":
                continue
            limpar_tela()
            return False

        # validar senha
        try:
            senha_login = int(senha_input)
        except ValueError:
            print("Senha inválida. Use apenas números.")
            time.sleep(1)
            if input("Deseja tentar novamente? (s/n): ").lower().strip() == "s":
                continue
            limpar_tela()
            return False

        if usuario_encontrado["senha"] != senha_login:
            print("Senha incorreta.")
            time.sleep(0.8)
            if input("Deseja tentar novamente? (s/n): ").lower().strip() == "s":
                continue
            limpar_tela()
            return False

        # sucesso
        usuario_atual = usuario_encontrado
        limpar_tela()
        print(f"Seja bem vindo {usuario_atual['nome']}")
        time.sleep(1)
        limpar_tela()
        return True


def saque_usuario():
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return

    while True:
        limpar_tela()
        print(f"Seu saldo atual é de: R$ {format_saldo(usuario_atual['saldo'])}")
        print()
        saque = ler_decimal("Qual valor gostaria de sacar? R$ ")
        if saque is None:
            print("Operação cancelada.")
            time.sleep(0.8)
            limpar_tela()
            return

        if saque <= 0:
            print("Valor deve ser maior que zero.")
            time.sleep(0.8)
            continue

        if saque > usuario_atual["saldo"]:
            print()
            print("Saldo insuficiente!")
            print()
            time.sleep(0.6)
            falha1 = input("deseja tentar novamente? (s/n): ").lower().strip()
            if falha1 == "s":
                continue
            limpar_tela()
            return

        confirmar = input("deseja confirmar o saque? (s/n): ").lower().strip()
        if confirmar != "s":
            limpar_tela()
            print("Operação cancelada.")
            time.sleep(0.8)
            continue

        try:
            confirmar_senha = ler_int("por favor, confirme sua senha: ")
        except Exception:
            print("Senha inválida.")
            time.sleep(0.8)
            continue

        if confirmar_senha != usuario_atual["senha"]:
            print("senha incorreta!")
            time.sleep(1)
            continue

        usuario_atual["saldo"] -= saque
        usuario_atual["saldo"] = Decimal(format_saldo(usuario_atual["saldo"]))  # normalizar
        print()
        print(f"Saque de R${format_saldo(saque)} realizado com sucesso!")
        print(f"Seu saldo atual é de: R${format_saldo(usuario_atual['saldo'])}")
        time.sleep(1.2)
        limpar_tela()
        return


def deposito_usuario():
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return

    while True:
        limpar_tela()
        print(f"Seu saldo atual é de: R$ {format_saldo(usuario_atual['saldo'])}")
        print()
        deposito = ler_decimal("Qual valor gostaria de depositar? R$ ")
        if deposito is None:
            print("Operação cancelada.")
            time.sleep(0.8)
            limpar_tela()
            return

        if deposito <= 0:
            print("Valor deve ser maior que zero.")
            time.sleep(0.8)
            continue

        confirmar = input("deseja confirmar o deposito? (s/n): ").lower().strip()
        if confirmar != "s":
            limpar_tela()
            print("Operação cancelada.")
            time.sleep(0.8)
            continue

        try:
            senha_deposito = ler_int("por favor, confirme sua senha: ")
        except Exception:
            print("Senha inválida.")
            time.sleep(0.8)
            continue

        if senha_deposito != usuario_atual["senha"]:
            print("senha incorreta!")
            time.sleep(1)
            continue

        usuario_atual["saldo"] += deposito
        usuario_atual["saldo"] = Decimal(format_saldo(usuario_atual["saldo"]))  # normalizar
        print()
        print(f"Deposito de R${format_saldo(deposito)} realizado com sucesso!")
        print(f"Seu saldo atual é de: R${format_saldo(usuario_atual['saldo'])}")
        time.sleep(1.2)
        limpar_tela()
        return


def extrato_usuario():
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return
    limpar_tela()
    print("=== EXTRATO DA CONTA ===")
    print(f"Nome: {usuario_atual['nome']} {usuario_atual['sobrenome']}")
    print(f"CPF: {usuario_atual['cpf']}")
    print(f"Saldo: R$ {format_saldo(usuario_atual['saldo'])}")
    print()
    input('Pressione "Enter" para voltar ao menu principal:')
    limpar_tela()


def tela_inicial():
    while True:
        limpar_tela()
        print("-" * 30)
        print("BEM VINDO AO BANCO DO BRASIL!")
        print("VOCÊ JÁ POSSUI UMA CONTA?")
        print("-" * 30)
        resposta = input("s ou n (ou w# para admin): ").lower().strip()
        if resposta == "n":
            cadastro_usuario()
            continue
        if resposta == "w#":
            admin()
            continue
        if resposta == "s":
            sucesso = login_usuario()
            if sucesso:
                menu_usuario()
            # ao voltar do menu_usuario, continuará aqui (usuário desconectado)
            continue


def admin():
    while True:
        limpar_tela()
        print("-" * 30)
        print("🔐 BANCO DO BRASIL(ADM) 🔐")
        print("-" * 30)
        print()
        login_admin = input("Digite o usuário admin: ").strip()
        senha_admin = input("digite a senha admin: ").strip()
        if login_admin == admin_usuario and senha_admin == admin_senha:
            limpar_tela()
            print("🔓 Acesso Liberado!")
            time.sleep(0.8)
            limpar_tela()
            menu_admin()
            return
        else:
            print("🔒 Acesso Negado!")
            time.sleep(0.8)
            if input("deseja tentar novamente? (s/n): ").lower().strip() == "s":
                continue
            limpar_tela()
            return


def menu_usuario():
    global usuario_atual
    if usuario_atual is None:
        print("nenhum usuario logado.")
        time.sleep(0.8)
        return
    while True:
        print("-" * 30)
        print(f"BEM VINDO AO BANCO DO BRASIL, {usuario_atual['nome']}!")
        print("O QUE VC GOSTARIA DE FAZER HOJE?")
        print("-" * 30)
        print("1 - FAZER UM SAQUE")
        print("2 - FAZER UM DEPOSITO")
        print("3 - EXTRATO DA CONTA")
        print("4 - DESCONECTAR")
        print()
        escolha = input("Digite o número (1,2,3 ou 4): ").strip()
        if escolha == "1":
            saque_usuario()
        elif escolha == "2":
            deposito_usuario()
        elif escolha == "3":
            extrato_usuario()
        elif escolha == "4":
            usuario_atual = None
            limpar_tela()
            print("desconectando...")
            time.sleep(1)
            limpar_tela()
            return
        else:
            print("Opção inválida.")
            time.sleep(0.8)
            limpar_tela()


def menu_admin():
    while True:
        limpar_tela()
        print("-" * 30)
        print("MENU ADMIN")
        print("-" * 30)
        print("1 - FAZER CADASTRO(S)")
        print("2 - EXCLUIR CADASTRO(S)")
        print("3 - CONSULTAR CADASTROS")
        print("4 - DESCONECTAR")
        escolha = input("escolha umas das opções (1,2,3 ou 4): ").strip()
        if escolha == "1":
            cadastro_usuario()
        elif escolha == "2":
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
                confirmar = input(f"Confirma a exclusão do usuário {encontrado['nome']} {encontrado['sobrenome']}? (s/n): ").lower().strip()
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
            time.sleep(1.2)
        elif escolha == "3":
            limpar_tela()
            print("=== LISTA DE USUÁRIOS CADASTRADOS ===")
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for u in usuarios:
                    print(f"Nome: {u['nome']} {u['sobrenome']}, CPF: {u['cpf']}, Saldo: R${format_saldo(u['saldo'])}")
            print()
            input("Pressione Enter para voltar ao menu admin...")
        elif escolha == "4":
            limpar_tela()
            print("desconectando admin...")
            time.sleep(1)
            limpar_tela()
            return
        else:
            print("Opção inválida.")
            time.sleep(0.8)


# LOOP PRINCIPAL
if __name__ == "__main__":
    while True:
        tela_inicial()