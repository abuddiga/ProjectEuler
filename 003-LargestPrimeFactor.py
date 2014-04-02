"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


import timeit
import math

NUM = 600851475143


def main():
    n = NUM
    if n % 2 == 0:
        lastFactor = 2
        n = n / 2
        while n % 2 == 0:
            n = n / 2
    else:
        lastFactor = 1

    factor = 3
    maxFactor = math.sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            lastFactor = factor
            n = n / factor
            while n % factor == 0:
                n = n / factor
            maxFactor = math.sqrt(n)
        factor = factor + 2

    if n == 1:
        return lastFactor
    else:
        return n

if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)