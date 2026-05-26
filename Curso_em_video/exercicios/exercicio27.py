nome = input('digite seu nome completo: ').title()
lista = nome.split()
print(f'O seu primeiro nome é "{lista[0]}" e o seu ultimo sobrenome é "{lista[-1]}"')