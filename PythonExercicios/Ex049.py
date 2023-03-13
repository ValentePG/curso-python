print('\033[31m-=' * 20)
t = int(input('Quer saber a tabuada de qual número?:\033[m '))
print('\033[31m-=\033[m' * 20)
for c in range(0, 11):
    m = t * c
    print('\033[31m{}  X {:2} = {}'.format(t, c, m))
print('FIM . . .\033[m')

# print(f"{t} X {c:2)} = {m}") = NOVO FORMAT

# print('{} X {:2} = {}'.format(t, c, m)) = ANTIGO FORMAT
