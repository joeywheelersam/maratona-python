import requests
from bs4 import BeautifulSoup

def limpandoString (texto):
    caracteres = "[<td>]/ " 
    for caracteres in caracteres:
        texto = texto.replace(caracteres, "")
    return texto

def criarLista (sopa):
    for card in sopa:
        sopa = limpandoString(str(card.find_all("td"))).split(",")
        print (sopa)

# view-source:https://www.iban.com/currency-codes

moedas = []
url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
cards = soup.find_all("tr")
criarLista (cards)

# PRIMEIRO DA LISTA - <td>AFGHANISTAN</td>
# ULTIMO DA LISTA - <td>ZIMBABWE</td>
# dicionario = {"country": "cidade", "currency": "moeda", "code": "código", "number": "numero"}
# moedas.append (dicionario)