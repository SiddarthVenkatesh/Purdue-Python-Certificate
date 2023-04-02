"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 05.4 - Hello Turtle
Date: 10/09/2021

Description:
    Creates multiple functions for each letter and then all of them are called in the main function to write 'hello turtle'

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
    setup(600, 400)
    width(9)


def draw_e(findPos, level):
    """Write this function."""
    penup()
    goto(findPos[0]+30,level+30)
    pendown()
    setheading(0)
    forward(60)
    left(90)
    circle(30, 315)
    penup()
    return pos()

def draw_h():
    """Write this function."""
    setheading(90)
    penup()
    pendown()
    forward(120)
    penup()
    goto(0,30)
    pendown()
    circle(-30,180)
    forward(30)
    return pos()

def draw_l(findPos, level):
    """Write this function."""
    penup()
    goto(findPos[0]+30,level)
    pendown()
    setheading(90)
    forward(120)
    return pos()

def draw_o(findPos, level):
    """Write this function."""
    penup()
    goto(findPos[0]+90,level+30)
    pendown()
    circle(30)
    return pos()

def draw_r(findPos, level):
    """Write this function."""
    penup()
    goto(findPos[0]+30,level)
    pendown()
    setheading(90)
    forward(60)
    goto(findPos[0]+30,findPos[1]-30)
    circle(-30,90)
    penup()
    return pos()


def draw_t(findPos, level):
    """Write this function."""
    penup()
    goto(findPos[0]+30,level)
    setheading(90)
    pendown()
    forward(120)
    penup()
    goto(findPos[0], level+90)
    setheading(0)
    pendown()
    forward(60)
    penup()
    return pos()


def draw_u(findPos, level):
    """Write this function."""
    penup()
    goto(findPos[0]+30, level+60)
    setheading(270)
    pendown()
    forward(30)
    circle(30,180)
    backward(30)
    forward(60)
    return pos()


def main():
    """After these lines, use your letter drawing functions
    to write code that will draw the words "hello turtle".
    """
    h = 0
    findPos = draw_h()
    findPos = draw_e(findPos, h)
    findPos = draw_l(findPos, h)
    findPos = draw_l(findPos, h)
    findPos = draw_o(findPos, h)

    h = -180
    x = -60

    findPos = (x,h)
    findPos = draw_t(findPos, h)
    findPos = draw_u(findPos, h)
    findPos = draw_r(findPos, h)
    findPos = draw_t(findPos, h)
    findPos = draw_l(findPos, h)
    findPos = draw_e(findPos, h)


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
