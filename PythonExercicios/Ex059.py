from time import sleep
resp = 0
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
print('='*50)
print('               OPÇÕES MATEMÁTICAS              ')
print('='*50)
while resp != 5:
    print('[1]SOMAR'
          '\n[2]MULTIPLICAR'
          '\n[3]MAIOR'
          '\n[4]NOVOS NÚMEROS'
          '\n[5]Sair do programa')
    print('='*50)
    resp = int(input('Escolha sua opção: '))
    if resp == 1:
        print('O número {} e o número {} somados resultam em {}'.format(n1, n2, n1 + n2))
    elif resp == 2:
        print('O número {} e o número {} múltiplicados resultam em {}'.format(n1, n2, n1 * n2))
    elif resp == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        else:
            print('O número {} é maior que o número {}'.format(n2, n1))
    elif resp == 4:
        n1 = int(input('Escolha um novo número: '))
        n2 = int(input('Escolha outro novo número: '))
    elif resp == 5:
        print('FINALIZANDO. . .')
    else:
        print('Digito Inválido')
    sleep(2)
    print('='*50)
