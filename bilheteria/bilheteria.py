ingresso_camarote = 300.00
ingresso_vip = 200.00
ingresso_pista = 100.00

print("Bem-vindo ao tickets, gostaria de comprar ingressos para o show do Nathan e nathanzinho ?")
confirmação = input("").lower()
if confirmação != "sim":
    print("Obrigado por visitar nosso site. Volte sempre!")
    exit()

print("Ótimo! Vamos começar o processo de compra do ingresso.")
ingresso = input("Digite o tipo de ingresso (VIP, Pista, Camarote): ").lower()
quantidade = int(input("Digite a quantidade de ingressos que deseja comprar: "))
print("Por favor, preencha o formulário abaixo para prosseguir com a compra do ingresso.")

for i in range(quantidade):
    print(f"\nFormulário para ingresso {i + 1}:")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Idade inválida, entrada somente para maiores de 18 anos.")
        idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    endereço = input("Digite seu endereço: ")
    cep = input("Digite seu CEP: ")

print("\nResumo da compra:")
if ingresso == "camarote":
    total = ingresso_camarote * quantidade
    print("Detalhes do comprador:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"CPF: {cpf}")
    print(f"Email: {email}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {endereço}")
    print(f"CEP: {cep}")
    print(f"total a pagar: R$ {total:.2f}")
    print(f"Tipo de ingresso: Camarote")
 
elif ingresso == "vip":
    total = ingresso_vip * quantidade
    print(f"Tipo de ingresso: VIP")
elif ingresso == "pista":
    total = ingresso_pista * quantidade
    print(f"Tipo de ingresso: Pista")
else:
    print("Tipo de ingresso inválido. Por favor, reinicie o processo de compra.")
    exit()

prosseguir = input("prosseguir com o pagamento?:").lower()
if prosseguir != "sim":
    print("Compra cancelada. Obrigado por visitar nosso site.")
    exit()
