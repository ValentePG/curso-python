from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?: '))
if jogador >= 3:
    print('JOGADA INVÁLIDA')
elif jogador >= 0:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 12)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 12)
    if computador == 0:
        if jogador == 0:
            print('O JOGO EMPATOU!')
        elif jogador == 1:
            print('VOCÊ GANHOU!')
        elif jogador == 2:
            print('VOCÊ PERDEU!')
    elif computador == 1:
        if jogador == 1:
            print('O JOGO EMPATOU!')
        elif jogador == 2:
            print('VOCÊ GANHOU!')
        elif jogador == 0:
            print('VOCÊ PERDEU!')
    elif computador == 2:
        if jogador == 1:
            print('VOCÊ PERDEU!')
        elif jogador == 2:
            print('O JOGO EMPATOU')
        elif jogador == 0:
            print('VOCÊ GANHOU!')
