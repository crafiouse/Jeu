from time import sleep
from os import system
from random import randint
import platform
def clear():
    if platform.system()== "Windows":
        system('cls')
    else:
        system('clear') 
from main import*
from entite import*

        

"""class Protagonistes:
    def __init__ (self,classe,nom=str,force=int,pv=int):
        self.nom=nom
        self.force=force
        self.pv=pv
        self.classe=classe
        
   def attaquer(self,cible):
        cible.pv=cible.pv-self.force
        print(f"{self.nom} a attaqué {cible.nom} qui a perdu {self.force} pv. Il est maintenant à {cible.pv} pv")
        return cible.pv
    def choix_classe(self):
        choix = int(input("Quelle classe voulez-vous incarner ?\n 1 : Sorcier \n 2 : Chevalier \n 3 : Elfe"))
        match choix:
            case 1:
                self.classe=Sorcier(20,2)
                print("vous êtes désormais un sorcier")
                sleep(2)
                return self.classe
            case 2:
                self.classe=Chevalier(10)
                print("vous êtes désormais un Chevalier")
                sleep(2)
                return self.classe
            case 3:
                print("tg")"""


class Joueur(Entite):
    def __init__(self,nom,hp,force,defense):
        super().__init__(nom,hp,force,defense)
        self.inventaire=[]
        self.xp=0
        self.xp_requis=10
        self.executed = False

    def lvlup(self):
        self.xp+=randint(1,3)
        self.force+=randint(1,3)
        self.defense+=randint(1,3)
        self.xp=0
        self.xp_requis+=5


    def ajout_inv(self,item):
        self.inventaire.append(item)

    def use_item(self,item):
        pass

    def update_execute_status(self, enemy):
        if not self.executed and isinstance(enemy, Giant):
            execute_seuil = self.hp * 0.15
            if self.hp <= execute_seuil:
                self.executed = True
                self.hp = 0
                print(f"{self.name} a été exécuté par {enemy.name}!")

