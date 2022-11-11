import requests, os
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
                print (valor)
                if chave == "cidade" or chave == "código":
                    dicionario [chave] = valor
        print (dicionario)
        input ("###")
        moedas.append (dicionario)

moedas = []      
url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
cards = soup.find_all("tr")
del cards[0]

criarLista(cards, moedas)