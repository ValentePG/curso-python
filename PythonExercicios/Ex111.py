from UtilidadesCeV.Moeda import Moeda

p = float(input('Digite o preço:R$ ').replace(',', '.'))
Moeda.resumo(p, 80, 35)
