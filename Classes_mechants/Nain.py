from Bot import Ennemi
import random
class Nain(Ennemi):
    def __init__(self, nom, hp, force, defense, valeur_xp, actions,classe):
        super().__init__(nom, hp, force, defense, valeur_xp, actions,classe)
        self.chance_dodge = 5  # Chance de 20% de dévier une attaque

    def prendre_dmg(self, dmg):
        # Vérifier si l'attaque est déviée
        if random.randint(1,10) > self.chance_dodge:
            # Si l'attaque n'est pas déviée, appliquer les dégâts normalement
            super().recevoir_degat(dmg)
        else:
            # Si l'attaque est déviée, ne pas appliquer de dégâts
            print(f"{self.nom} a dévié l'attaque!")


    def infliger_degat(self, cible):
        return (super().infliger_degat(cible),super().update_poison_status())
    
    def choisir_action(self, player):
        return super().choisir_action(player)


    