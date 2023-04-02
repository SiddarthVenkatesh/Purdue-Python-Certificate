"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/08/2021

Description:
    Ask user to enter number of packages purchased and then program will display discount amount and total amount of purchase after the discount.

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
    # Ask user for input on packcage number
    num = float(input('How many packages will be purchased: '))

    #Initialize price variable
    price = 0

    # Conditional statements
    if num < 0:
        print('  Invalid Input!')

    elif (num >= 0 and num < 5):
        price = num*79.0
        print('  No discount applied.')
        print('  The total price for purchasing', int(num), 'packages is ${0:,.2f}.'.format(price))

    elif (num >= 5 and num <= 24):
        price = num*79.0*0.9
        print('  10% discount applied.')
        print('  The total price for purchasing', int(num), 'packages is ${0:,.2f}.'.format(price))

    elif (num >= 25 and num <= 49):
        price = num*79.0*0.8
        print('  20% discount applied.')
        print('  The total price for purchasing', int(num), 'packages is ${0:,.2f}.'.format(price))

    elif (num >= 50 and num <= 99):
        price = num*79.0*0.7
        print('  30% discount applied.')
        print('  The total price for purchasing', int(num), 'packages is ${0:,.2f}.'.format(price))

    else:
        price = num*79.0*0.55
        print('  45% discount applied.')
        print('  The total price for purchasing', int(num), 'packages is ${0:,.2f}.'.format(price))

if __name__ == '__main__':
    main()
