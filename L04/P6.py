import numpy as np

def innerprod(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    return np.vdot(x, y)


if __name__ == '__main__':
    v = np.array([3, 4, 5, 6])
    u = np.array([1,-1, 0, 2.5])
    p = innerprod(v, u)
    print('<v|u> =', p)
    p = innerprod(u, v)
    print('<u|v> =', p)
    v = np.array([3 + 5j, -4j, 0, 1 - 1j, 6 + 9j])
    u = np.array([2 - 1j, -1.2, 7 + 8j, 3 - 5j, 1.1 + 2j])
    p = innerprod(v, u)
    print('<v|u> =', p)
    p = innerprod(u, v)
    print('<u|v> =', p)
 