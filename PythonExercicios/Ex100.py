from random import randint
from time import sleep


def sorteia(lista):
    """
    -> Preenche a lista com números sortidos.
    :param lista: lista numeros
    :return: none
    """

    print(f'Sorteando 5 valores da lista:', end='')
    for c in range(0, 5):
        num = randint(0, 10)
        sleep(0.5)
        lista.append(num)
        print(f' {num}', end='')
    print(' PRONTO!')


def somapar(par):
    sm = 0
    print(f'Somando os valores pares de {par}', end=',')
    for c in par:
        if c % 2 == 0:
            sm += c
    print(f'Temos {sm}')


numeros = list()
sorteia(numeros)
somapar(numeros)
