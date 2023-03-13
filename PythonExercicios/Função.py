def leiaint(num):
    while True:
        num = str(input('\033[32mOpção: \033[m')).strip()
        try:
            num = int(num)
        except (TypeError, ValueError):
            break
        if type(num) == int:
            break
    return num


def leiaidade(num):
    while True:
        num = str(input('Idade: ')).strip()
        try:
            num = int(num)
        except (TypeError, ValueError):
            break
        if type(num) == int:
            break
    return num


def leiafloat(num):
    while True:
        num = str(input('Digite um número real: ')).replace(',', '.')
        try:
            num = float(num)
        except (TypeError, ValueError):
            print(f'\033[31mERRO:Digite um número real válido: \033[m')
        if type(num) == float:
            if num == 0.0:
                num = 0
            break
    return num

