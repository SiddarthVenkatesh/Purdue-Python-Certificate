"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/12/2021

Description:
Ask user to choose a pocket number, and then display the color of that pocket.


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


def main():

    # Ask user to choose a pocket number
    num = int(input("Please choose a pocket number: "))


    if num < 0 or num > 36:
        print('  Invalid Input!')

    # Conditional statements to find correlating color to number
    elif num == 0:
        print('  Pocket number', num, 'is green.')

    elif num >= 1 and num <= 10:
        if num%2 == 1:
            print('  Pocket number', num, 'is red.')
        if num%2 == 0:
            print('  Pocket number', num, 'is black.')

    elif num >= 11 and num <= 18:
        if num%2 == 1:
            print('  Pocket number', num, 'is black.')
        if num%2 == 0:
            print('  Pocket number', num, 'is red.')

    elif num >= 19 and num <= 28:
        if num%2 == 1:
            print('  Pocket number', num, 'is red.')
        if num%2 == 0:
            print('  Pocket number', num, 'is black.')

    elif num >= 29 and num <= 36:
        if num%2 == 1:
            print('  Pocket number', num, 'is black.')
        if num%2 == 0:
            print('  Pocket number', num, 'is red.')


if __name__ == '__main__':
    main()
