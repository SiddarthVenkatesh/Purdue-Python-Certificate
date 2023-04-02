"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/28/2021

Description:
    Program prints and checks if a square is a Lo Shu Magic Square.

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

# Function that prints the square
def print_square(numList):

    for r in range(3):
        print(' ', end='')
        for c in range(3):
            print('%2d' % (numList[r][c]), end='')
        print('')

def is_magic(numList):

    # Loop that asks the user to enter 10 inputs and then adds each input to a list
    decision = True
    check = 0
    comboList = sum(numList, [])
    # while loop to check if Lo Shu magic square
    while decision == True:
        if sorted(comboList) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                decision = False
        # Checking rows
        for r in range(3):
            if sum(numList[r]) != 15:
                decision = False
        # Checking columns
        colList = []
        for r in range(3):
            for c in range(3):
                colList.append(numList[c][r])
            if sum(colList) != 15:
                decision = False
            colList.clear()
        # Checking diagonals
        diagList1 = []
        for d in range(3):
            diagList1.append(numList[d][d])
        if (sum(diagList1)) != 15:
            decision = False

        diagList2 = []
        for r in range(3):
            diagList2.append(numList[r][2-r])
        if (sum(diagList2)) != 15:
            decision = False

        return decision

def main():

    numList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    numList1 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    numList2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    # print statements
    for j in range(3):
        if j == 0:
            print('Your square is:')
            print_square(numList)
            # print statements
            if is_magic(numList) == True:
                print('It is a Lo Shu magic square!')
                print('')
            else:
                print('It is not a Lo Shu magic square.')
                print('')
        if j == 1:
            print('Your square is:')
            print_square(numList1)
            # print statements
            if is_magic(numList1) == True:
                print('It is a Lo Shu magic square!')
                print('')
            else:
                print('It is not a Lo Shu magic square.')
                print('')
        if j == 2:
            print('Your square is:')
            print_square(numList2)
            # print statements
            if is_magic(numList2) == True:
                print('It is a Lo Shu magic square!')
                print('')
            else:
                print('It is not a Lo Shu magic square.')
                print('')


if __name__ == '__main__':
    main()
