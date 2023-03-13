n = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o último valor: '))
nove = totpar = post = 0
mudou = False
tupla: tuple[int, int, int, int] = (n, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
for pos, t in enumerate(tupla):
    if t == 9:
        nove += 1
    if t == 3:
        post = pos
        mudou = True
    if t % 2 == 0:
        totpar += 1
if nove == 0:                                               # print(f'O valor 9 apareceu {Tupla.count(9)} vezes')'''
    print('O número 9 não foi digitado!')
else:
    print(f'O número 9 foi digitado {nove} vezes')
if mudou:
    print(f'O número 3 foi digitado na {post+1}ª posição')   # print(f'O valor 3 apareceu na {Tupla.index(3)}ª posição')
else:
    print(f'O número 3 não foi digitado!')
print('Os valores pares foram ', end='')
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')
