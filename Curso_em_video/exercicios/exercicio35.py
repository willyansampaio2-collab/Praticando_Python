r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Com esses três retas é possivel formar um triângulo.')
else:
    print('Não é possivel formar um triangulo com essas 3 retas.')