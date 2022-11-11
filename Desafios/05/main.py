import requests, os
from bs4 import BeautifulSoup

# Função que formata o texto da URL
def formatacao (texto):
    caracteres = "[<td>]/ " 
    for caracteres in caracteres:
        texto = texto.replace(caracteres, "")
    return texto

# Função que cria o database com todos os dados necessários da URL
def database (sopa):
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

# Programa principal
moedas = []      
url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
update = str (soup.find("p").next_sibling).replace("\n", "")
cards = soup.find_all("tr")
del cards[0] # Deletei o primeiro item da lista porque o valor chegou vazio.
database(cards)

# Menu informando o nome do aplicativo
print ("Bem-vindo ao Negociador de Moedas 1.0")
print (update + " da " + url)
print ("Escolha pelo número da lista o país que deseja consultar a moeda.")
input ("Tecle enter para iniciar o programa!")
os.system('cls' if os.name == 'nt' else 'clear')

# Lista todas as moedas cadastradas
for numero, lista in enumerate(moedas):
        print (f"#{numero} - {lista['cidade']}")

# Validação da solicitação do usuário
while True:
    try:
        resposta = int(input ("#: "))
        if (resposta <= len(moedas)):
            break
        else:
            print ("Não existe, escolha uma opção da lista!")
            continue
    except ValueError:
        print("Isso não é um número")

# Imprime na tela a solicitação do usuário
print ("Você escolheu o "+moedas[resposta].get("cidade"))
print ("O código da moeda é "+moedas[resposta].get("código"))