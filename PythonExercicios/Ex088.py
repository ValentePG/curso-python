from time import sleep
from random import randint
lista = list()
tot = 1
count = 0
print('-='*15)
print(f'{"MEGA SENA":^30}')
print('-='*15)
jogos = int(input('Quantos jogos quer que eu sorteie?:'))
print(f'{"-="*3} {"SORTEANDO"} {jogos} {"JOGOS"} {"-="*3}')
while tot <= jogos:
    while True:
        cpu = randint(1, 61)
        if cpu not in lista:
            lista.append(cpu)
            count += 1
        if count >= 6:
            count = 0
            break
    sleep(1)
    print(f'Jogo {tot}: {lista}')
    lista.clear()
    tot += 1
print(f'{"-="*5} {"BOA SORTE!"} {"-="*5}')

