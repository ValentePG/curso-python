from time import sleep
from Função import leiaidade
from Ex115.Arquivo import *


def escolhas():
    from Função import leiaint
    arq = 'cursoemvideo.txt'
    if not arquivoExiste(arq):
        criarArquivo(arq)
    while True:
        op = 0
        menu()
        try:
            op = leiaint('Opção: ')
            if op == 1:
                op1(arq)
            elif op == 2:
                op2(arq)
            elif op == 3:
                op3()
            else:
                print(f'\033[31mERRO:Digite um número entre as opções do MENU!\033[m')
        except (TypeError, ValueError):
            print(f'\033[31mERRO:Digite um número entre as opções do MENU!\033[m')
        except KeyboardInterrupt:
            sleep(1)
            print(f'\033[31mFinalizando o Programa!\033[m')
            break
        if op == 3:
            sleep(1)
            print(f'\033[31m    Finalizando o programa!\033[m')
            print(f'='*30)
            break


def menu():
    print('='*30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('='*30)
    print(f'\033[33m1 - \033[m\033[34mVer pessoas cadastradas\033[m')
    print(f'\033[33m2 - \033[m\033[34mCadastrar nova Pessoa\033[m')
    print(f'\033[33m3 - \033[m\033[34mSair do sistema\033[m')
    print('='*30)


def op1(nome=''):
    sleep(0.5)
    print('='*30)
    print(f'{"OPÇÃO 1":^30}\033[m')
    print('='*30)
    sleep(0.5)
    lerArquivo(nome)
    sleep(0.5)


def op2(arq=''):
    sleep(0.5)
    print('='*30)
    print(f'{"OPÇÃO 2":^30}')
    print('='*30)
    sleep(0.5)
    print('='*30)
    print(f'{"NOVO CADASTRO":^30}')
    print('='*30)
    nome = str(input('Nome: ')).strip()
    idade = leiaidade('Idade: ')
    cadastrar(arq, nome, idade)


def op3():
    sleep(0.5)
    print('='*30)
    print(f'{"OPÇÃO 3":^30}')
    print('='*30)
