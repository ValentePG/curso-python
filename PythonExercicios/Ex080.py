lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.insert(0, n)
        print('Inserindo valor ao final da lista')
    if c == 1:
        if n > lista[0]:
            lista.insert(1, n)
            print('Inserindo valor ao final da lista')
        elif n < lista[0]:
            lista.insert(0, n)
            print('Inserindo valor a posição 0!')
    if c == 2:
        if n < lista[0]:
            lista.insert(0, n)
            print('Inserindo valor na posição 0!')
        elif n > lista[1]:
            lista.insert(2, n)
            print('Inserindo valor na posição 2!')
        elif lista[0] < n < lista[1]:
            lista.insert(1, n)
            print('Inserindo valor na posição 1')
    if c == 3:
        if n < lista[0]:
            lista.insert(0, n)
            print('Inserindo valor na posição 1')
        elif n > lista[2]:
            lista.insert(3, n)
            print('Inserindo valor ao final da lista')
        elif lista[0] < n < lista[2]:
            if n > lista[1]:
                lista.insert(2, n)
                print('Inserindo valor na posição 2!')
            elif n < lista[1]:
                lista.insert(1, n)
                print('Inserindo valor na posição 1!')
    if c == 4:
        if n < lista[0]:
            lista.insert(0, n)
            print('Inserindo valor na posição 0!')
        elif n > lista[3]:
            lista.insert(4, n)
            print('Inserindo valor na posição 4!')
        elif lista[0] < n < lista[3]:
            if n < lista[1]:
                lista.insert(1, n)
                print('Inserindo valor na posição 1!')
            elif n > lista[2]:
                lista.insert(3, n)
                print('Inserindo valor na posição 3!')
            elif n < lista[2]:
                lista.insert(2, n)
                print('Inserindo valor na posição 2!')
            elif lista[1] > n > lista[2]:
                lista.insert(2, n)
                print('Inserindo valor na posição 2!')
print(f'Os valores digitados em ordem foram {lista}')
