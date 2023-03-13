people = list()
heavy = list()
thin = list()
register = 0
maior = menor = 0
while True:
    n = str(input('Name: ')).capitalize().strip()
    p = float(input('Weight: '))
    resp = ''
    people.append(n)
    people.append(p)
    register += 1
    while resp != 'N' and resp != 'Y':
        resp = str(input('You want stop?[Y/N]')).strip().upper()
    if resp == 'Y':
        break
print('-=' * 30)
print(f'Foram cadastradas {register} pessoas!')
for pos, c in enumerate(people):
    if type(c) == float:
        if pos == 1:
            maior = menor = c
            thin.append(people[pos-1])
            heavy.append(people[pos-1])
        elif pos != 1:
            if c > maior:
                heavy.clear()
                heavy.append(people[pos-1])
                maior = c
            elif c == maior:
                heavy.append(people[pos-1])
            if c < menor:
                thin.clear()
                thin.append(people[pos-1])
                menor = c
            elif c == menor:
                thin.append(people[pos-1])
print(f'O maior peso foi {maior}Kg. Peso de', end=' ')
for n in heavy:
    print(f'[{n}]', end=' ')
print()
print(f'O menor peso foi {menor}Kg. Peso de', end=' ')
for n in thin:
    print(f'[{n}]', end=' ')
