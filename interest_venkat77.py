"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 01.2 - Interest
Date: 09/05/2021

Description:
    Asks user for input regarding initial principal, annual interest rate, time, and number of times interest is compounded per year. Inputs are then inserted into
    a formula which will calculate final balance, which is printed at the end.

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

# Gather inputs from user
    print('Please enter the following quantities.')
    p = float(input('  How much is the initial deposit? '))
    r = float(input('  What is the annual interest rate in percent? '))
    n = float(input('  How many times per year is the interest compounded? '))
    t = float(input('  How many years will the account earn interest? '))

    # Formula for future balance
    fv = float(p*(1+((r/100)/n))**(n*t))

    # Rounding to only 2 decimals
    FV = (round(fv, 2))
    print('')

    # Final print statement showing future balance
    print('At the end of',t, 'years, this account will be worth ${:,}.'.format(FV))

if __name__ == '__main__':
    main()
