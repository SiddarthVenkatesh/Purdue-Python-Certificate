"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/11/2021

Description:
Ask user for certain inputs to use in a formula to find the final Reynolds number.

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

    # Users inputs for temperature, velocity, and pipe diameter
    temp = float(input('Enter the temperature in \u00B0C as 5, 10, or 15: '))
    v = float(input('Enter the velocity of water in the pipe: '))
    d = float(input("Enter the pipe's diameter: "))
    kv = 0.0
    Rc = 0.0

    # Conditional statements to find the correlating kinematic viscosity for the temperature
    if temp == 5:
        kv = 1.49*(10**-6)
        Rc = (v*d)/kv
        Rc = "{:.2e}".format(Rc)

    elif temp == 10:
        kv = 1.31*(10**-6)
        Rc = (v*d)/kv
        Rc = "{:.2e}".format(Rc)

    elif temp == 15:
        kv = 1.15*(10**-6)
        Rc = (v*d)/kv
        Rc = "{:.2e}".format(Rc)

    # Uses inputs in formula to find Reynolds number
    #Rc = (v*d)/kv

    # Print final statement
    print('At ' + str(temp) + "\u00B0C, the Reynolds number for flow at", v, 'm/s in a', d, 'm diameter pipe is ' + str(Rc) + '.')


if __name__ == '__main__':
    main()
