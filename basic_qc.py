import numpy as np

sqrt = np.sqrt
kron = np.kron

PI = np.pi

I = np.matrix([[1, 0],
               [0, 1]])

X = np.matrix([[0, 1],
               [1, 0]])

Y = np.matrix([[0, -1j],
               [1j, 0]])

Z = np.matrix([[1, 0],
               [0, -1]])

def rx(theta):
    return np.cos(theta/2) * I - 1j * np.sin(theta/2) * X

def ry(theta):
    return np.cos(theta/2) * I - 1j * np.sin(theta/2) * Y

def rz(theta):
    return np.cos(theta/2) * I - 1j * np.sin(theta/2) * Z

CX = np.matrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]])

CZ = np.matrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, -1]])


if __name__ == "__main__":
    print("=== Question 1: ===")

    in_state = 1/sqrt(2) * np.matrix([1,1,0,0]).T

    U = kron(rx(-PI/2), I) * CX * kron(I, rz(-PI/2)) * CX
    out_state = U * in_state

    print(in_state)
    print(U)
    print(out_state) 


    print("=== Question 2: ===")
    in_state = 1/sqrt(2) * np.matrix([0,0,1,1]).T
    out_state = U * in_state

    print(in_state)
    print(U)
    print(out_state) 

    print("=== Question 3: ===")
    in_state = 1/sqrt(2) * np.matrix([1,1,1,1]).T
    out_state = U * in_state

    print(in_state)
    print(U)
    print(out_state) 

    print("=== Question 4: ===")
    # This is not working :(
    in_state = 1/sqrt(8) * np.matrix([1,1,1,1,1,1,1,1]).T

    U_12 = kron(I, U)
    U_23 = kron(U, I)

    out_state = U_23 * U_12 * in_state

    print(in_state)
    print(U_23 * U_12)
    print(out_state) 
#
    #print(CX * kron(I, Z) * CX)
    #print(kron(Z, I) * kron(I, Z))
    #print(kron(Z, Z))
#
    #print(kron(Z, I))
    #print(kron(I, Z))
#
    #print(CX * np.matrix([1,1,0,0]).T)