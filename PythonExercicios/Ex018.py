import math
a = float(input('Digite o valor de um ângulo '))
ar = math.radians(a)
s = math.sin(ar)
c = math.cos(ar)
t = math.tan(ar)
print('O cosseno do ângulo {} é {:.2f} a tangente é {:.2f} e o seno é {:.2f}'.format(a, c, t, s))
