"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/21/2021

Description:
     The program uses nested loops to collect data and calculate the average rainfall over a period of years.

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
    # Asks user for number of years inputs
    years = float(input('Enter the number of years: '))
    # Initializes variables and lists
    y = 0
    totalMonths = int(12*years)
    i = 0
    j = 0
    rainfall = []
    monthList = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
    sum = 0
    avg = 0

    # Nested while loops
    while y < years:
        print(f"  For year No. {y + 1}")
        while i < 12:
            rain = float(input('    Enter the rainfall for ' + monthList[i] + ': '))
            if rain < 0:
                print('    Invalid input, please try again.')
            else:
                rainfall.append(rain)
                i += 1
        i = 0
        y += 1

    # Calculates total rainfall
    for j in range(0, len(rainfall)):
        sum += float(rainfall[j])

    # Calculates average of rainfall
    if sum > 0:
        avg = float(sum/len(rainfall))

    if years == 0:
        print('Invalid input.')
    else:
        print('There are', totalMonths, 'months.')
        print('The total rainfall is ' + '{:.2f}'.format(float(sum)) + ' inches.')
        print('The monthly average rainfall is ' + '{:.2f}'.format(float(avg)) + ' inches.')


if __name__ == '__main__':
    main()
