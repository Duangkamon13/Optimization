
import math
def cos_sim(a, b):
    dot_product = 0
    for i in range(len(a)):
        dot_product = dot_product + (a[i] * b[i])

    mag_a = math.sqrt(sum(ai**2 for ai in a))
    mag_b = math.sqrt(sum(bi**2 for bi in b))
    return dot_product / (mag_a * mag_b)

if __name__ == '__main__':
    cs = cos_sim([1, 0], [5, 5])
    print(cs)  

    cs = cos_sim([14, 0, 5], [5, 8, 4])
    print(cs) 