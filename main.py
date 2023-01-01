#https://excalidraw.com/#room=c32be8b72ac507f85b11,_00DXrB_vDc1R_d6D3GfZw


from os import system
import platform
def clear():
    if platform.system()== "Windows":
        system('cls')
    else:
        system('clear') 

from time import sleep
import Joueur
import Bot
from Classes_mechants import Geant
from Classes_mechants import Nain
from Classes_mechants import Vampire
from Classes_gentils import Sorcier
from Classes_gentils import Ranger
from Classes_gentils import Chevalier
import random

# Définir les ennemis disponibles
enemies = [
    Nain("Nain esquiveur", 50, 10, 5, 50, ["Attaque", "Esquive"], "Dwarf"),
    Geant("Géant exécuteur", 100, 15, 10, 100, ["Attaque", "Exécution"], "Giant"),
    Vampire("Vampire menaçant", 75, 12, 7, 75, ["Attaque", "Vampirisme"], "Vampire")
]

# Choisir un ennemi aléatoirement
current_enemy = random.choice(enemies)

# Demander à l'utilisateur quelle classe il veut utiliser
print("Choisissez votre classe:")
print("1. Mage (possède des potions)")
print("2. Chevalier (possède un bouclier qui bloque les dégâts de la prochaine attaque)")
print("3. Ranger (possède un poison qui inflige des dégâts chaque tour)")
class_choice = input()

# Créer le joueur en fonction de la classe choisie
if class_choice == "1":
    player = Joueur("Joueur", 100, 15, 10, "Sorcier")
elif class_choice == "2":
    player = Joueur("Joueur", 100, 15, 10, "Chevalier")
elif class_choice == "3":
    player = Joueur("Joueur", 100, 15, 10, "Ranger")

# Démarrer la boucle de jeu
while player.hp > 0 and current_enemy.hp > 0:
    # Afficher l'état du joueur et de l'ennemi
    print(f"{player.name} ({player.hp} PV) vs. {current_enemy.name} ({current_enemy.hp} PV)")

    # Demander au joueur ce qu'il veut faire
    print("Que voulez-vous faire?")
    print("1. Attaquer")
    if player.class_type == "Sorcier":
        print("2. Utiliser une potion")
    if player.class_type == "Chevalier":
        print("2. Activer votre bouclier")
    if player.class_type == "Ranger":
        print("2. Utiliser votre poison")
    action = input()

    # Exécuter l'action du joueur
    if action == "1":
        player.attack(current_enemy)
    elif action == "2" and player.class_type == "Sorcier":
        player.use_potion()
    elif action == "2" and player.class_type == "Chevalier":
        player.activate_shield()
    elif action == "2" and player.class_type == "Ranger":
        player.use_poison()

     # Mettre à jour le statut de poison du joueur (si applicable)
    player.update_poison_status()

    # Exécuter l'action de l'ennemi
    current_enemy.act(player)

    # Mettre à jour le statut d'exécution du joueur (si applicable)
    player.update_execute_status()

# Afficher le vainqueur
if player.hp > 0:
    print(f"{player.name} a triomphé!")
else:
    print(f"{current_enemy.name} a triomphé!")


