
ma_liste = list()
print(type(ma_liste))

ma_liste = [1,2,3,4,5,6,7,8,9]
print(ma_liste)

ma_liste.append(10)
print(ma_liste)

ma_liste = [3.119,"erzujhoi",56]
print(ma_liste)

ma_liste = ['c','f','m']
print(ma_liste[0])
print(ma_liste[2])
ma_liste[0] = 21

print(ma_liste)
#ajout a une list
ma_liste.append("Ajout")
print(ma_liste)
#inserer dans une liste
ma_liste = ['a', 'b', 'd', 'e']
print(ma_liste)
ma_liste.insert(2, 'c')
print(ma_liste)

#concaténation de liste += ou extend
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1 += ma_liste2
print(ma_liste1)
maliste = [11,12]
ma_liste1.extend(maliste)
print(ma_liste1)

#suppression éléments d'une liste del remove del variable_a_supp, utilisable sur liste
maliste = [-5, -2, 1, 4, 7, 10]
print(maliste)
del maliste[0]
print(maliste)

ma_liste = [31, 32, 33, 34, 35]
print(ma_liste)
ma_liste.remove(32)
print(ma_liste)

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1 # On incrémente i, ne pas oublier !

for elt in ma_liste: # elt va prendre les valeurs successives des éléments de ma_liste
   print(elt)

for i, elt in enumerate(ma_liste):
    print("À l'indice {} se trouve {}.".format(i, elt))

#tuple, liste non modifiable apres la création, ici on voit des tuplesqui contiennent 2 elts : l'indice puis l'objet
for elt in enumerate(ma_liste):
    print(elt)

autre_liste = [
    [1, 'a'],
    [4, 'd'],
    [7, 'g'],
    [26, 'z'],
] # J'ai étalé la liste sur plusieurs lignes
for nb, lettre in autre_liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))
#----les tuples-----
#definition d'un tûple entre parenthèse au lieu de crochet pour les listes
tuple_vide = ()
tuple_non_vide = (1,) # est équivalent à ci dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)

#affectation multiple
a,b,c = 1,2,3
print(a,b,c)

def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière et le reste de
    entier / divise_par"""
    valeuralacon = 99
    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste, valeuralacon

partie_entiere, reste , valeuralacon = decomposer(20, 3)
#le resultat est en fait un tuple
print("la partie entiere : {0}, reste {1} et la valeur a la con {2} ".format(partie_entiere,reste,valeuralacon))

#exemple join et split sur chaine str

def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""
    
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

print(str(afficher_flottant(3.99999999999998)))

#nombre varaible de paramètres
def fonction_inconnue(*parametres):
    print("J'ai reçu : {}.".format(parametres))

fonction_inconnue("ee","ee",4,7)
#les paramètres variables se situe après les paramètres standard, *paramètres est un tuple
def fonction_inconnuePnomme(nom,prenom,*parametres):
    print("J'ai reçu :{}{} {}.".format(nom,prenom,parametres))

fonction_inconnuePnomme("bernard","maurice","e",4)

#dans le cas de paramètres nommés, ils faut les mettre après le tuple de paramètres variables

def afficherTest(*parametres, sep='-', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

    print(chaine, end='')"""
    
    # Les paramètres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problèmes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des paramètres ne contient plus que des chaînes de caractères
    # À présent on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

afficherTest("ta","te")

afficherTest("t1","t2",sep=":")

afficherTest("t3","t4",sep=":",fin=" end \n")

liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(liste_des_parametres)
print(*liste_des_parametres)

#les liste de compréhension sont un moyen de filter ou modfier unhe liste, elle permettent de parcourir un liste et en renvoyant une autre modifié
print("----------------")
liste_origine = [0, 1, 2, 3, 4, 5]
liste_r=[nb * nb for nb in liste_origine]

print(liste_r)

liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_r=[nb for nb in liste_origine if nb % 2 == 0]
print(liste_r)

qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
liste_r=[nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits>qtt_a_retirer]
print(liste_r)

liste_origine = [1, 3, 2, 7, 5, 6, 4, 8, 9, 10]

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]
inventairetrié = liste_origine.sort()
print(liste_origine)

print(sorted(inventaire))

# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé
# On reconstitue l'inventaire trié
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in sorted(inventaire_inverse, \
    reverse=True)]
print(inventaire)

# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On trie l'inventaire inversé dans l'ordre décroissant
inventaire_inverse.sort(reverse=True)
print(inventaire_inverse)
# Et on reconstitue l'inventaire
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in inventaire_inverse]
print(inventaire)

#dictionnaire

mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
print(mon_dictionnaire)

#parentheses () pour les tuples, crochets [] pour les listes et accolades {} pour les dictionnaires 

print(mon_dictionnaire["mot de passe"])

mon_dictionnaire = {}
mon_dictionnaire[0] = "a"
mon_dictionnaire[1] = "e"
mon_dictionnaire[2] = "i"
mon_dictionnaire[3] = "o"
mon_dictionnaire[4] = "u"
mon_dictionnaire[5] = "y"
print(mon_dictionnaire)

echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# ... Seconde ligne des blancs
print(echiquier)

placard = {"chemise":3, "pantalon":6, "tee-shirt":7}
print(placard)

#les set sont comme des listes sauf que on peut pas mettre deux objets identiques

#suppression clé del ou pop
del placard["chemise"]
print(placard)

placard = {"chemise":3, "pantalon":6, "tee shirt":7}
placard.pop("chemise")
print(placard)

def fete():
    print("C'est la fête.")

def oiseau():
    print("Fais comme l'oiseau c...")

fonctions = {}
fonctions["fete"] = fete # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"]() # on essaye de l'appeler
print("--")

fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits:
    print(cle)

for valeur in fruits.values():
    print(valeur)   

if 21 in fruits.values():
    print("Un des fruits se trouve dans la quantité 21.")

for cle, valeur in fruits.items():
    print("La clé {} contient la valeur {}.".format(cle, valeur))

#on met ** pour récupérer les paramètres dans un dictionnaire
def fonction_inconnue(**parametres_nommes):
    """Fonction permettant de voir comment récupérer les paramètres nommés
    dans un dictionnaire"""
    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))

fonction_inconnue() # Aucun paramètre

fonction_inconnue(p=4, j=8)

#def fonction_inconnue(*en_liste, **en_dictionnaire): ici Tous les paramètres non nommés se retrouveront dans la variable en_liste
#et les paramètres nommés dans la variable

parametres = {"sep":" >> ", "end":" -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)

