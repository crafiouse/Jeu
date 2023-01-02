from Bot import Ennemi
import random
class Nain(Ennemi):
    def __init__(self, nom, hp, force, defense, valeur_xp, actions,classe):
        super().__init__(nom, hp, force, defense, valeur_xp, actions,classe)
        self.chance_dodge = 0.2  # Chance de 20% de dévier une attaque

    def prendre_dmg(self, dmg):
        # Vérifier si l'attaque est déviée
        if random.random() > self.chance_dodge:
            # Si l'attaque n'est pas déviée, appliquer les dégâts normalement
            super().take_dmg(dmg)
        else:
            # Si l'attaque est déviée, ne pas appliquer de dégâts
            print(f"{self.name} a dévié l'attaque!")
    
    def update_execute_status(self, player):
            if self.classe=="Geant":
                execute_seuil = self.hp * 0.15
                if self.hp <= execute_seuil:
                    self.executed = True
                    self.hp = 0
                    print(f"{player.nom} a été exécuté par {self.nom}!")
            else:
                return None
    
    def choisir_action(self, player):
        return super().choisir_action(player)
    def infliger_degat(self, cible):
        return (super().infliger_degat(cible),super().update_poison_status())