'''aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*30)
if aluno['média'] < 7:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'APROVADO'
for i in aluno.keys():  # KEYS
    print(f' - {i} é igual a {aluno[i]}')'''

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}:'))
print('-='*30)
if 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
elif aluno['Media'] < 5:
    aluno['Situação'] = 'REPROVADO'
else:
    aluno['Situação'] = 'APROVADO'
for k, v in aluno.items():    # ITEMS
    print(f'{k} é igual a {v}')
