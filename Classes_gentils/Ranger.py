import Joueur

class Ranger(Joueur):
    def __init__(self, nom,hp,force,defense):
        super().__init__(nom,hp,force,defense)
    
    def poison_arrow(self, enemy):
        enemy.poisoned = True
        enemy.poison_dura = 3
