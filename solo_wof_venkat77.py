"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 12.1 - Solo Wheel of Fortune
Date: 12/05/2021

Description:
    Creates Wheel of Fortune

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
import random as r

def load_phrases():
    phraseList = []
    with open('phrases.txt') as fo:
        for line in fo:
            phraseList.append(line.rstrip())
    r.shuffle(phraseList)

    return phraseList

def spin_the_wheel():

    wheel = ['$500', '$500', '$500', '$500', '$550', '$550', '$600', '$600', '$600', '$600', '$650', '$650', '$650', '$700', '$700', '$800', '$800', '$900', '$2,500', 'BANKRUPT', 'BANKRUPT']
    r.shuffle(wheel)
    print(f'The wheel landed on {wheel[1]}.')

    if wheel[1] == 'BANKRUPT':
        cash = 0

    vowels = ['a', 'e', 'i', 'o', 'u']
    constants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    q = True
    while q == True:
        const = input(f'Pick a constant: ')
        if const in vowels:
            print('Vowels must be purchased.')
        elif (type(const) is int) == True:
            print(f'The character {const} is not a letter.')
        elif (len(const)) > 1:
            print('Please enter exactly one character.')
        else:
            q = False

    if const in word:
        numC = word.count(const)
        print(f'There is {numC} {const}, which earns you {wheel[1]}')

        charInds = []
        for i in range(len(word)):
            if (word[i] == const):
                charInds.append(i)

        newBlanks = list(blanks)
        for j in charInds:
            newBlanks[j] = const
        newBlanks = "".join(newBlanks)

    return newBlanks


def main():

    phraseList = load_phrases()
    round = 1
    word = phraseList[round]

    while True:
        blankList = []
        for x in word:
            if x != " ":
                blankList.append("_")
            else:
                blankList.append(x)
        blanks = "".join(blankList)

        print(word)
        print(blanks)

        print('Welcome to Solo Wheel of Fortune!')
        print('')
        print(f':: Solo WoF :::::::::::::::::::::::::::::: Round {round} of 4 ::')
        print(':: %39s              ::' % (blanks))
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print('::   AEIOU   ::   BCDFGHJKLMNPQRSTVWXYZ   ::         $0 ::')
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

        print('Menu:')
        print('  1 - Spin the wheel.')
        print('  2 - Buy a vowel.')
        print('  3 - Solve the puzzle.')
        print('  4 - Quit the game.')

        choice = int(input('Enter the number of your choice: '))
        if choice == 1:
            spin = spin_the_wheel()
            print(newBlanks)


if __name__ == '__main__':
    main()
