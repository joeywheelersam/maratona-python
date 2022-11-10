import requests
from bs4 import BeautifulSoup

def limpandoString (texto):
    caracteres = "[<td>]/ " 
    for caracteres in caracteres:
        texto = texto.replace(caracteres, "")
    return texto

def criarLista (sopa, moedas):
    for texto in sopa:
        nome = ["cidade", "moeda", "código", "numero"]
        sopa = limpandoString(str(texto.find_all("td"))).split(",")
        dicionario = dict()
        for chave, valor in zip(nome, sopa):
            dicionario [chave] = valor
        moedas.append (dicionario)
        
def main ():
    url = "https://www.iban.com/currency-codes"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    update = str (soup.find("p").next_sibling).replace("\n", "")
    cards = soup.find_all("tr")
    moedas = []
    criarLista(cards, moedas)
    print (moedas)