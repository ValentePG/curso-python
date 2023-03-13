f = str(input('Digite uma frase qualquer: ')).replace(' ', '').lower()
tpf = f[::-1]
print('{} invertido é {}'.format(f, tpf))
if f == tpf:
    print('Esta frase é um palìndromo')
else:
    print('Esta frase não é um palindromo')
