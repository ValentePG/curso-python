valorcasa = float(input('\033[7;97mQual é o valor da casa que quer comprar?:R$\033[m '))
salario = float(input('\033[7;97mQuanto é o seu salário mensal?:R$\033[m '))
prestacao = int(input('\033[7;97mEm quantos anos você vai pagar a casa?:\033[m '))
anos = prestacao * 12
pm = valorcasa / anos
s = salario * 30 / 100
if pm > s:
    print('\033[7;97mEmpréstimo Negado!\033[m')
elif pm <= s:
    print('\033[7;97mEmpréstimo Aprovado!\033[m', end='')
    print('\033[7;97mO valor da prestação mensal é R${:.2f}\033[m'.format(pm))
