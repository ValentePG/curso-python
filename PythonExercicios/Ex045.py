from random import randint
from time import sleep
cpu = randint(1, 3)
print('\033[1;32m=' * 20)
print('\033[1;31m      JOKENPO')
print('\033[1;32m=' * 20)
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
player = int(input('Escolha uma opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if player == cpu:
    print('Os dois fizeram a mesma jogada!,\033[1;33mO JOGO EMPATOU!\033[m')
elif player == 1 and cpu == 2:
    print('A cpu jogou Papel e você jogou Pedra,\033[1;31mVOCÊ PERDEU!\033[m')
elif player == 1 and cpu == 3:
    print('A cpu jogou Tesoura e você jogou Pedra,\033[1;32mVOCÊ GANHOU!\033[m')
elif player == 2 and cpu == 1:
    print('A cpu jogou Pedra e você jogou Papel,\033[1;32mVOCÊ GANHOU!\033[m')
elif player == 2 and cpu == 3:
    print('A cpu jogou Tesoura e você jogou Papel,\033[1;31mVOCÊ PERDEU!\033[m')
elif player == 3 and cpu == 1:
    print('A cpu jogou Pedra e você jogou Tesoura,\033[1;31mVOCÊ PERDEU!\033[m')
elif player == 3 and cpu == 2:
    print('A cpu jogou Papel e você jogou Tesoura,\033[1;32mVOCÊ GANHOU!\033[m')
else:
    print('JOGADA INVÁLIDA!!!')
print('\033[1;31mFINALIZANDO . . .')
sleep(2)
