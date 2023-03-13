from UtilidadesCeV.Moeda import Moeda

p = float(input('Digite o preço:R$ ').replace(',', '.'))
d = int(input('Quantos % de desconto ou acréscimo?: '))
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p, True)}')
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p, True)}')
print(f'{Moeda.moeda(p)} recebendo um aumento de {d}% vale {Moeda.aumentar(p, d, True)}')
print(f'{Moeda.moeda(p)} recebendo um desconto de {d}% vale {Moeda.diminuir(p, d, True)}')
