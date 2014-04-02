"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


import timeit
import math

LIMIT = 21

def gcd(a, b):
    if b:
        return gcd(b, (a % b))
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)

def main():
    smallest_multiple = 1
    for x in range(1, LIMIT):
        smallest_multiple = lcm(smallest_multiple, x)

    return smallest_multiple


if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)