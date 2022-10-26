# Declare abaixo uma variável chamada year e atribua a ela o ano em que Python foi criado (tipo int).
year = 1989
print (year)
print ()

# Declare abaixo uma variável chamada third_principle e atribua a ela a 3ª linha do "Zen of Python" (tipo string).
third_principle = "Explicit is better than implicit."
print (third_principle)
print ()

# Declare abaixo uma variável chamada am_i_learning e armazene o valor True (tipo boolean).
am_i_learning = True
print (am_i_learning)
print ()

# Declare abaixo uma variável chamada MyHouseColorIsBlue, porém corrija seu padrão de nomenclatura para o estilo Python (snake_case). Em seguida, atribua a ela o valor True (tipo boolean).
my_house_color_is_blue = True
print (my_house_color_is_blue)
print ()

# Atribua à variável answer o valor da variável (option_a ou option_b) que tiver a resposta correta da pergunta apresentada no print:
print("O que significa Mutable?")
option_a = "Significa que pode ser alterado"
option_b = "Significa que nao pode ser alterado"
answer = option_a
print (answer)
print ()

# Atribua à variavel answer o valor True ou False, com base na afirmação dentro do print (True = afirmação verdadeira. False = afirmação falsa):
print("Uma lista (list) no Python é mutável?")
answer = True
print (answer)
print ()

# Atribua à variável numbers uma lista dos números de 1 a 5 em sequência (todos tipo int).
numbers = [1, 2, 3, 4, 5]
print (numbers)
print ()

# Atribua à variável size_number o tamanho da lista numbers criada no xercício anterior. Dica - use uma função para descobrir o tamanho.
size_numbers = len(numbers)
print (size_numbers)
print ()

# Use o print para imprimir a soma das variáveis n1 e n2 (não mexa na declaração das variáveis, apenas no print).
n1 = 10
n2 = "40"
print(n1 + int(n2))
print ()

# Atribua à variavel answer o valor True ou False, com base na afirmação dentro do print:
print("Uma Tuple é mutavel.")
answer = False
print (answer)
print ()

# Na variavel order, insira no dicionário as seguintes keys e values:
  # order_id = 1337
  # order_value = 12.40
  # customer_email = contato@maratonapython.com.br
  # customer_phone = 112233445
  # customer_zip_code = 989222-119
order = {
  "order_id" : 1337,
  "order_value" : 12.40,
  "customer_email" : "contato@maratonapython.com.br",
  "customer_phone" : "(11)2233445",
  "customer_zip_code" : "989222-119"
}
print (order)
print ()

# Com base no dict order (criado acima), imprima o valor da key "customer_email".
print(order["customer_email"])
print ()

# Com base no dict order (criado acima), imprima o valor da key "order_id".
print(order["order_id"])
print ()

# Com base no dict order (criado acima), adicione uma nova key chamada status com o value string de "delivered" (usando apenas 1 linha).
order["status"] = "delivered"

# Com base no dict order (criado acima), imprima o valor da key "status".
print(order["status"])
print ()

# Abaixo está criada uma lista com alguns alunos da Maratona Python e vamos agora trabalhar um pouco com ela.
students = ["Bruno", "Fernando", "Luiza", "Henrique", "Fernanda", "Lucas"]
print (students)
print ()

# Ops! Esqueci do aluno Michael. Adicione ele na última posição da lista. OBS - Não altere a declaração da lista! Adicione o aluno na lista students com uma linha de código nova, utilizando uma função.
students.append("Michael")
print (students)
print ()

# Ops! A Luiza saiu do projeto. Remova a Luiza da lista.
students.remove("Luiza")
print (students)
print ()

# Quantos alunos estão na lista? (consulte a quantidade usando a função "len" dentro do print).
print(len(students))
print ()

# No print faça uma operação para verificar se a "Bruno" está na lista students.
print("Bruno" in students)
print ()

# No print faça uma operação para verificar se a "Luiza" está na lista students.
print("Luiza" in students)
print ()

# No print imprima a lista students em ordem reversa (reverse).
# print(students[::-1])
students.reverse()
print(students)
print ()

# Atribua à variável answer o valor da variável (option_a ou option_b) que tiver a resposta correta da pergunta apresentada no print:
print("De onde vem o print() e o len()?")
option_a = "Da Python Standard library"
option_b = "Do além"
answer = option_a
print(answer)

## Linha de Chegada ##
print("\nWinners win")
print(u"\U0001F40D" + " Maratona Python")
# © 2022 Maratona Python. Todos os direitos reservados.
# https://brunofraga.com