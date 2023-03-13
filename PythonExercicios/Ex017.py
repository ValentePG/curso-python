from math import hypot
Co = float(input('Digite o valor do cateto oposto '))
Cad = float(input('Digite o valor do cateto adjacente '))
hi = hypot(Co, Cad)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
