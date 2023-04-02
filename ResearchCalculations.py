"Calculates velocities of fuel and air for certain range of equivalence ratios"

def main():

    eq_ratios = [0.7,0.65,0.6,0.55,0.5]

    for i in range(len(eq_ratios)):
        print('Equivalence Ratio: ', eq_ratios[i])
        af_real = 34.33/eq_ratios[i]
        print('A/F real:', af_real)
        v_ratio = af_real*(81.3/1180)
        v_f = 22/(1+v_ratio)
        print('Vfuel: %.3f' % (v_f))
        v_a = 22-v_f
        print('Vair: %.3f'% (v_a))
        print('')


if __name__ == '__main__':
    main()
