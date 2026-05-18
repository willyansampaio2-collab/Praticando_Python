import random

alunos = ['pedro', 'ricardo', 'maria', 'jose', 'olivia', 'Willyan', 'augusto', 'lara', 'clara']
ordem = random.shuffle(alunos)

for numero, alunos in enumerate(alunos, start=1):
    print(f'{numero}º: {alunos}')