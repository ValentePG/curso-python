produto = float(input('Digite o preço do produto:R$ '))
parcelado = produto + (produto * 10/100)
print('O valor do produto com desconto de 15% a vista é R${}'.format((produto - (produto * 15/100))))
print('O valor do produto com desconto de 15% parcelado é R${}'.format((parcelado - (parcelado * 15/100))))
