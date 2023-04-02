"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 09.4 - Course Info
Date: 11/22/2021

Description:
    Process two text files and create and return multiple text files.

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
import string
# loads state data from text file
def get_word_frequency():

    data = []
    punc = string.punctuation
    with open('xian_1.txt') as fo:
        x = fo.read()
        data = x.split()
        #for i in range(len(data)):
        #    data[i] = data[i]

        for i in range(len(data)):
            for c in range(len(punc)):
                if punc[c] in data[i]:
                    data[i].replace(punc[c],'')

        #data.sort()


        #data_set = set(data)

        #for i in range(len(x)):
        #    data1.append(x[i].split())
        #for line in fo:
        #    data1.append(line.rstrip())

#    stateDict = {}
    # Creates dictionary of states as keys and capitals as values
#    for i in range(len(data1)):
#        info = data1[i].split(', ')
#        state = info[1]
#        capital = info[0]
#        stateDict[state] = capital

    return data

def main():

    print(get_word_frequency())


if __name__ == '__main__':
    main()
