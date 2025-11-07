import numpy as np

def plane3d(Px, Py, n, k):
    Px = np.asarray(Px)
    Py = np.asarray(Py)
    n = np.asarray(n)
    Pz = (k - n[0]*Px - n[1]*Py) / n[2]
    return Pz


if __name__ == '__main__':
    # Plane
    n = np.array([0.57735027, 0.57735027, 0.57735027])
    k = 3
    # Points on a plane
    x, y = 0, 0
    z = plane3d(x, y, n, k)
    print(f'p = ({x}, {y}, {z})')
    xs = np.linspace(-2, 2, 3)
    ys = np.linspace(-2, 2, 3)
    X, Y = np.meshgrid(xs, ys)
    Z = plane3d(X, Y, n, k)
    for i in range(3):
        for j in range(3):
            print(f'ps = ({X[i,j]}, {X[i,j]}, {Z[i,j]})')