"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/27/2021

Description:
    Program shows the frequency of each number occurring when rolling two die a certain number of times.

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



from math import *

import random as r

def roll_d6():

    dice = r.randint(1,6)
    return dice

def get_2d6_rolls(num):

    # Loop that asks the user to enter 10 inputs and then adds each input to a list
    finalList = []
    for i in range(num):
        roll1 = roll_d6()
        roll2 = roll_d6()
        pairRoll = roll1 + roll2
        finalList.append(pairRoll)

    return finalList

def main():

    num = 1000000
    numList = get_2d6_rolls(num)
    # print statements
    print('Roll  Frequency')
    for k in range(2, 13):
        print('%3.0f' % (k), end='')
        print('%9.2f' % (float(numList.count(k) / num)*100), end='')
        print('%')

if __name__ == '__main__':
    main()
