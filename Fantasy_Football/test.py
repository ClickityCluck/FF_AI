"""
Created on Sun Oct 30 15:48:10 2016

@author: Shane
"""

# import('ff_classes')
import draft_class
data_list = [0 for j in range(5)]
data_list[0] = ['Shontavius leJohn John leShawn',130]
data_list[1] = ['HaHa Clinton-dix',100]
data_list[2] = ['RU Joking',30]
data_list[3] = ['No M Srs',10]
data_list[4] = ['Ok Then',230] 
player_dict = dict([[j+1,data_list[j]] for j in range(len(data_list))])
pick_order = ['aa','bb','cc','dd']

drf = Draft(player_dict,'bb')
print(drf.Current_drafter)
print(drf.Pick_order)

drf.next_state(1)
print(drf.Current_drafter)
print(drf.Pick_order)

drf.next_state(2)
print(drf.Current_drafter)
print(drf.Pick_order)

drf.next_state(3)
print(drf.Current_drafter)
print(drf.Pick_order)

drf.next_state(4)
print(drf.Current_drafter)
print(drf.Pick_order)
 

# pl = Player(data_list)
#pl.print()
# a = pl.get_value()