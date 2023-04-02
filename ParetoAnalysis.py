"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Team Name: JJSC Engineering
Date: 04/14/2022

"""
def main():

    mpl = input('Enter mpl: ')
    fsd = input('Enter fsd: ')
    ssd = input('Enter ssd: ')
    alt = input('Enter altitude: ')
    print('')

    if mpl == '01':
        MPL = 1
    if mpl == '02':
        MPL = 5
    if mpl == '03':
        MPL = 10

    if fsd == '04':
        FSD = 4
    if fsd == '05':
        FSD = 4.5
    if fsd == '06':
        FSD = 5

    if ssd == '07':
        SSD = 3.5
    if ssd == '08':
        SSD = 4

    if alt == '09':
        ALT = 100
    if alt == '10':
        ALT = 125
    if alt == '11':
        ALT = 150
    if alt == '12':
        ALT = 200

    print('dv_change = 4;')
    print(f'desired_alt = {ALT};')
    print(f'diameter1 = {FSD};')
    print(f'diameter2 = {SSD};')
    print(f'mpl = {MPL};')


if __name__ == '__main__':
    main()
