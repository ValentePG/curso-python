dados = dict()
gols = list()
total = cont = 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols {dados["nome"]} fez na partida {c}:')))
    total += gols[c]
dados['gols'] = gols.copy()
dados['total'] = total
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador joelson jogou {partidas}')
for c in dados['gols']:
    print(f'   => Na partida {cont}, fez {c} gols.')
    cont += 1
print(f'Foi um total de {dados["total"]}.')
