lista = list()
removeu = False
while True:
    n = int(input('Digite um valor: '))
    resp = ''
    lista.append(n)
    for n in lista:
        if lista.count(n) >= 2:
            lista.remove(n)
            removeu = True
    if removeu:
        print('Número duplicado!Não vou adicionar!')
        removeu = False
    else:
        print('Número adicionado com sucesso!')
    while resp != 'N' and resp != 'S':
        resp = str(input('Quer continuar?[S/N]')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')
