from Funçao import mtp
a = b = 0
while True:
    try:
        a = int(input('Digite um valor '))
        b = int(input('Digite outro valor '))
    except ValueError:
        print('\033[31mO número digitado não é inteiro\033[m')
        print('\033[32mPor favor digite um número inteiro!\033[m')
    if a != 0 and b != 0:
        break
mtp(a, b)
