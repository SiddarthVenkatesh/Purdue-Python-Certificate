"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/29/2021

Description:
    Creates a pie chart using user's input values.

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
    # Initiates a list of months in the year
    calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Initiates list of sales list
    sales = []
    # loop that fills list with sales values from the user's input
    for i in range(len(calendar)):
        ans = input(f'Enter the sales for {calendar[i]}: ')
        sales.append(ans)
    # rgb values for colors corresponding to each month
    c = ('#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A')
    # creates the pie chart
    ax.pie(sales, colors = c, labels = calendar)
    # labels the chart title
    ax.set_title('Monthly Sales Values')
    # prints the pie chart
    plt.show()


if __name__ == '__main__':
    main()
