from time import sleep
jogadores = list()
dados = dict()
golsfeitos = 0
while True:
    gols = list()
    total = 0
    print('-'*30)
    dados['nome'] = str(input('Nome Do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    for c in range(1, partidas+1):
        golsfeitos = int(input(f'Quantos gols {dados["nome"]} fez na {c}º partida: '))
        gols.append(golsfeitos)
        total += golsfeitos
    dados['gols'] = gols.copy()
    dados['total'] = total
    jogadores.append(dados.copy())
    resp = ''
    while True:
        if resp != 'S' and resp != 'N':
            resp = str(input('Quer Continuar?:[S/N] ')).upper().strip()[0]
        else:
            break
    del gols
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for n, c in enumerate(jogadores):
    print(f'{n:>3} ', end='')
    for f in c.values():
        print(f'{str(f):<15}', end='')
    print()
print('-'*40)
while True:
    cont = 0
    jogador = int(input('MOSTRAR DADOS DE QUAL JOGADOR?:(999 para parar) '))
    qtd = len(jogadores)-1
    if jogador <= qtd:
        print(f'--LEVANTAMENTO DO JOGADOR {jogadores[jogador]["nome"]}:')
        for c in jogadores[jogador]["gols"]:
            print(f'    No Jogo {cont+1} fez {c}.')
            sleep(1)
            cont += 1
    elif jogador > qtd and jogador != 999:
        print(f'ERRO NÃO EXISTE JOGADOR COM CÓDIGO {jogador}! Tente novamente.')
    elif jogador == 999:
        break
    print('-'*40)
print('ENCERRANDO...')
