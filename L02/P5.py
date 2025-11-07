def numsys(n):
    binary = bin(n)
    hexa = hex(n)
    return binary, hexa


results = numsys(20)
print('results =', results)

b, h = numsys(30)
print('b =', b)
print('h =', h)
