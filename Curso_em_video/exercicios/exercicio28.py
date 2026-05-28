import random

numero = random.randint(0, 5)
num = int(input('Tente adivinhar o numero que eu escolhi de 0 a 5: '))

if num == numero:
    print(f'Parabens você acertou.')
    print(f'O número que eu escolhi foi {numero}.')
else:
    print('Você errou!')
    print(f'O número que eu escolhi foi {numero}.')