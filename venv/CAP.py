import requests
from bs4 import BeautifulSoup as BS

#variáveis
url = 'https://www.basketball-reference.com/contracts/GSW.html'
response = requests.get(url)
content = response.content
site = BS(content, 'html.parser')

#listas
jogadores = []
idades = []
salarios1 = []
salarios2 = []
salarios3 = []
salarios4 = []
salarios5 = []
salarios6 = []

#html do jogador
jogadorhtml = site.findAll('th', attrs={'data-stat': 'player'})
#html idade
idadehtml = site.findAll('td', attrs={'data-stat': 'age_today'})
#htmls do salários
salario1html = site.findAll('td', attrs={'data-stat': 'y1'})
salario2html = site.findAll('td', attrs={'data-stat': 'y2'})
salario3html = site.findAll('td', attrs={'data-stat': 'y3'})
salario4html = site.findAll('td', attrs={'data-stat': 'y4'})
salario5html = site.findAll('td', attrs={'data-stat': 'y5'})
salario6html = site.findAll('td', attrs={'data-stat': 'y6'})

for jogador in jogadorhtml:
    jogadorinfo = jogador.find('a')
    jogadores.append(jogadorinfo)
#    print(jogador.text)

for idade in idadehtml:
    idades.append(idade)
#    print(idade)

for salario1 in salario1html:
    salarios1.append(salario1)
#    print(salario1)

for salario2 in salario2html:
    salarios2.append(salario2)
#    print(salario2)

for salario3 in salario3html:
    salarios3.append(salario3)
#    print(salario3)

for salario4 in salario4html:
    salarios4.append(salario4)
#    print(salario4)

for salario5 in salario5html:
    salarios5.append(salario5)
#    print(salario5)

for salario6 in salario6html:
    salarios6.append(salario6)
#    print(salario6)

for c in range (0, len(jogadores)):
#    print(f'{jogadores[c]} {idades[c]} {salarios1[c]} {salarios2[c]} {salarios3[c]} {salarios4[c]} {salarios5[c]} {salarios6[c]}')
#    print(jogadores[c])

