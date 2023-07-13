import requests
from bs4 import BeautifulSoup
import csv
import datetime

url = 'https://delivery.bergamini.com.br/produtos/hipermercado-bergamini-jacana/produto/50574-cerveja-pilsen-puro-malte-imperio-lata-269ml'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Obter a data atual
data_atual = datetime.datetime.now().strftime('%Y-%m-%d')

# Nome do arquivo CSV com data
nome_arquivo = f"preco_imperio_{data_atual}.csv"

# Abre o arquivo CSV para escrita
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    # Cria o objeto writer
    writer = csv.writer(arquivo_csv)

    # Escreve o cabeçalho do arquivo CSV
    writer.writerow(['Produto', 'Preço atual', 'Preço antigo'])

    # Encontra o item de cerveja Império
    cerveja = soup.find('div', {'class': 'item product'})

    # Extrai as informações de preço da cerveja Império
    nome = cerveja.find('div', {'class': 'name'}).text.strip()
    preco_atual = cerveja.find('div', {'class': 'current-price'}).text.strip()
    preco_antigo = cerveja.find('div', {'class': 'old-price'}).text.strip()

    # Escreve as informações em uma linha do arquivo CSV
    writer.writerow([nome, preco_atual, preco_antigo])
