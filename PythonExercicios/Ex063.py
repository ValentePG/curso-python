n = int(input('Quantos termos (a partir do terceiro) de uma fibonnaci você quer mostrar?: '))
c = 2
t1 = 0
t2 = 1
print('{} -> {} ->'.format(t1, t2), end=' ')
while c < n:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    if c <= n:
        print('{} -> '.format(t3), end='')
    c += 1
print('FIM')
