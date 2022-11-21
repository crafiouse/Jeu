#https://excalidraw.com/#room=c32be8b72ac507f85b11,_00DXrB_vDc1R_d6D3GfZw

class Protagonistes:
    def __init__ (self,classe,nom=str,force=int,pv=int):
        self.nom=nom
        self.force=force
        self.pv=pv
        self.classe=classe
        
    def attaquer(self,cible):
        cible.pv=cible.pv-self.force
        print(f"{self.nom} a attaqué {cible.nom} qui a perdu {self.force} pv. Il est maintenant à {cible.pv} pv")
        return cible.pv
    def choix_classe(self):
        choix = int(input("Quelle classe voulez-vous incarner ? 1 : Sorcier \n 2 : Chevalier \n 3 : Elfe"))
        match choix:
            case 1:
                classe=Sorcier(20,2)
                print("vous êtes désormais un sorcier")
                return classe
            case 2:
                classe=Chevalier(10)
                print("vous êtes désormais un Chevalier")
                return classe
            case 3:
                print("tg")
    
    
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
    def bloquer(self,cible):
        self.pv+=cible.force
        self.bouclier_dura-=5
        print(f"{self.nom} se prépare à parer la prochaine attaque")
    
    
    
    
    
    
    