from math import radians, sin, cos, tan

angulo = float(input("digite o valor de um angulo: "))
angulo_r = radians(angulo)
seno = sin(angulo_r)
cossseno = cos(angulo_r)
tangente = tan(angulo_r)

print(f'os respectivos valores do angulo de {angulo}° são:')
print(f'seno: {seno:.2f}')
print(f'cosseno: {cossseno:.2f}')
print(f'tangente: {tangente:.2f}')