import random
from enemies import WeakBandit, BanditArcher
from player import player

enemiesamount = [1, 2, 3, 4, 5]
enemiesamountchance = [5, 2.5, 1.25, 0.625, 0.3125]
def main(player):
    Action = input("Do you want to stay (1) or leave (2)")
    Player = player()
    AvailableAttacks = []
    for i in range(len(player.equippedinventorylist)):
        for key in player.attacks:
            if player.equippedinventory[player.equippedinventorylist[i-1]]['Class'] in player.attacks[key]:
                value = [key for key, val in player.attacks.items() if val == player.attacks[key]]
                for i in range(len(value)):
                    if value[i] not in AvailableAttacks:
                        AvailableAttacks.append(value[i])
    while Action != 2:
        EnemyAmountList = random.choices(enemiesamount, enemiesamountchance, k=1)
        EnemyAmount = EnemyAmountList[0]
        EnemiesRemaining = EnemyAmount
        FrontLineEnemies = {}
        BackLineEnemies = {}

        FrontLineEnemies = random.randint(1,EnemyAmount-1)
        BackLineEnemies = EnemyAmount - FrontLineEnemies
        for i in range(FrontLineEnemies):
            Enemy = WeakBandit()
            FrontLineEnemies['Bandit'+(i+1)] = {}
            FrontLineEnemies['Bandit'+(i+1)]['Health'] = Enemy.WBanditHealth
            FrontLineEnemies['Bandit'+(i+1)]['Attack'] = Enemy.WBanditAttack
            FrontLineEnemies['Bandit'+(i+1)]['Stab'] = Enemy.WBanditStab
            FrontLineEnemies['Bandit'+(i+1)]['Throw'] = Enemy.DaggerThrow


        for i in range(BackLineEnemies):
            Enemy = BanditArcher()
            FrontLineEnemies['Archer'+(i+1)] = {}
            FrontLineEnemies['Archer'+(i+1)]['Health'] = Enemy.WBanditHealth
            FrontLineEnemies['Archer'+(i+1)]['Attack'] = Enemy.WBanditAttack
            FrontLineEnemies['Archer'+(i+1)]['Fire Arrow'] = Enemy.FireArrow
        print(f"You have encountered {EnemyAmount} enemies! {BackLineEnemies} of them are on the back row and cannot be hit until you have killed the {FrontLineEnemies} enemies on the front row")
        Action = input("Do you want to fight (1) or run (2)")
        if Action == 2:
            break
        elif Action == 1:
            while EnemiesRemaining != 0:
                print(f"You have {len(AvailableAttacks)} attack(s) you can do. They are:")
                for i in range(len(AvailableAttacks)):
                    print(f"{AvailableAttacks[i]} ({i+1})")
                AttackNum = int(input("What attack would you like to use"))
                Attack = AvailableAttacks[AttackNum-1]
                if EnemiesRemaining > FrontLineEnemies:
                    if Attack == 'Stab':
                        damage = player.Stab()
                        FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health'] = FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health'] - damage
                        print(f"You dealt {damage} damage; the bandit is now on {FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health']} health")
                    elif Attack == 'Slash':
                        damage = player.Slash()
                        FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health'] = FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health'] - damage
                        print(f"You dealt {damage} damage; the bandit is now on {FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health']} health")
                    elif Attack == 'ShieldBash':
                        damage = player.ShieldBash()
                        FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health'] = FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health'] - damage
                        print(f"You dealt {damage} damage; the bandit is now on {FrontLineEnemies['Bandit'+((EnemyAmount-EnemiesRemaining)+1)]['Health']} health")