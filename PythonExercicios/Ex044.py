print(f"\033[31m{'LOJAS GUANABARA':=^40}\033[m")
p = float(input('\033[32mQual é o preço do produto?:R$\033[m '))
mp = str(input('\033[32mQual é o modo de pagamento?:\033[m ')).capitalize().strip()
prestacao = int(input('\033[32mSe o método for cartão, em quantas parcelas irá pagar?:\033[m '))
avista = p - (p * 10 / 100)
avistac = p - (p * 5 / 100)
cartao3x = p + (p * 20 / 100)
if mp == 'Cartão' and prestacao == 0:
    print('Sua compra recebe 5% de desconto pagando á vista no cartão')
    print('\033[33mVocê irá pagar R${:.2f}\033[m'.format(avistac))
elif mp == 'Cartão' and prestacao >= 3:
    print('Sua compra recebe 20% de juros comprando em 3x ou mais parcelas')
    print('\033[31mVocê irá pagar R${:.2f}\033[m'.format(cartao3x))
elif mp == 'Cartão' and 1 <= prestacao <= 2:
    print('Sua compra irá custar o mesmo preço entre 1 e 2 parcelas')
    print('\033[34mVocê irá pagar R${:.2f}\033[m'.format(p))
else:
    print('Sua compra irá receber 10% de desconto se comprar á vista com dinheiro')
    print(f"\033[35mVocê irá pagar R${avista:.2f}\033[m")
