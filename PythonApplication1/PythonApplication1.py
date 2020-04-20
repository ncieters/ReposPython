from math import *

a=10
ma_liste1 = [1, 2, 3]

def fonc(a,ma_liste):
    a =+ 1
    ma_liste.append(4) #objet modifié
    ma_liste= [1, 2, 3, 5] #pas de modif

fonc(a,ma_liste1)
print(a)
print(ma_liste1)

print(sqrt(a))


"""module multipli contenant la fonction table"""

import os

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# test de la fonction table
if __name__ == "__main__":
    table(4)
    os.system("pause")
    