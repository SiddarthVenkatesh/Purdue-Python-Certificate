"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 10/08/2021

Description:
    Asks user for input on the number of points for the star and then draw and fill in the star accordingly.

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

def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

def main():
    """Write your code below this line."""
    # Ask user for number of points on star
    num = int(input('Enter the number of points on the star: '))
    # Calculates angle
    A = 360/num
    # Sets the direction of turtle
    setheading(270+A)
    # Fills the star shape with crimson color
    fillcolor('#DC143C')
    begin_fill()

    i = 0
    while i < (2*num):
        if i % 2 == 0:
            forward(60)
            left(180-A)
            i += 1
        else:
            forward(60)
            right(180-(2*A))
            i += 1

    end_fill()


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
