"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 10/03/2021

Description:
    Program that asks the user to enter a valid score five times. The program then displays a letter grade after each score is entered.
    After all the scores are entered, it should display the average of the scores and the letter grade corresponding to that average.

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
# Function checks if the score is valid
def get_valid_score():
    valid = 0
    while valid == 0:
        score = float(input('Enter a score: '))
        # checks if input is invalid
        if (score) < 0 or (score) > 100:
            print('  Invalid Input. Please try again.')
        else:
            valid = 1
    return score

# Function finds the average
def calc_average(score):
    average = float(sum(score) / len(score))
    return average

# Function determines the grade
def determine_grade(score):
    if score >= 91 and score <= 100:
        grade = 'A'
    elif score >= 82 and score < 91:
        grade = 'B'
    elif score >= 73 and score < 82:
        grade = 'C'
    elif score >= 64 and score < 73:
        grade = 'D'
    elif score >= 0 and score < 64:
        grade = 'F'
    return grade

# Main function
def main():

    i = 0
    listAvg = []
    # Runs program 5 times
    while i < 5:
        listAvg.append(get_valid_score())
        grade = determine_grade(int(listAvg[i]))
        print(f'  The letter grade for {float(listAvg[i])} is {grade}.')
        i+=1
    avg = calc_average(listAvg)
    # Prints all statements
    print('')
    print('Results:')
    print(f'  The average score is {avg:.2f}.')
    print(f'  The letter grade for {avg:.2f} is {determine_grade(avg)}.')


if __name__ == '__main__':
    main()
