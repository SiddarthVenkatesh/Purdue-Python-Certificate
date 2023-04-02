"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 11/30/2021

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

import datetime
import matplotlib.pyplot as plt

def main():
    # Initiates price list
    with open('indiana_covid_19_data_fall_2021.txt', 'r') as fo:
        fileString = fo.read()
        fileList = fileString.split()

    dates = []
    for i in range(len(fileList)):
        if i % 4 == 0:
            dates.append(fileList[i])

    positives = []
    for i in range(len(fileList)):
        if i % 4 == 2:
            positives.append((float(fileList[i]))/1000)

    dailyTotal = []
    for i in range(len(positives)):
        if i == 0:
            dailyTotal.append(positives[i])
        else:
            dailyTotal.append((dailyTotal[i-1] + positives[i]))


    x = []
    for date in dates:
        y, m, d = date.split('-')
        dt = datetime.date(int(y), int(m), int(d))
        x.append(dt)

    # This line of code initiates the subplots
    fig, ax = plt.subplots()
    # creates the line plot
    ax.bar(x, dailyTotal, width=1)
    # chart labels
    ax.set_title('Positive COVID-19 Cases in Indiana')

    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')

    ax.set_ylim(0,1200)

    fig.autofmt_xdate()

#    ax.set_ylim(0,1000)
#    ax.set_yticks([0,200,400,600,800,1000])

    #ax.set_xticklabels(['2020-03','2020-05','2020-07','2020-09','2020-11','2021-01','2021-03','2021-05','2021-07','2021-09','2021-11'])

    # prints the chart
    plt.show()


if __name__ == '__main__':
    main()
