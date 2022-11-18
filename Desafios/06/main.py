import requests, os
from bs4 import BeautifulSoup
from babel.numbers import format_currency

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
        universalCurrency = "Nouniversalcurrency" in sopa
        if universalCurrency == False:
            for chave, valor in zip(nome, sopa):
                if chave == "cidade" or chave == "código":
                    dicionario [chave] = valor
        else:
            continue
        moedas.append (dicionario)

# Programa principal
moedas = []      

# Requisição a URL
url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

# Capturando as informações necessárias da URL
update = str (soup.find("p").next_sibling).replace("\n", "")
tabela = soup.find_all("tr")
del tabela[0] # Deletei o primeiro item da lista porque o valor chegou vazio.

# Criando o database 
database(tabela)

# Menu informando o nome do aplicativo
print ("Bem-vindo ao Negociador de Moedas 1.0")
print (update + " da " + url)
print ("Escolha pelo número os dois países que deseja negociar as moedas.")
input ("Tecle enter para iniciar o programa!")
os.system('cls' if os.name == 'nt' else 'clear')

# Lista todas as moedas cadastradas
for numero, lista in enumerate(moedas):
        print (f"#{numero} - {lista['cidade']}")

# Validação da solicitação do usuário
while True:
    try:
        resposta = int(input ("Informe pelo número o país de origem da moeda: "))
        if (resposta <= len(moedas)):
            print ("Você escolheu o "+ moedas[resposta].get("cidade"))
            print ("O código da moeda é "+ moedas[resposta].get("código"))
            break
        else:
            print ("Não existe, escolha uma opção da lista!")
            continue
    except ValueError:
        print("Isso não é um número")

# print ("Infor")

# Link do formulário de entrega: https://form.typeform.com/to/FplJEfwQ​
# Para isso vamos fazer um scrapping na Wise informando os códigos e quantidade via URL. (https://wise.com/gb/currency-converter/brl-to-usd-rate?amount=50)
# O programa deve permitir que o usuário selecione 2 países da lista (origem e destino) e informe a quantidade que deseja converter entre moedas.
# Envie os códigos das moedas dos países selecionados + quantia de conversão para o site da TransferWise via URL: Exemplo: https://wise.com/gb/currency-converter/brl-to-usd-rate?amount=5
# Veja o 'brl' para 'usd' na url e também o amout=quantia...
# Faça o Scrapping na TransferWise com o Requests e Beautiful Soup
# Talvez você não consiga pegar o valor já convertido da Wise, seja inteligente e faça um cálculo simples pegando um outro valor chave lá na página.
# Para retornar pro usuário o valor formatado você pode usar o Babel.numbers http://babel.pocoo.org/en/latest/api/numbers.html Exemplo de uso da função format_currency: