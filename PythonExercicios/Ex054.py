from datetime import date
m = 0
mn = 0
for c in range(1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    i = date.today().year - n
    if i < 21:
        mn += 1
    else:
        m += + 1
print('Há {} pessoas com 21 ou mais de 21 anos'.format(m))
print('Há {} pessoas menores de 21 anos'.format(mn))
