import Função
try:
    n = Função.leiaint('Digite um Valor: ')
except KeyboardInterrupt:
    n = 0
    print('\033[31mO usuário preferiu não inserir os dados\033[m')
try:
    m = Função.leiafloat('Digite um valor: ')
except KeyboardInterrupt:
    m = 0
    print('\033[31mO usuário preferiu não inserir os dados\033[m')
print(f'O número inteiro digitado foi {n} o número real foi {m}')
