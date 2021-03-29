import random
import time
from ascii_art import *

TWO_SECONDS = 2
FIGHTS_BACK_TEXT = 'The opponent fights back with... '
INPUT_MESSAGE = 'Type r, p, or s to fight with Rock, Paper, or Scissors or q to Quit: '
YOUR_WEAPON_IS = 'Your weapon is '
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
CURRENT = 'current'
R = 'r'
P = 'p'
S = 's'
Q = 'q'
FIRST_INDEX = 0
THIRD_INDEX = 2
weapons = [ROCK, PAPER, SCISSORS]
ascii_art = {
    ROCK: rock,
    PAPER: paper,
    SCISSORS: scissors
}

ascii_conversion = {
    rock: R,
    paper: P,
    scissors: S
}

print('Welcome to Rock-Paper-Scissors Game!')

initial_input = input(INPUT_MESSAGE)

scoreboard = {
    'player': 0,
    'computer': 0,
    'tie': 0
}

player_history = {
    ROCK: 0,
    PAPER: 0,
    SCISSORS: 0
}

game_rule = {
    rock: P,
    paper: S,
    scissors: R
}

opponent_output = {
    CURRENT: ""
}


def opp_output():
    max_weapon = max(player_history, key=player_history.get)
    if player_history[ROCK] == player_history[PAPER] == player_history[SCISSORS]:
        opponent_output[CURRENT] = ascii_art[weapons[random.randint(FIRST_INDEX, THIRD_INDEX)]]
    elif max_weapon == ROCK:
        opponent_output[CURRENT] = paper
    elif max_weapon == PAPER:
        opponent_output[CURRENT] = scissors
    elif max_weapon == SCISSORS:
        opponent_output[CURRENT] = rock
    return opponent_output[CURRENT]


def get_winner(user_move, enemy_move):
    if game_rule[enemy_move] == user_move:
        print("You Won")
        scoreboard["player"] += 1
    elif ascii_conversion[enemy_move] == user_move:
        scoreboard["tie"] += 1
        print("Tie Game")
    else:
        scoreboard["computer"] += 1
        print("Computer Won")


def add_to_history(user_input):
    enemy_move_text = opp_output()

    if user_input == R:
        player_history[ROCK] += 1
        print(YOUR_WEAPON_IS + rock)
    elif user_input == P:
        player_history[PAPER] += 1
        print(YOUR_WEAPON_IS + paper)
    elif user_input == S:
        player_history[SCISSORS] += 1
        print(YOUR_WEAPON_IS + scissors)
    else:
        print('player won {0} times'.format(str(scoreboard['player'])))
        print('computer won {0} times'.format(str(scoreboard['computer'])))
        print('and there were {0} ties'.format(str(scoreboard['player'])))
        return
    print(FIGHTS_BACK_TEXT)
    time.sleep(TWO_SECONDS)
    print(enemy_move_text)
    get_winner(user_input, enemy_move_text)
    print(border)
    reprint = input(INPUT_MESSAGE)
    validate_input(reprint)


def validate_input(game_input):
    lowered_input = game_input.lower()
    if lowered_input != R and lowered_input != P and lowered_input != S and lowered_input != Q:
        reprint = input(INPUT_MESSAGE)
        validate_input(reprint)
    else:
        add_to_history(lowered_input)


validate_input(initial_input)
