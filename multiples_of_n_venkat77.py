"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/27/2021

Description:
    Program that that accepts an integer as its first argument and a list of integers as its second argument.
    When called, this function should return a new list containing the integers from its second argument which
    are multiples of its first argument.

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

def multiples_of(num, numList):

    # Loops through random list of ints to check if they are multiples or not
    finalList = []
    for i in range(len(numList)):
        if numList[i] % num == 0:
            finalList.append(numList[i])

    return finalList

def main():

    # creates random integer and list of random ints
    num = 13
    numList = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]
    # print statements
    print('Original list of numbers:')
    print(' ', numList)
    print(f'Numbers in the list that are multiples of {num}:')
    print(' ', multiples_of(num, numList))

if __name__ == '__main__':
    main()
