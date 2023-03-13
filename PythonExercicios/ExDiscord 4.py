m1, v1 = input('Digite o nome e a velocidade do primeiro veículo: ').split()
m2, v2 = input('Digite o nome e a velocidade do segundo veículo: ').split()

v1 = v1.replace(',', '.')
v2 = v2.replace(',', '.')

v2 = float(v2)
v1 = float(v1)

if v1 > v2:
    print(f'O veículo {m1} é mais veloz!')
elif v2 > v1:
    print(f'O veículo {m2} é mais veloz!')
else:
    print(f'Tanto {m1} quanto {m2} tem a mesma velocidade')
