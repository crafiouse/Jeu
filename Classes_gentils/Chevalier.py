from Player import Joueur
class Chevalier(Joueur):
    def __init__(self,nom,hp,force,defense,dura_bouclier,classe):
        super().__init__(nom,hp,force,defense,classe)
        self.dura_bouclier=dura_bouclier
        self.dura_bouclier=3 #Durabilité= 3 utilisations de la capacité

    def parer(self):
        if self.dura_bouclier>1:
            self.defense+=5
            self.dura_bouclier-=1
            print(self.dura_bouclier)
        else:
            None
    
    def recevoir_degat(self, dmg):
        return super().recevoir_degat(dmg)
    
    def infliger_degat(self, cible):
        return super().infliger_degat(cible)