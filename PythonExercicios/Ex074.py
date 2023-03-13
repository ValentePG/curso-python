from random import randint
tupla: tuple[int, int, int, int, int] = (randint(0, 10), randint(0, 10),
                                         randint(0, 10), randint(0, 10),
                                         randint(0, 10))
maior = menor = c = 0
print('Listagem de números: ', end='')
for t in tupla:
    '''if c == 0:
        maior = t
        menor = t
    if t > maior:
        maior = t
    if t < menor:
        menor = t'''
    print(f'{t}', end=' ')
    c += 1
'''print(f'\nO maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')'''
print(f'\nO maior número sorteado foi {max(tupla)}')
print(f'O menor número sorteado foi {min(tupla)}')
