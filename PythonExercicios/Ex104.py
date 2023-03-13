def leiaint(num):
    while True:
        num = str(input('Digite um valor: ')).strip()
        if num.isnumeric():
            num = int(num)
            break
        elif not num.isnumeric():
            print('\033[031mERRO!Digite um valor inteiro válido.\033[m')
    return num


n = leiaint('Digite um valor: ')
print(f'Você digitou o número {n}')
