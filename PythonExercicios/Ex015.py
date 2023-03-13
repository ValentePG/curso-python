D = int(input('Quantos dias alugado? '))
Km = float(input('Quantos Km rodados? '))
aluguel = (60 * D) + (Km * 0.5)
print('O total a pagar é R${:.2f}'.format(aluguel))
