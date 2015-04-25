def isprime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

primes = 0
count = 1
pSum = 0
while primes < 1000:
    count = count + 1
    if isprime(count):
        primes = primes + 1
        pSum = pSum + count

print(pSum)
