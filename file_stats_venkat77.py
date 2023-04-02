"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 08.3 - File Stats
Date: 11/06/2021

Description:
    Write a Python program that reads the contents of a file and determines the number of words in the file,
    the number of lines in the file, and average number of words per line

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

    with open('frontiero_v_richardson.txt') as fo:
        # converts text file to list of strings
        everything = fo.read()
        wordList = everything.split()
        words = len(wordList)
    print('Total number of words:', words)

    with open('frontiero_v_richardson.txt') as fo2:
        # finds the number of readlines
        linesList = fo2.readlines()
        lines = len(linesList)
        # finds the average words per line
        avg = float(words/lines)

    # print statements
    print('Total number of lines:', lines)
    print('Average number of words per line: %.1f' % avg)


if __name__ == '__main__':
    main()
