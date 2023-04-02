"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 03.1 - Arrows
Date: 09/21/2021

Description:
    Asks user how many arrows to draw, and then uses nested loops to draw the pattern of arrows shown in the sample terminal.

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
    # Ask user for input
    num = int(input('How many arrows should I draw? '))

    count = 0
    # Outside loop to create num of rows of arrows
    while count < num:
        arrow = '<'
        i = 0
        # Inside loop to create num of dashes in each arrow
        while i < count:
            arrow = arrow + '-'
            i += 1
        arrow = arrow + '>'
        print(arrow)
        count += 1



if __name__ == '__main__':
    main()
