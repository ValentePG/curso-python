def aumentar(x=0, y=0, f=True):
    n = x * y / 100
    m = x + n
    if not f:
        return m
    else:
        return moeda(float(m))


def diminuir(x=0, y=0, f=True):
    n = x * y / 100
    m = x - n
    if not f:
        return m
    else:
        return moeda(float(m))


def dobro(x=0, f=True):
    n = x * 2
    if not f:
        return n
    else:
        return moeda(float(n))


def metade(x=0, f=True):
    n = x / 2
    if not f:
        return n
    else:
        return moeda(float(n))


def moeda(x):
    return f'{"R$"}{x:.2f}'.replace('.', ',')


def resumo(x, a=0, r=0):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    p = moeda(x).replace('.', ',')
    d = dobro(x).replace('.', ',')
    m = metade(x).replace('.', ',')
    g = aumentar(x, a).replace('.', ',')
    di = diminuir(x, r).replace('.', ',')
    print(f'{"Preço analisado:":<20}', end='')
    print(f'{p}')
    print(f'{"Dobro do preço:":<20}', end='')
    print(f'{d}')
    print(f'{"Metade do preço:":<20}', end='')
    print(f'{m}')
    print(f'{a}{"% de aumento:":<18}', end='')
    print(f'{g}')
    print(f'{r}{"% de desconto:":<18}', end='')
    print(f'{di}')
    print('-'*30)
