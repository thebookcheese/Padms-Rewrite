import random

Slime_Forest_Enemies = ['Slime', 'RedSlime']

class Slime:
    SlimeActions = ['SlimeJump']
    def __init__(self):
        self.SlimeHealth = random.randint(10,20)
        self.SlimeAttack = random.randint(1,5)
    def SlimeJump(self):
        damage = random.randint(self.SlimeAttack, self.SlimeAttack + 5)
        return damage

class RedSlime:
    RSlimeActions = ['RSlimeJump','RSlimeHarden']
    def __init__(self):
        self.RSlimeHealth = random.randint(15,25)
        self.RSlimeAttack = random.randint(3, 8)
    def RSLimeJump(self):
        damage = random.randint(self.SlimeAttack, self.SlimeAttack + 5)
        return damage
    def RSlimeHarden(self):
        return True

class WeakBandit:
    WeakBanditActions = ['Stab','Dagger Throw']
    def __init__(self):
        self.WBanditHealth = random.randint(30,40)
        self.WBanditAttack = random.randint(4,10)
    
    def WBanditStab(self):
        hitchance = 75
        if hitchance <= random.randint(1,100):
            print("The weak bandit missed his stab")
            return 0
        else:
            damage = random.randint(self.WBanditAttack-3, self.WBanditAttack + 2)
            if damage <= 0:
                damage = 1
            return damage

    def DaggerThrow(self):
        hitchance = 80
        if hitchance <= random.randint(1,100):
            print("The dagger tried (and failed) to throw a dagger at you")