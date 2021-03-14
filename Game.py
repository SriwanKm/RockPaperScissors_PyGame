print('Welcome to Rock-Paper-Scissors Game!')
start = input('Type r, p, or s to fight with Rock, Paper, or Scissors: ')



player_history = {
    "Rock": 0,
    "Paper": 0,
    "Scissors": 0
}


def opponent_output():
    print(max(player_history, key=player_history.get))


def add_to_history(user_input):
    if user_input == 'r':
        player_history['Rock'] += 1
    elif user_input == 'p':
        player_history['Paper'] += 1
    else:
        player_history['Scissors'] += 1
    print(player_history)
    opponent_output()
    reprint = input('Type r, p, or s to fight with Rock, Paper, or Scissors: ')
    validate_input(reprint)


def validate_input(game_input):
    if game_input.lower() != 'r' and game_input.lower() != 'p' and game_input.lower() != 's':
        reprint = input('Type r, p, or s to fight with Rock, Paper, or Scissors: ')
        validate_input(reprint)
    else:
        add_to_history(game_input.lower())


validate_input(start)

