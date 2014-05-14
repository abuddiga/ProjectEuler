"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""


import timeit
import math

NUM = 10001

def isPrime(n):
    if n == 2 or n % 2 == 0:
        return False

    i = 3
    upper = int(math.sqrt(n)) + 1

    while i < upper:
        if n % i == 0:
            return False
        i += 2

    return True

def main():
    n = 1
    p = 1
    while n < NUM:
        p += 2
        if isPrime(p):
            n += 1

    return p

if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)