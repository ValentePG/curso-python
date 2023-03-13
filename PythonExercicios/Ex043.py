P = float(input('\033[34mDigite seu peso em KG:\033[m '))
A = float(input('\033[34mDigite sua altura:\033[m '))
IMC = P / (A ** 2)
if IMC < 18.5:
    print('\033[31mSeu imc é {:.2f}'.format(IMC))
    print('ABAIXO DO PESO\033[m')
elif 18.5 <= IMC < 25:
    print('\033[32mSeu imc é {:.2f}'.format(IMC))
    print('PESO IDEAL\033[m')
elif 25 <= IMC < 30:
    print('\033[31mSeu imc é {:.2f}'.format(IMC))
    print('SOBRE PESO\033[m')
elif 30 <= IMC < 40:
    print('\033[31mSeu imc é {:.2f}'.format(IMC))
    print('OBESIDADE\033[m')
else:
    print('\033[31mSeu imc é {:.2f}'.format(IMC))
    print('OBESIDADE MÓRBIDA\033[m')
