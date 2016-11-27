class Draft(object):
    ''' Class object for the entire draft '''

    def __init__(self,player_dict,current_drafter):   
        '''initialize a Draft instance'''
        self.Available_players = player_dict
        self.League_size = len(pick_order)
        self.Lineups = dict([[pick_order[j],[]] for j in range(self.League_size)])
        self.Pick_order = pick_order
        self.Current_drafter = current_drafter
    
    def start(self):
        # Returns a representation of the starting state of the game.
        pass

    def current_drafter(self, state):
        return self.pick_order()
        # Takes the game state and returns the current player's
        # number.
        pass

    def next_state(self,chosen_player):
        self.Lineups[self.Current_drafter] = self.Lineups[self.Current_drafter] + self.Available_players.pop(chosen_player)
        if self.Current_drafter == self.Pick_order[self.League_size -1]:
            self.Pick_order = self.Pick_order[::-1]
            
        else:
            self.Current_drafter = self.Pick_order[self.Pick_order.index(self.Current_drafter) + 1]
            
        #chosen_player_ID = Int(input('Who dun got picked?'))


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
    


		

    