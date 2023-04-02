"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/15/2021

Description:
    Write a function namedrandom_numberthat returns a random integer.  The function shouldhave one argument which specifies
    how many digits the random number it returns shouldhave. Then use this function in a program that gives the user a simple math quiz.
    The program should display a random two digit number and a random three digit number that are to be added.

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

# Create random numbers
def random_number(length):
    if length == 2:
        return r.randint(10,99)
    if length == 3:
        return r.randint(100,999)

def main():

    # hold random numbers
    num1 = random_number(2)
    num2 = random_number(3)
    answer = num1 + num2

    # Display to user
    print('   ', end = '')
    print(num1)
    print('+ ', end = '')
    print(num2)
    print('-----')
    print('=', end='')

    # User inputs their solution
    check = int(input(' '))
    check == answer

    # Checking accuracy of answers
    if check == answer:
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {answer}.')






if __name__ == '__main__':
    main()
