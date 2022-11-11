import requests, os
from bs4 import BeautifulSoup

# Menu de Boas vindas
def menu (update):
    print ("Bem-vindo ao Negociador de Moedas 1.0")
    print (update + " da " + url)
    input ("Tecle enter para iniciar o programa!")
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que formata o texto da URL
def formatacao (texto):
    caracteres = "[<td>]/ " 
    for caracteres in caracteres:
        texto = texto.replace(caracteres, "")
    return texto

# Função que cria o database com todos os dados necessários da URL
def database (sopa, moedas):
    for texto in sopa:
        nome = ["cidade", "moeda", "código", "numero"]
        sopa = formatacao(str(texto.find_all("td"))).split(",")
        dicionario = dict()
        universalCurrency =  "Nouniversalcurrency" in sopa
        if universalCurrency == False:
            for chave, valor in zip(nome, sopa):
                if chave == "cidade" or chave == "código":
                    dicionario [chave] = valor
        else:
            continue
        moedas.append (dicionario)

# Nouniversalcurrency

# Programa principal
moedas = []      
url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
update = str (soup.find("p").next_sibling).replace("\n", "")
cards = soup.find_all("tr")
del cards[0] # Deletei o primeiro item da lista porque o valor chegou vazio.

#menu (update)
database(cards, moedas)



# view-source:https://www.iban.com/currency-codes
# Link do formulário de entrega: https://form.typeform.com/to/oig2ytw1

# Imprimir a lista => print(#[número] - [Nome do País])
# A input do usuário deve ser apenas números e não pode ser maior do que a listagem do menu (opções do menu).
# Validar para quando digitar letras, apenas aceitar números => print("Isso não é um número")
# Validar valores maiores que o tamanho da lista => print("Não existe, escolha uma opção da lista!")
# Use try: / except: quando converter a input do usuário para int.
# Após o usuário selecionar um país, informe o código da moeda daquele país => print (Você escolheu [país] e o código da moeda é [código])