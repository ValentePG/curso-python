from time import sleep


def maior(*num):
    if len(num) == 0:
        print('Analisando os valores passados...')
        print('Foram informados 0 números ao todo.')
        print('O maior valor informado foi 0.')
    else:
        print('Analisando os valores passados...')
        for c in num:
            print(f'{c}', end=' ')
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')
        print('-='*30)


print('-='*30)
maior(2, 9, 4, 5, 6, 7, 8)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
