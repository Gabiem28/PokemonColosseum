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
     def __init__(self, name: str, type: str, hp: int, attack: int, defense: int, moves: list):
          # Data types in order: string, string, int, int, int, list? We should ignore height and weight
          self.name = name
          self.type = type
          self.hp = hp
          self.attack = attack
          self.defense = defense
          self.moves = moves
          self.used_moves = []
            
     # Test
     # def __repr__(self):
     #     return f"Pokemon({self.name}, {self.type}, {self.hp}, {self.attack}, {self.defense}, {self.moves})"

     ###########################################################

     # Once damage reaches below 0, set automatically to 0 to not worry about negatives
     def take_damage(self, damage):
          self.hp -= damage
          if self.hp < 0:
               self.hp = 0

     # For handling when pokemon is fainted
     def is_fainted(self):
          return self.hp <= 0
     
     # String that only returns pokemon name
     def __str__(self):
          return self.name
     
     

