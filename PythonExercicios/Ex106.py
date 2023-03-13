def sistema(txt):
    a = len(txt) + 4
    print('\033[30;46m~'*a)
    print(f'  {txt}')
    print('~'*a)


def acessando(ajuda):
    from time import sleep
    a = f'Acessando Manual do comando {ajuda}'
    b = len(a) + 4
    print('\033[30;43m~'*b)
    print(f' {a}')
    print('~'*b)
    sleep(0.5)
    return help(ajuda)


while True:
    sistema('SISTEMA DE AJUDA PYhelp')
    FB = str(input('\033[mFunção ou biblioteca > ')).lower().strip()
    if FB == 'fim':
        break
    else:
        acessando(FB)
print('\033[31;107mATÉ A PRÓXIMA!')
