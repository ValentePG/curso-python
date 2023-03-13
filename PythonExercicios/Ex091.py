from random import randint
from time import sleep
Count = 1
jogadores = {'player1': randint(1, 6), 'player2': randint(1, 6),
             'player3': randint(1, 6), 'player4': randint(1, 6)}
print('Valores sorteados')
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(1.5)
print('Ranking')
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'  {Count}º lugar:{i} com {jogadores[i]}')
    sleep(1.5)
    Count += 1
