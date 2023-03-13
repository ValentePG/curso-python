s = 0
i = int(input('Digite um valor: '))
for c in range(1, i + 1):
    if i % c == 0:
        print('\033[31m', end='')
        s += 1
    else:
        print('\033[32m', end='')
    print('{} '.format(c), end='')
if s == 2:
    print('\n\033[33mO número {} possui {} divisores e é um número primo!\033[m'.format(i, s))
else:
    print('\n\033[37mO número {} não é primo pois possui {} divisores\033[m'.format(i, s))
