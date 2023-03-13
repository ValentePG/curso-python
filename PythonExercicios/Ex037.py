from time import sleep
print('\033[31m-' * 20)
n = int(input('Digite um valor: '))
print('-' * 20)
print('\033[97m[1].BINÁRIO')
print('\033[34m[2].OCTAL')
print('\033[33m[3].HEXADECIMAL\033[m')
print('\033[31m-' * 20)
c = int(input('\033[31mQual a base de conversão quer usar?'))
if c == 1:
    bina = bin(n)[2:]
    print('O número {} convertido em binário é {}'.format(n, bina))
elif c == 2:
    octa = oct(n)[2:]
    print('O número {} convertido para octal é {}'.format(n, octa))
elif c == 3:
    hexa = hex(n)[2:]
    print('O número {} convertido para hexadecimal é {}'.format(n, hexa))
else:
    print('Opção Inválida')
print('Finalizando. . .')
sleep(3)
