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

slime_forest.main(player)