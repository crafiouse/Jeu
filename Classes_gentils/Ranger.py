from Player import Joueur

class Ranger(Joueur):
    def __init__(self, nom,hp,force,defense,classe):
        super().__init__(nom,hp,force,defense,classe)
    
    def poison(self, enemy):
        enemy.poisoned = True
        enemy.poison_dura = 3
