while True:
    c = 1
    print('-=' * 20)
    n = int(input('Quer ver a tabuada de qual número?: '))
    print('-=' * 20)
    if n < 0:
        break
    while c <= 10:  # for c in range (1, 11):
        m = n * c
        print(f'{n} x {c:2} = {m}')
        c += 1
print('FINALIZANDO. . .')
