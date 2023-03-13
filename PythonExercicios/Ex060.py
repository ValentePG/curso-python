# import factorial from math
n1 = int(input('Digite um valor para calcular o fatorial: '))
c = n1
fatorial = 1
while c > 0:  # FATORIAL COM WHILE
    if c != 1:
        print('{} X '.format(c), end='')
    elif c == 1:
        print('{} = {}'.format(c, fatorial))
    fatorial = fatorial * c
    c = c - 1
print('A fatorial de {} é {}'.format(n1, fatorial))

'''for c in range(n1, 0, -1): # FATORIAL COM FOR
    if c != 1:
        print('{} X '.format(c, c - 1), end='')
    elif c == 1:
        print('{} = {}'.format(c, fatorial))
    fatorial = fatorial * c
    c -= 1'''
