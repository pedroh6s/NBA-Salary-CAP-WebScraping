import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
times = ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Chicago Bulls', 'Charlotte Hornets', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']
siglas = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

df_time = pd.DataFrame({'Time': times})
print(df_time)

escolha = int(input('Escolha o código do  time desejado: '))
print(f'O time escolhido foi o {times[escolha]}!')

url = f'https://www.basketball-reference.com/contracts/{siglas[escolha]}.html'
#teamurl = 'https://www.basketball-reference.com/contracts/{team}.html'

response = requests.get(url)
content = response.content
soup = bs(content, 'html.parser')

jogador = []
idade = []
salario1 = []
salario2 = []
salario3 = []
salario4 = []
salario5 = []
salario6 = []
contrato = []

for item in soup.tbody.findAll('th'):
    item = item.text
    jogador.append(item)
#print(jogador)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'age_today'}):
    item = item.text
    idade.append(item)
#print(idade)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'y1'}):
    item = item.text
    item = item.replace('$', '')
    item = item.replace(',', '')
    salario1.append(item)
#print(salario1)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'y2'}):
    item = item.text
    item = item.replace('$', '')
    item = item.replace(',', '')
    salario2.append(item)
#print(salario2)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'y3'}):
    item = item.text
    item = item.replace('$', '')
    item = item.replace(',', '')
    salario3.append(item)
#print(salario3)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'y4'}):
    item = item.text
    item = item.replace('$', '')
    item = item.replace(',', '')
    salario4.append(item)
#print(salario4)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'y5'}):
    item = item.text
    item = item.replace('$', '')
    item = item.replace(',', '')
    salario5.append(item)
#print(salario5)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'y6'}):
    item = item.text
    item = item.replace('$', '')
    item = item.replace(',', '')
    salario6.append(item)
#print(salario6)

for item in soup.tbody.findAll('td', attrs={'data-stat': 'signed_using'}):
    item = item.text
    contrato.append(item)
#print(contrato)

dataframe = pd.DataFrame({'Jogador': jogador,
                         'Idade': idade,
                         'Ano 1': salario1,
                         'Ano 2': salario2,
                         'Ano 3': salario3,
                         'Ano 4': salario4,
                         'Ano 5': salario5,
                         'Ano 6': salario6,
                         'Tipo de Contrato': contrato})

print(dataframe)

dataframe.to_csv(f'{times[escolha]}.csv')

