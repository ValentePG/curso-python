valor = list()
for c in range(0, 5):
    valor.append(int(input(f'Digite o {c}º valor: ')))
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} nas posições', end=' ')
for pos, c in enumerate(valor):
    if c == max(valor):
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(valor)} nas posições', end=' ')
for pos, c in enumerate(valor):
    if c == min(valor):
        print(f'{pos}...', end=' ')
