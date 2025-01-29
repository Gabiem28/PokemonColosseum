# Program name: Pokemon.py
#
# Date: January 17, 2025
#
# Author: Gabriel Malabanan
#
# Program Description: The program defines the Pokemon class, which represents attributes of a Pokemon in the game
#                      Each Pokemon has attributes such as name, type, HP, attack, defense and their moves.
#                      Class should also handle taking damage, selecting moves, or checking if Pokemon has fainted.
#
#


import random 

class Pokemon:
     def __init__(self, name, type, hp, attack, defense, moves):
          self.name = name
          self.type = type
          self.hp = hp
          self.attack = attack
          self.defense = defense
          self.moves = moves
            

