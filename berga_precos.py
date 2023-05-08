import requests
from bs4 import BeautifulSoup
import csv
import datetime

url = 'https://delivery.bergamini.com.br/produtos/hipermercado-bergamini-jacana/setores/bebidas/cervejas'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#encontrar todos os itens da lista de cerjevas
cervejas = soup.find_all('div', {'class': 'item'})

# Obter a data atual
data_atual = datetime.datetime.now().strftime('%d/%m/%Y')

# Abre o arquivo csv para escrita
with open('bergamini_precos.csv', 'w', newline='') as csvfile:
    # Cria o objeto de gravação
    writer = csv.writer(csvfile, delimiter=';')

    # Escreve o cabeçalho
    writer.writerow(['Data', 'Nome', 'Preço atual', 'Preço antigo'])


# Loop pelos itens de cerveja
for cerveja in cervejas:
    nome = cerveja.find('div', {'class': 'name'}).text.strip()
    preco_atual = cerveja.find('div', {'class': 'current-price'}).text.strip()
    preco_antigo = cerveja.find('div', {'class': 'old-price'}).text.strip()

# Escreve as informações no arquivo csv
writer.writerow([data_atual, nome, preco_atual, preco_antigo])

# Imprime as informações no console
print(data_atual, nome, preco_atual, preco_antigo)

# Path: berga_precos.py

