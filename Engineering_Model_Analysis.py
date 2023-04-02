"""
Author: Siddarth Aadi Venkatesh Kumar, venkat77@purdue.edu
Team Name: JJSC Engineering
Date: 04/14/2022

"""
import matplotlib.pyplot as plt
import numpy as np

def main():

    r_shaft_data = np.arange(0.000254, 0.005334, 0.000254) # 0.01 inches to 0.2 inches in meters
    torque_data = np.arange(0.0, 6.5, 0.5) # N*m

    # Shear Stress vs. Shaft Radius
    torque = 3.0 # N*m
    shear_stress = (2*torque)/(np.pi*r_shaft_data**3)

    plt.plot(r_shaft_data, shear_stress)
    plt.xlabel('Shaft Radius (m)')
    plt.ylabel('Shear Stress (Pa)')
    plt.title('Shear Stress vs. Shaft Radius')
    plt.grid()
    plt.show()

    # Shear Stress vs. Torque
    radius = 0.002794 # 0.11 inches in meters
    shear_stress2 = (2*torque_data)/(np.pi*radius**3)

    plt.plot(torque_data, shear_stress2)
    plt.xlabel('Torque (N*m)')
    plt.ylabel('Shear Stress (Pa)')
    plt.title('Shear Stress vs. Torque')
    plt.grid()
    plt.show()

    # Shear Strain vs. Shaft Radius
    theta = 2*np.pi
    length = 0.06985 # 2.75 inches in meters
    shear_strain = (r_shaft_data*theta)/length

    plt.plot(r_shaft_data, shear_strain)
    plt.xlabel('Shaft Radius (m)')
    plt.ylabel('Shear Strain (radians)')
    plt.title('Shear Strain vs. Shaft Radius')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
