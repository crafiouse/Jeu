class Entite:
    def __init__(self,nom,hp,force,defense):
        self.nom=nom
        self.hp=hp
        self.force=force
        self.defense=defense

    def recevoir_degat(self,dmg):
        self.hp -= dmg
        if self.hp<0:
            self.hp=0

    def infliger_degat(self,cible):
        dmg=self.force-cible.defense
        cible.recevoir_degat(dmg)
