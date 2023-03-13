c = 1
f = 0
m = 0
while c < 6:
    print('=' * 35)
    sex = str(input('Digite o sexo da {}ª pessoa:[M/F] '.format(c))).lower().strip()[0]
    if sex == 'f':
        print('Sexo Feminino registrado com sucesso!')
        c += 1
        f += 1
    elif sex == 'm':
        print('Sexo Masculino registrado com sucesso!')
        m += 1
        c += 1
    else:
        print('Digito inválido!')
print('=' * 35)
print('Foram registradas {} pessoas no programa sendo elas {} femininos e {} masculinos'.format((c - 1), f, m))

'''while sex not in 'MmFf'
        sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().lower()[0]
   print('Sexo {} registrado com sucesso'.format(sex))'''
