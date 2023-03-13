from random import randint
cpu = 1
player = 0
p = 0
while player != cpu: # JOGO MAIS DIFICIL
    cpu = randint(0, 10)
    print('=' * 50)
    player = int(input('Tente adivinhar o número que a cpu escolheu: '))
    if player != cpu:
        print('\033[31mA cpu escolheu {} e você {}, TENTE NOVAMENTE!!!\033[m'.format(cpu, player))
        p += 1
    elif player == cpu:
        print('\033[32mA cpu escolheu {} e você também! VOCÊ GANHOU!!!\033[m'.format(cpu))
        p += 1
print('Foram precisos {} palpites para vencer!'.format(p))

'''while not acertou: # JOGO MAIS FÁCIL
    jogador = int(input('Qual é o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = true
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        else:
            print('Menos...Tente mais uma vez.')
   print('Acertou com {} tentativas. Parabéns!'.format(p))'''
        
