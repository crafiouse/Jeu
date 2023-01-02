from Bot import Ennemi
class Vampire(Ennemi):
    def __init__(self, nom, hp, force, defense, valeur_xp, actions,):
        super().__init__(nom, hp, force, defense, valeur_xp, actions,)
        self.vampirisme_taux = 0.1  # Taux de vampirisme de 10%

    def attack(self, cible):
        # Appliquer les dégâts normaux
        super().attack(cible)
        # Récupérer une partie des dégâts infligés sous forme de vie supplémentaire
        self.hp += self.vampirism_rate * (cible.attack - self.defense)
