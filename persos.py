class Protagonistes:
    def __init__ (self,nom=str,force=int,pv=int):
        self.nom=nom
        self.force=force
        self.pv=pv
        
    def attaquer(self,cible):
        cible.pv=cible.pv-self.force
        print(f"{self.nom} a attaqué {cible.nom} qui a perdu {self.force} pv. Il est maintenant à {cible.pv} pv")
        return cible.pv
    
    
    
    
    
    
    
    
    
    
    