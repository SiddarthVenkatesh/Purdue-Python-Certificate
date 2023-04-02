"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 04.1 - Falling
Date: 10/01/2021

Description:
    Function that accepts an object’s falling time (in seconds) as an argument, and then calculates and returns the distance in meters
    that the object will fall during that time.

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
# Falling distance function
def falling_dist(t):
    d = 0.5*(8.87)*((t)**2)
    return d

# Prints formatted output in this function
def main():
    print('Time (s)  Distance (m)')
    print('----------------------')
    for i in range(5, 55, 5):
        print(f'{i:8}{falling_dist(i):14.1f}')


if __name__ == '__main__':
    main()
