import control

def main():
    omega = [2,1]
    M,Phi,omega=control.freqresp(v,omega)

if __name__ == '__main__':
    main()
