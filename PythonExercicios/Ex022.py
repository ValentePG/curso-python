nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} Letras'.format(len(nome.replace(' ', ''))))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
