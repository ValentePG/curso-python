valor = int(input('Digite o valor que será sacado: '))
lista = [50, 20, 10, 1]
c = 0
for elem in lista:
    while True:
        if elem <= valor:
            valor -= elem
            c += 1
        elif c > 0:
            print(f'{c} notas {elem}.')
            c = 0
            break
        else:
            break
#  Não faço a minima ideia do que aconteceu aqui!
