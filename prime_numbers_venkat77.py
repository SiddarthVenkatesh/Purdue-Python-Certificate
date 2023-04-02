"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/04/2021

Description:
    Program takes an integer input and checks if the number is prime or not.

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
# Function checks if num is prime or not
def is_prime(num):
    checkPrime = True
    # Runs through all possiblities leading up to num
    for p in range(2, int(num**(1/2))):
        if num % p == 0:
            checkPrime = False
    if num == 1:
        checkPrime = False
    return checkPrime

# Main function calls is_prime and prints statements
def main():

    runner = 0
    while runner == 0:
        num = int(input('Enter a positive integer (-1 to quit): '))
        if num < 0:
            runner+=1
        elif is_prime(num) == False:
            print(f'  {num} is not prime.')
        else:
            print(f'  {num} is prime!')


if __name__ == '__main__':
    main()
