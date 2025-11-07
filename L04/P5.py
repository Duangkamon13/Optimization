import numpy as np

def natresp(a, t, x0):
    t = np.asarray(t)       
    return x0 * np.exp(a * t)


if __name__ == '__main__':
    C0 = 100
    C5 = natresp(-0.14, 5, C0)
    print('C5 =', C5)
    ts = np.linspace(0, 5, 6)
    Cs = natresp(-0.14, ts, 100)
    print(('C: ' + '{:.0f}%.. '*6).format(*Cs))
