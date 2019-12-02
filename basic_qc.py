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

    in_state = np.matrix([1,1,0,0]).T

    U_12 = kron(I, rx(-PI/2)) * CX * kron(I, rz(PI/2)) * CX
    out_state = U_12 * in_state

    print(in_state)
    print(U_12)
    print(out_state) 


    print("=== Question 2: ===")
    in_state = np.matrix([0,0,1,1]).T
    out_state = U_12 * in_state

    print(in_state)
    print(U_12)
    print(out_state) 

    print("=== Question 3: ===")
    in_state = np.matrix([1,1,1,1]).T
    out_state = U_12 * in_state

    print(in_state)
    print(U_12)
    print(out_state) 

    print("=== Question 4: ===")
    # This is not working :(
    in_state = np.matrix([1,1,1,1,1,1,1,1]).T

    U_12 = kron(I, kron(I, rx(-PI/2)) * CX * kron(I, rz(PI/2)) * CX)
    U_23 = kron(kron(I, rx(-PI/2)) * CX * kron(I, rz(PI/2)) * CX, I)

    out_state = U_23 * U_12 * in_state

    print(in_state)
    print(U_23 * U_12)
    print(out_state) 