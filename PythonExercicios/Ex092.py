from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano De Contratação: '))
    dados['Salário'] = int(input('Salário:R$'))
    dados['Aposentadoria'] = (dados['Contratação'] - nascimento) + 35
print('-='*30)
for k, v in dados.items():
    print(f'{k} = {v}')
