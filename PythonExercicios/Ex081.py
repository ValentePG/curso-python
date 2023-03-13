lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = str(input('Você quer continuar?[S/N]')).strip().upper()
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'A ordem decrescente dos números na lista é {lista}')
print(f'A quantidade de valores dentro da lista é {len(lista)}')
contador = lista.count(5)
if contador > 0:
    print(f'O número 5 apareceu {contador} vezes nas posições', end=' ')
    for pos, c in enumerate(lista):
        if c == 5:
            print(f'{pos}...', end=' ')
else:
    print(f'O número 5 não foi digitado!')
