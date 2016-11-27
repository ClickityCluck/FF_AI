# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:40:36 2016

@author: Shane
"""

class Player(object):
    def __init__(self,data_list):
        self.player_id = data_list[0]
        self.position = data_list[1] # QB, RB, WR, TE, K, ST, D 
        self.VoR = data_list[2]
        if len(data_list) > 3:
            pass
        
    def print(self):
        print('player ID: {0}'.format(self.player_id))
        print('position: {0}' .format(self.position))
        print('Value over Replacement: {0}'.format(self.VoR))
        
    def get_value(self):
        return self.VoR