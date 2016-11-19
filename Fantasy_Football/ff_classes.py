"""
Created on Sun Oct 30 17:59:22 2016

@author: Shane & Zach
"""

class Draft(object):
''' Class object for the entire draft '''

    def __init__(self,top_players,pick_order = list(range(4))):   
        '''initialize a Draft instance'''
        self.Available_players = top_players
        self.League_size = len(pick_order)
        self.Lineups = [[] for j in range(self.League_size-1)]
        self.Current_drafter = pick_order[0]
    
    def start(self):
        # Returns a representation of the starting state of the game.
        pass

    def current_drafter(self, state):
        return self.pick_order()
        # Takes the game state and returns the current player's
        # number.
        pass

    def next_state(self, state, play):
        chosen_player_ID = Int(input('Who dun got picked?'))
        
        
        self.Current_drafter
        # Takes the game state, and the move to be applied.
        # Returns the new game state.
        pass

    def legal_plays(self, state_history):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.
        pass

    def winner(self, state_history):
        # Takes a sequence of game states representing the full
        # game history.  If the game is now won, return the player
        # number.  If the game is still ongoing, return zero.  If
        # the game is tied, return a different distinct value, e.g. -1.
        pass
    

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
		
class Drafter(object):
    def __init__(self,remaining_positions = ):
        self.player_id = data_list[0]
        self.position = data_list[1]
        self.VoR = data_list[2]
        if len(data_list) > 3:
            pass
        
    def print(self):
        print('player ID: {0}'.format(self.player_id))
        print('position: {0}' .format(self.position))
        print('Value over Replacement: {0}'.format(self.VoR))
        
    def get_value(self):
        return self.VoR
    