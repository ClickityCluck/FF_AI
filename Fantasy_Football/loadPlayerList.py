# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:16:05 2017

@author: ClickityCluck
"""

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
    