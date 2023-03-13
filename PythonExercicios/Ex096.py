def area(a, b):
    t = a * b
    print(f'A área do terreno {a}X{b} é de {t:.1f}m².')


print('     CONTROLE DE TERRENOS')
print('-'*30)
k = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
area(k, c)
