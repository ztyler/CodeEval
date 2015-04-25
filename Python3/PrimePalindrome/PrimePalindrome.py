def isprime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

for i in reversed(range(1001)):
    if (str(i) == str(i)[::-1]) & isprime(i):
        print(i)
