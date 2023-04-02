"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/29/2021

Description:
    Creates a line plot based on values from text files.

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

import matplotlib.pyplot as plt

def main():
    # This line of code initiates the subplots
    fig, ax = plt.subplots()
    # Initiates price list
    prices = []
    with open('2008_Weekly_Gas_Averages.txt') as fo:
            for line in fo:
                prices.append(line.rstrip())
    for i in range(len(prices)):
        prices[i] = float(prices[i])
    # Initiates list of weeks
    weeks = []
    # loop that fills list with week values
    for i in range(1,53):
        weeks.append(i)
    # creates the line plot
    ax.plot(weeks, prices)
    # chart labels
    ax.set_title('2008 Weekly Gas Prices')

    ax.set_xlabel('Weeks (by number)')
    ax.set_ylabel('Average Price (dollars/gallon)')

    ax.set_xlim(1,52)
    ax.set_ylim(1.5, 4.25)
    ax.grid()
    # prints the pie chart
    plt.show()


if __name__ == '__main__':
    main()
