while True:
    print('=' * 35)
    # print('{:^35}'.format('BANCO CEV'))
    print(f"{'BANCO CEV':^35}")
    print('=' * 35)
    n = int(input('Que valor você quer sacar?:R$'))
    if n > 0:
        if n % 50 == 0:
            divi = n // 50
            if divi != 0:
                print(f'Será necessário {divi} cédulas de R$50')
        elif n % 50 != 0:
            divi = n // 50
            resto = n % 50
            if divi != 0:
                print(f'Será necessário {divi} cédulas de R$50')
            if resto % 20 == 0:
                divi = resto // 20
                if divi != 0:
                    print(f'Será necessário {divi} cédulas de R$20')
            elif resto % 20 != 0:
                divi = resto // 20
                if divi != 0:
                    print(f'Será necessário {divi} cédulas de R$20')
                resto = resto % 20
                if resto % 10 == 0:
                    divi = resto // 10
                    if divi != 0:
                        print(f'Será necessário {divi} cédulas de R$10')
                elif resto % 10 != 0:
                    divi = resto // 10
                    if divi != 0:
                        print(F'Será necessário {divi} cédulas de R$10')
                    resto = resto % 10
                    if resto % 1 == 0:
                        divi = resto // 1
                        if divi != 0:
                            print(f'Será necessário {divi} cédulas de R$1')
    print('=' * 35)
    Resp = str(input('Quer sacar mais?:[S/N] ')).strip().upper()
    while True:
        if Resp in 'SsNn':
            break
        else:
            Resp = str(input('Quer sacar mais?:[S/N] ')).strip().upper()
    if Resp == 'N':
        break
print('=' * 35)
print('VOLTE SEMPRE AO BANCO DO CURSO EM VIDEO! TENHA UM BOM DIA!')
