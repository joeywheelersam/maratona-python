#########################################################
##### Arquivo em Python apenas para testar as aulas #####
#########################################################

import subprocess
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')

resultado=input("Fechar programa? ")
# Fecha programa
if resultado=="s" or resultado=="S":
    print ("Resposta SIM.")
    input ()
    sys.exit()
# Não fecha o programa
elif resultado=="n" or resultado=="N":
    print ("Resposta NÃO.")
    input ()
    if __name__ == '__main__':
      cmd = r"python teste.py"
      subprocess.call(cmd, shell=True)
# Resposta errada
else:
    print ("Resposta ERRADA")
    input ()
    if __name__ == '__main__':
      cmd = r"python teste.py"
      subprocess.call(cmd, shell=True)