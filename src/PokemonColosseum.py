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

# Function for the calculations


def main():
    # Start loading the files
    pokedex = load_pokemon_data('pokemon-data.csv')
    moves_data = load_moves_data('moves.csv')



    print ("Welcome to Pokemon Colosseum!")
    player_name = input("Enter Player Name: \n")

    player_team = random.sample(pokedex, 3)
    opponent_team = random.sample(pokedex, 3)

    # variable to store the pokemon names
    # 'p' stands for pokemon
    player_pokemons = [p.name for p in player_team]
    opponent_pokemons = (p.name for p in opponent_team)

    print(f"Team Opponent enters with {', '.join(player_pokemons)}.")
    print(f"Team {player_name} enters with {', '.join(opponent_pokemons)}.")
    print("Let the battle begin!\n")
    
    # Coin toss 
    if random.choice([True, False]):
        print("Coin toss goes to --- Team Rocket to start the attack!")
        turn = 'opponent'
    else:
        print(f"Coin toss goes to --- Team {player_name} to start the attack!")
        turn = 'player'

    # Main loop for the battle
    while player_team and opponent_team:
        # Player's turn
        if turn =='player':
            # To differentiate who is attacking and defending
            attacker = player_team[0]
            defender = opponent_team[0]
            print(f"Choose the move for {attacker.name}:")
            

            # Make another list to store used moves, to prevent using again before all moves have been used
            # This logic checks number of moves, not specifically checking the actual moves. If so, use set()
            # On top before game starts, to check if any moves have been used.
            if len(attacker.used_moves) == len(attacker.moves):
                attacker.used_moves = [] # Reset list if all moves have been used

            # Display moves, including used ones
            print(f"Choose the move for {attacker.name}:")
            for i, move in enumerate(attacker.moves, 1): # list all moves
                if move in attacker.used.moves:
                    print(f"{i}.) {move} (used)")
                else:
                    print(f"{i}.) {move}")

            # Get player's choice
            choice = int(input(f"Team {player_name}'s choice: ")) - 1
            move = attacker.moves[choice]

            # Input validation if move has been used
            if move in attacker.used.moves:
                print("This move has already been used! Choose another move.")
                continue
            
            # Append move tWhereo used moves list when used
            attacker.used_moves.append(move)

