''' EXERCICIO 86 MELHORADO: '''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]:'))
        if matriz[l][c] == 0:
            maior = matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*20)
print(f'A soma dos valores pares digitados foi {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')
