import os
import platform
def limpar_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

limpar_tela()
frase = 'curso em video python'
print("=" * 128)
print("""
 █████╗ ███╗   ██╗ █████╗ ██╗     ██╗███████╗███████╗
██╔══██╗████╗  ██║██╔══██╗██║     ██║██╔════╝██╔════╝
███████║██╔██╗ ██║███████║██║     ██║███████╗█████╗
██╔══██║██║╚██╗██║██╔══██║██║     ██║╚════██║██╔══╝
██║  ██║██║ ╚████║██║  ██║███████╗██║███████║███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚══════╝
""".center(128))
#len serve para te dizer a quantidade de algo.
qnt_caracter = len(frase)
#count serve para fazer contagem de quantas vezes algo aparece. funciona em tipos como: strings, listas, tuplas.
contagem = frase.count('o')
contagem_limitada = frase.count('o', 0, 13)
#já o find serve para encontrar algo, ele procura a posição onde aparece, caso nã exista ele retorna o valor "-1".
procura = frase.find('deo')
procura_nada = frase.find('android')
#O in serve para verificar se um valor existe dentro de algo.
existe = 'curso' in frase

print("LEN:")
print(f' O (len) serve para dizer a quantidade. Na variavel frase: "{frase}", o len vai dar o resultado de {qnt_caracter} caracteres.')
print()
print('COUNT:')
print(f' O (count) ele serve para fazer a contagem de algo: aparecem {contagem} "o" na frase: "{frase}".')
print(f' Outro metodo de utilizar o (count) é definindo um indice: aparecem {contagem_limitada} "o" na frase "{frase}" do indice 0 ao 13.')
print()
print('FIND:')
print(f' O (find) serve para encontrar algo, ele procura a posição onde aparece. Na frase "{frase}", a string "deo" começa\n no indice {procura}.')
print(f' Caso o argumento do (find) não seja encontrado ele retorna o valor {procura_nada}.')
print()
print('IN:')
print(f' O (in), ele é usado para verificar se um valor existe dentro de algo. Se existir ele retorna o valor: {existe}.')
print()

print("=" * 128)
print("""
████████╗██████╗  █████╗ ███╗   ██╗███████╗███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗  ██████╗ █████╗  ██████╗
╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗██╔═══██╗
   ██║   ██████╔╝███████║██╔██╗ ██║███████╗█████╗  ██║   ██║██████╔╝██╔████╔██║███████║██║     ███████║██║   ██║
   ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║██║     ██╔══██║██║   ██║
   ██║   ██║  ██║██║  ██║██║ ╚████║███████║██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝
""".center(128))

frase2 = '   Aprendendo Python  '
#O replace serve para substituir texto por outro texto.
substituir = frase.replace('python', 'Android')
#o upper() serve para transformar o texto em MAIÚSCULO.
maiusculo = frase.upper()
#o lower() serve para transformar o texto em minúsculo.
minusculo = frase.lower()
#o capitalize torna a Primeira letra maiúscula.
capitalizar = frase.capitalize()
#o title torna a Primeira Letra De Cada Palavra Maiúscula.
titulo = frase.title()
#Remove espaços das pontas tanto no inicio como no final.
limpar = frase2.strip()
limpar_direita = frase2.rstrip()
limpar_esquerda = frase2.lstrip()
#O split divide o texto em uma lista com cada palavra.
lista = frase.split()
#O join é o inverso do split, ele junta textos.
juntar = ' '.join(lista)

print('REPLACE:')
print(f' O (replace) substituí um texto por outro, a frase: "{frase}" vai ficar: "{substituir}".')
print()
print('UPPER:')
print(f' O (upper) serve para transformar o texto em MAIÚSCULO: "{maiusculo}".')
print()
print('LOWER:')
print(f' O (lower) serve para transformar o texto em minúsculo: "{minusculo}".')
print()
print('CAPITALIZE:')
print(f' O (capitalize) torna somente a Primeira letra maiúscula: "{capitalizar}".')
print()
print('TITLE:')
print(f' O (title) torna somente a Primeira letra maiúscula de cada palavra: "{titulo}".')
print()
print('STRIP:')
print(f' O (strip) ele vai remover espaços no inicio e no final das frases.')
print(f' Nesse exemplo a frase: "{frase2}", vai ficar: "{limpar}".')
print(f' Também da pra remover do lado desejado // direita: "{limpar_direita}", esquerda: "{limpar_esquerda}".')
print()
print('SPLIT:')
print(f' O (split) ele divide as palavras e cria uma lista. A frase: "{frase}" -> {lista}.')
print()
print('JOIN:')
print(f' O (join) é o contrario de split, ele junta as palavras. A lista: "{lista}" -> {juntar}.')
print()
print("=" * 128)
