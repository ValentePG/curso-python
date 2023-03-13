from random import randint
from time import sleep
g = 0
while True:
    cpu = randint(1, 10)
    print('\033[34m-=' * 10)
    print('   PAR OU IMPAR')
    print('-=' * 10)
    n = int(input('Diga um valor entre 1 e 10: '))
    while True:
        if 10 >= n > 0:
            break
        else:
            n = int(input('Diga um valor entre 1 e 10: '))
    choice = str(input('Você quer PAR ou IMPAR?:[P/I]\033[m ')).strip().upper()[0]
    while True:
        if choice in 'PiIp':
            break
        else:
            choice = str(input('\033[34mVocê quer PAR ou IMPAR?:[P/I]\033[m ')).strip().upper()[0]
    print('\033[33m-\033[m' * 60)
    sm = cpu + n
    print(f'\033[7;97mA cpu escolheu {cpu} e você escolheu {n}.Total de {sm}', end=' ')
    if sm % 2 == 0:  # PAR
        print('DEU PAR\033[m')
        if choice == 'P':
            sleep(0.5)
            print('\033[32mVOCÊ GANHOU!!!')
            g += 1
        elif choice == 'I':
            sleep(0.5)
            print('\033[31mVOCÊ PERDEU!!!\033[m')
            break
    else:  # IMPAR
        print('DEU IMPAR\033[m')
        if choice == 'P':
            sleep(0.5)
            print('\033[31mVOCÊ PERDEU!!!\033[m')
            break
        elif choice == 'I':
            sleep(0.5)
            print('\033[32mVOCÊ GANHOU!!!')
            g += 1
    print('Vamos Jogar Novamente\033[m')
    print('\033[33m-\033[m' * 60)
print('\033[33m-\033[m' * 60)
sleep(0.5)
print(f'\033[31mGAME OVER!\033[m \033[32mVOCÊ GANHOU {g} VEZES\033[m')
