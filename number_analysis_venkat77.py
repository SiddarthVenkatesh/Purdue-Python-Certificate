"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/27/2021

Description:
    Program collects ten float numbers from user and calculates certain data for numbers in that list.

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

def get_number_list():

    # Loop that asks the user to enter 10 inputs and then adds each input to a list
    finalList = []
    for i in range(1,10):
        num = float(input(f'  number  {i} of 10: '))
        finalList.append(num)
    num10 = float(input(f'  number 10 of 10: '))
    finalList.append(num10)

    return finalList

def main():

    print('Enter 10 numbers:')
    numList = get_number_list()
    hnum = max(numList)
    lnum = min(numList)
    total = sum(numList)
    avg = total/10.0
    # print statements
    print(f'Highest number: {hnum:.2f}')
    print(f'Lowest number: {lnum:.2f}')
    print(f'Total: {total:.2f}')
    print(f'Average: {avg:.2f}')

if __name__ == '__main__':
    main()
