cidade = str(input('digite o nome da sua Cidade: ')).strip().title()
if cidade.startswith('Santo'):
    print(f'A cidade: {cidade} começa com a palavra "santo".')
else:
    print(f'A cidade: {cidade} não começa com a palavra "santo".')