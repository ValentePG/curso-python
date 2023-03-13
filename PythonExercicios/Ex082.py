lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ''
    while resp != 'N' and resp != 'S':
        resp = str(input('Você quer continuar?:[S/N]')).strip().upper()
    if resp == 'N':
        break
par = list()
impar = list()
for c in lista:
    if c % 2 == 0:
        par.append(c)
    elif c % 2 != 0:
        impar.append(c)
lista.sort()
print(f'Os valores digitados na lista foram {lista}')
par.sort()
print(f'Os valores pares dentro da lista foram {par}')
impar.sort()
print(f'Os valores impares dentro da lista foram {impar}')
