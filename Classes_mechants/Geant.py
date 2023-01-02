from Bot import Ennemi
class Geant(Ennemi):
    def __init__(self, nom, hp, force,defense, valeur_xp,actions,classe):
        super().__init__(nom, hp,force, defense, valeur_xp,actions,classe)

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
        return (super().infliger_degat(cible),super().update_poison_status(),self.update_execute_status(cible))

