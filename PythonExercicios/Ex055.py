mp = 0
mn = 0
for c in range(1, 6):
    p = float(input('Digite o {}o peso: '.format(c)))
    if c == 1:
        mp = p
        mn = p
    else:
        if p > mp:
            mp = p
        elif p < mn:
            mn = p
print('O maior peso foi {}Kg'.format(mp))
print('O menor peso foi {}Kg'.format(mn))
