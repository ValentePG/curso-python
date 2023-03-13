from datetime import date


def voto(a=0):
    if a < 16:
        return 'não Vota!.'
    elif 18 <= a < 65:
        return 'é obrigado a votar!.'
    elif a > 65 or 18 > a >= 16:
        return 'não é obrigado a votar!.'


print('-='*15)
nasc = int(input('Ano de Nascimento: '))
i = date.today().year - nasc
print(f'Com {i} anos você {voto(i)}')
