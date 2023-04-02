"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 08.4 - Number Writer
Date: 11/11/2021

Description:
    Asks user for number of times program should print a random number and then writes it onto a file.

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
import random as r

def main():
    # Asks user for input
    amnt = int(input('How many numbers would you like? '))
    # opens file and sets as fo
    with open('random_numbers.txt', 'w') as fo:
        # loop to write number to file
        for i in range(amnt):
            num = str(r.randint(1019,1215))
            fo.write(num + '\n')


if __name__ == '__main__':
    main()
