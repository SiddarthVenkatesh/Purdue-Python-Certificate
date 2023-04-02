"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/15/2021

Description:
    Program lets the user plays rock, paper, scissors against the computer.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
# import random library
import random as r

# function to get computer's choice
def get_computer_choice():

    rps = ['rock', 'paper', 'scissors']
    comp = r.choice(rps)
    return comp

# function to get player's choice
def get_player_choice():

    valid = 0
    while valid == 0:
        player = input('Choose rock, paper, or scissors: ')
        if player == 'rock' or player == 'paper' or player == 'scissors':
            return player
            valid += 1
        else:
            print('You made an invalid choice. Please try again.')

# function to get winner's choice
def get_winner(comp, player):
    # If player and winner have the same choice
    if comp == player:
        return 'tie'

    elif comp == 'rock' and player == 'scissors':
        print(f'  The computer chose {comp}, and you chose {player}.')
        print('  rock beats scissors')
        print('  You lost.  Better luck next time.')
        print('Thanks for playing.')
        return 'computer'

    elif comp == 'rock' and player == 'paper':
        print(f'  The computer chose {comp}, and you chose {player}.')
        print('  paper beats rock')
        print('  You won the game!')
        print('Thanks for playing.')
        return 'player'

    elif comp == 'paper' and player == 'rock':
        print(f'  The computer chose {comp}, and you chose {player}.')
        print('  paper beats rock')
        print('  You lost.  Better luck next time.')
        print('Thanks for playing.')
        return 'computer'

    elif comp == 'paper' and player == 'scissors':
        print(f'  The computer chose {comp}, and you chose {player}.')
        print('  scissors beats paper')
        print('  You won the game!')
        print('Thanks for playing.')
        return 'player'

    elif comp == 'scissors' and player == 'paper':
        print(f'  The computer chose {comp}, and you chose {player}.')
        print('  scissors beats paper')
        print('  You lost.  Better luck next time.')
        print('Thanks for playing.')
        return 'computer'

    elif comp == 'scissors' and player == 'rock':
        print(f'  The computer chose {comp}, and you chose {player}.')
        print('  rock beats scissors')
        print('  You won the game!')
        print('Thanks for playing.')
        return 'player'

def main():


    comp = get_computer_choice()
    player = get_player_choice()
    decision = get_winner(comp,player)

    if decision == 'tie':
        print(f'  The computer chose {comp}, and you chose {player}.')
        print("  Its a tie. Starting over.")
        print('')
        get_winner(get_computer_choice(),get_player_choice())


if __name__ == '__main__':
    main()
