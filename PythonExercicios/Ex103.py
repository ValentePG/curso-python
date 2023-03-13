def ficha(nome='', gols=''):
    if nome == '' and gols == '':
        nome = '<desconhecido>'
        gols = 0
        gols = int(gols)
        return f'O jogador {nome} fez {gols} gols(s) no campeonato.'
    elif nome == '' and gols[0].isascii():
        nome = '<desconhecido>'
        gols = 0
        gols = int(gols)
        return f'O jogador {nome} fez {gols} gols(s) no campeonato.'
    elif gols == '':
        gols = 0
        gols = int(gols)
        return f'O jogador {nome} fez {gols} gols(s) no campeonato.'
    elif gols[0].isascii():
        gols = 0
        gols = int(gols)
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    else:
        return f'O jogador{nome} fez {gols} gol(s) no campeonato.'


# Principal
name = str(input('Nome do jogador: '))
gol = str(input('Gols: '))
resp = ficha(name, gol)
print(resp)
