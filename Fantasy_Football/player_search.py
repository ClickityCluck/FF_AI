# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:45:58 2017

@author: Shane
"""

import csv
with open('playerList.txt', newline='') as inputfile:
    playerList = list(csv.reader(inputfile))
    
for j in range(len(playerList)):
    playerList[j][4] = float(playerList[j][4])
    


def pickedPlayer(playerList):
    print('Who was picked: ')
    pick = input()
    playerMatch = playerSearch(playerList,pick)
    if len(playerMatch) > 1:
        print('More info')
        playerMatch = pickedPlayer(playerMatch)
        #print('You picked {0}'.format(playerMatch))
        return playerMatch
    else:
        print('You picked {0}'.format(playerMatch[0]))
        return playerMatch[0]
    

def playerSearch(playerList,searchString):
    import re
    if type(searchString) != str:
        searchString = str(searchString)
    Matches = []
    for i in range(len(playerList)):
         for j in range(len(playerList[i])):
                 match=re.search(searchString, playerList[i][j])
                 if match != None:
                     Matches.append(i)
    return [playerList[j] for j in Matches]

