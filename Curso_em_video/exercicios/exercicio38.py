def num_maior(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "São iguais!"
    
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

print(f'O numero maior é: {num_maior(num1, num2)}')