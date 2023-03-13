from datetime import date
anonasc = int(input('\033[34mDigite seu ano de nascimento:\033[m '))
i = date.today().year - anonasc
print('\033[31mO atleta tem {} anos\033[m'.format(i))
if i <= 9:
    print('\033[35mCATEGORIA MIRIM')
elif i <= 14:
    print('\033[33mCATEGORIA INFANTIL')
elif i <= 19:
    print('\033[32mCATEGORIA JUNIOR')
elif i == 20:
    print('\033[31mCATEGORIA SÊNIOR')
else:
    print('\033[30mCATEGORIA MASTER\033[m')
