import numpy as np

def rmse(yp, y):
    yp = np.asarray(yp)
    y = np.asarray(y)
    return np.sqrt(np.mean((yp - y) ** 2))


if __name__ == '__main__':
    ys = np.array([1, 2, 3, 4, 8])
    yps = np.array([0.8, 2.3, 2.8, 4.2, 8.1])
    E = rmse(yps, ys)
    print('E =', E)

    ys = np.array([10, 2, 30, 4, 80, -15, 26, 12])
    yps = np.array([8.7, 2.3, 40, 3.1, 81, -10, 20, 13])
    E = rmse(yps, ys)
    print('E =', E)
