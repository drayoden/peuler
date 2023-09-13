# sum of primes below two million

sumof = 0
maxn = 2000000

def isprime(n):
    if n <= 1: 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for x in range(1,maxn):
    if isprime(x):
        print(f'prime: {x}')
        sumof += x

print(f'sum of all primes below {maxn}: {sumof}')