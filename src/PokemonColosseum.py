from Pokemon import Pokemon
import random
import csv
import math


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
            moves_data[name] = {'type' : type, 'power' : int(power), 'accuracy' : accuracy }
    return moves_data


# Use key value pair to store effectiveness table
type_matchup_table = { 
    'Normal' : {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1},
    'Fire' : {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric':1, 'Grass': 2},
    'Water' : {'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Electric': 1, 'Grass': 0.5},
    'Electric': {'Normal': 1, 'Fire': 1, 'Water': 2, 'Electric': 0.5, 'Grass': 0.5},
    'Grass' : {'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Electric': 1, 'Grass': 0.5}
}

# Formula to calculate damage
# damage(m, a, b) = p(m) * (a(a))/d(b)) * stab * typeeffect(m, b) * random
def calc_damage(move, attacker, defender, moves_data):
    power = moves_data[move]['power']
    type = moves_data[move]['type']
    attacking_stat = attacker.attack
    defensive_stat = defender.defense

    # formula for stab
    # will be 1 unless attacker uses a move whose type matches attacker's type, in which case value will be 1.5
    if type == attacker.type:
        stab = 1.5
    else:
        stab = 1

    type_effect = type_matchup_table.get(type, {}).get(defender.type, 1)

    # Random float value generator
    random_num = random.uniform(0.5, 1)

    damage = (power * attacking_stat // defensive_stat) * stab * type_effect * random_num

    # Round up to give whole number
    return math.ceil(damage)

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
    pokedex = load_pokemon_data('data/pokemon-data.csv')
    moves_data = load_moves_data('data/moves-data.csv')

    print ("Welcome to Pokemon Colosseum!")
    player_name = input("Enter Player Name: \n")

    player_team = random.sample(pokedex, 3)
    opponent_team = random.sample(pokedex, 3)

    # variable to store the pokemon names
    # 'p' stands for pokemon
    player_pokemons = [p.name for p in player_team]
    opponent_pokemons = [p.name for p in opponent_team]

    print(f"Team Opponent enters with {', '.join(opponent_pokemons)}.")
    print(f"Team {player_name} enters with {', '.join(player_pokemons)}.")
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
        if turn == 'player':
            # To differentiate who is attacking and defending
            attacker = player_team[0]
            defender = opponent_team[0]
            
            # Make another list to store used moves, to prevent using again before all moves have been used
            # This logic checks number of moves, not specifically checking the actual moves. If so, use set()
            # On top before game starts, to check if any moves have been used.
            if len(attacker.used_moves) == len(attacker.moves):
                attacker.used_moves = [] # Reset list if all moves have been used

            while True:
                # Display moves, including used ones
                print(f"Choose the move for {attacker.name}:")
                for i, move in enumerate(attacker.moves, 1): # list all moves
                    if move in attacker.used_moves:
                        print(f"{i}.) {move} (used)")
                    else:
                        print(f"{i}.) {move}")
            
                choice = (input(f"Team {player_name}'s choice: "))

                if choice.isdigit() and 1 <= int(choice) <= len(attacker.moves):
                    choice = int(choice) - 1
                    move = attacker.moves[choice]
                    break
                else:
                    print("Invalid selection. Please choose a valid move.")

            # Input validation if move has been used
            if move in attacker.used_moves:
                print("This move has already been used! Choose another move.")
                continue
            
            # Append move to used moves list when used
            attacker.used_moves.append(move)

            # Calculate damage using formula from calc_damage
            damage = calc_damage(move, attacker, defender, moves_data)

            defender.take_damage(damage)
            
            print(f"{attacker.name} used '{move}' on {defender.name}.")
            print(f"Damage to {defender.name}: {damage} points")
            print(f"Now {defender.name} has {defender.hp} HP.")

            # Check if defending pokemon hp has reached 0 / has fainted
            if defender.is_fainted():
                print(f"{defender.name} faints back to its pokeball.\n")
                opponent_team.pop(0)
                
                if opponent_team:
                    print(f"Next for Team Opponent, {opponent_team[0].name} enters the battle!")

        # Opponent's turn
        else:
            attacker = opponent_team[0]
            defender =  player_team[0]

            # Make another list to store used moves, to prevent using again before all moves have been used
            # This logic checks number of moves, not specifically checking the actual moves. If so, use set()
            # On top before game starts, to check if any moves have been used.
            if len(attacker.used_moves) == len(attacker.moves):
                attacker.used_moves = [] # Reset list if all moves have been used

            # Check for opponent if moves have been used or not
            available_moves = []
            for move in attacker.moves:
                if move not in attacker.used_moves:
                    available_moves.append(move)

            # Randomly select a move
            move = random.choice(available_moves)

            # Mark a move as used
            attacker.used_moves.append(move)

            # Calculate the damage using formula from calc_damage
            damage = calc_damage(move, attacker, defender, moves_data)

            defender.take_damage(damage)

            print(f"Team Opponent's {attacker.name} used '{move}' on {defender.name}." )
            print(f"Damage to {defender}: {damage} points")
            print(f"Now {defender} has {defender.hp} HP.")

            if defender.is_fainted():
                print(f"{defender.name} faints back to its pokeball.\n")
                player_team.pop(0)

                if player_team:
                    print(f"Next for Team {player_name}, {player_team[0].name} enters battle!")

        if turn == 'player':
            turn = 'opponent'
        else:
            turn = 'player' 
            

            # Message if one team wins
    if player_team:
        print(f"All of Team Opponent's Pokemon fainted. and Team {player_name} prevails!")
    else:
        print("All of Team Player's Pokemon fainted, and Team Opponent prevails!")

if __name__ == "__main__":
    main()

