"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Assignment: 09.3 - Course Info
Date: 11/22/2021

Description:
    Create nested dictionary with course information and user can access this information by entering in the course number.

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

def get_course_data():
    # creates dictionary
    courseData = {'CS101':{'room':'3004', 'instructor':'Django', 'time':'9:00 a.m.'}, 'CS102':{'room':'4501', 'instructor':'Idle', 'time':'10:00 a.m.'}, 'CS103':{'room':'6755', 'instructor':'Rich', 'time':'11:00 a.m.'}, 'NT110':{'room':'1244', 'instructor':'Marshal', 'time':'12:00 p.m.'}, 'CM241':{'room':'1411', 'instructor':'Pickle', 'time':'2:00 p.m.'}}

    return courseData

def main():

    num = input('Enter a course number: ') # ask user for input
    courseData = get_course_data()

    if num in courseData:
        courseInfo = courseData.get(num) # choose from outer dictionary key
        prof = courseInfo.get('instructor') # instructor
        rm = courseInfo.get('room') # room
        time = courseInfo.get('time') # time

        print(f'  The details for course {num} are:')
        print(f'    Instructor: {prof}')
        print(f'          Room: {rm}')
        print(f'          Time: {time}')

    else:
        print(f'  {num} is an invalid course number.') # if course num is not in the dictionary



if __name__ == '__main__':
    main()
