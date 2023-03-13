from time import sleep
r1 = float(input('\033[7;97mDigite o valor da primeira reta:\033[m '))
r2 = float(input('\033[7;97mDigite o valor da segunda reta:\033[m '))
r3 = float(input('\033[7;97mDigite o valor da terceira reta:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 != r2 != r3 != r1:
     print('\033[7;97mTriângulo Escaleno\033[m')
    elif r1 == r2 == r3:
     print('\033[7;97mTriangulo Equilátero\033[m')
    else:
     print('\033[7;97mTriângulo Isóiceles\033[m')
else:
     print('\033[7;97mEssas retas não formam um triângulo!\033[m')
print('\033[7;97mFINALIZANDO. . .\033[m')
sleep(2)
