import random
import time
from ascii_art import *

TWO_SECONDS = 2
FIGHTS_BACK_TEXT = 'The opponent fights back with... '
INPUT_MESSAGE = 'Type r, p, or s to fight with Rock, Paper, or Scissors: '
YOUR_WEAPON_IS = 'Your weapon is '
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
CURRENT = 'current'
R = 'r'
P = 'p'
S = 's'
FIRST_INDEX = 0
THIRD_INDEX = 2
weapons = [ROCK, PAPER, SCISSORS]
ascii_art = {
    ROCK: rock,
    PAPER: paper,
    SCISSORS: scissors
}

print('Welcome to Rock-Paper-Scissors Game!')

start = input(INPUT_MESSAGE)

player_history = {
    ROCK: 0,
    PAPER: 0,
    SCISSORS: 0
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


def print_opp_output():
    return opp_output()


def add_to_history(user_input):
    enemy_move_text = print_opp_output()

    if user_input == R:
        player_history[ROCK] += 1
        print(YOUR_WEAPON_IS + rock)
    elif user_input == P:
        player_history[PAPER] += 1
        print(YOUR_WEAPON_IS + paper)
    else:
        player_history[SCISSORS] += 1
        print(YOUR_WEAPON_IS + scissors)
    print(FIGHTS_BACK_TEXT)
    time.sleep(TWO_SECONDS)
    print(enemy_move_text)
    print(player_history)
    print(border)
    reprint = input(INPUT_MESSAGE)
    validate_input(reprint)


def validate_input(game_input):
    if game_input.lower() != R and game_input.lower() != P and game_input.lower() != S:
        reprint = input(INPUT_MESSAGE)
        validate_input(reprint)
    else:
        add_to_history(game_input.lower())


validate_input(start)
