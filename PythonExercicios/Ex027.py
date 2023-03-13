nome = str(input('Digite seu nome completo: ').strip())
n = nome.split()
print('Primeiro nome: {}'.format(n[0].title()))
print('Último nome: {}'.format(n[len(n)-1].title()))
