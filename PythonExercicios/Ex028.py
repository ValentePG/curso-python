from random import randint as r
n = r(0, 5)
np = int(input('Digite um número entre 0 e 5 '))
if n == np:
    print('Você acertou!')
else:
    print('Você errou!')
