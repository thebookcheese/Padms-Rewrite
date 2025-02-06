from player import Player
import slime_forest
import weapons

player = Player()
places = ['Slime Forest']
TimesShopUsed = 0

def Traveler():
    print(f"Where do you want to travel to?")
    for i in range(len(places)):
        print(f"the {places[i]} ({i+1})")
    WhereGo = int(input())
    WhereGoActual = places[WhereGo-1]
    if WhereGoActual == 'Slime Forest':
        slime_forest.main(player)

def Blacksmith():
    SwordOrShield = int(input("Do you want to upgrade your equipped weapon (1) or shield (2)"))
    if SwordOrShield == 1:
        for key in player.equippedinventory:
            if player.equippedinventory[key]['Type'] == 'Weapon':
                GoldCost = player.equippedinventory[key]['TimesBlacksmithUsed'] * 50
                if player.Gold == GoldCost or player.Gold > GoldCost:
                    player.Gold = player.Gold - GoldCost
                    player.equippedinventory[key]['Attack'] = player.equippedinventory[key]['Attack'] + 1
                    print("Successfully upgraded")
                else:
                    print("You do not have enough money")
    elif SwordOrShield == 2:
        for key in player.equippedinventory:
            if player.equippedinventory[key]['Type'] == 'Shield':
                GoldCost = ['TimesBlacksmithUsed'] * 50
                if player.Gold == GoldCost or player.Gold > GoldCost:
                    player.Gold = player.Gold - GoldCost
                    player.equippedinventory[key]['Defense'] = player.equippedinventory[key]['Defense'] + 1
                    print("Successfully Upgrades")
                else:
                    print("You have not enough money")
    else:
        print("invalid input")

def Shop():
    WeaponOptions = ['Sword']
    CurrentSelection = []
    def ReloadCurrentSelection():
        player.CurrentSelection.clear()
        for i in range(3):
            weapon = WeaponOptions[0]
            if weapon == 'Sword':
                sword = weapons.Sword()
                player.CurrentSelection.append(sword.dict)
    if player.TimesShopUsed == 0:
        ReloadCurrentSelection()
        player.TimesShopUsed = player.TimesShopUsed + 1
    
    ShopAction = input('Are you here to \nBuy (1) \nSell (2) \nLeave (3)')
    if ShopAction == '1':
        print("Your options are")
        for i in range(3):
            print(player.CurrentSelection[i]['Name'] + " that does " + str(player.CurrentSelection[i]['Attack']) + " damage for " + str(player.CurrentSelection[i]['Cost']) + " gold (" + str(i+1) + ")")
        print('exit (4)')
        i=0
        WeaponPicked = int(input('What weapon do you want to buy?'))
        if WeaponPicked == 1:
            if player.Gold >= CurrentSelection[0]['Cost']:
                player.Gold = player.Gold - CurrentSelection[0]['Cost']
                player.unequippedinventory[CurrentSelection[0]['Name']] = CurrentSelection[0]
                player.unequippedinventorylist.append(CurrentSelection[0]['Name'])
            else:
                print("You have not enought money")
        elif WeaponPicked == 2:
            if player.Gold >= CurrentSelection[1]['Cost']:
                player.Gold = player.Gold - CurrentSelection[1]['Cost']
                player.unequippedinventory[CurrentSelection[1]['Name']] = CurrentSelection[1]
                player.unequippedinventorylist.append(CurrentSelection[1]['Name'])
            else:
                print("You have not enought money")
        elif WeaponPicked == 3:
            if player.Gold >= CurrentSelection[2]['Cost']:
                player.Gold = player.Gold - CurrentSelection[2]['Cost']
                player.unequippedinventory[CurrentSelection[2]['Name']] = CurrentSelection[2]
                player.unequippedinventorylist.append(CurrentSelection[2]['Name'])
            else:
                print("You have not enought money")
        

def Inventory():
    if len(player.unequippedinventory) > 0:
        for i in range(len(player.unequippedinventory)):
            print(f"{player.unequippedinventory[player.unequippedinventorylist[i]]['Name']} ({i+1})")
        ToBeEquippedItem = int(input('What do you want to equip'))
        ToBeEquipped = player.unequippedinventorylist[ToBeEquippedItem-1]
        Type = player.unequippedinventory[ToBeEquipped]['Type']
        for value in player.equippedinventory:
            if value['Type'] == Type:
                player.unequippedinventorylist.append(value['Name'])
                player.unequippedinventory[value['Name']] = value
                del player.equippedinventory[value]
                player.equippedinventorylist.remove(value['Name'])
                player.equippedinventory[ToBeEquipped['Name']] = ToBeEquipped
                player.equippedinventorylist.append(ToBeEquipped['Name'])
                del player.unequippedinventory[ToBeEquipped]
                del player.unequippedinventorylist[ToBeEquippedItem-1]
    else:
        print("You don't have anything unenquipped")

                


TownGo = 0
while True:
    TownGo = int(input("Where in the town do you want to go \nBlacksmith (1) \nTraveler (2) \nAccess Inventory (3) \nShop (4) \nLeave (5)"))
    if TownGo == 1:
        Blacksmith()
    elif TownGo == 2:
        Traveler()
    elif TownGo == 3:
        Inventory()
    elif TownGo == 4:
        Shop()
    elif TownGo == 5:
        exit()