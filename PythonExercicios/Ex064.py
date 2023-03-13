n = sm = qtd = 0
while n != 999:
    sm = sm + n
    qtd = qtd + 1
    n = int(input('Digite um número: '))
    if n == 999:
        qtd = qtd - 1
print('Foram digitados {} números e a soma entre eles deu {}'.format(qtd, sm))
