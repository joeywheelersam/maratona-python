# Função Create recebendo dois parâmetros de comida e decrição
def add_food (comida=0, descricao="0"):
  # If verifica se pelo menos um dos parâmetros são inteiro, teste 1
  if type(comida)==int or type(descricao)==int:
    print ("Ambos os valores precisam ser do tipo string.")
    print ("#####################################")
  # Elif verifica se um dos parâmetros está nulo, teste 2
  elif descricao=="0":
    print ("Você precisa passar o nome da comida e descrição.")
    print ("#####################################")
  # Else caso os dois parâmetros sejam string
  else:
    # Buscar comida no dicionário
    result = comida in food_list
    # If para verificar se a comida está no dicionário, teste 3
    if result==True:
      print (f"{comida.capitalize()} já está cadastrado no dicionário.")
      print ("#####################################")
    # Else caso a comida não exista e fazendo o cadastro no dicionário, teste 4
    else:
      food_list[comida] = descricao
      print (f"{comida.capitalize()} cadastrado com sucesso.")
      print ("#####################################")

# Função Read recebendo um parâmetro de comida
def get_food (comida="0"):
  # If verifica se a comida é inteiro, teste 1
  if type(comida)==int:
    print ("O nome da comida precisa ser do tipo string.")
    print ("#####################################")
  # Elif verifica se o parâmetro está nulo, teste 2
  elif comida=="0":
    print ("Você precisa passar o nome da comida para consultar a descrição.")
    print ("#####################################")
  # Else caso o parâmetro seja string
  else:
    # Buscar comida no dicionário
    result = comida in food_list
    # If caso não encontre a comida no dicionário, teste 3
    if result==False:
      print (f"{comida.capitalize()} não existe no dicionário.")
      print ("#####################################")
    # Else caso a comida exista e deletando a comida no dicionário, teste 4
    else:
      descricao = food_list[comida]
      print (f"A descrição de {comida.capitalize()} é {descricao.capitalize()}.")
      print ("#####################################")

# Função Update recebendo dois parâmetros de comida e decrição
def update_food (comida=0, descricao="0"):
  # If verifica se pelo menos um dos parâmetros são inteiro, teste 1
  if type(comida)==int or type(descricao)==int:
    print ("Ambos os valores precisam ser do tipo string.")
    print ("#####################################")
  # Elif verifica se um dos parâmetros está nulo, teste 2
  elif descricao=="0":
    print ("Você precisa passar o nome da comida e descrição.")
    print ("#####################################")
  # Else caso os dois parâmetros sejam string
  else:
    # Buscar comida no dicionário
    result = comida in food_list
    # If caso não encontre a comida no dicionário, teste 3
    if result==False:
      print (f"{comida.capitalize()} não existe no dicionário.")
      print ("#####################################")
    # Else caso a comida exista e deletando a comida no dicionário, teste 4
    else:
      food_list[comida] = descricao
      print (f"{comida.capitalize()} descrição atualizada para: {descricao.capitalize()}.")
      print ("#####################################")

# Função Delete recebendo um parâmetro de comida
def delete_food (comida="0"):
  # If verifica se a comida é inteiro, teste 1
  if type(comida)==int:
    print ("O nome da comida precisa ser do tipo string.")
    print ("#####################################")
  # Elif verifica se o parâmetro está nulo, teste 2
  elif comida=="0":
    print ("Você precisa passar o nome da comida.")
    print ("#####################################")
  # Else caso o parâmetro seja string
  else:
    # Buscar comida no dicionário
    result = comida in food_list
    # If caso não encontre a comida no dicionário, teste 3
    if result==False:
      print (f"{comida.capitalize()} não existe no dicionário.")
      print ("#####################################")
    # Else caso a comida exista e deletando a comida no dicionário, teste 4
    else:
      del food_list[comida]
      print (f"{comida.capitalize()} foi deletado com sucesso.")
      print ("#####################################")

# use esta parte de cima para declarar a 4 funções #
#####################################################
#####!! NÃO EDITE O CÓDIGO ABAIXO DESTA LINHA !!#####

#criação da food_list
food_list = {
  'paçoquinha': 'Um doce de amendoím brasileiro',
  'brigadeiro': 'Um doce muito delicioso',
  'pizza': 'um tipo de comida da italia',
  'hamburguer': 'comida dos USA'
}

#################################
######## TESTES ADD_FOOD ########
#################################

# ADD_FOOD - TESTE 1
print("\n#### ADD_FOOD - TESTE 1 ####")
print("Usando add_food com valores sendo int")
print("add_food(100, 23)\n")
#excuta:
add_food(100, 23)

# ADD_FOOD - TESTE 2
print("\n#### ADD_FOOD - TESTE 2")
print("Usando add_food sem passar a descrição.")
print("add_food('pizza')\n")
#excuta:
add_food('pizza')

# ADD_FOOD - TESTE 3
print("\n#### ADD_FOOD - TESTE 3")
print("Usando add_food com comida já existente.")
print("add_food('brigadeiro', 'Um doce brasileiro')\n")
#excuta:
add_food('brigadeiro', 'Um doce brasileiro')

# ADD_FOOD - TESTE 4
print("\n#### ADD_FOOD - TESTE 4")
print("Usando add_food adicionando uma comida.")
print("add_food('lasanha', 'Camadas de massa e molho')\n")
#excuta:
add_food('lasanha', 'Camadas de massa e molho')

#####################################
######## TESTES DELETE_FOOD #########
#####################################

# DELETE_FOOD - TESTE 1
print("\n#### DELETE_FOOD - TESTE 1")
print("Usando delete_food com valor sendo int")
print("delete_food(100)\n")
#excuta:
delete_food(100)

# DELETE_FOOD - TESTE 2
print("\n#### DELETE_FOOD - TESTE 2")
print("Usando delete_food sem nenhum valor.")
print("delete_food()\n")
#excuta:
delete_food()

# DELETE_FOOD - TESTE 3
print("\n#### DELETE_FOOD - TESTE 3")
print("Usando delete_food com comida que não existe na lista.")
print("delete_food('massa')\n")
#excuta:
delete_food('massa')

# DELETE_FOOD - TESTE 4
print("\n#### DELETE_FOOD - TESTE 4")
print("Usando delete_food removendo uma comida.")
print("delete_food('paçoquinha')\n")
#excuta:
delete_food('paçoquinha')

#####################################
######## TESTES UPDATE_FOOD #########
#####################################

# UPDATE_FOOD - TESTE 1
print("\n#### UPDATE_FOOD - TESTE 1")
print("Usando update_food com valores sendo int")
print("update_food(100, 23)\n")
#excuta:
update_food(100, 23)

# UPDATE_FOOD - TESTE 2
print("\n#### UPDATE_FOOD - TESTE 2")
print("Usando update_food sem passar a descrição.")
print("update_food('pizza')\n")
#excuta:
update_food('pizza')

# UPDATE_FOOD - TESTE 3
print("\n#### UPDATE_FOOD - TESTE 3")
print("Usando update_food com comida não existente.")
print("update_food('sorvete', 'Um doce gelado da italia')\n")
#excuta:
update_food('sorvete', 'Um doce gelado da italia')

# UPDATE_FOOD - TESTE 4
print("\n#### UPDATE_FOOD - TESTE 4")
print("Usando update_food e atualizando uma comida.")
print("update_food('brigadeiro', 'Melhor doce do mundo.')\n")
#excuta:
update_food('brigadeiro', 'Melhor doce do mundo.')

###################################
######## TESTES GET_FOOD ##########
###################################

# GET_FOOD - TESTE 1
print("\n#### GET_FOOD - TESTE 1")
print("Usando get_food com valor sendo int")
print("get_food(505)\n")
#excuta:
get_food(505)

# GET_FOOD - TESTE 2
print("\n#### GET_FOOD - TESTE 2")
print("Usando get_food sem passar a comida.")
print("get_food()\n")
#executa
get_food()

# GET_FOOD - TESTE 3
print("\n#### GET_FOOD - TESTE 3")
print("Usando get_food com comida não existente.")
print("get_food('noodle')\n")
#executa
get_food('noodle')

# GET_FOOD - TESTE 4
print("\n#### GET_FOOD - TESTE 4")
print("Usando get_food e pesquisando a descrição uma comida.")
print("get_food('hamburguer')\n")
#executa
get_food('hamburguer')

#####!!!!!!!!!!!!!! THE END !!!!!!!!!!!!!!#####
## Linha de Chegada ##
print("\n Winners win")
print(u"\U0001F40D" + " Maratona Python")
# © 2022 Maratona Python. Todos os direitos reservados.
# https://brunofraga.com