n1 = int(input('\033[31mDigite um valor: \033[m'))
n2 = int(input('\033[31mDigite outro valor: \033[m'))
s = n1 + n2
print('A soma dos valores {}{} e {}{} é {}{}{}'.format('\033[31m', n1, n2, '\033[m', '\033[33m', s, '\033[m'))
