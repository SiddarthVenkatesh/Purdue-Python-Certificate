"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 11/04/2021

Description:
    Program collects ten float numbers from user and calculates certain data for numbers in that list.

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



def pig(phrase):

    # splitting phrase
    splitList = phrase.split()
    finalList = []
    # for loop to go through list
    run1 = 0
    for i in range(len(splitList)):
        word = splitList[i]
        l1 = word[0]
        word = word[1:] + l1 + 'ay'
        if i == 0:
            word = word.capitalize()
        else:
            word = word.lower()
        finalList.append(word)
    # joins the list into one string
    finalPhrase = ' '.join(finalList)

    return finalPhrase

def main():

    phrase = input('Enter a string: ')
    print('Pig latin:', pig(phrase))

if __name__ == '__main__':
    main()
