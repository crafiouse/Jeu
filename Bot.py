from time import sleep
from os import system
from random import randint
import platform
from entite import*
def clear():
    if platform.system()== "Windows":
        system('cls')
    else:
        system('clear') 
        
        
"""class Antagonistes:
    def __init__ (self,classe,nom=str,force=int,pv=int):
        self.nom=nom
        self.force=force
        self.pv=pv
        self.classe=classe
    
    def attaquer(self,cible):
        cible.pv=cible.pv-self.force
        print(f"{self.nom} a attaqué {cible.nom} qui a perdu {self.force} pv. Il est maintenant à {cible.pv} pv")
        return cible.pv"""
        
class Ennemi(Entite):
    def __init__(self,nom,hp,force,defense,valeur_xp,action):
        super().__init__(nom,hp,force,defense)
        self.valeur_xp=valeur_xp
        self.action=action
        
    def choisir_action(self):
        return self.action[randint(len(self.action)-1)]