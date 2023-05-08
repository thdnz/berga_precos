import requests
from bs4 import BeautifulSoup
import
url = 'https://delivery.bergamini.com.br/produtos/hipermercado-bergamini-jacana/setores/bebidas/cervejas'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#encontrar todos os itens da lista de cerjevas
cervejas = soup.find_all('div', {'class': 'product-item'})

# Loop pelos itens de cerveja
for cerveja in cervejas:
    nome = cerveja.find('div', {'class': 'name'}).text.strip()
    preco_atual = cerveja.find('div', {'class': 'current-price'}).text.strip()
    preco_antigo = cerveja.find('div', {'class': 'old-price'}).text.strip()

    print(f"Nome: {nome} - Preço atual: {preco_atual} - Preço antigo: {preco_antigo}")
