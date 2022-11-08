import requests
from bs4 import BeautifulSoup

def menu():
    choice = str(input("Precisa verificar mais algum site? s/n ")).lower()
    if choice == "s" or choice =="n":
        if choice == "n":
            print("Programa Encerrado!")
            return
        elif choice == "s":
            main()
    else:
        print("Opção inválida.")
        menu()


def main ():
    print ("Bem-vindo ao Negociador de Moedas 1.0")
    print ("Escolha pelo número da lista o país que deseja consultar o código da moeda")

    url = "https://www.iban.com/currency-codes"
    r = requests.get (url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.find_all("tbody")

    for card in cards:
        print (card.find("td"))
        break
    
    menu()
main()

# print (cards)

# <tr>
# <td>AFGHANISTAN</td>
# <td>Afghani</td>
# <td>AFN</td>
# <td>971</td>
# </tr>


# No site do IBAN, no HTML a listagem é feita em uma tabela (table).
# Crie uma lista [] para armazenar os países e seus códigos de moeda.
# Cada país pode ser um dicionário dentro da lista, contendo as chaves 'nome' e 'código da moeda'.
# Alguns países não possuem moeda universal (No universal currency), não adicione esses países na lista.
# A input do usuário deve ser apenas números e não pode ser maior do que a listagem do menu (opções do menu).
# Validar para quando digitar letras, apenas aceitar números (print = "Isso não é um número")
# Validar valores maiores que o tamanho da lista (print = Não existe, escolha uma opção da lista:)
# Use try: / except: quando converter a input do usuário para int.
# Após o usuário selecionar um país, informe o código da moeda daquele país (print = Você escolheu [país] e o código da moeda é [código])

# 🥇 Conteúdo que pode te ajudar muito:
# https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

# Link do formulário de entrega: https://form.typeform.com/to/oig2ytw1