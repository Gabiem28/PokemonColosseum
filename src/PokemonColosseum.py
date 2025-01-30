from Pokemon import Pokemon
import random
import csv

# Load Pokemon data from csv file given
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

# Load moves data from csv given
def load_moves_data(filename):
    moves_data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, type, category, contest, pp, power, accuracy = row
            moves_data[name] = {type : type, 'power' : int(power), 'accuracy' : accuracy }
    return moves_data

# pokedex = load_pokemon_data('data/pokemon-data.csv')
# Print(pokedex[10])

# Main game

# print ("Welcome to Pokemon Colosseum!")
# print ("Enter Player Name: ")
# print ("Team Rocket enters with: ") ; Can assign '1' to team for easier tracking
# print ("Team Professor enters with: ") assign '2' for Team Professor

# print("Let the battle begin!")
# print ("Coin toss goes to ===== {team name} to start the attack!")
# if lands on 1, Team Rocket, if 2, Team Professor.
# need to store information on opponent's pokemons
 