import requests
from bs4 import BeautifulSoup


page = requests.get('https://valorinveste.globo.com/cotacoes/dolar/')
soup = BeautifulSoup(page.content, 'html.parser')
soup.find('span', {'class':'tabela-data__ticker__lastQuote'}).text
