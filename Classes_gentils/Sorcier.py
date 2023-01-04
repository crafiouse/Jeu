
from Player import Joueur
class Sorcier(Joueur):
    def __init__(self,nom,hp,force,defense,nbr_potions,classe):
        super().__init__(nom,hp,force,defense,classe)
        self.nbr_potions=nbr_potions

    def soin(self):
        if self.nbr_potions>0:
            self.hp+=10
            self.nbr_potions-=1
            print("Le SOrcier se soigne")
        else:
            print("Il ne reste plus de potions")