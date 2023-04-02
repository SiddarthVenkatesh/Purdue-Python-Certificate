"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 06.4 - Arch Spiral
Date: 10/24/2021

Description:
    Program draws an archimedian spiral

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

from turtle import *

# Import additional modules below this line.
from math import *

# Write new functions below this line (starting with unit 4).


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width('5')


def main():
    """Write your mainline logic here."""
    setheading(0)
    for i in range(1,2161,1):
        speed(0)
        x_c = float((i)*cos((radians(i)))/(pi**2))
        y_c = float((i)*sin((radians(i)))/(pi**2))
        goto(x_c,y_c)

if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
