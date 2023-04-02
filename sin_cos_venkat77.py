"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 12/1/2021

Description:
    Graph sine and cosine functions on chart.

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

import numpy
import matplotlib.pyplot as plt

def main():
    x = numpy.arange(0,2*numpy.pi,0.2)   # start,stop,step
    y1 = numpy.sin(x)
    y2 = numpy.cos(x)

    # This line of code initiates the subplots
    fig, ax = plt.subplots()
    # creates the line plot

    ax.plot(x,y1, color = 'r')
    ax.plot(x,y2, color = 'b')
    # chart labels
    ax.set_xticks([0.5*numpy.pi,numpy.pi,1.5*numpy.pi,2*numpy.pi])
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    ax.set_yticks([-1,1])

    for spine in ['top','right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')

#    ax.set_ylim(0,1000)
#    ax.set_yticks([0,200,400,600,800,1000])

    #ax.set_xticklabels(['2020-03','2020-05','2020-07','2020-09','2020-11','2021-01','2021-03','2021-05','2021-07','2021-09','2021-11'])

    # prints the chart
    plt.show()


if __name__ == '__main__':
    main()
