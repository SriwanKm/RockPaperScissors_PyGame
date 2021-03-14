import random
weapons = ['Rock', 'Paper', 'Scissors']
# print(weapons[random.randint(0, 2)])


print('Welcome to Rock-Paper-Scissors Game!')
start = input('Type r, p, or s to fight with Rock, Paper, or Scissors: ')



player_history = {
    "Rock": 0,
    "Paper": 0,
    "Scissors": 0
}

opponent_output = {
    "current": ""
}


def opp_output():
    max_weapon = max(player_history, key=player_history.get)
    if player_history.get('Rock') == player_history.get('Paper') == player_history.get('Scissors'):
        opponent_output['current'] = weapons[random.randint(0, 2)]
    elif max_weapon == 'Rock':
        opponent_output['current'] = 'Paper'
        # print('The opponent fight back with', 'PAPER!')
    elif max_weapon == 'Paper':
        opponent_output['current'] = 'Scissors'
        # print('The opponent fight back with', 'SCISSORS!')
    elif max_weapon == 'Scissors':
        opponent_output['current'] = 'Rock'
        # print('The opponent fight back with', 'ROCK!')
    return opponent_output['current']


def print_opp_output():
    print('The opponent fight back with', opp_output())



def add_to_history(user_input):
    print_opp_output()
    if user_input == 'r':
        player_history['Rock'] += 1
        print('Your weapon is ROCK')
    elif user_input == 'p':
        player_history['Paper'] += 1
        print('Your weapon is PAPER')
    else:
        player_history['Scissors'] += 1
        print('Your weapon is SCISSORS')
    print(player_history)
    reprint = input('Type r, p, or s to fight with Rock, Paper, or Scissors: ')
    validate_input(reprint)


def validate_input(game_input):
    if game_input.lower() != 'r' and game_input.lower() != 'p' and game_input.lower() != 's':
        reprint = input('Type r, p, or s to fight with Rock, Paper, or Scissors: ')
        validate_input(reprint)
    else:
        add_to_history(game_input.lower())


validate_input(start)

