from Pokemon import Pokemon
import random
import csv

# Load Pokemon data and moves from csv files given
def load_pokemon_data(filename):
    # Empty list where Pokemon will be stored as objects
    pokedex = []
    # Open file. Using "with" statement to ensure it automatically closes when encountering an error
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skips header of file
        for row in reader:
            name, type, hp, attack, defense, height, weight, moves = row
            moves = eval(moves) # Convert moves string into a list
            pokedex.append(Pokemon(name, type, int(hp), int(attack), int(defense), moves))
            return pokedex

# print ("Welcome to Pokemon Colosseum!")
# print ("Enter Player Name: ")
# print ("Team Rocket enters with: ") ; Can assign '1' to team for easier tracking
# print ("Team Professor enters with: ") assign '2' for Team Professor

# print("Let the battle begin!")
# print ("Coin toss goes to ===== {team name} to start the attack!")
# if lands on 1, Team Rocket, if 2, Team Professor.
# need to store information on opponent's pokemons
 