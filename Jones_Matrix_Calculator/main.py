from classes import LP, QWP, Mirror, HWP
import numpy as np

if __name__ == "__main__":
    chain = (LP(45), QWP(90), LP(0), HWP(0), LP(90))
    J = np.matrix([[1,0],[0,1]])
    for element in chain:
        J = np.dot(element.M,J)
    print(J)