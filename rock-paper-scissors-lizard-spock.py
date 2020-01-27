# Rock-paper-scissors-lizard-Spock template

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    if name == "rock":
        return 0
    if name == "Spock":
        return 1
    if name == "paper":
        return 2
    if name == "lizard":
        return 3
    if name == "scissors":
        return 4
    else: 
        print("Error: choose number in 0-4 range.")


def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number == 4:
        return "scissors"
    else: 
        print("Error: choice not valid")
    

def rpsls(player_choice): 
    comp_num = random.randint(0,4)
    comp_choice = number_to_name(comp_num)
    player_num = name_to_number(player_choice)

    # counterclockwise computer wins, clockwise computer loses
    if (player_num - comp_num) % 5 <= 2:
        print(f"Player: {player_choice}, Computer: {comp_choice} - Player wins!") 
    else:
        print(f"Player: {player_choice}, Computer: {comp_choice} - Computer wins!") 

    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")