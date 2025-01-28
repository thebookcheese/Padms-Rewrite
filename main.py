from player import Player
import slime_forest

player = Player()
places = ['Slime Forest']


def Traveler():
    print(f"Where do you want to travel to?")
    for i in range(len(places)):
        print(f"the {places[i]} ({i+1})")
    WhereGo = int(input())
    WhereGoActual = places[WhereGo-1]
    if WhereGoActual == 'Slime Forest':
        slime_forest.main(player)

def Blacksmith():
    SwordOrShield = input("Do you want to upgrade your equipped weapon or shield").lower()
    if SwordOrShield == 'weapon':
        for key in player.equippedinventory:
            if key['Type'] == 'Weapon':
                GoldCost = key['TimesBlacksmithUsed'] * 50
                if player.Gold >= GoldCost:
                    player.Gold = player.Gold - GoldCost
                    key['Attack'] = key['Attack'] + 1
                else:
                    print("You do not have enough money")
    elif SwordOrShield == 'shield':
        for key in player.equippedinventory:
            if key['Type'] == 'Shield':
                GoldCost = key['TimesBlacksmithUsed'] * 50
                if player.Gold >= GoldCost:
                    player.Gold = player.Gold - GoldCost
                    key['Defense'] = key['Defense'] + 1