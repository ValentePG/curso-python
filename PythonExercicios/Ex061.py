t = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
c = 0
while c < 10:
    print('{}'.format(t), end=' -> ')
    t = t + r
    c += 1
print('FIM')
