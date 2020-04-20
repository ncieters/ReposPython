
#chaine = str() # Crée une chaîne vide
## On aurait obtenu le même résultat en tapant chaine = ""

#while chaine.lower() != "q":
#    print("Tapez 'Q' pour quitter...")
#    chaine = input()

#print("Merci !")

prenom = "Paul"

nom = 'Cieters'

age=21
age2=27.6
message1 = "je m'appelle {0} {1} et j'ai {2} ans, {3}".format(prenom,nom,age,nom.upper())

print(message1)

# formatage d'une adresse
adresse = """
{no_rue}, {nom_rue}
 {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)

print(message1 + " et alors " + adresse)

message2 = "j'ai " + str(age) + " ans " + str(age2) + ":" + str(int(age2))
print(message2)

chaine= "Salut tout le monde$"
print(chaine[0] + " " + chaine[3] + " " + chaine[-1] +" " + chaine[-3] + " longueur chaine :" + str(len(chaine)))
#selection chiane de 4 a 9 inclu
print(chaine[4:9])
print(chaine[len(chaine)-1])
#chaine du début jusqu'au 3eme caractères
print(chaine[:3])
#chaine du 3eme carectère jusqu'a la fin
print(chaine[3:])

mot = "lac"
mot = "b" + mot[1:]
print(mot)

#count, find et replace

print("nombre de 'e':{0} resultat du find {1} ".format(chaine.count("e"), chaine.find("tout")))
chaine = chaine.replace("e","a",3)
print(chaine)
chaine = chaine.replace("tout","poux",3)
print(chaine)
chaine = chaine.replace("a","i",2)
print(chaine)
chaine = chaine.replace("l","t")
print(chaine)
#impossible de changer la chaine comme ceci chaine[0]="e"
print("["+chaine.center(80)+"]")
#equivalent padleft
print("["+chaine.zfill(23)+"]")
#equivalent padleft
print("["+chaine.ljust(23,'0')+"]")


