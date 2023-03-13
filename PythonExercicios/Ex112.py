from UtilidadesCeV.Moeda import Moeda
from UtilidadesCeV.Dado import dado

p = dado.leiadinheiro('Digite o Preço:R$')
Moeda.resumo(p, 30, 50)

