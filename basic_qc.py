import numpy as np

kron = np.kron

I = np.matrix([[1, 0],
               [0, 1]])

X = np.matrix([[0, 1],
               [1, 0]])

Y = np.matrix([[0, -1j],
               [1j, 0]])

Z = np.matrix([[1, 0],
               [0, -1]])

CX = np.matrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]])



if __name__ == "__main__":
    in_state = np.matrix([0,0,1,1]).T

    circ_op = CX * kron(Z,I) * CX * kron(I,-X)
    out_state = circ_op * in_state
    print(circ_op)
    print(out_state) 