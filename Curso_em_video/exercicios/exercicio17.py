import math

cat_op = float(input("digite o comprimento do cateto oposto: "))
cat_adj = float(input("digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cat_op, cat_adj)

print(f"o comprimento da hipotenusa é: {hipotenusa:.2f}")