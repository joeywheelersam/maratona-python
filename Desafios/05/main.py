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
            # remover cidade com
            if chave == "cidade" or chave == "código":
                dicionario [chave] = valor
        print (dicionario)
        input ("espere")
        moedas.append (dicionario)


# Programa principal
moedas = []      
url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

update = str (soup.find("p").next_sibling).replace("\n", "")
cards = soup.find_all("tr")

# Menu de Boas Vindas
print ("Bem-vindo ao Negociador de Moedas 1.0")
print (update + " da " + url)
input ("Tecle enter para iniciar o programa!")
os.system('cls' if os.name == 'nt' else 'clear')

criarLista(cards, moedas)

    

# view-source:https://www.iban.com/currency-codes
# ULTIMO DA LISTA - <td>ZIMBABWE</td>
# dicionario = {"country": "cidade", "currency": "moeda", "code": "código", "number": "numero"}

# Link do formulário de entrega: https://form.typeform.com/to/oig2ytw1



# Alguns países não possuem moeda universal (No universal currency), não adicione esses países na lista.

# Imprimir a lista => print(#[número] - [Nome do País])
# A input do usuário deve ser apenas números e não pode ser maior do que a listagem do menu (opções do menu).
# Validar para quando digitar letras, apenas aceitar números => print("Isso não é um número")
# Validar valores maiores que o tamanho da lista => print("Não existe, escolha uma opção da lista!")
# Use try: / except: quando converter a input do usuário para int.
# Após o usuário selecionar um país, informe o código da moeda daquele país => print (Você escolheu [país] e o código da moeda é [código])