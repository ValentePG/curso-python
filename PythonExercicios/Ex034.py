s = float(input('Digite o seu salário:R$'))
if s > 1250:
    print('O salário com aumento de 10% é R${}'.format(s + (s * 10 / 100)))
else:
    print('O salário com aumento de 15% é R${}'.format(s + (s * 15 / 100)))
