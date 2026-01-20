#sorteia um aluno para apagar o quadro

import random

al1 = input('digite o seu nome: ')
al2 = input('digite o seu nome: ')
al3 = input('digite o seu nome: ')
al4 = input('digite o seu nome: ')

alunos = [al1,al2,al3,al4]
sorteio = random.choice(alunos)


print(f'o aluno sorteado para apagar o quadro foi:{sorteio}')