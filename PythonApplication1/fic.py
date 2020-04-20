#chemin absolue C:\Users\etemp\source\ReposPython\ComServeurClient chemin relatif ..\rep1\fic1.txt
import os
import pickle

print(os.getcwd())
mon_fichier = open("fichier.txt", "r")
contenu = mon_fichier.read()
print(contenu)
mon_fichier.close()

mon_fichier = open("fichier.txt", "w") # Argh j'ai tout écrasé !
mon_fichier.write("Premier test d'écriture dans un fichier via Python")
mon_fichier.close()

score = {
  "joueur 1":    5,
  "joueur 2":   35,
  "joueur 3":   20,
  "joueur 4":    2,
}
with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    print(score_recupere)

