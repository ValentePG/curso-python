tot = caro = menor = c = 0
nomemenor = ' '
while True:
    print('-' * 40)
    nome = str(input('Digite o nome do produto: '))
    price = float(input('Digite o preço do produto:R$'))
    print('-' * 40)
    while c < 1:  # if cont == 0 or price < menor: menor = price nomemenor = nome
        menor = price
        nomemenor = nome
        c += 1
    if price < menor:
        menor = price
        nomemenor = nome
    tot += price   # c += 1 ficaria aqui no caso acima
    if price > 1000:
        caro += 1
    resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    while True:
        if resp in 'SsnN':
            break
        else:
            resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 40)
print(f'O total gasto com a compra foi R${tot:.2f}')
print(f'{caro} produtos tem o preço acima de R$1000')
print(f'O nome do produto mais barato é {nomemenor} custando R${menor:.2f}')
