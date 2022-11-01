import requests
from bs4 import BeautifulSoup

url = "http://www.globo.com"
r = requests.get (url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

# Deixa bonito o html
print(soup.prettify())

# Pega o title do html
print (soup.title)

# Pesquisa por todos "a", pode colocar na lista e trabalhar com ela
print (soup.find_all('a'))

# Pesquisa por uma id expecifica
print (soup.find(id="globalWebdepsScript"))

# Pegando os links do "a"
for link in soup.find_all('a'):
    print(link.get('href'))