# Para formatar os valores você pode usar .lower() e .strip()
# Para criar uma lista com os valores recebidos, você pode usar o .split()
# Você pode percorrer uma lista e interagir com cada item com o For Loop
# Aprenda a tratar erros da execução do Requests usando try: e except:
# Tratar os dados informado pelo usuário como gerar a url com o http:// e remover espaços em branco
# https://form.typeform.com/to/hao5dWiF?typeform-source=of8xwd4rhwy.typeform.com

import requests

url = []
resposta=True
for resposta in True:
    resposta = input ("Resposta: ")


print ("Bem-vindo ao verificador de sites 1.0!")
resposta = input ("Insira as URLs dos sites que dejesa verificar o status (separe por vírgula): ")
url = resposta.lower().split(",")

#r = requests.get(url)
#if (r.status_code == 200):
#    print (f"{url} - Site online.")
#else:
#    print (f"{url} - Site offline")
#print (r.status_code)

# Verificar se existe .com ou .com.br na requisição que o usuário solicitou.
#print ("URL inválida.")
# Estrutura de repetição, validar para o usuário digitar apenas s, S, n ou N.
#print ("Precisa verificar mais algum site? s/n")
# Caso digite não
#print ("Programa encerrado.")