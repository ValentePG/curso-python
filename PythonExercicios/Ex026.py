frase = str(input('Digite uma frase qualquer ').upper().strip())
print('Quantos "A" tem na frase: {}'.format(frase.count('A')))
print('Primeira Posição: {}'.format(frase.find('A')+1))
print('Última posição: {}'.format(frase.rfind('A')+1))
