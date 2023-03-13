from time import sleep


def contador(i, f, p):
    if f > i:
        for i in range(i, f + 1, p):
            print(f'{i}', end=' ')
            sleep(0.5)
        print('FIM!')
    elif f < i:
        for i in range(i, f - 1, -p):
            print(f'{i}', end=' ')
            sleep(0.5)
        print('FIM!')


# Principal
print('Mostrando Contagem de 1 até 10 pulando de 1 em 1')
contador(1, 10, 1)
print('-=' * 30)
print('Mostrando Contagem de 10 até 0 pulando de 2 em 2')
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('início: '))
b = int(input('Fim:    '))
c = int(input('Passo:  '))
print('-=' * 30)
if c < 0:
    c *= -1
if c == 0:
    print(f'Contagem de {a} até {b} de 1 em 1')
    contador(a, b, 1)
else:
    print(f'Contagem de {a} até {b} de {c} em {c}')
    contador(a, b, c)
print('-=' * 30)
