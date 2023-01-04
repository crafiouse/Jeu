from time import sleep
from os import system
from random import randint
import platform
from entite import Entite
def clear():
    if platform.system()== "Windows":
        system('cls')
    else:
        system('clear')

class Ennemi(Entite):
    def __init__(self,nom,hp,force,defense,valeur_xp,action,classe):
        super().__init__(nom,hp,force,defense,classe)
        self.valeur_xp=valeur_xp
        self.action=action

    def choisir_action(self,player):
        x= self.action[randint(1,len(self.action)-1)]
        if x=="Attaque":
            super().infliger_degat(player)
