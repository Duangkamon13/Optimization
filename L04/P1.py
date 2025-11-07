import numpy as np

def get_info(data):
    arr = np.array(data)  
    info = {
        "shape": arr.shape,
        "dtype": arr.dtype  
    }
    return arr, info

if __name__ == '__main__':
    x, info = get_info([1, 2, 3, 4])
    print('x =', x)
    print('info =', info)

    x, info = get_info([[1, 2, 3, 4]])
    print('x =', x)
    print('info =', info)

    x, info = get_info([[1], [2], [3], [4]])
    print('x =', x)
    print('info =', info)

    x, info = get_info([[1., 0], [0, 1.]])
    print('x =', x)
    print('info =', info)

    x, info = get_info([[2.5+1j, 1.5, 3j, 3+4.7j]])
    print('x =', x)
    print('info =', info)
