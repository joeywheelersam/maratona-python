# view-source:https://www.iban.com/currency-codes

import requests
from bs4 import BeautifulSoup

# Criando a Lista
#moedas = []

url = "https://www.iban.com/currency-codes"
r = requests.get (url)
html = r.text
soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all("tbody")
#print (cards)
for card in cards:
#   dicionario = {"country": "cidade", "currency": "moeda", "code": "código", "number": "numero"}
    print (card.find("tr").get_text())
#   moedas.append (dicionario)

# PRIMEIRO DA LISTA
# <tr>
# <td>AFGHANISTAN</td>
# <td>Afghani</td>
# <td>AFN</td>
# <td>971</td>
# </tr>

# ULTIMO DA LISTA
# <tr>
# <td>ZIMBABWE</td>
# <td>Zimbabwe Dollar</td>
# <td>ZWL</td>
# <td>932</td>
# </tr>