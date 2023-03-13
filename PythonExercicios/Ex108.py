from UtilidadesCeV.Moeda import Moeda

p = float(input('Digite o preço: ').replace(',', '.'))
d = int(input('Quantos % de desconto ou acréscimo?: '))
print(f'O dobro de R${Moeda.moeda(p)} é R${Moeda.moeda(Moeda.dobro(p))}')
print(f'A metade de R${Moeda.moeda(p)} é R${Moeda.moeda(Moeda.metade(p))}')
print(f'R${Moeda.moeda(p)} recebendo um aumento de {d}% vale R${Moeda.moeda(Moeda.aumentar(p, d))}')
print(f'R${Moeda.moeda(p)} recebendo um desconto de {d}% vale R${Moeda.moeda(Moeda.diminuir(p, d))}')
