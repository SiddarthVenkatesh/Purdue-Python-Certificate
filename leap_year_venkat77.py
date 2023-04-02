"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/08/2021

Description:
    Ask user to enter a year. Program will then display the number of days in February that year.

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
    # User inputs a year
    year = int(input('Please input a year: '))
    y = str(year)
    # Condition to check if year is divisible by 100 and 400
    if year%100 == 0:
        if year%400 == 0:
            print('In the year ' + y + ', February has 29 days.')
        else:
            print('In the year ' + y + ', February has 28 days.')

    # Condition to check if year is divisible by 4
    elif year%4 == 0:
        print('In the year ' + y + ', February has 29 days.')

    # If nothing in the loop passes through, year is not a leap year
    else:
        print('In the year ' + y + ', February has 28 days.')

if __name__ == '__main__':
    main()
