largura = float(input('Largura da parede: '))
altura = float(input('altura da parede: '))
area = largura*altura
tinta = 2

print(f'sua parede tema a dimensão de {largura}x{altura} e sua área é de {area:.2f}m²')
print(f'Para pintar essa parede, você precisará de {area/tinta:.2f}l de tinta')