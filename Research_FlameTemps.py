"Flame temperatures"

import numpy as np

def main():

    eq_ratios = [0.7,0.65,0.6,0.55,0.5]

    for i in range(len(eq_ratios)):
        print('Equivalence Ratio:', eq_ratios[i])
        N_ratio = (eq_ratios[i]*34.33*2/28.85)
        print('Mole Ratio of Air to Fuel: ', N_ratio)
        N_air = N_ratio*1
        print('Moles of air:', N_air)
        ast = N_air / (1+3.76)

        print('ast value:', ast)

        A = np.array([[-2, 2, 0], [1/ast, 0, 0], [0, 0, 2]])
        b = np.array([0, 2, 2*3.76*ast])
        x = np.linalg.solve(A, b)
        print(x)
        print('')



if __name__ == '__main__':
    main()
