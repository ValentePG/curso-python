tupla = ('ESTUDAR', 'PROGRAMAR',
         'CADERNO', 'CODIGO',
         'PYTHON', 'CURSO',
         'GUSTAVO', 'GUANABARA',
         'JORGE', 'LIVRO',
         'COMPUTADOR', 'JOVEM')
for t in tupla:
    print(f'\nNa palavra {t} temos', end=' ')
    for letra in t:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
