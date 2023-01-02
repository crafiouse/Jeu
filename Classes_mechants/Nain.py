from Bot import Ennemi
import random
class Dwarf(Ennemi):
    def __init__(self, nom, hp, force, defense, valeur_xp, actions,):
        super().__init__(nom, hp, force, defense, valeur_xp, actions,)
        self.chance_dodge = 0.2  # Chance de 20% de dévier une attaque

    def prendre_dmg(self, dmg):
        # Vérifier si l'attaque est déviée
        if random.random() > self.chance_dodge:
            # Si l'attaque n'est pas déviée, appliquer les dégâts normalement
            super().take_dmg(dmg)
        else:
            # Si l'attaque est déviée, ne pas appliquer de dégâts
            print(f"{self.name} a dévié l'attaque!")