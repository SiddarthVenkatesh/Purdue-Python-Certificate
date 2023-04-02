"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/21/2021

Description:
    Asks the user to enter a series of non-negative numbers. The user should enter a negative number to signal the end of the series. After
    the series is ended, the program will print their sum and average.

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


    numList = []

    while len(numList) >= 0:
        # Asks user for number
        num = float(input('Enter a non-negative number (negative to quit): '))

        # adding inputed number to total list
        if num >= 0:
            numList.append(num)
        if num < 0:
            # Sum of list
            sum = 0;
            for i in range(0, len(numList)):
                sum += numList[i]
            # Average of list
            if sum > 0:
                avg = float(sum/len(numList))
                print('  You entered', len(numList), 'numbers.')
                print('  Their sum is', '{:.3f}'.format(float(sum)), 'and their average is ' + '{:.3f}'.format(float(avg)) + '.')
                break
            # Checks to see if user inputs a negative number
            else:
                print("  You didn't enter any numbers.")
                break



if __name__ == '__main__':
    main()
