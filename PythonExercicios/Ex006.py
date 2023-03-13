n = int(input('\033[4;7;97mDigite um valor:\033[m '))
print('\033[31mO dobro de {} é {} \033[m \n\033[34mO triplo de {} é {}\033[m'.format(n, (n*2), n, (n*3)))
print('\033[33mA raiz quadrada de {} é {:.1f}\033[m'.format(n, (n**(1/2))))
