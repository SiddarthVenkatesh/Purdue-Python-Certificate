"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 08.5 - Number Reader
Date: 11/11/2021

Description:
    Asks user for number of times program should print a random number and then writes it onto a file.

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
    # opens file and sets as fo
    readList = []
    with open('random_numbers.txt') as fo:
        for line in fo:
            readList.append(line.rstrip())
    # loops throught the list to set each string into an int
    for i in range(len(readList)):
        readList[i] = int(readList[i])
    # set values
    amnt = len(readList)
    amnt2 = '{:,}'.format(len(readList))
    minVal = '{:,}'.format(min(readList))
    maxVal = '{:,}'.format(max(readList))
    sumVal = sum(readList)
    sumVal2 = '{:,}'.format(sum(readList))
    avgVal = '{:,.1f}'.format(float(sumVal / amnt))
    # print statements
    print(f'{amnt2} numbers were read from the file.')
    print(f'Min: {minVal}')
    print(f'Max: {maxVal}')
    print(f'Sum: {sumVal2}')
    print(f'Avg: {avgVal}')


if __name__ == '__main__':
    main()
