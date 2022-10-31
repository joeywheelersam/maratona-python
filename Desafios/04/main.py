# Função para formatar a lista colocando o https, www ou os dois tipos
# Função também tornar os dados minúsculo e separa os valores das urls
def formatar_lista (lista):
    for lista in lista.lower().split(","):
        lista = lista.strip()
        if "http://www." in lista:
            url.append(lista)
        elif "www." in lista:
            url.append("http://"+lista)
        else:
            url.append("http://www."+lista)

# Função para testar as URLs e imprime na tela os resultados
def testando (url):
    for solicitar in url:
        if ".com" in solicitar:
            try:
                r = requests.get(solicitar)
                if (r.status_code == 200):
                    print (f"{solicitar} - Site online. - {r.status_code}")
                else:
                    print(f"{solicitar} - Site offline. - {r.status_code}")
            except:
                print (f"{solicitar} - URL inválida.")
        else:
            print (f"{solicitar} - URL inválida.")

import requests, subprocess, os, sys

# Repetidor para fechar o programa ou abrir novamente caso o usuário queira
# A lista vai se repetir de forma vazia
contador = 0
while contador == 0:
    url = []
    print ("Bem-vindo ao verificador de sites 1.0!")
    resposta = input ("Insira as URLs dos sites que dejesa verificar o status (separe por vírgula): ")
    print ("\n###############################")
    formatar_lista(resposta)
    testando(url)
    print ("###############################\n")
    while contador == 0:
        resposta = input ("Precisa verificar mais algum site? s/n: ")
        if resposta == "s" or resposta == "S":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif resposta == "n" or resposta == "N":
            print ("Programa encerrado.")
            contador = 1
        else:
            print ("Valor inválido")