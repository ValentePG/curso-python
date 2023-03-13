d = float(input('Qual é a distância da viagem em km: '))
if d <= 200:
    p = d * 0.50
    print('O preço da passagem é R${}'.format(p))
else:
    p = d * 0.45
    print('O preço da passagem é R${}'.format(p))
