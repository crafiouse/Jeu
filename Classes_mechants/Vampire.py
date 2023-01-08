from random import randint
from Bot import Ennemi
class Vampire(Ennemi):
    def __init__(self, nom, hp, force, defense, valeur_xp, actions,classe):
        super().__init__(nom, hp, force, defense, valeur_xp, actions,classe)
        self.vampirisme_taux = 0.1  # Taux de vampirisme de 10%

    def Vampirisme(self, cible):
        # Appliquer les dégâts normaux
        if self.hp > 0:
            super().infliger_degat(cible)
        # Récupérer une partie des dégâts infligés sous forme de vie supplémentaire
            self.hp += self.vampirisme_taux * (cible.force - self.defense)



    def infliger_degat(self, cible):
        return (super().infliger_degat(cible),super().update_poison_status())

    def choisir_action(self,player):
        x= self.action[randint(1,len(self.action)-1)]
        if x=="Attaque":
            self.infliger_degat(player)
            print(f"le {self.name} attaque {player.name}")
        elif x=="Vampirisme":
            self.Vampirisme(player)
            print(f"le {self.classe} attaque {player.nom} et regagne {self.vampirisme_taux * (player.force - self.defense)} HP")
