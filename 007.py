# 10001st prime

def isprime(n):
    if n <= 1: 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primegen():
    n = 2
    while True:
        if isprime(n):
            yield n
        n += 1

primes = primegen()

for x in range(10001):
    print(f'{x+1}: {next(primes)}')