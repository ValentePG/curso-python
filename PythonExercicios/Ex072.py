extenso = ('zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Douze',
           'Treze', 'Quatorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um valor entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente!', end='')
    print(f'Você digitou o número {extenso[n]}')
    while True:
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
