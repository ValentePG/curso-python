from datetime import date
sexo = str(input('\033[34mVocê é homem ou mulher?[M/H]\033[m')).upper()
if sexo == 'M':
    print('\033[32mVocê não é obrigada a se alistar no exército!\033[m')
elif sexo == 'H':
    nasc = int(input('\033[34mDigite o ano que você nasceu:\033[m '))
    i = date.today().year - nasc
    print('\033[34mVocê tem {} anos\033[m'.format(i))
    if i < 18:
        falta = 18 - i
        anoalist = nasc + 18
        print('\033[31mVocê ainda não se alistou faltam {} anos para estar apto,'.format(falta), end=' ')
        print('seu alistamento será em {}\033[m'.format(anoalist))
    elif i == 18:
        print('\033[32mVocê está na idade para se alistar vá representar a pátria!!!\033[m')
    else:
        anoalist = nasc + 18
        print('\033[37mVocê se alistou a {} anos,'.format(i - 18), end=' ')
        print('seu alistamento foi em {}\033[m'.format(anoalist))
else:
    print('\033[31mDigito inválido!Recomece!\033[m')
