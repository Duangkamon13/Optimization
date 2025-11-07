import numpy as np

def marrange(A, B):
    A = np.asarray(A).ravel().reshape(-1, 1)   
    B = np.asarray(B).ravel().reshape(1, -1)   
    return A * B                               


if __name__ == '__main__':
    X = np.array([1, 2, 3]).reshape((-1,1))
    Y = np.array([0.5, 1, 5, 10]).reshape((-1,1))
    Z = marrange(X, Y)
    print(Z)
