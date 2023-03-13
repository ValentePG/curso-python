def fatorial(a, show=False):
    """
    -> Função para calcular o fatorial e mostrar ou não o processo!
    :param a: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor da fatorial de um número n.
    """
    f = 1
    for c in range(a, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} =', end=' ')
    return f


print('-'*30)
n = int(input('Digite um número: '))
mostrar = str(input('Mostrar cálculo ou não?:[S/N]')).upper().strip()[0]
print('-'*30)
if mostrar == 'S':
    print(fatorial(n, show=True))
else:
    print(fatorial(n))
