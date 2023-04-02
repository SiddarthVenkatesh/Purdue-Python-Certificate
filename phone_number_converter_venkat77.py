"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 11/06/2021

Description:
    Program takes in an alphanumeric string and outputs a fully numberic string

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



def convert_number(phrase):

    # makes string all lowercase
    phrase = phrase.lower()
    # list of the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # for loops to replace letters with numbers
    for i in range(3):
        phrase = phrase.replace(alphabet[i], '2')
    for i in range(3,6):
        phrase = phrase.replace(alphabet[i], '3')
    for i in range(6,9):
        phrase = phrase.replace(alphabet[i], '4')
    for i in range(9,12):
        phrase = phrase.replace(alphabet[i], '5')
    for i in range(12,15):
        phrase = phrase.replace(alphabet[i], '6')
    for i in range(15,19):
        phrase = phrase.replace(alphabet[i], '7')
    for i in range(19,22):
        phrase = phrase.replace(alphabet[i], '8')
    for i in range(22,26):
        phrase = phrase.replace(alphabet[i], '9')

    return phrase

def main():

    phrase = input('Enter a telephone number: ')
    print('The phone number is', convert_number(phrase))

if __name__ == '__main__':
    main()
