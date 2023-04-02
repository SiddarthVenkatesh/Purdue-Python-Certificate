"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 08.6 - Step Counter
Date: 11/12/2021

Description:
    Finds the average monthly steps from a given file

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
    with open('steps.txt') as fo:
        for line in fo:
            readList.append(line.rstrip())
    # loops throught the list to set each string into an int
    for i in range(len(readList)):
        readList[i] = int(readList[i])

    jan = readList[0:31] #31
    feb = readList[31:59] #28
    mar = readList[59:90] #31
    apr = readList[90:120] #30
    may = readList[120:151] #31
    jun = readList[151:181] #30
    jul = readList[181:212] #31
    aug = readList[212:243] #31
    sep = readList[243:273] #30
    oct = readList[273:304] #31
    nov = readList[304:334] #30
    dec = readList[334:365] #31

    monthList = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

    print('The average steps taken each month were:')
    for j in range(12):
        sumMonth = sum(monthList[j])
        avg = (sumMonth / (len(monthList[j])))
        print('%10s' % (months[j]), ': %1.2f' % (avg))


if __name__ == '__main__':
    main()
