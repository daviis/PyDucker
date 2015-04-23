def primeFinder(n):
    """
    @n:int
    """
    primes = []
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, n+1, i))
    return primes

numOfPrimes = 25
print("The first " + numOfPrimes)
# print("The first " + numOfPrimes + " " + primeFinder(numOfPrimes))