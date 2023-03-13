from UtilidadesCeV.Moeda import Moeda

p = float(input('Digite o preço: '))
d = int(input('Quantos % de desconto ou acréscimo?: '))
print(f'O dobro de R${p:.2f} é R${Moeda.dobro(p)}.')
print(f'A metade de R${p:.2f} é R${Moeda.metade(p)}.')
print(f'R${p:.2f} recebendo um aumento de {d}% vale R${Moeda.aumentar(p, d)}.')
print(f'R${p:.2f} recebendo um desconto de {d}% vale R${Moeda.diminuir(p, d)}.')
