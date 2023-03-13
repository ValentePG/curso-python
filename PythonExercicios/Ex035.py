r1 = float(input('Digite o comprimento da maior reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
# r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
if r2 + r3 > r1:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não formam um triângulo!')
