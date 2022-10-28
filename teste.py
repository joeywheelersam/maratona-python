#########################################################
##### Arquivo em Python apenas para testar as aulas #####
#########################################################

import requests

url = "https://www.globo.com"
r = requests.get(url)
print (r.status_code)
print (r.headers)
print (r.text)