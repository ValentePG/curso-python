fichas = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    fichas.append([nome, [nota1, nota2], média])
    resp = ''
    if resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar?:[S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-='*30)
print(f'{"No.":<4}  {"NOME":^10}  {"MÉDIA":>12}')
print('-'*30)
for c in range(0, len(fichas)):
    print(f'{c:<7} {fichas[c][0]:<12} {fichas[c][2]:>9.1f}')
while True:
    print('-' * 30)
    nota = int(input('Quer saber a nota de quem?(Digite 999 para cancelar): '))
    if nota <= len(fichas)-1:
        print(f'As notas do {fichas[nota][0]} foram {fichas[nota][1]}')
    if nota == 999:
        print('FINALIZANDO...')
        break
print('<<<<VOLTE SEMPRE>>>>')
