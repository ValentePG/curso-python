def mtp(x=0, y=0):
    c = 0
    if x < y:
        c = x
        x = y
        y = c
    if x == y:
        print('Os números digitados são iguais!')
    elif x % y == 0:
        print('Os números são múltiplos')
    else:
        print('Os números não são múltiplos')
