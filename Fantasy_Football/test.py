"""
Created on Sun Oct 30 15:48:10 2016

@author: Shane and Zach
"""
import csv
with open('playerList.txt', newline='') as inputfile:
    playerList = list(csv.reader(inputfile))
    
for j in range(len(playerList)):
    playerList[j][4] = float(playerList[j][4])

    
pickOrder = ['aa','bb','cc','dd']


from state import State
from player_search import pickedPlayer,playerSearch
drf = State(playerList,pickOrder)
print(drf.CurrentDrafter)
print(drf.PickOrder)
print(drf.AvailablePlayer)
#
#for j in range(2):
#    nextPick = pickedPlayer(drf.AvailablePlayer)
#    drf.next_state(drf.AvailablePlayer.index(nextPick))
    

