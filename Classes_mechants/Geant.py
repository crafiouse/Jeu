import Bot
class Giant(Bot):
    def __init__(self, nom, hp, force, valeur_xp,defense, hp_bonus):
        super().__init__(nom, hp + hp_bonus, valeur_xp,force, defense,)
        self.bonus_hp = hp_bonus