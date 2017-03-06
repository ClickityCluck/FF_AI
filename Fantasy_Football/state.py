class State(object):
    ''' Class object for the entire draft '''

    def __init__(self,playerList,pickOrder):   
        '''initialize a Draft instance'''
        self.AvailablePlayer = playerList
        self.LeagueSize = len(pickOrder)
        self.Lineups = dict([[pickOrder[j],[]] for j in range(self.LeagueSize)])
        self.PickOrder = pickOrder
        self.CurrentDrafter = pickOrder[0]
    
    def start(self):
        # Returns a representation of the starting state of the game.
        pass

    def currentDrafter(self, state):
        return self.PickOrder()
        # Takes the game state and returns the current player's
        # number.
        pass

    def next_state(self,chosenPlayer):
        self.Lineups[self.CurrentDrafter] = self.Lineups[self.CurrentDrafter].append(self.AvailablePlayer.pop(chosenPlayer))
        if self.CurrentDrafter == self.PickOrder[self.LeagueSize -1]:
            self.PickOrder = self.PickOrder[::-1]         
        else:
            self.CurrentDrafter = self.PickOrder[self.PickOrder.index(self.CurrentDrafter) + 1]
            
        #chosenPlayer_ID = Int(input('Who dun got picked?'))


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
    


		

    