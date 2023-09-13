# smallest multiple
# find the smallest positive number divisible by all numbers 1 to 20

from functools import reduce

def lcm(a,b):
    gcd,tmp = a,b
    while tmp != 0:
        gcd,tmp = tmp, gcd % tmp
    r = int(a * b / gcd)
    print(f'{a},{b}: {r}')
    return r

reduce(lcm, range(1,21))