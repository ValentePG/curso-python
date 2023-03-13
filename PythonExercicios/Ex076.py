print('-='*30)
print(f'{"LISTAGEM DE PREÇOS":^55}')
print('-='*30)
tupla = ('Lápis', 1.75,
         'Borracha', 2.00,
         'caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
c = 0
for t in tupla:
    if c % 2 == 0:
        print(f'{t:.<50}', end='')
    else:
        print(f'R${t:>8.2f}')
    c += 1
print('-=' * 30)
