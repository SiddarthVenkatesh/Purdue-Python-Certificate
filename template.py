"""
Author: Your Name, login@purdue.edu
Assignment: m.n - Assignment Name
Date: MM/DD/YYYY

Description:
    Describe your program here.

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

        while stopper ==  0:
            state = r.choice(stateList) # chooses random state
            stateIndex = stateList.index(state)
            q = input(f'What is the capital of{state} (enter 0 to quit)? ')
            q = q.title()

            if q == '0': # for ending program
                if correct + incorrect == 0:
                    print('You answered 0 out of 0 questions correctly.')
                    stopper = 1
                else:
                    print(f'You answered {correct} out of {(correct + incorrect)} questions correctly.')
                    stopper = 1

            elif q not in capitalList:
                print('  That is incorrect.')
                print(f'  The capital of{state} is {((capitalList[stateIndex]).title())}.')
                incorrect += 1

            elif q in capitalList:
                if q == ((capitalList[stateIndex]).title()):
                    stateList.pop(stateIndex)
                    capitalList.pop(stateIndex)
                    print('  That is correct!')
                    correct += 1
                else:
                    print('  That is incorrect.')
                    print(f'  The capital of{state} is {((capitalList[stateIndex]).title())}.')
                    incorrect += 1


if __name__ == '__main__':
    main()
