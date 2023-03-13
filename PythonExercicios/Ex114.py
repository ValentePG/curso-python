import urllib.request
try:
    url = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print(f'Servidor indisponivel')
else:
    print(f'Servidor disponivel')
    print(url.read())  # ler o código do site
