#https://excalidraw.com/#room=c32be8b72ac507f85b11,_00DXrB_vDc1R_d6D3GfZw


from os import system
import platform
def clear():
    if platform.system()== "Windows":
        system('cls')
    else:
        system('clear') 

from time import sleep
from Player import Joueur
from Bot import Ennemi
from Classes_mechants.Geant import Geant
from Classes_mechants.Nain import Nain
from Classes_mechants.Vampire import Vampire
from Classes_gentils.Sorcier import Sorcier
from Classes_gentils.Ranger import Ranger
from Classes_gentils.Chevalier import Chevalier
import random
from entite import*

# Définir les ennemis disponibles
enemies = [
    Nain("Nain esquiveur", 50, 10, 5, 50,["Attaque", "Esquive"], "Nain"),
    Geant("Géant exécuteur", 120, 15, 10,40, 80, ["Attaque", "Exécution"], "Géant"),
    Vampire("Vampire menaçant", 75, 12, 7, 75, ["Attaque", "Vampirisme"], "Vampire")
]

# Choisir un ennemi aléatoirement
#ennemi_aventure = random.choice(enemies)
ennemi_aventure = enemies[random.randint(1,3)-1]
# Demander à l'utilisateur quelle classe il veut utiliser
print("Choisissez votre classe:")
print("1. Mage (possède des potions)")
print("2. Chevalier (possède un bouclier qui bloque les dégâts de la prochaine attaque)")
print("3. Ranger (possède un poison qui inflige des dégâts chaque tour)")
class_choix = input()
print("comment t'appelles-tu jeune aventurier ?")
nom_joueur=input()
# Créer le joueur en fonction de la classe choisie
if class_choix == "1":
    player = Sorcier(nom_joueur, 100, 15, 10,3, "Sorcier")
elif class_choix == "2":
    player = Chevalier(nom_joueur, 100, 15, 10,3, "Chevalier")
elif class_choix == "3":
    player = Ranger(nom_joueur, 100, 15, 10, "Ranger")

# Démarrer la boucle de jeu
while player.hp > 0 and ennemi_aventure.hp > 0:
    # Afficher l'état du joueur et de l'ennemi
    print(f"{player.nom} ({player.hp} PV) vs. {ennemi_aventure.nom} ({ennemi_aventure.hp} PV)")

    # Demander au joueur ce qu'il veut faire
    print("Que voulez-vous faire?")
    print("1. Attaquer")
    if player.classe == "Sorcier":
        print("2. Utiliser une potion")
    if player.classe == "Chevalier":
        print("2. Activer votre bouclier")
    if player.classe == "Ranger":
        print("2. Utiliser votre poison")
    action = input()

    # Exécuter l'action du joueur
    if action == "1":
        player.infliger_degat(ennemi_aventure)
    elif action == "2" and player.classe == "Sorcier":
        player.soin()
        ennemi_aventure.choisir_action(player)
    elif action == "2" and player.classe == "Chevalier":
        player.parer()
    elif action == "2" and player.classe == "Ranger":
        player.poison(ennemi_aventure)

     # Mettre à jour le statut de poison du joueur (si applicable)
    player.update_poison_status()

    # Exécuter l'action de l'ennemi
    #ennemi_aventure.choisir_action(player)
    ennemi_aventure.infliger_degat(player)
    # Mettre à jour le statut d'exécution du joueur (si applicable)
    #ennemi_aventure.update_execute_status(ennemi_aventure)

# Afficher le vainqueur
if player.hp > 0:
    print(f"{player.nom} a triomphé!")
else:
    print(f"{ennemi_aventure.nom} a triomphé!")


