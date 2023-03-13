maiori = h = m = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('IDADE: '))
    s = str(input('SEXO:[M/F] ')).strip().upper()[0]
    while True:
        if s in 'MmFf':
            break
        else:
            s = str(input('SEXO:[M/F] ')).strip().upper()[0]
    if i > 18:
        maiori += 1
    if s == 'M':
        h += 1
    elif s == 'F':
        if i < 20:
            m += 1
    print('-' * 30)
    resp = str(input('Quer continuar?:[S/N] ')).strip().upper()[0]
    while True:
        if resp in 'SsNn':
            break
        else:
            resp = str(input('Quer continuar?:[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'Há {maiori} pessoas com mais de 18 anos e {h} homens cadastrados')
print(f'Há {m} mulheres abaixo de 20 anos')
