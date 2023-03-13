matriz = list()
linha1 = list()
linha2 = list()
linha3 = list()
mudou = False
soma = maior = 0
for c in range(0, 3):
    for i in range(0, 3):
        n = int(input(f'Digite o valor na posição {c, i}: '))
        if c == 0:
            linha1.append(n)
        elif c == 1:
            linha2.append(n)
        elif c == 2:
            linha3.append(n)
print('-='*30)
matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])
linha1.clear()
linha2.clear()
linha3.clear()
for c in matriz[0]:
    print(f'[{c:^5}]', end='')
    if c % 2 == 0:
        soma += c
mudou = True
for c1 in matriz[1]:
    if c1 > maior:
        maior = c1
    if c1 % 2 == 0:
        soma += c1
    if mudou:
        print()
        print(f'[{c1:^5}]', end='')
        mudou = False
    else:
        print(f'[{c1:^5}]', end='')
mudou = True
for c2 in matriz[2]:
    if c2 % 2 == 0:
        soma += c2
    if mudou:
        print()
        print(f'[{c2:^5}]', end='')
        mudou = False
    else:
        print(f'[{c2:^5}]', end='')
print()
print(f'{"-="*30}')
print(f'A soma dos valores pares digitados foi {soma}')
print(f'A soma dos valores na terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {maior}')
