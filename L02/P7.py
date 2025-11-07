"""
Given Taylor series, a value of sine function can be approximated from
sin(x) \approx sum_{n=0}^{M-1} (-1)^n)/((2n+1)!) x^(2n+1),
where M is a number of terms. The larger M is,
the more accurate the approximate is. For example,
M = 5, sin(x) ≃x-x^3/3!+x^5/5!-x^7/7!+x^9/9!.
M =6, sin(x)≃x-x^3/3!+x^5/5!-x^7/7!+x^9/9!+x^11/11!.
Write a function, named approx_sin(x, tol),
to take 2 argument: x for an angle in radian and tol for tolerance.
The function computer approximate value of sin(x) for M terms such that
the last term in the series is smaller than the tolerance.
"""

def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i

    return f


def approx_sin(x, M):
    sinv = 0

    # Write your code here!!!

    for n in range(M):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / fact(2 * n + 1)
        sinv += term

    return sinv


if __name__ == '__main__':
    x = float(input('x:'))
    M = int(input('M:'))

    print('sin(%.2f) = %.5f'%(x, approx_sin(x, M)))