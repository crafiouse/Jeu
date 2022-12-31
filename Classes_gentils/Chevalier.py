class Chevalier:
    def __init__(self,nom,hp,force,defense,dura_bouclier):
        super().__init__(nom,hp,force,defense)
        self.dura_bouclier=dura_bouclier
        self.dura_bouclier=3
        
    def parer(self):
        if self.dura_bouclier>1:
            self.defense+=5
            self.dura_bouclier-=1
            print(self.dura_bouclier)
        else:
            print("Le bouclier n'est plus en état")