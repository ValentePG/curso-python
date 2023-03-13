sm = qtd = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    qtd += 1
    sm += n
print(f'Foram digitados {qtd} e a soma entre eles foi {sm}')
