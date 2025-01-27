import random

class Player:
    def __init__(self):
        self.PlayerLevel = 1
        self.RemainingXP = 100
        self.Gold = 0

        self.PlayerHealth = 100
        BaseAttack = 3
        BaseDefense = 1
        self.equippedinventory = {
            'Rusty Sword': {
                'Attack': 1, 
                'Class': 'Sword'
            },
            'Light Shield': {
                'Attack': 1,
                'Defense': 2, 
                'Class': 'Shield'
            }
        }
        self.equippedinventorylist = ['Rusty Sword','Light Shield']
        TotalAttack = 0
        TotalDefense = 0
        self.attacks = {
            'Stab': ['Sword','Dagger','Pike'],
            'Slash':['Sword','Battleaxe', 'Axe', 'Long Sword'],
            'ShieldBash': ['Shield']
        }
        for key in self.equippedinventory:
            if 'Attack' in self.equippedinventory[key]:
                TotalAttack = TotalAttack + self.equippedinventory[key]['Attack']
            if 'Defense' in self.equippedinventory[key]:
                TotalDefense = TotalDefense + self.equippedinventory[key]['Defense']
        self.TotalAttack = TotalAttack + BaseAttack
        self.TotalDefense = TotalDefense + BaseDefense
    
    def Stab(self):
        damage = random.randint(self.TotalAttack-3, self.TotalAttack + 3)
        hitchance = 75
        if damage < 0 or random.randint(1,100) > hitchance:
            damage = 0
            print("You missed!")
        return damage

    def Slash(self):
        damage = random.randint(self.TotalAttack-1, self.TotalAttack + 1)
        hitchance = 85
        if damage < 0 or random.randint(1,100) > hitchance:
            damage = 0
            print("You missed!")
        return damage
    
    def ShieldBash(self):
        damage = random.randint(self.TotalAttack - 2, self.TotalAttack)
        return damage