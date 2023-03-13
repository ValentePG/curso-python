Tabela = ('Palmeiras', 'Internacional', 'Flamengo',
          'Fluminense', 'Corinthians', 'Athlético-PR',
          'Atlético-MG',
          'América-MG',
          'Fortaleza', 'São Paulo', 'Botafogo',
          'Santos', 'Bragantino', 'Goiás', 'Coritiba',
          'Ceará', 'Cuiabá', 'Atlético Goianianse',
          'Avaí', 'Juventude')
print('=' * 30)
print('    TABELA DO BRASILEIRÃO')
print('=' * 30)
print(f'Lista de times {Tabela}')
print('=' * 30)
print(f'Os primeiros 5 colocados são {Tabela[0:5]}')
print('=' * 30)
print(f'Os 4 últimos colocados da tabela são {Tabela[16:21]}')
print('=' * 30)
print(f'Os times em ordem alfabética:{sorted(Tabela)}')
print('=' * 30)
for pos, time in enumerate(Tabela):  # print(f'O flamengo está na posição {Tabela.index("Flamengo")+1} posição')
    if time == 'Flamengo':
        print(f'O Flamengo está na {pos+1}ª posição')
