from random import shuffle
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
a5 = [a1, a2, a3, a4]
shuffle(a5)
print('A ordem de apresentação será ')
print(a5)
