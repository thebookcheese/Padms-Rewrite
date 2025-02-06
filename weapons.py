import random

raritys = ['Common','Uncommon','Rare','Epic','Mythic']
rarity_weights = [50, 30, 10, 7.5, 2.5]

class Sword:
    def __init__(self):
        names = ['Rusty Sword', 'Sharp Sword', 'Deadly Sword']
        CommonNameWeights = [85, 17, 3]
        UncommonNameWeights = [75, 25, 5]
        RareNameWeights = [60, 35, 10]
        EpicNameWeights = [40, 50, 15]
        MythicNameWeights = [10, 65, 30]

        Class = 'Sword'
        Type = 'Weapon'
        rarityList = random.choices(raritys, rarity_weights, k=1)
        rarity = rarityList[0]
        attacktype = 'Single'
        if rarity == 'Common':
            SwordNameList = random.choices(names, CommonNameWeights, k=1)
            SwordName = SwordNameList[0]
            if SwordName == names[0]:
                damage = random.randint(1,3)
            elif SwordName == names[1]:
                damage = random.randint(2, 5)
            elif SwordName == names[2]:
                damage = random.randint(3, 7)
        elif rarity == 'Uncommon':
            SwordNameList = random.choices(names, UncommonNameWeights, k=1)
            SwordName = SwordNameList[0]
            if SwordName == names[0]:
                damage = random.randint(4,8)
            elif SwordName == names[1]:
                damage = random.randint(5, 10)
            elif SwordName == names[2]:
                damage = random.randint(6, 12)
        elif rarity == 'Rare':
            SwordNameList = random.choices(names, RareNameWeights, k=1)
            SwordName = SwordNameList[0]
            if SwordName == names[0]:
                damage = random.randint(7,14)
            elif SwordName == names[1]:
                damage = random.randint(8, 16)
            elif SwordName == names[2]:
                damage = random.randint(9, 18)
        elif rarity == 'Epic':
            SwordNameList = random.choices(names, EpicNameWeights, k=1)
            SwordName = SwordNameList[0]
            if SwordName == names[0]:
                damage = random.randint(10,20)
            elif SwordName == names[1]:
                damage = random.randint(11, 22)
            elif SwordName == names[2]:
                damage = random.randint(12, 24)
        elif rarity == 'Mythic':
            SwordNameList = random.choices(names, MythicNameWeights, k=1)
            SwordName = SwordNameList[0]
            if SwordName == names[0]:
                damage = random.randint(13,26)
            elif SwordName == names[1]:
                damage = random.randint(14, 28)
            elif SwordName == names[2]:
                damage = random.randint(15, 30)
        
        self.dict = {}
        self.dict['Attack'] = damage
        self.dict['TimesBlacksmithUsed'] = 0
        self.dict['Class'] = Class
        self.dict['Type'] = Type
        self.dict['Rarity'] = rarity
        self.dict['AttackType'] = attacktype
        self.dict['Name'] = SwordName
        Cost = (damage*3)*2
        self.dict['Cost'] = Cost