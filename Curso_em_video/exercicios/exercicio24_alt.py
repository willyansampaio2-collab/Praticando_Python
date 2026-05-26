cidade = str(input('digite o nome da sua Cidade: ')).strip().title()
if cidade[:5] == 'Santo':
    print(f'A cidade: {cidade} começa com a palavra "Santo".')
else:
    print(f'A cidade: {cidade} não começa com a palavra "Santo".')