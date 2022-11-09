import requests, os
from bs4 import BeautifulSoup

# Criei essa função para limpar a string com os caracteres especiais
def limpando (texto):
    remover = "[<td>]/ " 
    for remover in remover:
        texto = texto.replace(remover, "")
    return texto

# Função menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = str(input("Precisa verificar mais algum site? s/n: ")).lower()
    if choice == "s" or choice =="n":
        if choice == "n":
            print("Programa Encerrado!")
            return
        elif choice == "s":
            main()
    else:
        input ("Opção inválida!\nTecle enter para digitar novamente!")
        menu()

# Função main
def main ():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Criando o Beautiful Soup
    url = "https://www.iban.com/currency-codes"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    
    # Coletando informações na URL
    cards = soup.find_all("tr")
    update = str (soup.find("p").next_sibling).replace("\n", "")

    print ("Bem-vindo ao Negociador de Moedas 1.0")
    print (update + " da " + url)
    input ("Tecle enter para iniciar o programa!")
    os.system('cls' if os.name == 'nt' else 'clear')
    resposta = input("Escolha pelo número da lista o país que deseja consultar o código da moeda: ")

    menu()
main()

# view-source:https://www.iban.com/currency-codes
# Link do formulário de entrega: https://form.typeform.com/to/oig2ytw1

# Crie uma lista [] para armazenar os países e seus códigos de moeda.
# Cada país pode ser um dicionário dentro da lista, contendo as chaves 'nome' e 'código da moeda'.
# Alguns países não possuem moeda universal (No universal currency), não adicione esses países na lista.
# A input do usuário deve ser apenas números e não pode ser maior do que a listagem do menu (opções do menu).
# Validar para quando digitar letras, apenas aceitar números (print = "Isso não é um número")
# Validar valores maiores que o tamanho da lista (print = Não existe, escolha uma opção da lista:)
# Use try: / except: quando converter a input do usuário para int.
# Após o usuário selecionar um país, informe o código da moeda daquele país (print = Você escolheu [país] e o código da moeda é [código])