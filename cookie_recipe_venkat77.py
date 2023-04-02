"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/05/2021

Description:
    Asks user for input regarding number of cookies needed, calculates amount of ingredients needed, and prints out proportions of ingredients.

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
    cookies = int(input('How many cookies do you want to make? '))

    # Proportions of ingredients
    sugar = round((1.75/48)*cookies, 2)
    butter = round((1/48)*cookies, 2)
    flour = round((2.5/48)*cookies, 2)

    # Changes number of cookies from int to string
    c = str(cookies)
    # Print out proportions of ingredients
    print('To make ' + c + ' cookies, you will need:')
    print('%7.2f cups of sugar' % (sugar))
    print('%7.2f cups of butter' % (butter))
    print('%7.2f cups of flour' % (flour))

if __name__ == '__main__':
    main()
