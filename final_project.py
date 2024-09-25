import random
import requests

# Generate a random Pokémon:
# Generate a random number between 1 and 151 to use as the Pokémon ID number
# Using the Pokémon API get a Pokémon based on its ID number


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    # Extract additional stats from the Pokémon data
    stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon['stats']}

    # Create a dictionary that contains the returned Pokémon's name, id, height, weight and other stats
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        # New stats
        'base_experience': pokemon['base_experience'],
        'attack': stats['attack'],
        'defense': stats['defense'],
        'speed': stats['speed']
    }


def run():
    # Play multiple rounds and record the outcome of each round
    # The player with the largest number of rounds won, wins the game
    num_rounds = int(input("How many rounds would you like to play? "))
    my_score = 0
    opponent_score = 0

    valid_stats = ['id', 'height', 'weight', 'base_experience', 'attack', 'defense', 'speed']

    for round_number in range(1, num_rounds + 1):
        print(f"Round {round_number}")

        # Get multiple Pokémon for the player to choose from
        my_pokemons = [random_pokemon() for _ in range(3)]
        for index, pokemon in enumerate(my_pokemons):
            print(f"{index + 1}: {pokemon['name']} (ID: {pokemon['id']} Height: {pokemon['height']}, Weight: {pokemon['weight']}, "
                  f"Base Experience: {pokemon['base_experience']}, Attack: {pokemon['attack']}, "
                  f"Defense: {pokemon['defense']}, Speed: {pokemon['speed']})")

        # Player chooses which Pokémon to use
        choice = int(input("Choose your Pokémon by entering the corresponding number: ")) - 1

        my_pokemon = my_pokemons[choice]
        print(f'You chose {my_pokemon["name"]}')

        # Opponent chooses a random Pokémon
        opponent_pokemon = random_pokemon()
        print(f'The opponent chose {opponent_pokemon["name"]}')

        # Determine who chooses the stat this round
        if round_number % 2 == 1:  # Odd rounds: player chooses (1, 3, 5)
            print(
                "Available stats to choose from: id, height, weight, base_experience, attack, defense, speed")
            my_stat_choice = input('Which stat do you want to use? ')

            # Opponent uses the same stat
            opponent_stat_choice = my_stat_choice
            print(f'The opponent will also compare based on {opponent_stat_choice}.')

        else:  # Even rounds: opponent chooses (2, 4)
            opponent_stat_choice = random.choice(valid_stats)
            print(f'The opponent chose to compare based on {opponent_stat_choice}.')
            my_stat_choice = opponent_stat_choice  # Player uses the same stat

        # Comparing stats
        my_stat = my_pokemon[my_stat_choice]
        opponent_stat = opponent_pokemon[opponent_stat_choice]

        print(f'Your {my_stat_choice}: {my_stat}')
        print(f'Opponent\'s {opponent_stat_choice}: {opponent_stat}')

        if my_stat > opponent_stat:
            print('You win this round!')
            my_score += 1
        elif my_stat < opponent_stat:
            print('You lose this round!')
            opponent_score += 1
        else:
            print('This round is a draw!')

    # Display final score
    print("\n--- Final Score ---")
    print(f"You: {my_score} | Opponent: {opponent_score}")
    if my_score > opponent_score:
        print("Congratulations! You are the winner!")
    elif my_score < opponent_score:
        print("Opponent is the winner!")
    else:
        print("It's a tie!")


run()
