import numpy as np

def ray(o, v, t):
    o = np.asarray(o)
    v = np.asarray(v)
    return o + t * (v - o)


if __name__ == '__main__':
    O = np.array((0,0,0))
    V = np.array((0,0,10))
    for t in (0, 0.5, 1, 1.5, 2):
        print('P =', ray(O,V,t))
    O = np.array((0,0,0))
    V = np.array((200,300,40))
    for t in (0, 0.5, 1, 1.5, 2):
        print('P =', ray(O,V,t))
    O = np.array((50,50,-10))
    V = np.array((200,300,40))
    for t in (0, 0.5, 1, 1.5, 2):
        print('P =', ray(O,V,t))
