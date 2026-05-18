import math

angulo = int(input("digite o valor de um angulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'os respectivos valores do angulo de {angulo}° são:')
print(f'seno: {sen:.2f}')
print(f'cosseno: {cos:.2f}')
print(f'tangente: {tan:.2f}')