class Sorcier:
    def __init__(self,mana=int,potions=int):
        self.mana=mana
        self.potions=potions
        
    def soin(self):
        if self.mana>5 and self.potions>1:
            self.pv+=30/100*self.pv
            self.mana-=5
            self.potions-=1