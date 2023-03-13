from time import sleep
n = sm = qtd = maior = menor = 0
while n != 2:
    print('='*30)
    print('       Escolha entre'
          '\n[1]Digitar um número'
          '\n[2]Parar o programa')
    n = int(input('Digite uma opção: '))
    if n == 1:
        n1 = int(input('Digite um valor: '))
        sm += n1
        qtd += 1
        if qtd == 1:
            maior = menor = n1
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
    else:
        print('=' * 30)
        print('FINALIZANDO . . .')
        print('=' * 30)
        sleep(1)
if qtd != 0:
    m = sm / qtd
    print('foram digitados {} números  e a soma deles foi {} e a média é {:.2f}'.format(qtd, sm, m))
    print('O maior foi {} e o menor foi {}'.format(maior, menor))
