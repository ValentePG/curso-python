t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
tr = int(input('Quantos termos deseja ver?: '))
c = 0
resp = 1
qtd = 0
while resp != 0:
    while c < tr:
        print('{}'.format(t), end=' -> ')
        t += r
        qtd += 1
        c += 1
    resp = int(input('Quantos termos deseja ver mais? '))
    if resp != 0:
        resp = resp + c
        while c < resp:
            print('{}'.format(t), end=' -> ')
            t += r
            qtd += 1
            c += 1
    else:
        print('Foram mostrados {} termos'.format(qtd))
