"""
@author: Zach & Shane 
"""

import datetime
from random import choice

class MonteCarlo(object):
    def __init__(self, draft, **kwargs):
        self.draft = draft
        self.states = []
        seconds = kwargs.get('time', 90)
        self.calculation_time = datetime.timedelta(seconds=seconds)
        

    def update(self, state):
        self.states.append(state)
        

    def get_play(self):
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()
        

    def run_simulation(self):
        states_copy = self.states[:]
        state = states_copy[-1]
        # hmmm, our Draft Class is conlifcting witht he rest of the psuedo-code
        # from this point on
        