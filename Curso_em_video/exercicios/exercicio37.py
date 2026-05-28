num = int(input('Digite um número inteiro: '))

print('1 - Binário:')
print('2 - Octal:')
print('3 - Hexadecimal')
escolha =  int(input('Escolha a converção que você deseja fazer: (1, 2 ou 3) '))
condição = True

if escolha == 1:
    print('Binário:', bin(num))
elif escolha == 2:
    print('Octal:', oct(num))
elif escolha == 3:
    print('Hexadecimal:', hex(num))
else:
    print('Opção invalida!')