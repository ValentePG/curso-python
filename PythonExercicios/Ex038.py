n1 = int(input('\033[31mEscreva o primeiro número: '))
n2 = int(input('\033[34mEscreva o segundo número:\033[m '))
if n1 > n2:
    print('\033[31m{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('\033[34m{} é maior que {}'.format(n2, n1))
else:
    print('\033[32mOs dois números são iguais')
