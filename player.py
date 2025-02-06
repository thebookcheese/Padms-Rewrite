import random

class Player:
    def __init__(self):
        self.PlayerLevel = 1
        self.RemainingXP = 100
        self.Gold = 0

        self.PlayerHealth = 100
        self.BaseAttack = 3
        self.BaseDefense = 1
        self.equippedinventory = {
            'Rusty Sword': {
                'Attack': 1,
                'TimesBlacksmithUsed' : 0,
                'Class': 'Sword',
                'Type': 'Weapon',
                'Rarity' : 'Common',
                'AttackType' : 'Single',
            },
            'Light Shield': {
                'Attack': 1,
                'Defense': 2, 
                'TimesBlacksmithUsed' : 0,
                'Class': 'Shield',
                'Type': 'Shield',
                'AttackType': 'Single',
                'Rarity': 'Common',
            }
        }
        self.equippedinventorylist = ['Rusty Sword','Light Shield']
        self.unequippedinventory = {

        }
        self.unequippedinventorylist = []
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
        self.TotalAttack = TotalAttack + self.BaseAttack
        self.TotalDefense = TotalDefense + self.BaseDefense
        self.TimesShopUsed = 0
        self.CurrentSelection = []
    
    def Stab(self):
        StabAttack = 0
        for key in self.equippedinventory:
            if 'Attack' in self.equippedinventory[key] and self.equippedinventory[key]['Class'] in self.attacks['Stab']:
                StabAttack = StabAttack + self.equippedinventory[key]['Attack']
        hitchance = 75
        StabAttack = StabAttack + self.BaseAttack
        damage = random.randint(StabAttack, StabAttack + 3)
        if damage < 0 or random.randint(1,100) > hitchance:
            damage = 0
            print("You missed!")
        return damage

    def Slash(self):
        SlashAttack = 0
        for key in self.equippedinventory:
            if 'Attack' in self.equippedinventory[key] and self.equippedinventory[key]['Class'] in self.attacks['Slash']:
                SlashAttack = SlashAttack + self.equippedinventory[key]['Attack']
        hitchance = 85
        damage = random.randint(SlashAttack, SlashAttack + 3)
        if damage <= 0 or random.randint(1,100) > hitchance:
            damage = 0
            print("You missed!")
        return damage
    
    def ShieldBash(self):
        BashAttack = 0
        for key in self.equippedinventory:
            if 'Attack' in self.equippedinventory[key] and self.equippedinventory[key]['Class'] in self.attacks['ShieldBash']:
                BashAttack = BashAttack + self.equippedinventory[key]['Attack']
        damage = random.randint(BashAttack - 2, BashAttack)
        return damage