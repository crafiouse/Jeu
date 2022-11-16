#https://excalidraw.com/#room=c32be8b72ac507f85b11,_00DXrB_vDc1R_d6D3GfZw

class Protagonistes:
    def __init__ (self,nom=str,force=int,pv=int):
        self.nom=nom
        self.force=force
        self.pv=pv
        
    def attaquer(self,cible):
        cible.pv=cible.pv-self.force
        print(f"{self.nom} a attaqué {cible.nom} qui a perdu {self.force} pv. Il est maintenant à {cible.pv} pv")
        return cible.pv
    
    
class Sorcier:
    def __init__(self,mana=int,potions=int):
        self.mana=mana
        self.potions=potions
        
    def soin(self):
        if self.mana>5 and self.potions>1:
            self.pv+=30/100*self.pv
            self.mana-=5
            self.potions-=1
            
class Chevalier:
    def __init__(self,bouclier_dura=int):
        self.bouclier_dura=bouclier_dura
    
    
    
    
    
    
    
    