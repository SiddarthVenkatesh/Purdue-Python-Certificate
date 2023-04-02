"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 05.1 - Maze
Date: 10/08/2021

Description:
    This program's main function is to move the turtle from the center to the exit in the right side of the maze.

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
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width(5)

def main():
    """Write your code below this line."""
    forward(11)
    right(90)
    forward(60)
    left(90)
    forward(25)
    right(90)
    forward(95)
    left(90)
    forward(95)
    left(90)
    forward(25)
    right(90)
    forward(95)
    left(90)
    forward(130)
    right(90)
    forward(30)

# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
