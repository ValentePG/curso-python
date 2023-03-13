t = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
decimo = t + (11 - 1) * r
for c in range(t, decimo, r):
    print('{}'.format(c), end=' -> ')
print('FIM')
