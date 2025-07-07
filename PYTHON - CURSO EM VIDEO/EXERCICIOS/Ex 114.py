# import requests

# site = str(input('Qual site quer consultar? [url completa] '))

# try:
#     resposta = requests.get(site, timeout=5)
#     if resposta.status_code == 200:
#         print('Site acessivel')
#     else:
#         print(f'Site respondeu com status {resposta.status_code}')
# except requests.ConnectionError:
#     print("Erro de conexão. O site pode estar fora do ar.")
# except requests.Timeout:
#     print("Tempo de espera excedido. O site demorou para responder.")
# except requests.RequestException as e:
#     print(f"Erro ao tentar acessar o site: {e}")

import urllib
import urllib.error
import urllib.request

try:
    site_url = 'https://www.googleSEILTES.com/'
    site = urllib.request.urlopen(site_url)
except urllib.error.URLError:
    print(f'O site {site_url} não esta acessivel')
else:
    print('CONSEGUI ACESSAR')