n1 = int(input('digite um numero para ver sua tabuada: '))
print(f'-'*14)
for n in range(10):
    mult = n+1
    print(f'{n1} X {mult:2} = {n1*mult}')
print(f'-'*14)