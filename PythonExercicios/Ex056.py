sm = 0
menosde = 0
maioridade = 0
m = 0
maisvelho = ''
for c in range(1, 5):
    print('\033[31m========== {}ª PESSOA ==========\033[m'.format(c))
    n = str(input('\033[32mQual é o seu nome:\033[m ')).strip()
    i = int(input('\033[33mQual é a sua idade:\033[m '))
    s = str(input('\033[34mQual é o seu sexo:[F/M]\033[m ')).lower().strip()
    sm += i
    m = sm / 4
    if s == 'm':
        if i > maioridade:
            maioridade = i
            maisvelho = n
    elif s == 'f':
        if i < 20:
            menosde += 1
    else:
        print('COMANDO INVÁLIDO!')
print('A média de idade do grupo é {:.1f} anos'.format(m))
print('O nome do homem mais velho é {} com {} anos'.format(maisvelho, maioridade))
print('Há {} mulheres com menos de 20 anos'.format(menosde))
