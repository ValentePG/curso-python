t = float(input('\033[34mDigite a nota do teste do aluno: '))
p = float(input('Digite a nota da prova do aluno:\033[m '))
m = (t + p) / 2
if m < 5.0:
    print('\033[31mA média do aluno foi {:.1f}'.format(m))
    print('ALUNO REPROVADO!\033[m')
elif 5.0 <= m < 6.9:
    print('\033[33mA média do aluno foi {:.1f}'.format(m))
    print('ALUNO EM RECUPERAÇÃO\033[m')
else:
    print('\033[32mA média do aluno foi {:.1f}'.format(m))
    print('ALUNO APROVADO\033[m')
