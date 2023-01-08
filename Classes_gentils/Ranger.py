from Player import Joueur

class Ranger(Joueur):
    def __init__(self, nom,hp,force,defense,classe):
        super().__init__(nom,hp,force,defense,classe)
    
    def poison(self, enemy):
        enemy.poisoned = True
        enemy.poison_dura = 3
        
    def recevoir_degat(self, dmg):
        return super().recevoir_degat(dmg)
    
    def infliger_degat(self, cible):
        return super().infliger_degat(cible)