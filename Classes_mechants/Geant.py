from random import randint
from Bot import Ennemi
class Geant(Ennemi):
    def __init__(self, nom, hp, force,defense,seuil_execute, valeur_xp,actions,classe):
        super().__init__(nom, hp,force, defense, valeur_xp,actions,classe)
        self.seuil_execute=seuil_execute
        self.execute_actif=False

    def execute(self, player):
        # Activer l'exécution si le joueur a moins de PV que le seuil d'exécution
        if player.hp <= self.seuil_execute:
            self.execute_active = True

        # Infliger des dégâts supplémentaires si l'exécution est active
        if self.execute_actif:
            self.infliger_degat(player)*2
            print(f"{player.nom} est en proie au Géant et subi plus de dégat")
        else:
            self.infliger_degat(player)

    def choisir_action(self,player):
        x= self.action[randint(1,len(self.action)-1)]
        if x=="Attaque":
            self.infliger_degat(player)
        elif x=="Exécution":
            self.execute(player)

    def infliger_degat(self, cible):
        return (super().infliger_degat(cible),super().update_poison_status())
    
    def update_execute_status(self, player):
        return super().update_execute_status(player)

