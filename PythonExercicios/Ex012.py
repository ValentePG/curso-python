P = float(input('Digite o preço do produto:R$ '))
print('O desconto equivale a R${}'.format((P * 5 / 100)))
print('O preço do produto com desconto de 5% é R${:.2f}'.format((P - (P * 5 / 100))))
