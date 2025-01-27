import random

Slime_Forest_Enemies = ['Slime', 'RedSlime']

class Slime:
    SlimeActions = ['SlimeJump']
    def __init__(self):
        self.SlimeHealth = random.randint(10,20)
        self.SlimeAttack = random.randint(1,5)
        self.SlimeDefense = random.randint(0,1)
    def SlimeJump(self):
        damage = random.randint(self.SlimeAttack, self.SlimeAttack + 5)
        return damage

class RedSlime:
    RSlimeActions = ['RSlimeJump','RSlimeHarden']
    def __init__(self):
        self.RSlimeHealth = random.randint(15,25)
        self.RSlimeAttack = random.randint(3, 8)
        self.RSlimeDefense = random.randint(0,1)
    def RSLimeJump(self):
        damage = random.randint(self.SlimeAttack, self.SlimeAttack + 5)
        return damage
    def RSlimeHarden(self):
        return True
