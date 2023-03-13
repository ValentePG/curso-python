D = float(input('\033[1;33mQuanto dinheiro em reais você tem na carteira:R$\033[m'))
print('\033[4;32mVocê pode comprar {:.2f} doláres com\033[4m {}{} reais{}'.format((D/5.20), '\033[4;33m', D, '\033[m'))
print('\033[4;37mVocê pode comprar {:.2f} euros com\033[4m {}{} reais{}'.format((D/5.04), '\033[4;33m', D, '\033[m'))
