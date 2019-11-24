# Implement an algorithm for determining all generators of the cyclic group (ℤ𝑛,+), where 𝑛≥2 is a natural number.
# A generator of (ℤ𝑛,+) is an element 𝑔̂ ∈ℤ𝑛 such that for every 𝑥̂ ∈ℤ𝑛 there exists 𝑘∈{0,1,…,𝑛−1} such that 𝑥̂ =𝑘𝑔̂ .

#Determine if a number is prime
def isPrime(n):
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    while i <= n / 2:
        if n % i == 0:
            return False
        i += 2
    return True


#Compute the GCD of 2 numbers
def gcd(a, b):
    if a > b:
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    else:
        while a != 0:
            r = b % a
            b = a
            a = r
        return b


#Determine if 2 numbers are relatively prime
def relativelyPrime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False


#Compute the phi from the Euler's function
def computePhi(n, listOfFactors):
    phi = n
    for factor in listOfFactors:
        phi = phi * (1 - 1 / factor)
    return phi


#return Euler's function to determine the total number of genertors
def eulerFunction(n):
    if isPrime(n):
        return n - 1
    else:
        i = 2
        factors = []
        m = n
        while m != 1:
            if m % i == 0:
                factors.append(i)
                while m % i == 0:
                    m = m / i
            i += 1
        return computePhi(n, factors)


# return the list of all generators of n
def allGenerators(n):
    generators = []
    for generator in range(0, n):
        if relativelyPrime(generator, n):
            generators.append(generator)
    return generators


if __name__ == '__main__':
    print(eulerFunction(12).__int__())
    print(allGenerators(12))
