import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import pandas as PD

#variáveis
url = 'https://www.basketball-reference.com/contracts/GSW.html'
response = requests.get(url)
content = response.content
site = BS(content, 'html.parser')

dados_completos = []

for item in site.findAll('tbody'):
    dados = []
    dados.append(item['a'])
    dados.append(item['data-stat': 'age_today'])
    dados.append(item['data-stat': 'y1'])
    dados.append(item['data-stat': 'y2'])
    dados.append(item['data-stat': 'y3'])
    dados.append(item['data-stat': 'y4'])
    dados.append(item['data-stat': 'y5'])
    dados.append(item['data-stat': 'y6'])
    dados_completos.append(dados)

print(dados_completos)

