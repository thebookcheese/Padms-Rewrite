import random
from enemies import Slime, RedSlime

def main(player):
    print("Welcome to the slime forest")
    Action = int(input("Do you want to: \nStay (1) \nLeave (2)"))
    if Action == 2:
        import main
    AvailableAttacks = []
    for i in range(len(player.equippedinventorylist)):
        for key in player.attacks:
            if player.equippedinventory[player.equippedinventorylist[i-1]]['Class'] in player.attacks[key]:
                value = [key for key, val in player.attacks.items() if val == player.attacks[key]]
                for i in range(len(value)):
                    if value[i] not in AvailableAttacks:
                        AvailableAttacks.append(value[i])
    while Action != 2:
        Enemy = random.randint(1,10)
        if Enemy <= 9:
            print("You encounter a slime")
            slime = Slime()
            Action = int(input("Do you want to: \nFight (1) \nRun (2)"))
            if Action == 2:
                import main
            while slime.SlimeHealth > 0:
                if Action == 1:
                    print(f"You have {len(AvailableAttacks)} attack(s) you can do. They are:")
                    for i in range(len(AvailableAttacks)):
                        print(f"{AvailableAttacks[i]} ({i+1})")
                    AttackNum = int(input("What attack would you like to use"))
                    Attack = AvailableAttacks[AttackNum-1]
                    if Attack == 'Stab':
                        damage = player.Stab()
                        slime.SlimeHealth = slime.SlimeHealth - damage
                        print(f"You dealt {damage} damage; the slime is now on {slime.SlimeHealth} health")
                    elif Attack == 'Slash':
                        damage = player.Slash()
                        slime.SlimeHealth = slime.SlimeHealth - damage
                        print(f"You dealt {damage} damage; the slime is now on {slime.SlimeHealth} health")
                    elif Attack == 'ShieldBash':
                        damage = player.ShieldBash()
                        slime.SlimeHealth = slime.SlimeHealth - damage
                        print(f"You dealt {damage} damage; the slime is now on {slime.SlimeHealth} health")
                    
                    Sdamage = slime.SlimeJump()
                    if Sdamage-player.TotalDefense <= 0:
                        print("You are too strong for the slime to damage you")
                    else:
                        player.PlayerHealth = player.PlayerHealth - (Sdamage-player.TotalDefense)
                        print(f"You have taken {Sdamage-player.TotalDefense} damage from the slime; you are now on {player.PlayerHealth} health")
                elif Action == 2:
                    break
                
                if player.PlayerHealth <= 0:
                    print('you died')
                    exit()
                if slime.SlimeHealth <= 0:
                    print("you killed the slime")
                    GoldGained = random.randint(5,15)
                    player.Gold = player.Gold + GoldGained
                    print(f"You gained {GoldGained} gold, you now have {player.Gold} gold")
                    break
                Action = int(input("Do you want to: \nFight (1) \nRun (2)"))
        elif Enemy == 10:
            print("You encounter the red slime (1/10 chance)")
            rslime = RedSlime()
            Action = int(input("Do you want to: \nFight (1) \nRun (2)"))
            if Action == 1:
                while rslime.RSlimeHealth > 0:
                    HardenActive = False
                    HardenCount = 0
                    if HardenActive == True and HardenCount < 1:
                        HardenCount = HardenCount + 1
                    elif HardenCount >= 1:
                        HardenActive = False
                        HardenCount = 0
                    if Action == 1:
                        print(f"You have {len(AvailableAttacks)} attack(s) you can do. They are:")
                        for i in range(len(AvailableAttacks)):
                            print(f"{AvailableAttacks[i]} ({i+1})")
                        AttackNum = int(input("What attack would you like to use"))
                        Attack = AvailableAttacks[AttackNum-1]
                        if Attack == 'Stab':
                            damage = player.Stab()
                            if HardenActive == False:
                                rslime.RSlimeHealth = rslime.RSlimeHealth - damage
                                print(f"You dealt {damage} damage; the slime is now on {rslime.RSlimeHealth} health")
                        elif Attack == 'Slash':
                            damage = player.Slash()
                            if HardenActive == False:
                                rslime.RSlimeHealth = rslime.RSlimeHealth - damage
                                print(f"You dealt {damage} damage; the slime is now on {rslime.RSlimeHealth} health")
                        elif Attack == 'ShieldBash':
                            damage = player.ShieldBash()
                            if HardenActive == False:
                                rslime.RSlimeHealth = rslime.RSlimeHealth - damage
                                print(f"You dealt {damage} damage; the slime is now on {rslime.RSlimeHealth} health")
                    
                        Attack = random.randint(1,2)
                        if Attack == 1:
                            Sdamage = rslime.RSlimeJump()
                            if (Sdamage - player.TotalDefense) <= 0:
                                print("You are too strong for the slime to damage you")
                            else:
                                player.PlayerHealth = player.PlayerHealth - (Sdamage-player.TotalDefense)
                                print(f"You have taken {Sdamage-player.TotalDefense} damage from the slime; you are now on {player.PlayerHealth} health")
                        elif Attack == 2:
                            HardenActive = rslime.RSlimeHarden()
                
                    elif Action == 2:
                        break
                
                if player.PlayerHealth <= 0:
                    print('you died')
                    exit()
                if rslime.RSlimeHealth <= 0:
                    print("you killed the red slime")
                    GoldGained = random.randint(10,30)
                    player.Gold = player.Gold + GoldGained
                    print(f"You gained {GoldGained} gold, you now have {player.Gold} gold")
                    Action = int(input("Do you want to: \nStay (1) \nLeave (2)"))
                Action = int(input("Do you want to: \nStay (1) \nLeave (2)"))
            else:
                break


                