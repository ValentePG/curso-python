pessoas = list()
dados = dict()
mulheres = list()
maiormedia = list()
qtd = sm = 0
while True:
    sexo = ''
    dados['nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        if sexo != 'M' and sexo != 'F':
            sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
        else:
            break
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    sm += dados['idade']
    qtd += 1
    if dados['sexo'] == 'F':
        mulheres.append(dados.copy())
    pessoas.append(dados.copy())
    resp = ''
    while True:
        if resp != 'S' and resp != 'N':
            resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
        else:
            break
    if resp in 'N':
        del dados
        break
print('-='*30)
m = sm/qtd
print(f'- Foram cadastradas {qtd} pessoas.')
print(f'- A média de idade do grupo é {m:.0f} anos.')
print(f'- As mulheres cadastradas foram', end=' ')
for c in mulheres:
    print(c['nome'], end=' ')
print(f'\n- Lista das pessoas acima da média;')
for c in pessoas:
    if c['idade'] > m:
        for k, v in c.items():
            print(f'{k} = {v};', end='')
        print('\n')
print('<<<ENCERRANDO>>>')
