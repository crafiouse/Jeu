from Bot import Ennemi
class Vampire(Ennemi):
    def __init__(self, nom, hp, force, defense, valeur_xp, actions,classe):
        super().__init__(nom, hp, force, defense, valeur_xp, actions,classe)
        self.vampirisme_taux = 0.1  # Taux de vampirisme de 10%

    def attack(self, cible):
        # Appliquer les dégâts normaux
        super().attack(cible)
        # Récupérer une partie des dégâts infligés sous forme de vie supplémentaire
        self.hp += self.vampirism_rate * (cible.attack - self.defense)

    def choisir_action(self, player):
        return super().choisir_action(player)
    
    def update_execute_status(self, player):
            if self.classe=="Geant":
                execute_seuil = self.hp * 0.15
                if self.hp <= execute_seuil:
                    self.executed = True
                    self.hp = 0
                    print(f"{player.nom} a été exécuté par {self.nom}!")
            else:
                return None

    def infliger_degat(self, cible):
        return (super().infliger_degat(cible),super().update_poison_status())