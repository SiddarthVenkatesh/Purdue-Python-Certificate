"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/24/2021

Description:
    A program that predicts the approximate size of a population of organisms, which is done by asking the user to input the starting
    number of organisms, the average daily population increase as a percentage, and the number of days the organisms will be left to multiply.

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
    # Asks user for inputs needed for calculations
    start = float(input('Starting number, in million: '))
    percent = float(input('Average daily increase, in percent: '))
    days = int(input('Number of days to multiply: '))

    # Calculates rates
    rate = percent/100.0
    i = 0
    j = 0
    today = 0

    print('Day   Approx. Pop')

    # for loop to print out population values for each day
    for i in range(0, days+1):
        print(' ', i, '     ', '{:.4f}'.format((start*(1+rate)**i )))



if __name__ == '__main__':
    main()
