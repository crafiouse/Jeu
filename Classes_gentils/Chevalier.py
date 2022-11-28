class Chevalier:
    def __init__(self,bouclier_dura=int):
        self.bouclier_dura=bouclier_dura 
    def bloquer(self,cible):
        self.pv+=cible.force
        self.bouclier_dura-=5
        print(f"{self.nom} se prépare à parer la prochaine attaque")