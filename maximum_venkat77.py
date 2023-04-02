"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 04.2 - Maximum
Date: 10/01/2021

Description:
    Program calls a function that will figure out which number out of two that the user inputs is greater.

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
# Greater integer function
def max_of_two(integer1, integer2):
    if integer1 > integer2:
        return integer1
    else:
        return integer2


def main():
    # Ask user for input
    first = input('Enter the first integer: ')
    second = input('Enter the second integer: ')
    print('The number', max_of_two(first, second), 'is greater.')


if __name__ == '__main__':
    main()
