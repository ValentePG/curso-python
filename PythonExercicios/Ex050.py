s = 0
p = 0
for c in range(1, 8):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        s += n
        p += 1
print('Você digitou {} valores pares e a soma deles é {}'.format(p, s))
