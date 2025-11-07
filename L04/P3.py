import numpy as np
def normalize(v):
    v = np.asarray(v)
    norm = np.linalg.norm(v)
    return v / norm


if __name__ == '__main__':
    v = np.array([3, 4])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2))

    v = np.array([3, 4, 2])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2 + u[2]**2))

    v = np.array([3, 4, 2, 5])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2 + u[2]**2 + u[3]**2))
